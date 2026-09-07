#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_lesson — مولّد دروس من عُقد الرسم المعرفي.

الفكرة: كل عقدة في الرسم (247 عقدة) تحوي مفاهيم ومعادلات وتطبيقات ومصادر
مكتوبة بيد الخبراء. هذا المولّد يأخذ العقدة ويبني منها **مسوّدة درس كاملة**
بالهيكل المكوّن من 16 عنصراً + اختبار من 5 أسئلة قابل للتصحيح الآلي
(مُولَّد من بيانات العقدة نفسها، مع مشتّتات من عُقد أخرى حتى لا يكون الجواب بديهياً).

التوليد **حتمي**: بذرة الرقم العشوائي مشتقة من معرّف العقدة، فالدرس نفسه
يُنتَج نفسه في كل مرة.

الاستخدام:
    python3 tools/gen_lesson.py list                 # العُقد بلا درس
    python3 tools/gen_lesson.py gen rx.criticality   # يولّد درساً لعقدة
    python3 tools/gen_lesson.py gen --ready          # العقدة «الجاهزة للدراسة الآن»
    python3 tools/gen_lesson.py gen --level 0        # كل عقد المستوى 0
    python3 tools/gen_lesson.py gen --all --limit 10 # أول 10 بلا دروس
    python3 tools/gen_lesson.py preview nuc.fission  # يعرض دون كتابة ملف

ملاحظة أمان: لا يولّد المولّد محتوى في النطاقات الثلاثة الممتنعة (MAP/18) —
فهو يستمدّ مادته من حقول العقدة المنشورة فقط، ويُنتج أسئلة «تعرّف واستدعاء»
لا «خطوات تنفيذ».
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from kg.schema import DOMAINS, DEPTHS, SOURCES, STAGES, registry  # noqa: E402

LESSONS = os.path.join(ROOT, "lessons")
PROFILE = os.path.join(ROOT, "progress", "profile.json")
PASS = 80


# ------------------------------------------------------------------ مساعدات
def deps_map(nodes):
    """id → قائمة العُقد التي تعتمد عليه (محسوبة من حقل prereqs)."""
    dep = {i: [] for i in nodes}
    for n in nodes.values():
        for p in (n.prereqs or []):
            if p in dep:
                dep[p].append(n.id)
    return dep


