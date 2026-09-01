#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
المدرّس التفاعلي — «الفريق يسألك» (X.10، X.9، X.19، X.27).

الاستخدام:
    python3 tools/tutor.py                # يبدأ من أول درس لم تُتقنه
    python3 tools/tutor.py --lesson 001   # درس محدد
    python3 tools/tutor.py --status       # أين أنا؟

أوامر داخل الجلسة (تُكتب أثناء سؤال):
    شرح   → إعادة شرح المفهوم بطريقة أخرى
    بسط   → شرح مبسّط جداً
    مثال  → مثال محلول إضافي
    تشبيه → تشبيه من الحياة اليومية
    مخطط  → رسم نصي يوضّح الفكرة
    سؤال  → اطرح سؤالك الحر (يُسجَّل في دفتر الباحث)
    تخطي  → تخطّي السؤال
    توقف  → إنهاء الجلسة وحفظ التقدّم
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

LESSONS = os.path.join(ROOT, "lessons")
PROFILE_JSON = os.path.join(ROOT, "progress", "profile.json")
NOTEBOOK = os.path.join(ROOT, "progress", "notebook.md")

PASS = 80          # بوابة المفاهيم (X.9)
COMMANDS = {"شرح", "بسط", "مثال", "تشبيه", "مخطط", "سؤال", "تخطي", "توقف", "؟", "help"}


# ------------------------------------------------------------- أدوات -------
def parse(path):
    txt = open(path, encoding="utf-8").read()
    meta = {}
    m = re.search(r"^---\n(.*?)\n---\n", txt, re.S | re.M)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    quiz = []
    qm = re.search(r"```quiz\n(.*?)\n```", txt, re.S)
    if qm:
        quiz = json.loads(qm.group(1))
    body = txt.replace(m.group(0), "") if m else txt
    return meta, body, quiz


def all_lessons():
    out = []
    for f in sorted(os.listdir(LESSONS)):
        if f.endswith(".md"):
            meta, body, quiz = parse(os.path.join(LESSONS, f))
            if meta.get("id"):
                out.append((meta["id"], f, meta, body, quiz))
    return out


def load_profile():
    return json.load(open(PROFILE_JSON, encoding="utf-8")) if os.path.exists(PROFILE_JSON) \
        else {"learner": "المتعلّم", "topics": {}}


