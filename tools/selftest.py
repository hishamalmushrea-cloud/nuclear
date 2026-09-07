#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
selftest — حزام أمان للنظام كله (X.33: الاستمرارية).

لماذا؟
    المستودع ينمو: عقد جديدة، مختبرات جديدة، دروس جديدة. أي تعديل يمكن أن يكسر
    شيئاً في مكان آخر بصمت. هذا الملف يشغّل كل الفحوصات التي يمكن تشغيلها
    بلا تفاعل بشري، ويخبرك «أخضر/أحمر» في ثوانٍ.

الاستخدام:
    python3 tools/selftest.py            # كل الفحوصات
    python3 tools/selftest.py -v         # مع تفصيل

الفحوصات:
    1. سلامة الرسم (build.py --check): لا دورات، لا معرّفات مكررة، لا شروط مجهولة
    2. اتساق المراحل: لا عقدة تعتمد على عقدة في مرحلة لاحقة
    3. صحة كل ملفات Python (ترجمة)
    4. صحة كل الدروس (واجهة أمامية + كتلة quiz قابلة للتحليل + مفتاح إجابة)
    5. فيزياء المختبر 06: الحل العددي يطابق التحليلي (≤ 5 pcm)
    6. رياضيات الفصل: V''(x) = 1/[x²(1−x)²] واستقلال δU عن التركيز
    7. اتساق ملف التقدّم مع الرسم (كل عقدة لها سجل)
    8. أدوات سطر الأوامر لا تنهار (--help لكل أداة)
