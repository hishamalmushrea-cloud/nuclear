#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة بناء الخريطة المعرفية (Curriculum Architect + Knowledge Graph Manager).

ماذا تفعل:
  1. تجمع كل العقد من tools/kg/nodes_*.py.
  2. تتحقق من السلامة: معرّفات مكررة، شروط مسبقة مجهولة، دورات (cycles)،
     عقد يتيمة، تناقض المرحلة مع الشروط المسبقة.
  3. تحسب: الترتيب الطوبولوجي للدراسة، العمق في الرسم، المسارات الحرجة،
     الروابط المقترحة (related) من تقاسم الشروط المسبقة.
  4. تُصدر:
       graph/knowledge_graph.json
       graph/edges.csv
       MAP/01-grand-tree.md     (الشجرة الكبرى — مولّد)
       MAP/03-prerequisites.md  (جدول المتطلبات — مولّد)
       MAP/04-study-order.md    (ترتيب الدراسة — مولّد)
       site/graph_data.json     (للعارض التفاعلي)

الاستخدام:
    python3 tools/build.py            # بناء كامل
    python3 tools/build.py --check    # تحقق فقط بدون كتابة ملفات
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict, deque

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from kg.schema import (DOMAINS, STAGES, DEPTHS, SOURCES, LEVELS_0_14,  # noqa: E402
                       user_level, load_nodes, registry)

OUT_GRAPH = os.path.join(ROOT, "graph")
OUT_MAP = os.path.join(ROOT, "MAP")
OUT_SITE = os.path.join(ROOT, "site")

DEPTH_ORDER = {"core": 0, "supporting": 1, "advanced": 2, "specialized": 3, "research": 4}


# ------------------------------------------------------------------ تحقق -----
def validate(nodes, reg):
    errors, warnings = [], []

    ids = [n.id for n in nodes]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errors.append(f"معرّفات مكررة: {sorted(dup)}")

    for n in nodes:
        for p in n.prereqs:
            if p not in reg:
                errors.append(f"{n.id}: شرط مسبق غير موجود → {p}")
            if p == n.id:
                errors.append(f"{n.id}: شرط مسبق يشير إلى نفسه")

    # دورات
    color = {n.id: 0 for n in nodes}
    stack_cycle = []

    def dfs(u, path):
        color[u] = 1
        path.append(u)
        for v in reg[u].prereqs:
            if v not in reg:
                continue
            if color[v] == 0:
                dfs(v, path)
            elif color[v] == 1:
                stack_cycle.append(" → ".join(path[path.index(v):] + [v]))
        path.pop()
        color[u] = 2

    for n in nodes:
        if color[n.id] == 0:
            dfs(n.id, [])
    for c in stack_cycle:
        errors.append(f"دورة في الشروط المسبقة: {c}")

    # تناقض المرحلة: أي شرط مسبق يجب أن يكون في مرحلة ≤ مرحلة العقدة
    for n in nodes:
        for p in n.prereqs:
            if p in reg:
                pr = reg[p]
                if pr.stage > n.stage:
                    warnings.append(
                        f"{n.id} (مرحلة {n.stage}) يعتمد على {p} (مرحلة {pr.stage})"
                    )

    # عقد يتيمة (لا شرط مسبق ولا يعتمد عليها أحد)
    dependents = defaultdict(list)
    for n in nodes:
        for p in n.prereqs:
            dependents[p].append(n.id)
    for n in nodes:
        if not n.prereqs and not dependents[n.id]:
            warnings.append(f"عقدة معزولة: {n.id}")
    return errors, warnings, dependents


