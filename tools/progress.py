#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف تقدّم المتعلّم + بوابات الانتقال (X.8 / X.9 / X.20).

الأوامر:
    python3 tools/progress.py init                       # إنشاء/تصفير الملف من الرسم
    python3 tools/progress.py show                       # عرض حالة التقدّم
    python3 tools/progress.py set <node-id> <L1..L5> <%> # تحديث موضوع
    python3 tools/progress.py quiz   <node-id>           # اختبار قصير (أسئلة نصية)
    python3 tools/progress.py report                     # تقرير فجوات + الجاهزية
    python3 tools/progress.py next                       # أفضل المواضيع التالية
    python3 tools/progress.py due                        # المستحق للمراجعة اليوم (X.19)
    python3 tools/progress.py review                     # جلسة مراجعة متباعدة (SM-2)
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from kg.schema import DOMAINS, LEVELS_0_14, load_nodes, registry, user_level  # noqa: E402

PROFILE_JSON = os.path.join(ROOT, "progress", "profile.json")
PROFILE_MD = os.path.join(ROOT, "progress", "profile.md")

STATUS = [(0, "🔴 غير معروف"), (25, "🟠 مبتدئ"), (45, "🟡 متوسط"),
          (65, "🟢 متقن"), (80, "🔵 متقدم"), (92, "🟣 بحثي")]


def status_of(mastery: float) -> str:
    s = STATUS[0][1]
    for thr, name in STATUS:
        if mastery >= thr:
            s = name
    return s


def load_profile():
    if os.path.exists(PROFILE_JSON):
        with open(PROFILE_JSON, encoding="utf-8") as f:
            return json.load(f)
    return {"learner": "المتعلّم", "updated": "", "notes": "", "topics": {}}


