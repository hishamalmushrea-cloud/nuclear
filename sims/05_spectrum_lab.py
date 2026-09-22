# -*- coding: utf-8 -*-
"""
المختبر 05 — مختبر التحليل الطيفي لغاما (محاكاة كاشف HPGe/NaI).

ماذا تتعلم:
  1. معايرة الطاقة: كيف تحوّل «رقم القناة» إلى «طاقة keV».
  2. تحديد النويدات من مواقع القمم.
  3. حساب مساحة القمة الصافية (طرح خلفية خطية).
  4. عدم اليقين الإحصائي وحدّ الكشف الأدنى (MDA).

النموذج: قمم غاوسية فوق خلفية متناقصة + ضجيج بواسون في كل قناة،
مع دقة تزداد سوءاً مع الطاقة: FWHM = sqrt(a + b·E).
"""
from __future__ import annotations

import math

try:
    from .engine import (RNG, ask, ask_float, ask_int, good, header, note, pause,
                         plot, poisson, rel_err, seed, step, table, warn)
except ImportError:
    from engine import (RNG, ask, ask_float, ask_int, good, header, note, pause,
                        plot, poisson, rel_err, seed, step, table, warn)

NCH = 512
EMAX = 3000.0                      # keV (مدى الطاقة)
GAIN = EMAX / NCH                  # keV لكل قناة
FWHM_A, FWHM_B = 1.2, 0.0018       # keV² لكل keV — دقة نموذجية لكاشف متوسط

# (الاسم، الطاقة keV، الشدة النسبية)
LIBRARY = {
    "أمريسيوم-241": [(59.5, 0.36)],
    "سيزيوم-137":   [(661.7, 0.85)],
    "كوبالت-60":    [(1173.2, 1.0), (1332.5, 1.0)],
    "صوديوم-22":    [(511.0, 1.8), (1274.5, 1.0)],
    "بوتاسيوم-40":  [(1460.8, 0.11)],
    "يود-131":      [(364.5, 0.82), (636.9, 0.07)],
}


def fwhm(e):
    return math.sqrt(FWHM_A + FWHM_B * e)


def sigma_ch(e):
    return fwhm(e) / 2.355 / GAIN


def build_spectrum(nuclides, scale, live_time, bkg_level):
    spec = [0.0] * NCH
    # خلفية متناقصة أُسّياً
    for c in range(NCH):
        spec[c] += bkg_level * math.exp(-c / (NCH / 3.0)) + 0.15 * bkg_level
    peaks = []
    for name in nuclides:
        for e, inten in LIBRARY[name]:
            mu = e / GAIN
            s = sigma_ch(e)
            amp = scale * inten * live_time / 10.0
            for c in range(NCH):
                spec[c] += amp * math.exp(-0.5 * ((c - mu) / s) ** 2) / (s * math.sqrt(2 * math.pi))
            peaks.append((name, e, mu))
    noisy = [poisson(v) for v in spec]
    return noisy, peaks


def show_spectrum(spec, lo=0, hi=NCH):
    seg = spec[lo:hi]
    plot(list(range(lo, hi)), seg,
         title="الطيف المقاس (عدد لكل قناة)", ylabel="رقم القناة", height=16)


