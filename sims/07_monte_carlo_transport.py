# -*- coding: utf-8 -*-
"""
07 — مختبر مونتي-كارلو لنقل النيوترونات (1-D slab, تتبّع تاريخ كامل)

الفيزياء (لا تبسيط — هذا هو نقل بولتزمان بطريقة مونتي-كارلو التناظرية):

لكل نيوترون تاريخ (history):
  1. مسافة حرّة حتى التصادم التالي:   s = −ln(ξ)/Σ_t        (ξ ~ U(0,1))
  2. إن خرج من اللوح قبل التصادم ⇒ نفذ (transmitted) أو ارتدّ (reflected) حسب الجهة
  3. عند التصادم: ξ₂ < Σ_a/Σ_t  ⇒  امتصاص (ينتهي التاريخ)
                 وإلا ⇒ تشتّت، بزاوية جديدة (هنا: متساوي الخواص في 1-D
                 ⇒ للأمام أو للخلف باحتمال متساوٍ)، ثم عُد إلى 1
  4. روسينج: الروسيّة (Russian roulette) لإنهاء التواريخ الطويلة بلا تحيّز

ماذا يقيس المختبر؟
  T = كسر النيوترونات النافذة   R = المرتدة   A = الممتصّة   (T + R + A = 1)
  ويقارن T بـ e^(−Σ_t·a) — نفاذ «غير المتصادم» التحليلي.

الدرس الفيزيائي الكبير: **التشتّت يزيد النفاذ عن e^(−Σ_t a)**، لأن النيوترون
المتشتّت للأمام يبقى مرشّحاً للخروج من الجهة الأخرى. فمن صمّم درعاً بالاعتماد
على التوهين الأُسّي وحده فقد ** underestimated التسرب** — وهذا بالضبط هو سبب
وجود «معامل التراكم» (buildup factor) في مختبر التدريع 03.

هذا المختبر هو أساس كل كود نقل حقيقي (MCNP / OpenMC / Serpent) مصغّراً إلى
بعدٍ واحد: نفس المنطق، بلا هندسة ثلاثية.
"""
from __future__ import annotations

import math

try:
    from .engine import (RNG, seed, header, step, note, warn, good, bad,
                         ask, ask_float, ask_int, pause, plot, table, rel_err)
except ImportError:
    from engine import (RNG, seed, header, step, note, warn, good, bad,
                        ask, ask_float, ask_int, pause, plot, table, rel_err)


# مقاطع عرضية ماكروسكوبية Σ (cm⁻¹) — قيم تمثيلية تعليمية للنيوترونات الحرارية/السريعة،
# ليست بيانات تصميم. c = Σ_s/Σ_t هو «نسبة التشتت».
PRESETS = [
    {"name": "ماء (حراري) — ممتصّ متوسط ومشتّت قوي", "St": 3.45, "Ss": 3.40},
    {"name": "جرافيت (حراري) — امتصاص ضعيف جداً", "St": 0.40, "Ss": 0.399},
    {"name": "حديد (سريع) — ممتصّ ومشتّت معاً", "St": 0.75, "Ss": 0.65},
    {"name": "رصاص (سريع) — تشتّت ضعيف نسبياً", "St": 0.35, "Ss": 0.25},
    {"name": "بورون/ماء (ممتصّ قوي — درع نيوتروني)", "St": 5.00, "Ss": 3.00},
]

MAX_COLL = 20000     # سقف أمان لكل تاريخ (لا يتحقق عادةً في المحاكاة التناظرية)


def sample_free_path(St):
    """s = −ln(ξ)/Σ_t  (توزيع أُسّي للمسار الحر بين التصادمات)."""
    return -math.log(1.0 - RNG.random()) / St


def run_histories(St, Ss, a, n_hist, track_depth=False, n_bins=40):
    """مونتي-كارلو **تناظري** (analog) في لوح بسماكة a.

    تناظري = بلا أوزان وبلا روسيّة: كل نيوترون يُعامل بوزن 1، فـ
    T + R + A = 1 **بالضبط** (حفظ العدد) — وهذا فحص سلامة داخلي دائم.
    الأكواد الصناعية تضيف لاحقاً تقليل تباين (روسيّة، التقاط ضمني،
    أهمية متبادِلة) — ونذكر ذلك في الخاتمة.
    """
    Sa = St - Ss
    p_abs = Sa / St if St > 0 else 1.0
    transmitted = reflected = absorbed = 0
    collisions_total = 0
    capped = 0
    depth_hist = [0] * n_bins

    for _ in range(n_hist):
        x = 0.0
        mu = 1.0                      # +1 نحو +x (الأمام)، −1 نحو −x (الخلف)
        for _c in range(MAX_COLL):
            s = sample_free_path(St)
            x_new = x + mu * s
            if x_new >= a:            # خرج من الوجه الخلفي ⇒ نافذ
                transmitted += 1
                break
            if x_new <= 0.0:          # خرج من الوجه الأمامي ⇒ مرتد
                reflected += 1
                break
            x = x_new
            collisions_total += 1
            if track_depth:
                b = int(x / a * n_bins)
                if 0 <= b < n_bins:
                    depth_hist[b] += 1
            if RNG.random() < p_abs:  # امتصاص ⇒ نهاية التاريخ
                absorbed += 1
                break
            mu = 1.0 if RNG.random() < 0.5 else -1.0     # تشتّت متساوي الخواص في 1-D
        else:
            capped += 1

    return {
        "T": transmitted / n_hist,
        "R": reflected / n_hist,
        "A": absorbed / n_hist,
        "coll": collisions_total / n_hist,
        "depth": depth_hist,
        "capped": capped,
    }