def save_profile(p):
    os.makedirs(os.path.dirname(PROFILE_JSON), exist_ok=True)
    with open(PROFILE_JSON, "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=2)
    write_md(p)


def write_md(p):
    nodes = registry()
    lines = ["# ملف تقدّم المتعلّم (X.8)\n",
             f"> مولّد تلقائياً من `progress/profile.json` عبر `tools/progress.py`.\n",
             f"- المتعلّم: **{p.get('learner', '—')}**",
             f"- آخر تحديث: **{p.get('updated', '—')}**\n",
             "| المجال | الموضوع | المستوى | الإتقان | الحالة |",
             "|---|---|---|---|---|"]
    topics = p.get("topics", {})
    for tid in sorted(topics, key=lambda t: (nodes[t].domain if t in nodes else "", t)):
        t = topics[tid]
        node = nodes.get(tid)
        name = node.ar if node else tid
        dom = DOMAINS[node.domain]["ar"] if node else "—"
        lines.append(f"| {dom} | {name} `{tid}` | {t.get('level','—')} | "
                     f"{t.get('mastery',0)}٪ | {status_of(t.get('mastery',0))} |")
    lines.append("")
    with open(PROFILE_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ------------------------------------------------- التكرار المتباعد (X.19) -----
def level_of(m):
    """تحويل نسبة الإتقان إلى مستوى L0..L5."""
    if m >= 92:
        return "L5"
    if m >= 80:
        return "L4"
    if m >= 65:
        return "L3"
    if m >= 45:
        return "L2"
    if m >= 25:
        return "L1"
    return "L0"


def sm2(topic: dict, q: int, today: str) -> dict:
    """خوارزمية SM-2 (SuperMemo 2) متباعدة الفواصل.

    q = جودة الاستذكار 0..5:
      5 استجابة مثالية · 4 صحيح بتردّد · 3 صحيح بصعوبة
      2 خطأ لكن تذكّرته بعد الإجابة · 1 خطأ وتذكّرت الإجابة · 0 نسيان تام
    """
    import datetime as _dt

    q = max(0, min(5, int(q)))
    ef = float(topic.get("ef", 2.5))
    reps = int(topic.get("reps", 0))
    iv = float(topic.get("interval", 0) or 0)

    if q < 3:
        reps, iv = 0, 1.0
    else:
        reps += 1
        iv = 1.0 if reps == 1 else (6.0 if reps == 2 else max(1.0, iv * ef))

    ef = ef + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    ef = max(1.3, min(3.0, ef))

    m = int(topic.get("mastery", 0) or 0)
    if q >= 4:
        m = min(100, m + 5)
    elif q == 3:
        m = min(100, m + 2)
    else:
        m = max(0, m - 8)

    topic["ef"] = round(ef, 3)
    topic["reps"] = reps
    topic["interval"] = round(iv, 2)
    topic["last_review"] = today
    topic["due"] = (_dt.date.fromisoformat(today) + _dt.timedelta(days=iv)).isoformat()
    topic["mastery"] = m
    topic["status"] = status_of(m)
    topic["level"] = level_of(m)
    return topic


def due_list(p, nodes, today, limit=20):
    """المواضيع المستحقة للمراجعة اليوم: المستحقة + التي بدأت ولم تُجدول."""
    items = []
    for nid, t in p.get("topics", {}).items():
        m = t.get("mastery", 0) or 0
        if m <= 0:
            continue
        due = t.get("due")
        if due is None:                       # بدأ ولم يُجدول بعد ⇒ يستحق الآن
            items.append((nid, t, True))
        elif due <= today:
            items.append((nid, t, False))
    items.sort(key=lambda x: (x[2] is False, x[1].get("mastery", 0)))
    return items[:limit]


def cmd_due(args):
    p = load_profile()
    nodes = registry()
    items = due_list(p, nodes, args.today)
    print(f"\n=== مستحق للمراجعة ({args.today}) ===")
    if not items:
        print("  لا شيء مستحق. (ابدأ موضوعاً جديداً: python3 tools/progress.py next)")
        return
    print("  #  الموضوع                                   الإتقان  الفاصل  الاستحقاق")
    print("  ─────────────────────────────────────────────────────────────────────")
    for i, (nid, t, newbie) in enumerate(items, 1):
        n = nodes.get(nid)
        name = (n.ar if n else nid)[:36]
        print(f"  {i:2d} {name:<38} {t.get('mastery',0):>5}٪  "
              f"{t.get('interval','—'):>6}  {t.get('due','الآن') if not newbie else 'غير مُجدول'}")
    print(f"\n  شغّل: python3 tools/progress.py review")


def cmd_review(args):
    """جلسة مراجعة متباعدة: استذكار نشط ثم تقييم ذاتي 0..5."""
    import datetime as _dt

    p = load_profile()
    nodes = registry()
    items = due_list(p, nodes, args.today, limit=args.limit)
    if not items:
        print("لا شيء مستحق للمراجعة اليوم.")
        return

    print("\n=== جلسة مراجعة متباعدة (X.19) ===")
    print("القاعدة: **استذكر قبل أن تكشف الإجابة** — القيمة كلها في المحاولة، لا في الجواب.\n")
    done = 0
    for nid, t, _ in items:
        n = nodes.get(nid)
        name = n.ar if n else nid
        print("─" * 64)
        print(f"📘 {name}  (`{nid}`)")
        print(f"   إتقانك الآن: {t.get('mastery',0)}٪ · مراجعات سابقة: {t.get('reps',0)} · "
              f"الفاصل: {t.get('interval','—')} يوم")
        if n and n.concepts:
            print(f"   المفاهيم المطلوبة ({len(n.concepts)}):")
        try:
            input("   ✍️  اذكر ما تتذكره الآن (بصوت أو كتابة)، ثم اضغط Enter للكشف… ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if n and n.concepts:
            for c in n.concepts:
                print(f"      • {c}")
        if n and n.eqs:
            print("   المعادلات:")
            for e in n.eqs[:4]:
                print(f"      › {e}")
        if n and n.prereqs:
            pre = ", ".join(f"{(nodes[q].ar if q in nodes else q)}" for q in n.prereqs[:4])
            print(f"   يفترض: {pre}")
        try:
            q = input("؟ قيّم استذكارك من 0 (نسيت تماماً) إلى 5 (مثالي): ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if q == "" or not q.isdigit():
            print("   (تخطّي)")
            continue
        t2 = sm2(p["topics"][nid], int(q), args.today)
        p["topics"][nid] = t2
        done += 1
        print(f"   → الفاصل القادم: {t2['interval']} يوم · الاستحقاق: {t2['due']} · "
              f"الإتقان: {t2['mastery']}٪ ({t2['status']})")
        if args.limit and done >= args.limit:
            break

    if done:
        p["updated"] = args.today
        save_profile(p)
        print(f"\n✅ رُوجعت {done} موضوعاً · حدّث ملف التقدّم.")


# ---------------------------------------------------------------- أوامر -----
def cmd_init(args):
    nodes = load_nodes()
    p = {"learner": args.name or "المتعلّم", "updated": args.today, "notes": "",
         "topics": {}}
    if args.all:
        for n in nodes:
            p["topics"][n.id] = {"level": "L0", "mastery": 0, "status": status_of(0)}
    save_profile(p)
    print(f"✅ أُنشئ الملف بـ{len(p['topics'])} موضوعاً.")


def cmd_show(args):
    p = load_profile()
    nodes = registry()
    topics = p.get("topics", {})
    if not topics:
        print("الملف فارغ — نفّذ: python3 tools/progress.py init --all")
        return
    tot = len(nodes)
    done = sum(1 for t, v in topics.items() if v.get("mastery", 0) >= 65)
    avg = sum(v.get("mastery", 0) for v in topics.values()) / max(1, len(topics))
    print(f"المتعلّم: {p.get('learner')} | آخر تحديث: {p.get('updated','—')}")
    print(f"المواضيع المسجّلة: {len(topics)}/{tot} | المتقنة (≥65٪): {done} | "
          f"متوسط الإتقان: {avg:.1f}٪\n")
    by_dom = {}
    for tid, v in topics.items():
        n = nodes.get(tid)
        d = n.domain if n else "?"
        by_dom.setdefault(d, []).append(v.get("mastery", 0))
    print("| المجال | عدد مسجّل | متوسط الإتقان |")
    print("|---|---|---|")
    for d, vals in sorted(by_dom.items(), key=lambda kv: -sum(kv[1]) / len(kv[1])):
        name = DOMAINS.get(d, {}).get("ar", d)
        print(f"| {name} | {len(vals)} | {sum(vals)/len(vals):.0f}٪ |")


def cmd_set(args):
    p = load_profile()
    nodes = registry()
    if args.node not in nodes:
        print(f"⚠️  معرّف غير معروف: {args.node}")
        return
    lvl = args.level.upper()
    if lvl not in {"L1", "L2", "L3", "L4", "L5", "L0"}:
        print("المستوى يجب أن يكون L1..L5 (أو L0)")
        return
    m = max(0, min(100, int(args.mastery)))
    p.setdefault("topics", {})[args.node] = {"level": lvl, "mastery": m,
                                             "status": status_of(m)}
    p["updated"] = args.today
    save_profile(p)
    print(f"✅ {nodes[args.node].ar} ({args.node}) → {lvl} · {m}٪ · {status_of(m)}")


def cmd_report(args):
    p = load_profile()
    nodes = registry()
    topics = p.get("topics", {})
    ready, blocked, weak = [], [], []
    for n in sorted(nodes.values(), key=lambda x: (user_level(x), x.id)):
        v = topics.get(n.id, {})
        m = v.get("mastery", 0)
        missing = [q for q in n.prereqs if topics.get(q, {}).get("mastery", 0) < 65]
        if missing:
            blocked.append((n, missing, m))
        elif m < 65:
            ready.append((n, m))
        if 0 < m < 65:
            weak.append((n, m))
    print("=== تقرير الفجوات (X.20) ===")
    print(f"مواضيع جاهزة للدراسة (شروط مستوفاة، إتقان <65٪): {len(ready)}")
    print(f"مواضيع محجوبة لشروط ناقصة: {len(blocked)}")
    print(f"مواضيع بدأت ولم تُتقن: {len(weak)}\n")

    print("— أعلى 15 مواضيع تأثيراً (تفتح أكبر عدد من المواضيع):")
    impact = {n.id: sum(1 for m in nodes.values() if n.id in m.prereqs) for n in nodes.values()}
    top = sorted(nodes.values(), key=lambda n: -impact[n.id])[:15]
    for n in top:
        cnt = impact[n.id]
        m = topics.get(n.id, {}).get("mastery", 0)
        print(f"   {n.ar} `{n.id}` — يفتح {cnt} موضوعاً — إتقانك: {m}٪")

    if blocked:
        print("\n— أمثلة على مواضيع محجوبة (اكتشف السبب):")
        for n, missing, m in blocked[:10]:
            miss = "، ".join(f"{nodes[q].ar} ({topics.get(q,{}).get('mastery',0)}٪)"
                             for q in missing)
            print(f"   {n.ar} — ينقصه: {miss}")


def cmd_next(args):
    p = load_profile()
    nodes = registry()
    topics = p.get("topics", {})
    cands = []
    for n in nodes.values():
        m = topics.get(n.id, {}).get("mastery", 0)
        if m >= 80:
            continue
        if any(topics.get(q, {}).get("mastery", 0) < 65 for q in n.prereqs):
            continue
        impact = sum(1 for m2 in nodes.values() if n.id in m2.prereqs)
        cands.append((impact + (0 if n.depth == "core" else -3), -n.hours, n))
    cands.sort(key=lambda t: (-t[0], -t[1]))
    print("=== الخطوة التالية المقترحة (X.28) ===")
    for _, _, n in cands[:8]:
        lv = user_level(n)
        print(f"- {n.ar} `{n.id}` — المستوى {lv} ({LEVELS_0_14[lv]}) · "
              f"{n.hours} ساعة · صعوبة {n.diff}/5 · {n.depth}")


def cmd_quiz(args):
    nodes = registry()
    if args.node not in nodes:
        print("معرّف غير معروف")
        return
    n = nodes[args.node]
    print(f"=== اختبار قصير: {n.ar} ({n.en}) — المستوى {user_level(n)} ===")
    print("\n١) المفاهيم — اشرح باختصار:")
    for c in n.concepts[:4]:
        print(f"   • {c}")
    if n.eqs:
        print("\n٢) المعادلات — اكتب واشرح حدود كل رمز:")
        for e in n.eqs:
            print(f"   • {e}")
    if n.apps:
        print("\n٣) تطبيقات — اذكر مثالاً عملياً لكل من:")
        for a in n.apps[:3]:
            print(f"   • {a}")
    print("\n٤) سؤال ربط: اربط هذا الموضوع بموضوع سابق درسته، وبتطبيق فعلي.")
    print("\n٥) سؤال نقدي: ما افتراضٌ غير معلن في هذا الموضوع؟ وما أثر انهياره؟")
    print("\nصحّح إجابتك بمراجعة مفاهيم العقدة في graph/knowledge_graph.json، "
          "ثم سجّل النتيجة:")
    print(f"   python3 tools/progress.py set {n.id} L2 <النسبة>")


def main():
    import datetime
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--today", default=datetime.date.today().isoformat())

    ap = argparse.ArgumentParser(parents=[common])
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init", parents=[common])
    s.add_argument("--all", action="store_true")
    s.add_argument("--name")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("show", parents=[common]); s.set_defaults(func=cmd_show)
    s = sub.add_parser("report", parents=[common]); s.set_defaults(func=cmd_report)
    s = sub.add_parser("next", parents=[common]); s.set_defaults(func=cmd_next)

    s = sub.add_parser("set", parents=[common])
    s.add_argument("node"); s.add_argument("level"); s.add_argument("mastery")
    s.set_defaults(func=cmd_set)

    s = sub.add_parser("quiz", parents=[common])
    s.add_argument("node")
    s.set_defaults(func=cmd_quiz)

    s = sub.add_parser("due", parents=[common], help="المستحق للمراجعة اليوم")
    s.set_defaults(func=cmd_due)

    s = sub.add_parser("review", parents=[common], help="جلسة مراجعة متباعدة (SM-2)")
    s.add_argument("--limit", type=int, default=10)
    s.set_defaults(func=cmd_review)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
