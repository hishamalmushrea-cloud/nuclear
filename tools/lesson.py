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
    per_kind = {}          # {نوع السؤال: [صحيح، مجموع]}
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
        kind = q.get("k") or "concept"
        ok, tot = per_kind.get(kind, [0, 0])
        tot += 1
        if ans == q["a"]:
            print("   ✅ صحيح.")
            score += 1
            ok += 1
        else:
            print(f"   ❌ غير صحيح. الصحيح: {q['o'][q['a']]}")
        per_kind[kind] = [ok, tot]
        if q.get("why"):
            print(f"   💡 {q['why']}")
    pct = round(100.0 * score / len(quiz))
    kinds = {k: round(100.0 * ok / tot) for k, (ok, tot) in per_kind.items()}
    if len(kinds) > 1:
        print("  📊 حسب النوع: " + " · ".join(
            f"{NAMES.get(k, k)} {v}٪" for k, v in sorted(kinds.items())))
    return pct, kinds
    print("\n" + "─" * 64)
    print(f"  النتيجة: {score}/{len(quiz)} = {pct}٪")
    if pct >= 80:
        print("  🟢 اجتزتَ البوابة المفاهيمية (≥80٪).")
    elif pct >= 60:
        print("  🟡 قريب — أعد قراءة الأخطاء الشائعة ثم أعد الاختبار غداً.")
    else:
        print("  🟠 أعد قراءة الدرس، وسأشرح النقاط الصعبة بطريقة أخرى (X.10).")
    return pct, kinds


def record(meta, pct, per_kind=None):
    """يسجّل نتيجة درس في ملف التقدّم.

    يخزّن — فوق الإتقان — أبعاد بوابة X.9:
      attempts: آخر 5 درجات (بُعد «الدرجات»)
      dim:      نسب الإجابة الصحيحة حسب نوع السؤال
                concept (مفاهيم) · term (مصطلحات) · calc (حساب/معادلات)
    """
    if pct is None or not os.path.exists(PROFILE):
        return
    p = json.load(open(PROFILE, encoding="utf-8"))
    nodes = meta.get("nodes", "[]")
    try:
        node_ids = json.loads(nodes.replace("'", '"'))
    except Exception:
        node_ids = []
    per_kind = per_kind or {}
    for nid in node_ids:
        prev = p.get("topics", {}).get(nid, {}).get("mastery", 0)
        # سقف متحفّظ: اجتياز درس تمهيدي لا يعني إتقاناً بحثياً (بوابة X.9)
        new = max(prev, min(pct, 85))
        lvl = "L2" if new >= 75 else "L1"
        t = p.setdefault("topics", {}).get(nid, {}) or {}
        t["level"] = lvl
        t["mastery"] = new
        t["status"] = status_of(new)
        attempts = list(t.get("attempts", []))[-4:] + [int(pct)]
        t["attempts"] = attempts
        t["best_quiz"] = max(int(pct), int(t.get("best_quiz", 0) or 0))
        t["last_quiz"] = datetime.date.today().isoformat()
        dim = dict(t.get("dim", {}) or {})
        for k, v in per_kind.items():
            dim[k] = int(round(max(float(dim.get(k, 0)), float(v))))
        if dim:
            t["dim"] = dim
        p.setdefault("topics", {})[nid] = t
    p["updated"] = datetime.date.today().isoformat()
    json.dump(p, open(PROFILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if node_ids:
        extra = ""
        if per_kind:
            extra = " · " + "، ".join(
                f"{NAMES.get(k, k)} {v}٪" for k, v in sorted(per_kind.items()))
        print(f"  📝 سُجّلت النتيجة في: {', '.join(node_ids)}{extra}")


NAMES = {"concept": "المفاهيم", "term": "المصطلحات", "calc": "الحساب"}


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
        pct, kinds = run_quiz(meta, quiz)
        record(meta, pct, kinds)
    elif cmd == "learn":
        show(meta, body)
        try:
            input("… اضغط Enter للبدء بالاختبار …")
        except (EOFError, KeyboardInterrupt):
            print()
        pct, kinds = run_quiz(meta, quiz)
        record(meta, pct, kinds)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