def run():
    header("المختبر 05 — التحليل الطيفي لغاما",
           "معايرة، تحديد نويدات، مساحة صافية، وحدّ كشف")
    _s = ask("رقم البذرة العشوائية (فارغ = عشوائي)", "")
    seed(int(_s) if _s.strip().lstrip("-").isdigit() else None)

    print("\nالنويدات المتاحة:")
    names = list(LIBRARY)
    for i, n in enumerate(names, 1):
        print(f"   {i}) {n}")
    raw = ask("أرقام النويدات المجهولة لك (مثال: 2 3) أو 0 للمفاجأة", "2 3")
    if raw.strip() == "0":
        chosen = [RNG.choice(names)]
    else:
        chosen = [names[int(t) - 1] for t in raw.split() if t.isdigit() and 1 <= int(t) <= len(names)]
    if not chosen:
        chosen = [names[1]]

    live = ask_float("زمن القياس الحيّ (ثانية)", 600.0, 1.0)
    scale = ask_float("«قوة» المصدر (شدة نسبية)", 1.0, 0.01)
    bkg = ask_float("مستوى الخلفية (عدد/قناة)", 8.0, 0.0)

    spec, peaks = build_spectrum(chosen, scale, live, bkg)
    step("هذا ما يراه جهازك:")
    show_spectrum(spec)

    # -------- 1) المعايرة --------
    step("الخطوة 1: معايرة الطاقة")
    note("اختر قمتين واضحتين، اذكر رقم القناة لكل منهما، وسنحسب العلاقة E = a·ch + b.")
    c1 = ask_int("رقم القناة للقمة الأولى", int(peaks[0][2]), 0, NCH - 1)
    e1 = ask_float("ما طاقة هذه القمة (keV)؟ (إن كنت تعرفها من مصدر معياري)", 661.7, 1.0)
    c2 = ask_int("رقم القناة للقمة الثانية", int(peaks[-1][2]) if len(peaks) > 1 else NCH - 20, 0, NCH - 1)
    e2 = ask_float("ما طاقة هذه القمة (keV)؟", 1332.5, 1.0)

    if c1 == c2:
        warn("القناتان متطابقتان — لا يمكن المعايرة.")
        a, b = GAIN, 0.0
    else:
        a = (e2 - e1) / (c2 - c1)
        b = e1 - a * c1
    print(f"\n  المعايرة:  E[keV] = {a:.4f} × القناة + {b:.2f}")
    note(f"المعايرة الحقيقية للجهاز: E = {GAIN:.4f} × القناة + 0")

    # -------- 2) تحديد النويدات --------
    step("الخطوة 2: استخدم المعايرة لتحديد قمم أخرى")
    # نعثر على القمم تلقائياً (بحث عن مواضع محلية) ثم يخمن المستخدم
    found = []
    pmax = max(spec) if spec else 1
    for c in range(7, NCH - 7):
        if spec[c] != max(spec[c-3:c+4]):
            continue
        base = min(spec[c-6], spec[c+6])          # خط الأساس المحيط
        # يجب أن تكون القمة أعلى من جانبيها (لا مجرد نتوء على منحدر الخلفية)
        if spec[c] <= max(spec[c-6], spec[c+6]):
            continue
        # عتبة مزدوجة: أهمية إحصائية (3.5σ) + أهمية نسبية مقابل أعلى قمة
        if (spec[c] - base > 3.5 * math.sqrt(max(base, 1.0))
                and spec[c] > 0.15 * pmax):
            if not found or c - found[-1] > 6:
                found.append(c)
    found = sorted(found, key=lambda c: -spec[c])[:8]
    found.sort()
    rows = []
    for c in found:
        e = a * c + b
        match, diff = "؟", 1e9
        for name, lst in LIBRARY.items():
            for ee, _ in lst:
                if abs(ee - e) < diff:
                    match, diff = f"{name} ({ee:g} keV)", abs(ee - e)
        rows.append((c, f"{e:.1f}", spec[c], match if diff < 25 else "غير مطابق"))
    table(rows, ["القناة", "الطاقة المحسوبة keV", "العدد", "أقرب نويدة"])

    print("\n  النويدات الحقيقية في العينة: " + "، ".join(chosen))
    note("في العمل الحقيقي لا أحد يخبرك الجواب: تعتمد على الطاقة + الشدة + عمر النصف معاً.")

    # -------- 3) المساحة الصافية --------
    step("الخطوة 3: احسب المساحة الصافية لقمة تختارها")
    if found:
        c_peak = ask_int("رقم قناة مركز القمة", found[-1], 1, NCH - 2)
    else:
        c_peak = int(NCH / 2)
    half = ask_int("نصف عرض منطقة القمة (قنوات)", max(3, int(3 * sigma_ch(1000))), 1, 40)
    lo_p, hi_p = max(0, c_peak - half), min(NCH - 1, c_peak + half)
    lo_b, hi_b = max(0, c_peak - 2 * half), max(0, c_peak - half - 1)
    lo_b2, hi_b2 = min(NCH - 1, c_peak + half + 1), min(NCH - 1, c_peak + 2 * half)

    gross = sum(spec[lo_p:hi_p + 1])
    n_pk = hi_p - lo_p + 1
    side1 = sum(spec[lo_b:hi_b + 1]) if hi_b >= lo_b else 0
    side2 = sum(spec[lo_b2:hi_b2 + 1]) if hi_b2 >= lo_b2 else 0
    n_b = (hi_b - lo_b + 1 if hi_b >= lo_b else 0) + (hi_b2 - lo_b2 + 1 if hi_b2 >= lo_b2 else 0)
    bkg_per_ch = (side1 + side2) / n_b if n_b else 0.0
    net = gross - bkg_per_ch * n_pk
    sigma_net = math.sqrt(gross + (bkg_per_ch * n_pk) * (n_pk / n_b if n_b else 0))

    print(f"\n  العدد الإجمالي في منطقة القمة: {gross}")
    print(f"  الخلفية المقدّرة: {bkg_per_ch:.2f}/قناة × {n_pk} قناة = {bkg_per_ch*n_pk:.1f}")
    print(f"  **المساحة الصافية = {net:.1f} ± {sigma_net:.1f}** "
          f"(عدم يقين نسبي {100*sigma_net/max(net,1e-9):.1f}٪)")

    # -------- 4) MDA --------
    step("الخطوة 4: حدّ الكشف الأدنى (MDA)")
    Lc = 1.64 * math.sqrt(bkg_per_ch * n_pk)                 # المستوى الحرج
    Ld = 2.71 + 4.65 * math.sqrt(bkg_per_ch * n_pk)          # حدّ الكشف الأدنى بالعدد
    print("  صيغة شائعة للعدّ (Currie):")
    print("     المستوى الحرج  Lc = 1.64·√B")
    print("     حدّ الكشف      Ld = 2.71 + 4.65·√B")
    print(f"  هنا B = {bkg_per_ch*n_pk:.1f} ⇒ Lc = {Lc:.1f} عدد، Ld = {Ld:.1f} عدد")
    if net > Ld:
        good(f"القمة «مكتشفة» فعلاً (الصافي {net:.0f} > Ld).")
    else:
        warn("القمة تحت حدّ الكشف: لا تستطيع إعلان اكتشافها — بل تعلن حدّاً أعلى.");

    step("دروس هذا المختبر")
    note("• المعايرة تحوّل «رقم قناة» إلى «طاقة»؛ بدونها الطيف بلا معنى فيزيائي.")
    note("• المساحة الصافية ≠ العدد الإجمالي: الخلفية تُقدَّر من جانبي القمة وتُطرح.")
    note("• عدم يقين المساحة الصافية يجمع عدم يقين الإجمالي والخلفية.")
    note("• «لم أرَ قمة» لا يعني «لا وجود للنويدة»؛ يعني «أقل من MDA» — وهذا فرق جوهري في التقارير.")
    note("• في العمل الحقيقي تُضاف تصحيحات: الكفاءة مقابل الطاقة، التراكب، الزمن الميت، الهندسة.")
    print()


def main():
    run()


if __name__ == "__main__":
    main()