# ------------------------------------------------------- حسابات على الرسم ----
def compute_levels(nodes, reg):
    """أطول مسار من الجذور = مستوى العقدة في الرسم."""
    indeg = {n.id: len([p for p in n.prereqs if p in reg]) for n in nodes}
    children = defaultdict(list)
    for n in nodes:
        for p in n.prereqs:
            if p in reg:
                children[p].append(n.id)
    q = deque(sorted([i for i, d in indeg.items() if d == 0]))
    lvl = {i: 0 for i in indeg}
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in children[u]:
            lvl[v] = max(lvl[v], lvl[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return lvl, topo, children


def compute_related(nodes, children, reg, max_links=6):
    """روابط مقترحة: إخوة (يتقاسمون شرطاً مسبقاً) + آباء + أبناء."""
    siblings = defaultdict(set)
    parents = defaultdict(set)
    for n in nodes:
        for p in n.prereqs:
            if p in reg:
                parents[n.id].add(p)
                siblings[p].add(n.id)
    rel = {}
    for n in nodes:
        s = set()
        for p in parents[n.id]:
            s |= (siblings[p] - {n.id})
        s |= set(children[n.id])
        s |= parents[n.id]
        s.discard(n.id)
        # رتّب: الأقرب في المرحلة ثم المجال
        scored = sorted(
            s, key=lambda x: (abs(reg[x].stage - n.stage), x != n.domain and reg[x].domain != n.domain, x)
        )
        rel[n.id] = scored[:max_links]
    return rel


def critical_path(nodes, reg, lvl):
    """أطول مسار زمني (بالساعات) في الرسم — «العمود الفقري للمنهج»."""
    best = {n.id: (n.hours, [n.id]) for n in nodes}
    for n in sorted(nodes, key=lambda x: lvl[x.id]):
        for p in n.prereqs:
            if p not in reg:
                continue
            cand = (best[p][0] + n.hours, best[p][1] + [n.id])
            if cand[0] > best[n.id][0]:
                best[n.id] = cand
    end = max(best.values(), key=lambda t: t[0])
    return end


# ------------------------------------------------------------- المولّدات -----
def md_header(title, sub=""):
    return (f"# {title}\n\n{sub}\n\n"
            "> ⚙️ **هذا ملف مولّد آلياً.** لا تعدّله يدوياً: عدّل البيانات في "
            "`tools/kg/nodes_*.py` ثم نفّذ `python3 tools/build.py`.\n\n")


def gen_tree(nodes, reg, lvl):
    by_dom = defaultdict(list)
    for n in nodes:
        by_dom[n.domain].append(n)
    lines = [md_header("MAP/01 — الشجرة الكبرى للعلوم والتكنولوجيا النووية",
                       "المصدر الوحيد للحقيقة: `tools/kg/nodes_*.py` → `graph/knowledge_graph.json`.")]

    total_h = sum(n.hours for n in nodes)
    core_h = sum(n.hours for n in nodes if n.depth == "core")
    lines.append("## إحصاءات الخريطة\n")
    lines.append(f"- عدد العقد (الموضوعات): **{len(nodes)}**")
    lines.append(f"- عدد المجالات: **{len(by_dom)}**")
    lines.append(f"- إجمالي الساعات التقديرية لكل الخريطة: **{total_h:,} ساعة**")
    lines.append(f"- الساعات للمواد **الأساسية (core)** فقط: **{core_h:,} ساعة** "
                 "(≈ 3 سنوات دراسة بدوام كامل)")
    lines.append(f"- أطول سلسلة شرط مسبق (عمق الرسم): **{max(lvl.values()) + 1}** مستوى\n")

    lines.append("## الشجرة بحسب المجال\n")
    for d in sorted(by_dom, key=lambda x: min(n.stage for n in by_dom[x])):
        info = DOMAINS[d]
        items = sorted(by_dom[d], key=lambda n: (n.stage, n.diff, n.id))
        h = sum(n.hours for n in items)
        lines.append(f"### {info['ar']} — `{d}` ({info['en']})")
        lines.append(f"*{len(items)} موضوع · {h} ساعة تقديرية*\n")
        for n in items:
            badge = {"core": "🔵 أساسي", "supporting": "⚪ مساند", "advanced": "🟣 متقدم",
                     "specialized": "🟠 تخصصي", "research": "🔬 بحثي"}[n.depth]
            lines.append(
                f"- **{n.ar}** · *{n.en}* · `{n.id}`  \n"
                f"  المرحلة {n.stage} ({STAGES[n.stage]}) · صعوبة {n.diff}/5 · "
                f"{n.hours} ساعة · {badge} · الشروط: "
                + (", ".join(f"`{p}`" for p in n.prereqs) if n.prereqs else "—")
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def gen_prereq(nodes, reg, related, lvl):
    lines = [md_header("MAP/03 — جدول المتطلبات السابقة (Prerequisites)",
                       "لكل موضوع: ما يجب إتقانه قبله، وما يفتحه لاحقاً.")]
    lines.append("| المعرّف | الموضوع | المجال | المرحلة | الشروط المسبقة | يفتح الطريق إلى | صعوبة | ساعات |")
    lines.append("|---|---|---|---|---|---|---|---|")
    children = defaultdict(list)
    for n in nodes:
        for p in n.prereqs:
            children[p].append(n.id)
    for n in sorted(nodes, key=lambda x: (x.stage, x.domain, x.id)):
        pre = ", ".join(f"`{p}`" for p in n.prereqs) or "—"
        nxt = ", ".join(f"`{c}`" for c in sorted(children[n.id])[:6]) or "—"
        if len(children[n.id]) > 6:
            nxt += f" (+{len(children[n.id]) - 6})"
        lines.append(f"| `{n.id}` | {n.ar} | {DOMAINS[n.domain]['ar']} | {n.stage} | "
                     f"{pre} | {nxt} | {n.diff}/5 | {n.hours} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def gen_levels(nodes, reg):
    """MAP/02 — توزيع الموضوعات على المستويات الخمسة عشر."""
    by = defaultdict(list)
    for n in nodes:
        by[user_level(n)].append(n)
    lines = [md_header("MAP/02 — المستويات الخمسة عشر (0 إلى 14)",
                       "تصنيف موضوعاتي للمراحل. الترتيب الفعلي للدراسة داخل كل مستوى "
                       "يتبع الترتيب الطوبولوجي في MAP/04.")]
    lines.append("| المستوى | الاسم | عدد المواضيع | الساعات | Examples |")
    lines.append("|---|---|---|---|---|")
    for k in sorted(LEVELS_0_14):
        items = by.get(k, [])
        h = sum(n.hours for n in items)
        ex = "، ".join(sorted(n.ar for n in items)[:4]) or "—"
        lines.append(f"| {k} | {LEVELS_0_14[k]} | {len(items)} | {h} | {ex} |")
    lines.append("")
    for k in sorted(LEVELS_0_14):
        items = sorted(by.get(k, []), key=lambda n: (n.diff, n.id))
        if not items:
            continue
        lines.append(f"## المستوى {k}: {LEVELS_0_14[k]}\n")
        for n in items:
            core = "🔵" if n.depth == "core" else {"supporting": "⚪", "advanced": "🟣",
                                                  "specialized": "🟠", "research": "🔬"}[n.depth]
            lines.append(f"- {core} **{n.ar}** `{n.id}` — {n.hours} ساعة · صعوبة {n.diff}/5")
        lines.append("")
    return "\n".join(lines) + "\n"


def gen_order(nodes, reg, topo, lvl, crit):
    lines = [md_header("MAP/04 — ترتيب الدراسة (Topological Study Order)",
                       "الترتيب مولّد طوبولوجياً: لا يظهر موضوع قبل كل شروطه المسبقة. "
                       "الترتيب داخل المرحلة استرشادي (بالصعوبة ثم المجال).")]
    lines.append("## العمود الفقري: أطول مسار زمني في الخريطة\n")
    hours, path = crit
    lines.append(f"**{hours:,} ساعة** عبر {len(path)} موضوعاً:\n")
    lines.append(" → ".join(f"`{p}`" for p in path))
    lines.append("\nهذا المسار هو «الحد الأدنى المتصل» من الأساسيات حتى موضوع بحثي.\n")

    by_stage = defaultdict(list)
    for n in nodes:
        by_stage[n.stage].append(n)
    lines.append("## الترتيب بحسب المرحلة\n")
    cum = 0
    for s in sorted(by_stage):
        items = sorted(by_stage[s], key=lambda n: (lvl[n.id], n.diff, n.domain, n.id))
        h = sum(n.hours for n in items)
        cum += h
        lines.append(f"### المرحلة {s}: {STAGES[s]}")
        lines.append(f"*{len(items)} موضوع · {h} ساعة · المجموع التراكمي: {cum:,} ساعة*\n")
        for i, n in enumerate(items, 1):
            pre = ", ".join(f"`{p}`" for p in n.prereqs) or "—"
            lines.append(f"{i}. **{n.ar}** (`{n.id}`) — صعوبة {n.diff}/5 · {n.hours} ساعة · "
                         f"الشروط: {pre}")
        lines.append("")
    return "\n".join(lines) + "\n"


# ----------------------------------------------------------------- main ------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="تحقق فقط دون كتابة")
    args = ap.parse_args()

    nodes = load_nodes()
    reg = registry()
    errors, warnings, dependents = validate(nodes, reg)
    lvl, topo, children = compute_levels(nodes, reg)
    related = compute_related(nodes, children, reg)
    crit = critical_path(nodes, reg, lvl)

    print(f"عقد: {len(nodes)} | مجالات: {len({n.domain for n in nodes})} | "
          f"حروف (روابط شرط مسبق): {sum(len(n.prereqs) for n in nodes)}")
    for w in warnings:
        print(f"  ⚠️  {w}")
    if errors:
        print("\n❌ أخطاء تمنع البناء:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("✅ التحقق من الرسم: لا دورات، لا معرّفات مكررة، لا شروط مجهولة.")
    if args.check:
        return

    os.makedirs(OUT_GRAPH, exist_ok=True)
    os.makedirs(OUT_MAP, exist_ok=True)
    os.makedirs(OUT_SITE, exist_ok=True)

    graph = {
        "meta": {
            "name_ar": "خريطة المعرفة النووية الكبرى",
            "name_en": "Nuclear Master Knowledge Graph",
            "version": "1.0.0",
            "generated_by": "tools/build.py",
            "node_count": len(nodes),
            "domain_count": len({n.domain for n in nodes}),
            "critical_path_hours": crit[0],
            "critical_path": crit[1],
            "stages": STAGES,
            "levels_0_14": LEVELS_0_14,
            "domains": DOMAINS,
            "depths": DEPTHS,
            "sources": SOURCES,
        },
        "nodes": [],
        "edges": [],
    }
    for n in nodes:
        d = n.to_dict()
        d["graph_level"] = lvl[n.id]
        d["level_0_14"] = user_level(n)
        d["level_0_14_ar"] = LEVELS_0_14[user_level(n)]
        d["related"] = related[n.id]
        d["dependents"] = sorted(dependents[n.id])
        graph["nodes"].append(d)
        for p in n.prereqs:
            graph["edges"].append({"from": p, "to": n.id})

    with open(os.path.join(OUT_GRAPH, "knowledge_graph.json"), "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)

    with open(os.path.join(OUT_GRAPH, "edges.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["from", "to"])
        for e in graph["edges"]:
            w.writerow([e["from"], e["to"]])

    # للعارض التفاعلي
    with open(os.path.join(OUT_SITE, "graph_data.json"), "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, separators=(",", ":"))

    write(os.path.join(OUT_MAP, "01-grand-tree.md"), gen_tree(nodes, reg, lvl))
    write(os.path.join(OUT_MAP, "02-levels-0-14.md"), gen_levels(nodes, reg))
    write(os.path.join(OUT_MAP, "03-prerequisites.md"), gen_prereq(nodes, reg, related, lvl))
    write(os.path.join(OUT_MAP, "04-study-order.md"), gen_order(nodes, reg, topo, lvl, crit))
    print("📄 كُتبت: graph/knowledge_graph.json, graph/edges.csv, "
          "MAP/01, MAP/02, MAP/03, MAP/04, site/graph_data.json")


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