"""
from __future__ import annotations

import json
import math
import os
import py_compile
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

VERBOSE = "-v" in sys.argv or "--verbose" in sys.argv

GREEN, RED, YELLOW = "✅", "❌", "⚠️ "
_results = []


def check(name, fn):
    """يشغّل فحصاً ويسجّل النتيجة."""
    try:
        ok, msg = fn()
    except Exception as exc:  # noqa: BLE001
        ok, msg = False, f"{type(exc).__name__}: {exc}"
    _results.append((ok, name, msg))
    print(f"  {GREEN if ok else RED} {name}" + (f" — {msg}" if msg else ""))
    return ok


def run(cmd, **kw):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, **kw)


# ------------------------------------------------------------------ 1) الرسم
def t_graph():
    r = run([sys.executable, "tools/build.py", "--check"])
    ok = r.returncode == 0 and "✅" in r.stdout
    return ok, r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr.strip()[:120]


def t_stages():
    from kg.schema import registry, STAGES  # noqa: E402
    nodes = registry()
    bad = []
    for n in nodes.values():
        for p in n.prereqs:
            if p in nodes and nodes[p].stage > n.stage:
                bad.append(f"{n.id}({n.stage})←{p}({nodes[p].stage})")
    return (not bad), ("انحدار مراحل: " + ", ".join(bad[:5])) if bad else f"{len(nodes)} عقدة متسقة"


# ------------------------------------------------------------- 2) صحة الكود
def t_compile():
    errs = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__", "node_modules"}]
        for f in filenames:
            if not f.endswith(".py"):
                continue
            p = os.path.join(dirpath, f)
            try:
                py_compile.compile(p, doraise=True, cfile=tempfile.mktemp())
            except Exception as exc:  # noqa: BLE001
                errs.append(f"{os.path.relpath(p, ROOT)}: {exc}")
    return (not errs), "; ".join(errs[:3]) if errs else "كل ملفات Python تُترجم"


# ------------------------------------------------------------- 3) الدروس
def t_lessons():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import lesson as L  # noqa: E402
    d = os.path.join(ROOT, "lessons")
    files = sorted(f for f in os.listdir(d) if f.endswith(".md"))
    if not files:
        return False, "لا دروس"
    problems = []
    for f in files:
        path = os.path.join(d, f)
        try:
            meta, body, quiz = L.parse(path)
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{f}: {exc}")
            continue
        if not meta.get("id"):
            problems.append(f"{f}: بلا معرّف")
        if len(body) < 500:
            problems.append(f"{f}: نص قصير ({len(body)} حرفاً)")
        if len(quiz) < 3:
            problems.append(f"{f}: {len(quiz)} أسئلة فقط")
        for i, q in enumerate(quiz):
            if not q.get("q"):
                problems.append(f"{f}#{i}: سؤال بلا نص")
            if q.get("a") in (None, ""):
                problems.append(f"{f}#{i}: بلا إجابة صحيحة")
    return (not problems), "; ".join(problems[:4]) if problems else f"{len(files)} دروس سليمة"


# --------------------------------------------------- 4) فيزياء المختبر 06
def t_diffusion_real():
    """المختبر 06: k العددي مقابل التحليلي."""
    sys.path.insert(0, ROOT)
    sys.path.insert(0, os.path.join(ROOT, "sims"))
    mod = {}
    src = open(os.path.join(ROOT, "sims", "06_neutron_diffusion.py"), encoding="utf-8").read()
    src = src.replace('from .engine import', 'from engine import')
    exec(compile(src, "06_neutron_diffusion", "exec"), mod)  # noqa: S102
    worst = 0.0
    for m in mod["PRESETS"]:
        a_c = mod["critical_thickness"](m)
        if a_c is None:
            continue
        kn = mod["k_of_thickness"](m, a_c)
        ka = mod["k_analytic"](m, a_c)
        worst = max(worst, abs(kn - ka) * 1e5)
    ok = worst <= 5.0
    return ok, f"أسوأ فرق بين العددي والتحليلي: {worst:.2f} pcm (الحد 5)"


# --------------------------------------------------- 5) رياضيات الفصل
def t_separation():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import separation as S  # noqa: E402
    worst = 0.0
    for x in (0.00711, 0.045, 0.2, 0.5, 0.8):
        v = S.value_function(x)
        h = 1e-5
        num = (S.value_function(x + h) - 2 * v + S.value_function(x - h)) / h ** 2
        ana = 1.0 / (x ** 2 * (1 - x) ** 2)
        worst = max(worst, abs(num - ana) / ana)
    ok1 = worst < 1e-4

    # استقلال قدرة الفصل عن التركيز
    def du(alpha, x, F=1.0):
        R = lambda z: z / (1 - z)  # noqa: E731
        Rp = R(x) * math.sqrt(alpha)
        Rw = R(x) / math.sqrt(alpha)
        xp = Rp / (1 + Rp)
        xw = Rw / (1 + Rw)
        P = (F * x - F * xw) / (xp - xw)
        W = F - P
        return P * S.value_function(xp) + W * S.value_function(xw) - F * S.value_function(x)

    a = du(1.01, 0.00711)
    b = du(1.01, 0.5)
    ok2 = abs(a - b) / max(1e-30, abs(a)) < 1e-9
    swu = S.swu(0.00711, 0.045, 0.0025, 1.0)
    ok3 = 6.5 < swu < 7.2
    return (ok1 and ok2 and ok3), (f"V'' خطأ نسبي {worst:.1e} · استقلال δU عن x: "
                                   f"{'نعم' if ok2 else 'لا'} · SWU={swu:.3f}")


# --------------------------------------------------- 5ب) مولّد الدروس
def t_generator():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import gen_lesson as G  # noqa: E402
    nodes = G.registry()
    dep = G.deps_map(nodes)
    a, _ = G.build_lesson("math.stat", nodes, {"topics": {}}, dep=dep)
    b, _ = G.build_lesson("math.stat", nodes, {"topics": {}}, dep=dep)
    if a != b:
        return False, "التوليد غير حتمي"
    problems = []
    import lesson as L  # noqa: E402
    for f in sorted(os.listdir(os.path.join(ROOT, "lessons"))):
        if not f.endswith(".md"):
            continue
        try:
            meta, body, quiz = L.parse(os.path.join(ROOT, "lessons", f))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{f}: {exc}")
            continue
        if not meta.get("id"):
            problems.append(f"{f}: بلا معرّف")
        if len(quiz) < 3:
            problems.append(f"{f}: {len(quiz)} أسئلة")
        seen = set()
        for i, q in enumerate(quiz):
            if q.get("a") not in (0, 1, 2, 3):
                problems.append(f"{f}#{i}: مفتاح إجابة غير صالح")
            if len(set(q.get("o", []))) != len(q.get("o", [])):
                problems.append(f"{f}#{i}: خيارات مكرّرة")
            if q.get("q") in seen:
                problems.append(f"{f}#{i}: سؤال مكرّر")
            seen.add(q.get("q"))
    return (not problems), "; ".join(problems[:4]) if problems else "التوليد حتمي وكل الدروس صالحة"


# --------------------------------------------------- 5ج) التكرار المتباعد
def t_sm2():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    from progress import sm2, due_list  # noqa: E402
    t = {"mastery": 70}
    seq = []
    for q, day in ((4, "2026-09-02"), (5, "2026-09-03"), (5, "2026-09-09")):
        sm2(t, q, day)
        seq.append(t["interval"])
    if seq != [1.0, 6.0, 15.6]:
        return False, f"تسلسل الفواصل خاطئ: {seq}"
    before = t["mastery"]
    sm2(t, 1, "2026-09-21")           # فشل ⇒ إعادة + تراجع
    if t["reps"] != 0 or t["interval"] != 1.0 or t["mastery"] >= before:
        return False, "الفشل لا يعيد الجدولة ولا يخفض الإتقان"
    d = due_list({"topics": {"a": {"mastery": 50, "due": "2026-09-01"},
                             "b": {"mastery": 30},
                             "c": {"mastery": 0, "due": "2026-01-01"}}}, {}, "2026-09-07")
    if [x[0] for x in d] != ["b", "a"]:
        return False, "قائمة الاستحقاق خاطئة"
    return True, f"فواصل SM-2: 1 → 6 → 15.6 يوم · الفشل يعيد الجدولة · الاستحقاق صحيح"


# --------------------------------------------------- 5د) بوابات X.9
def t_gates():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    from progress import stage_stats, gate_pass, GATE  # noqa: E402
    from kg.schema import registry  # noqa: E402
    nodes = registry()
    prof = {"topics": {}}
    for n in nodes.values():
        if n.stage <= 1:
            prof["topics"][n.id] = {"mastery": 90, "attempts": [88, 92],
                                    "dim": {"concept": 95, "term": 90, "calc": 85}}
    st = stage_stats(prof, nodes, 1)
    if st is None:
        return False, "لا عُقد في المرحلة 1"
    if not gate_pass(st):
        return False, f"بوابة لم تُجتز رغم اكتمال الأبعاد: مفاهيم {st['concepts']:.0f} مصطلحات {st['terms']:.0f}"
    # إنقاص بُعد واحد يجب أن يُسقط البوابة
    for t in prof["topics"].values():
        t["dim"]["term"] = 50
    st2 = stage_stats(prof, nodes, 1)
    if gate_pass(st2):
        return False, "البوابة تجتاز رغم المصطلحات 50٪"
    if GATE != {"concepts": 80, "marks": 70, "terms": 80, "cumulative": 75}:
        return False, f"عتبات البوابة تغيّرت: {GATE}"
    return True, f"العتبات 80/70/80/75 محفوظة · اجتياز كامل ✅ · سقوط عند مصطلحات 50٪ ❌"


# --------------------------------------------------- 5هـ) مونتي-كارلو للنقل
def t_montecarlo():
    sys.path.insert(0, os.path.join(ROOT, "sims"))
    import importlib
    M = importlib.import_module("07_monte_carlo_transport")
    M.seed(12345)
    p = M.PRESETS[0]
    a = 3.0 / p["St"]
    r = M.run_histories(p["St"], p["Ss"], a, 4000)
    bal = r["T"] + r["R"] + r["A"]
    if abs(bal - 1.0) > 1e-9:
        return False, f"حفظ العدد منحرف: T+R+A = {bal:.9f}"
    if r["capped"]:
        return False, f"{r['capped']} تاريخاً وصل سقف التصادمات"
    if not (0.30 < r["T"] < 0.47):
        return False, f"نفاذ غير متوقع للماء عند 3λ: T = {r['T']:.4f}"
    if r["R"] <= r["T"]:
        return False, f"توقّعنا ارتداداً أكبر من النفاذ (خراب المقامر): R={r['R']:.3f} T={r['T']:.3f}"
    if r["A"] <= 0:
        return False, "لا امتصاص رغم Σa > 0"
    # وسط ممتصّ قوي: يجب أن يهيمن الامتصاص
    p5 = M.PRESETS[4]
    r5 = M.run_histories(p5["St"], p5["Ss"], 3.0 / p5["St"], 2000)
    if r5["A"] <= r5["T"]:
        return False, "في وسط ممتصّ قوي يجب أن يهيمن A على T"
    return True, (f"حفظ العدد = 1 بالضبط · T={r['T']:.3f} R={r['R']:.3f} A={r['A']:.3f} · "
                  f"الممتصّ القوي: A={r5['A']:.3f} > T={r5['T']:.3f}")


# --------------------------------------------------- 6) ملف التقدّم
def t_profile():
    from kg.schema import registry  # noqa: E402
    p = os.path.join(ROOT, "progress", "profile.json")
    if not os.path.exists(p):
        return False, "لا ملف تقدّم"
    prof = json.load(open(p, encoding="utf-8"))
    nodes = registry()
    missing = [k for k in nodes if k not in prof.get("topics", {})]
    extra = [k for k in prof.get("topics", {}) if k not in nodes]
    ok = not missing and not extra
    return ok, (f"عقد بلا سجل: {len(missing)} · سجلات بلا عقدة: {len(extra)}"
                if not ok else f"{len(prof.get('topics', {}))} سجل مطابق للرسم")


# --------------------------------------------------- 7) واجهات الأوامر
def t_cli():
    tools = ["tools/build.py", "tools/progress.py", "tools/lesson.py",
             "tools/tutor.py", "tools/separation.py", "tools/site_index.py",
             "tools/gen_lesson.py", "tools/selftest.py"]
    bad = []
    for t in tools:
        r = run([sys.executable, t, "--help"])
        if r.returncode not in (0, 2):
            bad.append(f"{t}: كود خروج {r.returncode}")
    return (not bad), "; ".join(bad) if bad else f"{len(tools)} أداة تستجيب"


def main() -> int:
    import argparse as _ap
    parser = _ap.ArgumentParser(description="فحص ذاتي للنظام النووي المعرفي")
    parser.add_argument("-v", "--verbose", action="store_true", help="تفصيل إضافي")
    parser.add_argument("--quick", action="store_true", help="تخطّي الفحوصات البطيئة")
    parser.parse_args()

    print("\n🧪 فحص ذاتي للنظام النووي المعرفي")
    print("─" * 60)
    check("الرسم المعرفي (build --check)", t_graph)
    check("اتساق المراحل", t_stages)
    check("ترجمة كل ملفات Python", t_compile)
    check("سلامة الدروس والاختبارات", t_lessons)
    check("فيزياء المختبر 06 (عددي = تحليلي)", t_diffusion_real)
    check("رياضيات الفصل (V'' و SWU)", t_separation)
    check("مولّد الدروس (حتمي + دروس صالحة)", t_generator)
    check("التكرار المتباعد (SM-2)", t_sm2)
    check("بوابات الانتقال X.9", t_gates)
    check("مونتي-كارلو للنقل (حفظ العدد)", t_montecarlo)
    check("ملف التقدّم مطابق للرسم", t_profile)
    check("أدوات سطر الأوامر", t_cli)

    passed = sum(1 for ok, _, _ in _results if ok)
    total = len(_results)
    print("─" * 60)
    print(f"  النتيجة: {passed}/{total} فحص ناجح")
    if passed == total:
        print("  " + GREEN + " النظام سليم — يمكنك التوسّع بأمان.\n")
        return 0
    print("  " + RED + " أصلح الفاشل قبل إضافة أي شيء جديد.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