def save_profile(p):
    json.dump(p, open(PROFILE_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def status_of(m):
    for thr, name in [(92, "🟣 بحثي"), (80, "🔵 متقدم"), (65, "🟢 متقن"),
                      (45, "🟡 متوسط"), (25, "🟠 مبتدئ"), (0, "🔴 غير معروف")]:
        if m >= thr:
            return name
    return "🔴 غير معروف"


def mastery_of(p, nid):
    return p.get("topics", {}).get(nid, {}).get("mastery", 0)


# ------------------------------------------------------- الشرح المتكيّف ----
def explain(mode, q, lesson_body):
    """خمس طرق للشرح (X.10) — تُستخدم عند الخطأ أو عند الطلب."""
    why = q.get("why", "")
    alt = q.get("alt", {})
    title = "شرح إضافي"
    if mode == "بسط":
        title = "شرح مبسّط جداً"
        text = alt.get("simple", why)
    elif mode == "تشبيه":
        title = "تشبيه"
        text = alt.get("analogy", "تخيّلها كوعاء يُفرغ: السؤال دائماً «كم بقي؟» و«كم مضى؟».")
    elif mode == "مثال":
        title = "مثال محلول"
        text = alt.get("example", "مثال: إن كان النشاط 100 وصار 25، فقد مرّ عمران نصف.")
    elif mode == "مخطط":
        title = "مخطط"
        text = alt.get("diagram", """
   الكمية │
       100│●
         │ ╲___
        50│     ●
         │       ╲_____
        25│            ●
         └────────────────► الزمن
              T½     2T½
        """)
    else:
        title = "شرح"
        text = alt.get("explain", why)
    print("\n" + "─" * 64)
    print(f"  {title}")
    print("─" * 64)
    print(text.strip())
    print("─" * 64 + "\n")


def ask_question(q, i, lesson_body, p, log):
    print(f"\nس{i}. {q['q']}")
    opts = q["o"]
    for j, o in enumerate(opts, 1):
        print(f"   {j}) {o}")
    attempts = 0
    while True:
        try:
            raw = input("   › ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return "stop", False
        if raw in ("توقف", "quit", "exit"):
            return "stop", False
        if raw in ("تخطي", "skip"):
            print(f"   ⏭  تجاوزنا. الجواب الصحيح: {opts[q['a']]}")
            return "next", False
        if raw in COMMANDS and raw not in ("تخطي", "توقف"):
            if raw == "سؤال":
                free = input("   ✍ اكتب سؤالك: ").strip()
                log.append(f"- سؤال أثناء الدرس: {free}")
                print("   📝 سُجّل في دفتر الباحث (progress/notebook.md).")
                continue
            if raw == "؟":
                print("   أوامر: شرح · بسط · مثال · تشبيه · مخطط · سؤال · تخطي · توقف")
                continue
            explain(raw, q, lesson_body)
            continue
        if raw.isdigit() and 1 <= int(raw) <= len(opts):
            ans = int(raw) - 1
            break
        print("   اكتب رقم الخيار، أو أحد الأوامر: شرح / بسط / مثال / تشبيه / مخطط / تخطي / توقف")
    attempts += 1
    if ans == q["a"]:
        print("   ✅ صحيح.")
        if q.get("why"):
            print(f"   💡 {q['why']}")
        return "next", True
    print(f"   ❌ ليس تماماً. الصحيح: {opts[q['a']]}")
    if q.get("why"):
        print(f"   💡 {q['why']}")
    print("   (اكتب «بسط» أو «تشبيه» أو «مثال» لأشرحها بطريقة أخرى، أو Enter للمتابعة)")
    try:
        nxt = input("   › ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return "next", False
    if nxt in COMMANDS and nxt not in ("تخطي", "توقف", "؟"):
        explain(nxt, q, lesson_body)
    return "next", False


# ------------------------------------------------------------- الجلسة ------
def run_lesson(lid, f, meta, body, quiz, p):
    print("\n" + "═" * 68)
    print(f"  {meta.get('title', f)}")
    print("═" * 68)
    print(body.strip())
    print("\n" + "═" * 68)
    print("  الآن الاختبار — يمكنك في أي لحظة كتابة: شرح/بسط/مثال/تشبيه/مخطط/سؤال/تخطي/توقف")
    print("═" * 68)
    try:
        input("  … اضغط Enter للبدء …")
    except (EOFError, KeyboardInterrupt):
        print()
        return None

    log = []
    score = 0
    answered = 0
    for i, q in enumerate(quiz, 1):
        state, ok = ask_question(q, i, body, p, log)
        if state == "stop":
            print("\n  (تم إنهاء الجلسة — لم تُحتسب النتيجة)")
            flush_log(lid, log, None)
            return "stop"
        if state == "next":
            answered += 1
            score += 1 if ok else 0

    pct = round(100.0 * score / max(1, len(quiz)))
    print("\n" + "═" * 68)
    print(f"  النتيجة: {score}/{len(quiz)} = {pct}٪")
    if pct >= PASS:
        print("  🟢 اجتزتَ البوابة المفاهيمية (≥80٪) — ننتقل للتالي.")
    elif pct >= 60:
        print("  🟡 قريب. أعد الدرس غداً (مراجعة متباعدة) ثم أعد الاختبار.")
    else:
        print("  🟠 لن نعاقبك (X.9): سنعيد الشرح بطريقة مختلفة في الجلسة القادمة.")

    # تسجيل
    try:
        node_ids = json.loads(meta.get("nodes", "[]").replace("'", '"'))
    except Exception:
        node_ids = []
    for nid in node_ids:
        prev = mastery_of(p, nid)
        if pct >= PASS:
            new = max(prev, min(85, pct))
        else:
            new = max(prev, min(45, pct))
        p.setdefault("topics", {})[nid] = {"level": "L2" if new >= 75 else "L1",
                                           "mastery": new, "status": status_of(new)}
    p["updated"] = datetime.date.today().isoformat()
    save_profile(p)
    if node_ids:
        print(f"  📝 سُجّل في: {', '.join(node_ids)}")
    flush_log(lid, log, pct)
    return pct


def flush_log(lid, log, pct):
    if not log and pct is None:
        return
    with open(NOTEBOOK, "a", encoding="utf-8") as fh:
        fh.write(f"\n\n## جلسة {datetime.date.today().isoformat()} — الدرس {lid}\n")
        if pct is not None:
            fh.write(f"- النتيجة: {pct}٪\n")
        for line in log:
            fh.write(line + "\n")


def choose_next(p, lessons):
    for lid, f, meta, body, quiz in lessons:
        try:
            nodes = json.loads(meta.get("nodes", "[]").replace("'", '"'))
        except Exception:
            nodes = []
        if nodes and min(mastery_of(p, n) for n in nodes) < PASS:
            return lid, f, meta, body, quiz
    return None


# --------------------------------------------------------------- main ------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson", default=None)
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    lessons = all_lessons()
    if not lessons:
        print("لا توجد دروس بعد.")
        return
    p = load_profile()

    if args.status:
        print("حالة الدروس:\n")
        for lid, f, meta, body, quiz in lessons:
            try:
                nodes = json.loads(meta.get("nodes", "[]").replace("'", '"'))
            except Exception:
                nodes = []
            ms = [mastery_of(p, n) for n in nodes] or [0]
            avg = min(ms)  # شرط الإتقان: كل عقد الدرس، لا المتوسط
            flag = "✅" if avg >= PASS else ("🟡" if avg >= 50 else "🔴")
            print(f"  {flag} {lid} — {meta.get('title','')} — متوسط الإتقان {avg:.0f}٪")
        return

    if args.lesson:
        target = next((x for x in lessons if x[0] == args.lesson), None)
        if not target:
            print("درس غير موجود. المتاح: " + ", ".join(x[0] for x in lessons))
            return
        lid, f, meta, body, quiz = target
    else:
        nxt = choose_next(p, lessons)
        if not nxt:
            print("🎉 كل الدروس المتاحة مجتازة. أضف دروساً جديدة في lessons/ أو قل «تابع».")
            return
        lid, f, meta, body, quiz = nxt

    while True:
        res = run_lesson(lid, f, meta, body, quiz, p)
        if res == "stop":
            return
        nxt = choose_next(p, lessons)
        if not nxt:
            print("\n🎉 أنهِتَ كل الدروس المتاحة. قل «تابع» لأضيف الدرس التالي.")
            return
        lid, f, meta, body, quiz = nxt
        print("\n" + "─" * 68)
        try:
            cont = input(f"الدرس التالي: {meta.get('title','')} — Enter للمتابعة أو «توقف»: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if cont in ("توقف", "quit", "exit"):
            return


if __name__ == "__main__":
    main()