def load_profile():
    if os.path.exists(PROFILE):
        try:
            return json.load(open(PROFILE, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            pass
    return {"topics": {}}


def mastery_of(prof, nid):
    t = prof.get("topics", {}).get(nid) or {}
    m = t.get("mastery", 0)
    return m if isinstance(m, (int, float)) else 0


def existing_node_map():
    """خريطة: معرّف العقدة → ملف الدرس (من الواجهات الأمامية lessons/*.md)."""
    out = {}
    if not os.path.isdir(LESSONS):
        return out
    for f in sorted(os.listdir(LESSONS)):
        if not f.endswith(".md"):
            continue
        txt = open(os.path.join(LESSONS, f), encoding="utf-8").read()
        m = re.search(r'^nodes:\s*\[(.*?)\]', txt, re.M)
        if not m:
            continue
        ids = re.findall(r'"([^"]+)"|\'([^\']+)\'', m.group(1))
        for a, b in ids:
            nid = a or b
            if nid:
                out[nid] = f
    return out


def next_lesson_id():
    used = set()
    if os.path.isdir(LESSONS):
        for f in os.listdir(LESSONS):
            m = re.match(r"(\d{3})-", f)
            if m:
                used.add(int(m.group(1)))
    i = 0
    while i in used:
        i += 1
    return f"{i:03d}"


def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:40] or "lesson"


def fmt_sources(keys):
    if not keys:
        return "- (أضف مصدراً: راجع MAP/09 لتصنيف المصادر A/B/C/D)"
    out = []
    for k in keys:
        meta = SOURCES.get(k)
        if not meta:
            out.append(f"- `{k}` (غير مسجّل في السجل — أضفه إلى `tools/kg/schema.py`)")
            continue
        lvl = meta.get("level", "?")
        url = meta.get("url", "")
        line = f"- **{meta.get('ar', k)}** — تصنيف `{lvl}`"
        if url:
            line += f" — <{url}>"
        out.append(line)
    return "\n".join(out)


def pick_others(nodes, node, pool_attr, k, rng):
    """يختار k عناصر «مشتّتة» من عُقد أخرى (لا من العقدة نفسها)."""
    items = []
    for other in nodes.values():
        if other.id == node.id:
            continue
        vals = getattr(other, pool_attr, None) or []
        if vals:
            items.append(vals[rng.randrange(len(vals))])
    rng.shuffle(items)
    seen, out = set(), []
    for it in items:
        key = it.strip()
        if key and key not in seen:
            seen.add(key)
            out.append(it)
        if len(out) >= k:
            break
    return out


def make_mcq(rng, q, correct, distractors, why, simple=None, kind="concept"):
    opts = [correct] + list(distractors)
    # أزل التكرار
    clean, seen = [], set()
    for o in opts:
        if o not in seen:
            seen.add(o)
            clean.append(o)
    while len(clean) < 4:
        clean.append("—")
    idx = list(range(len(clean)))
    rng.shuffle(idx)
    shuffled = [clean[i] for i in idx]
    ans = shuffled.index(correct)
    item = {"q": q, "o": shuffled, "a": ans, "why": why, "k": kind}
    if simple:
        item["alt"] = {"simple": simple}
    return item


# ------------------------------------------------------------------ التوليد
def build_quiz(node, nodes, rng, dep=None):
    dep = dep if dep is not None else deps_map(nodes)
    qs = []
    concepts = list(node.concepts or [])
    eqs = list(node.eqs or [])
    apps = list(node.apps or [])
    pres = [p for p in (node.prereqs or []) if p in nodes]
    deps = [d for d in dep.get(node.id, []) if d in nodes]

    if concepts:
        c = concepts[rng.randrange(len(concepts))]
        qs.append(make_mcq(
            rng, f"أيّ مما يلي يُعدّ من مفاهيم «{node.ar}»؟",
            c, pick_others(nodes, node, "concepts", 3, rng),
            why=f"من قائمة مفاهيم العقدة `{node.id}`: {c}",
            simple=f"الموضوع يتمحور حول: {c}", kind="concept"))

    if eqs:
        e = eqs[rng.randrange(len(eqs))]
        qs.append(make_mcq(
            rng, f"أيّ معادلة تنتمي إلى «{node.ar}»؟",
            e, pick_others(nodes, node, "eqs", 3, rng),
            why=f"هذه إحدى معادلات `{node.id}`؛ راجع قسم «المعادلات الأساسية» في الدرس.",
            simple="احفظ معادلة واحدة محورية لكل موضوع، واشتقّ الباقي منها.", kind="calc"))

    if pres:
        p = pres[rng.randrange(len(pres))]
        qs.append(make_mcq(
            rng, f"أيّ موضوع يُعدّ شرطاً مسبقاً لدراسة «{node.ar}»؟",
            f"{nodes[p].ar} (`{p}`)",
            [f"{nodes[o].ar} (`{o}`)" for o in _unrelated(nodes, node, 3, rng, dep)],
            why=f"`{p}` مدرج في شروط `{node.id}` في الرسم المعرفي.",
            simple="الشرط المسبق هو ما تفترضه معلومةً قبل أن تبدأ.", kind="concept"))

    if deps:
        d = deps[rng.randrange(len(deps))]
        qs.append(make_mcq(
            rng, f"إتقان «{node.ar}» يفتح لك الطريق إلى أيّ موضوع لاحقاً؟",
            f"{nodes[d].ar} (`{d}`)",
            [f"{nodes[o].ar} (`{o}`)" for o in _unrelated(nodes, node, 3, rng, dep)],
            why=f"`{d}` يعتمد على `{node.id}` في الرسم المعرفي.",
            simple="كل موضوع يفتح أبواباً؛ اعرف أين يوصلك قبل أن تدرسه.", kind="concept"))

    if apps:
        a = apps[rng.randrange(len(apps))]
        qs.append(make_mcq(
            rng, f"أيّ تطبيق عملي ينتمي إلى «{node.ar}»؟",
            a, pick_others(nodes, node, "apps", 3, rng),
            why=f"من تطبيقات `{node.id}`: {a}",
            simple="التطبيق هو ما يجعل الموضوع يستحق الوقت.", kind="concept"))

    # سؤال مصطلحات (ثنائي اللغة) — يغذّي بُعد «المصطلحات» في بوابات X.9
    others = [n for n in nodes.values() if n.id != node.id and n.en and n.en != node.en]
    if others and node.en:
        rng.shuffle(others)
        qs.append(make_mcq(
            rng, f"ما المقابل الإنجليزي لمصطلح «{node.ar}»؟",
            node.en,
            [o.en for o in others[:3]],
            why=f"`{node.id}` = {node.ar} / {node.en}",
            simple="المصطلحات الإنجليزية ضرورية: 95٪ من الأدبيات بهذه اللغة.",
            kind="term"))
    return qs


def _unrelated(nodes, node, k, rng, dep=None):
    dep = dep if dep is not None else deps_map(nodes)
    pool = [n for n in nodes.values()
            if n.id != node.id
            and n.id not in (node.prereqs or [])
            and n.id not in dep.get(node.id, [])]
    rng.shuffle(pool)
    return [n.id for n in pool[:k]]


def build_lesson(nid, nodes, prof, lid=None, dep=None):
    dep = dep if dep is not None else deps_map(nodes)
    node = nodes.get(nid)
    if node is None:
        raise SystemExit(f"⚠️  عقدة غير معروفة: {nid}")
    rng = random.Random(nid)          # توليد حتمي
    lid = lid or next_lesson_id()
    pres = [p for p in (node.prereqs or []) if p in nodes]
    deps = [d for d in dep.get(nid, []) if d in nodes]
    dom = DOMAINS.get(node.domain, {}).get("ar", node.domain)
    stage_ar = STAGES.get(node.stage, "")
    depth_ar = DEPTHS.get(node.depth, node.depth)

    pre_lines = "\n".join(
        f"- {nodes[p].ar} (`{p}`) — إتقانك الحالي: {mastery_of(prof, p)}٪"
        + ("  ⚠️ أنقص من 80٪ — راجعه أولاً" if mastery_of(prof, p) < PASS else "  ✅")
        for p in pres) or "- لا شيء — هذه نقطة بداية في الرسم."

    dep_lines = "\n".join(
        f"- {nodes[d].ar} (`{d}`) — إتقانك: {mastery_of(prof, d)}٪" for d in deps[:8]
    ) or "- (لا يعتمد عليه شيء بعد — نهاية فرع)"

    concepts_lines = "\n".join(f"{i+1}. **{c}**" for i, c in enumerate(node.concepts or [])) \
        or "- (أضف 3–5 مفاهيم للعقدة في `tools/kg/nodes_*.py`)"

    if node.eqs:
        eq_lines = "\n".join(f"| `{e}` |" for e in node.eqs)
        eq_block = "| المعادلة |\n|---|\n" + eq_lines
    else:
        eq_block = "(لا معادلات مسجّلة لهذه العقدة — أضفها إن وُجدت.)"

    apps_lines = "\n".join(f"- {a}" for a in (node.apps or [])) or "- (أضف تطبيقات)"
    quiz = build_quiz(node, nodes, rng, dep)
    quiz_json = json.dumps(quiz, ensure_ascii=False, indent=1)
    ex_lines = "\n".join(
        f"{i+1}. اشرح بلسانك، في 3 أسطر: **{c}**"
        for i, c in enumerate((node.concepts or [])[:5])) or "1. اكتب ما تعرفه عن الموضوع."

    tags = " · ".join(f"`{t}`" for t in (node.tags or [])) or "—"

    body = f"""---
id: {lid}
title: "{node.ar}"
nodes: ["{node.id}"]
stage: {node.stage}
generated: true
---

# {node.ar}

> **مسوّدة مولّدة آلياً** من عقدة الرسم `{node.id}` عبر `tools/gen_lesson.py`.
> المادة العلمية (المفاهيم، المعادلات، التطبيقات، المصادر) مأخوذة من بيانات العقدة
> التي كتبها الخبراء. ما يليها من شرحٍ وتمثيلٍ هو **مهمتك أنت** — أكمله في
> `progress/notebook.md`، ثم حسّن هذا الملف.

**بطاقة الموضوع:** مجال **{dom}** · المرحلة {node.stage} ({stage_ar}) ·
العمق: {depth_ar} · الصعوبة {node.diff}/5 · زمن التقدير {node.hours} ساعة ·
الوسوم: {tags}

## 1) ما هو؟
**{node.ar}** ({node.en}) — موضوع في مجال **{dom}**.

## 2) لماذا يهم؟
لأنه يفتح لك الطريق إلى:
{dep_lines}

## 3) المتطلبات السابقة
{pre_lines}

## 4) الفكرة الأساسية
{(node.concepts or ["—"])[0]}

## 5) شرح مبسط (مهمتك)
اكتب تشبيهاً من حياتك يشرح الفكرة الأساسية أعلاه في سطرين.
قاعدة التشبيه الجيد: **إن احتجت إلى شرح التشبيه، فهو ليس تشبيهاً**.

## 6) شرح جامعي
{concepts_lines}

## 7) المعادلات الأساسية
{eq_block}

## 8) مثال محلول (مهمتك)
اختر معادلة من القسم 7، وضع فيها أرقاماً واقعية من مصدر منشور
(مثال: بيانات IAEA PRIS، أو ENDF، أو مسألة من Lamarsh)، ثم:
1. اكتب المعطيات بوحداتها · 2. احسب · 3. **تحقق بالأبعاد** ·
4. اسأل: هل الناتج معقول بالحسّ؟ (قارنه برقم تعرفه من نفس المجال)

## 9) تطبيقات
{apps_lines}

## 10) أخطاء شائعة
- الخلط بين هذا الموضوع وما يشبهه: راجع «الشروط المسبقة» و«ما يفتحه» أعلاه.
- الحفظ دون تطبيق: كل مفهوم لم تُطبّقه في مسألة هو معرفة هشّة.
- نسيان الوحدات — راجع `MAP/07-commonly-forgotten.md` (قائمة التدقيق المضادة).

## 11) علاقته بموضوعات أخرى
**يفترض:** {' · '.join(f'`{p}`' for p in pres) or '—'}
**يُفضي إلى:** {' · '.join(f'`{d}`' for d in deps[:6]) or '—'}

## 12) أسئلة الاختبار
`python3 tools/tutor.py --lesson {lid}` (أو `python3 tools/lesson.py quiz {lid}`)

## 13) تمارين
{ex_lines}

## 14) مشروع تطبيقي آمن
صِف الموضوع في **صفحة واحدة** لشخص متخصص في مجال آخر، ثم اطلب منه أن يشرحه لك
بكلماته. إن اختلفت الصورتان، فالفجوة هي بالضبط ما لم تفهمه بعد.
(قياس بديل: اكتب 5 أسئلة يُفترض أن يجيب عنها من أتقن الموضوع — ثم أجب عنها.)

## 15) مصادر للتعمق
{fmt_sources(node.sources)}

## 16) ما المستوى التالي؟
{(chr(10) + '- ' + nodes[deps[0]].ar + f' (`{deps[0]}`)') if deps else '- (نهاية هذا الفرع — عد إلى MAP/04 لترتيب الدراسة)'}

## ملحق: كيف نعرف؟ كيف نقيس؟ أين الحدود؟ (X.16)
- **كيف نعرف؟** أي مصدر في القسم 15 — اذكر **تجربة أو قياساً** يقف وراء كل مفهوم.
- **كيف نقيس؟** ما الكمية المقاسة فعلياً، وما الكمية المحسوبة؟ ما أداة القياس؟
- **أين الحدود؟** ما نطاق صلاحية كل معادلة أعلاه، وماذا يحدث خارجه؟
- **ماذا لا نعرف؟** افتح `MAP/13-open-problems.md` وابحث عن مسألة مفتوحة تمسّ هذا الموضوع.

```quiz
{quiz_json}
```
"""
    return lid, body


def main() -> int:
    ap = argparse.ArgumentParser(description="مولّد دروس من عُقد الرسم المعرفي")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("list", help="العُقد التي لا درس لها")

    g = sub.add_parser("gen", help="توليد درس/دروس")
    g.add_argument("node", nargs="?", help="معرّف العقدة (مثال rx.criticality)")
    g.add_argument("--ready", action="store_true", help="العقدة الجاهزة للدراسة الآن")
    g.add_argument("--level", type=int, help="كل عُقد مستوىً معيّن")
    g.add_argument("--all", action="store_true", help="كل العُقد بلا دروس")
    g.add_argument("--limit", type=int, default=1)
    g.add_argument("--dry-run", action="store_true", help="اعرض دون كتابة")
    g.add_argument("--force", action="store_true", help="أعد توليد درس مولّد سابق في مكانه")

    p = sub.add_parser("preview", help="عرض درس دون كتابة ملف")
    p.add_argument("node")

    args = ap.parse_args()
    nodes = registry()
    dep = deps_map(nodes)
    prof = load_profile()
    covered = existing_node_map()

    if args.cmd == "list":
        miss = [n for n in nodes.values() if n.id not in covered]
        print(f"العُقد: {len(nodes)} · لها درس: {len(covered)} · بلا درس: {len(miss)}\n")
        for n in sorted(miss, key=lambda x: (x.stage, x.graph_level if hasattr(x, "graph_level") else 0, x.id))[:40]:
            print(f"  {n.id:<28} {n.ar}  (مرحلة {n.stage}، {n.hours}س)")
        if len(miss) > 40:
            print(f"  … و{len(miss)-40} عقدة أخرى")
        return 0

    targets = []
    if args.cmd == "preview":
        targets = [args.node]
    else:
        if args.node:
            targets = [args.node]
        elif args.ready:
            ready = [n.id for n in nodes.values()
                     if n.id not in covered
                     and mastery_of(prof, n.id) < PASS
                     and all(mastery_of(prof, p) >= PASS for p in (n.prereqs or []))]
            targets = ready[:max(1, args.limit)]
        elif args.level is not None:
            targets = [n.id for n in nodes.values()
                       if n.id not in covered and n.stage == args.level][:max(1, args.limit)]
        elif args.all:
            targets = [n.id for n in nodes.values() if n.id not in covered][:max(1, args.limit)]
        else:
            ap.print_help()
            return 2

    written = []
    for nid in targets:
        prev = covered.get(nid)
        lid = None
        if prev and getattr(args, "force", False):
            m = re.match(r"(\d{3})-", prev)
            if m:
                lid = m.group(1)
        lid, body = build_lesson(nid, nodes, prof, lid=lid, dep=dep)
        fname = f"{lid}-{slugify(nid.replace('.', '-'))}.md"
        path = os.path.join(LESSONS, fname)
        if args.cmd == "preview" or getattr(args, "dry_run", False):
            print(body)
            continue
        os.makedirs(LESSONS, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
        written.append((lid, nid, fname, len(build_quiz(nodes[nid], nodes, random.Random(nid), dep))))
        print(f"✅ {fname}  ({nid}) — {len(build_quiz(nodes[nid], nodes, random.Random(nid), dep))} أسئلة")

    if written:
        print(f"\n{len(written)} درساً جديداً. جرّب: python3 tools/tutor.py --lesson {written[0][0]}")
        print("حدّث الفهرس: python3 tools/site_index.py · وفّحص: python3 tools/selftest.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
