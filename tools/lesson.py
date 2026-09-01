#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
حلقة المدرّس: اعرض الدرس → اسأل → صحّح → سجّل في ملف التقدّم.

الأوامر:
    python3 tools/lesson.py list
    python3 tools/lesson.py show 000          # طباعة الدرس
    python3 tools/lesson.py quiz 000          # اختبار تفاعلي + تسجيل النتيجة
    python3 tools/lesson.py learn 000         # عرض الدرس ثم الاختبار مباشرة
"""
from __future__ import annotations

import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LESSONS = os.path.join(ROOT, "lessons")
PROFILE = os.path.join(ROOT, "progress", "profile.json")


def parse(path):
    txt = open(path, encoding="utf-8").read()
    meta = {}
    m = re.search(r"^---\n(.*?)\n---\n", txt, re.S | re.M)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    quiz = []
    qm = re.search(r"```quiz\n(.*?)\n```", txt, re.S)
    if qm:
        quiz = json.loads(qm.group(1))
    body = txt
    if m:
        body = body.replace(m.group(0), "")
    return meta, body, quiz


def list_lessons():
    if not os.path.isdir(LESSONS):
        print("لا يوجد مجلد lessons/ بعد")
        return
    print("الدروس المتاحة:\n")
    for f in sorted(os.listdir(LESSONS)):
        if not f.endswith(".md"):
            continue
        meta, _, quiz = parse(os.path.join(LESSONS, f))
        print(f"  {meta.get('id', f[:3])} — {meta.get('title', f)}  ({len(quiz)} سؤالاً)")


def show(meta, body):
    print(body.strip())
    print()


def run_quiz(meta, quiz):
    if not quiz:
        print("لا يوجد اختبار في هذا الدرس.")
        return None
    print("\n" + "═" * 64)
    print(f"  اختبار: {meta.get('title', '')}")
    print("═" * 64)
    score = 0
    for i, q in enumerate(quiz, 1):
        print(f"\nس{i}. {q['q']}")
        for j, o in enumerate(q["o"], 1):
            print(f"   {j}) {o}")
        while True:
            raw = input("؟ إجابتك (رقم): ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(q["o"]):
                ans = int(raw) - 1
                break
            print("   أدخل رقماً من الخيارات.")
        if ans == q["a"]:
            print("   ✅ صحيح.")
            score += 1
        else:
            print(f"   ❌ غير صحيح. الصحيح: {q['o'][q['a']]}")
        if q.get("why"):
            print(f"   💡 {q['why']}")
    pct = round(100.0 * score / len(quiz))
    print("\n" + "─" * 64)
    print(f"  النتيجة: {score}/{len(quiz)} = {pct}٪")
    if pct >= 80:
        print("  🟢 اجتزتَ البوابة المفاهيمية (≥80٪).")
    elif pct >= 60:
        print("  🟡 قريب — أعد قراءة الأخطاء الشائعة ثم أعد الاختبار غداً.")
    else:
        print("  🟠 أعد قراءة الدرس، وسأشرح النقاط الصعبة بطريقة أخرى (X.10).")
    return pct


def record(meta, pct):
    if pct is None or not os.path.exists(PROFILE):
        return
    p = json.load(open(PROFILE, encoding="utf-8"))
    nodes = meta.get("nodes", "[]")
    try:
        node_ids = json.loads(nodes.replace("'", '"'))
    except Exception:
        node_ids = []
    for nid in node_ids:
        prev = p.get("topics", {}).get(nid, {}).get("mastery", 0)
        # سقف متحفّظ: اجتياز درس تمهيدي لا يعني إتقاناً بحثياً (بوابة X.9)
        new = max(prev, min(pct, 85))
        lvl = "L2" if new >= 75 else "L1"
        p.setdefault("topics", {})[nid] = {"level": lvl, "mastery": new,
                                           "status": status_of(new)}
    p["updated"] = datetime.date.today().isoformat()
    json.dump(p, open(PROFILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if node_ids:
        print(f"  📝 سُجّلت النتيجة في: {', '.join(node_ids)}")


def status_of(m):
    for thr, name in [(92, "🟣 بحثي"), (80, "🔵 متقدم"), (65, "🟢 متقن"),
                      (45, "🟡 متوسط"), (25, "🟠 مبتدئ"), (0, "🔴 غير معروف")]:
        if m >= thr:
            return name
    return "🔴 غير معروف"


def find(slug):
    for f in sorted(os.listdir(LESSONS)):
        if not f.endswith(".md"):
            continue
        path = os.path.join(LESSONS, f)
        meta, body, quiz = parse(path)
        if meta.get("id") == slug or f.startswith(slug):
            return meta, body, quiz
    return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "list":
        list_lessons()
        return
    if len(sys.argv) < 3:
        print("حدد رقم الدرس، مثال: python3 tools/lesson.py show 000")
        return
    found = find(sys.argv[2])
    if not found:
        print("درس غير موجود")
        return
    meta, body, quiz = found
    if cmd == "show":
        show(meta, body)
    elif cmd == "quiz":
        pct = run_quiz(meta, quiz)
        record(meta, pct)
    elif cmd == "learn":
        show(meta, body)
        try:
            input("… اضغط Enter للبدء بالاختبار …")
        except (EOFError, KeyboardInterrupt):
            print()
        pct = run_quiz(meta, quiz)
        record(meta, pct)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