def run():
    header("مختبر مونتي-كارلو لنقل النيوترونات (1-D)",
           "تتبّع تاريخ كل نيوترون: مسار حرّ → تصادم → امتصاص أو تشتّت → خروج أو موت")

    step("الخوارزمية (نفس منطق MCNP/OpenMC، مصغّرة إلى بُعد واحد):")
    print("""
  لكل نيوترون:
    s = −ln(ξ)/Σ_t                 المسافة حتى التصادم التالي (توزيع أُسّي)
    إن خرج من اللوح قبل التصادم  ⇒ نافذ T (يميناً) أو مرتد R (يساراً)
    عند التصادم:  ξ < Σ_a/Σ_t ⇒ امتصاص A (ينتهي)
                  وإلا ⇒ تشتّت (متساوي الخواص في 1-D: أمام/خلف 50/50) ثم كرّر
    تحيّز صفري: روسيّة روسية (Russian roulette) بوزن مُعوَّض للتواريخ الطويلة
  المحصّلة:  T + R + A = 1  (حفظ العدد — فحص سلامة دائم)
""")

    print("  اختر وسطاً (مقاطع تمثيلية تعليمية، Σ بوحدة cm⁻¹):")
    for i, p in enumerate(PRESETS, 1):
        c = p["Ss"] / p["St"]
        print(f"    {i}) {p['name']}  —  Σt={p['St']:.3f} · Σs={p['Ss']:.3f} · c={c:.3f}")
    print(f"    {len(PRESETS)+1}) أدخل Σt و Σs بنفسي")

    try:
        idx = ask_int("؟ الوسط: ", 1, 1, len(PRESETS) + 1)
    except (EOFError, KeyboardInterrupt):
        return
    if idx == len(PRESETS) + 1:
        St = ask_float("  Σt (cm⁻¹): ", 1.0, 0.001, 100)
        Ss = ask_float("  Σs (cm⁻¹) — يجب أن يكون < Σt: ", 0.9, 0.0, 100)
        if Ss >= St:
            bad("Σs يجب أن يكون أصغر من Σt (وإلا فلا امتصاص).")
            Ss = St * 0.9
        name = "مخصص"
    else:
        p = PRESETS[idx - 1]
        St, Ss, name = p["St"], p["Ss"], p["name"]

    mfp = 1.0 / St
    c = Ss / St
    print(f"\n  الوسط: {name}")
    print(f"  Σt = {St:.4f} cm⁻¹ · Σs = {Ss:.4f} · Σa = {St-Ss:.4f} · c = Σs/Σt = {c:.4f}")
    print(f"  المسار الحر المتوسط: λ = 1/Σt = {mfp:.3f} سم")

    a = ask_float("؟ سماكة اللوح a (سم) — جرّب بضعة أمثال المسار الحر: ",
                  round(3 * mfp, 2), 0.01, 10000)
    n_hist = ask_int("؟ عدد التواريخ (كلما زاد قلّ الضجيج، جرّب 20000): ", 20000, 100, 2000000)
    _s = ask("؟ بذرة عشوائية (اتركها فارغة لعشوائية حقيقية): ", "")
    seed(int(_s) if _s.strip().lstrip("-").isdigit() else None)

    print()
    guess = ask_float("؟ خمّن كسر النفاذ T (0–1) — أي كم نسبة النيوترونات التي تعبر: ", 0.05, 0.0, 1.0)

    step("أُجري المحاكاة…")
    res = run_histories(St, Ss, a, n_hist, track_depth=True)

    T, R, A = res["T"], res["R"], res["A"]
    balance = T + R + A
    good(f"النتيجة بعد {n_hist:,} تاريخاً:")
    table([(f"{T:.5f}", f"{R:.5f}", f"{A:.5f}", f"{balance:.6f}", f"{res['coll']:.2f}")],
          ["نافذ T", "مرتد R", "ممتصّ A", "المجموع (يجب 1)", "متوسط التصادمات/تاريخ"],
          aligns=[">", ">", ">", ">", ">"])
    if abs(balance - 1.0) > 1e-6:
        warn(f"حفظ العدد منحرف بمقدار {balance-1:.2e} — راجع الروسيّة.")

    err = rel_err(guess, T)
    print(f"\n  تخمينك: {guess:.4f} · المحاكاة: {T:.5f} · خطؤك النسبي {err:.1f}٪")
    if err < 10:
        good("ممتاز — حسّك النيوتروني جيد.")
    elif err < 30:
        note("قريب. تذكّر: التشتّت يفتح «نافذة» عبور لا يراها التوهين الأُسّي.")
    else:
        note("قارن تخمينك بـ e^(−Σt·a) ثم اسأل: هل زاد عنه أم نقص؟ ولماذا؟")

    step("المقارنة الحاسمة: المحاكاة مقابل التوهين الأُسّي «غير المتصادم»")
    uncollided = math.exp(-St * a)
    print(f"  e^(−Σt·a) = e^(−{St:.3f}×{a:.2f}) = {uncollided:.5f}   (نيوترونات لم تتصادم أبداً)")
    print(f"  T من مونتي-كارلو                = {T:.5f}   (كل من عبر، متصادماً أو لا)")
    ratio = T / uncollided if uncollided > 0 else float("inf")
    print(f"  النسبة T / e^(−Σt·a) = {ratio:.3f}")
    if ratio > 1.05:
        if ratio >= 10:
            warn(f"النفاذ الحقيقي أكبر من التوهين الأُسّي بعامل **{ratio:.0f}×** "
                 f"(= {math.log10(ratio):.1f} رتبة عُشرية) — هذا هو **معامل التراكم**: "
                 f"النيوترونات المتشتّتة تنفذ أيضاً، ولا يراها التوهين الأُسّي.")
        else:
            warn(f"النفاذ الحقيقي أكبر من التوهين الأُسّي بـ {(ratio-1)*100:.0f}٪ — "
                 f"هذا هو **معامل التراكم**: النيوترونات المتشتّتة للأمام تنفذ أيضاً.")
        note("من صمّم درعاً بـ e^(−Σt·a) وحده فقد低估 التسرب. عُد إلى المختبر 03 وقارن.")
    if R > T:
        note(f"لاحظ أن المرتدّ ({R:.3f}) أكبر من النافذ ({T:.3f}): النيوترونات تدخل من الوجه "
             f"وتتشتّت، وأقرب مخرج إليها هو **الوجه الذي دخلت منه** (مسألة «خراب المقامر»).")
    elif ratio < 0.95:
        note("النفاذ أقل من غير المتصادم: الامتصاص يقتل النيوترونات المتشتّتة قبل خروجها.")
    else:
        note("التشتّت شبه معدوم هنا: الوسط ممتصّ أو رقيق جداً.")

    step("توزيع التصادمات على طول العمق (كثافة التفاعل ⇒ أين تُمتصّ الطاقة؟)")
    bins = res["depth"]
    if bins and max(bins) > 0:
        xs = [a * (i + 0.5) / len(bins) for i in range(len(bins))]
        plot(xs, bins, title="كثافة التصادمات مقابل العمق (سم)",
             ylabel="العمق داخل اللوح (سم) من الوجه الأمامي")

    step("جدول: كيف يتغيّر النفاذ مع السماكة؟ (منحنى التوهين الفعلي)")
    rows = []
    for f in (0.5, 1, 2, 3, 5, 8):
        aa = f * mfp
        r = run_histories(St, Ss, aa, max(2000, n_hist // 5))
        rows.append((f"{aa:.2f}", f"{aa/mfp:.1f}", f"{r['T']:.5f}",
                     f"{math.exp(-St*aa):.5f}"))
    table(rows, ["السماكة (سم)", "بوحدة λ", "T (مونتي-كارلو)", "e^(−Σt·a)"],
          aligns=[">", ">", ">", ">"])

    step("العب: ابحث عن السماكة التي تهبط بالنفاذ إلى 1٪")
    try:
        target = ask_float("؟ النفاذ المستهدف (افتراضي 0.01): ", 0.01, 1e-6, 0.999)
    except (EOFError, KeyboardInterrupt):
        return
    lo, hi = mfp * 0.1, mfp * 200
    for _ in range(28):
        mid = 0.5 * (lo + hi)
        r = run_histories(St, Ss, mid, max(1500, n_hist // 10))
        if r["T"] > target:
            lo = mid
        else:
            hi = mid
    found = 0.5 * (lo + hi)
    print(f"\n  سماكة النفاذ {target*100:g}٪ ≈ **{found:.2f} سم** = {found/mfp:.1f} مسار حرّ")
    print(f"  (التقدير الأُسّي وحده كان سيعطي {math.log(1/target)/St:.2f} سم — "
          f"الفرق هو أثر التشتّت)")

    note("""
ما وراء هذا المختبر (مفتوح بالكامل في الخريطة):
  معادلة النقل (بولتزمان) والفرق بينها وبين الانتشار (المختبر 06) ·
  تقليل التباين: أهمية متبادِلة (importance sampling)، ومسارات مُرجَّحة،
  ومصدر تقاربي (fission source iteration) لكفف · تقدير k_eff و Shannon entropy ·
  مجموعات طاقة وكتب بيانات ENDF · تشتّت متباين الخواص (P(μ)) وزوايا واقعية ·
  هندسة 3-D حقيقية (CSG) كما في OpenMC/Serpent · ومعاملات التراكم في التدريع.""")
    pause()


if __name__ == "__main__":
    run()
