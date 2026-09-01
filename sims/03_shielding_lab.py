# -*- coding: utf-8 -*-
"""
المختبر 03 — مختبر التدريع والجرعة.

مهمتك: صمّم درعاً يخفض معدل الجرعة إلى هدف محدّد، بأقل وزن/تكلفة ممكنة.
النموذج مبسّط لكنه صحيح فيزيائياً في خطوطه العامة:
   - التوهين الأُسّي:  I = I₀ · B · e^(−μx)
   - معامل «التراكم» B يزيد الجرعة عن التوهين البسيط (الأشعة المتشتتة).
   - قانون التربيع العكسي للمسافة.
   - تحويل معدل الجرعة إلى جرعة متراكمة:  الجرعة = المعدل × الزمن.

قيم μ/ρ تقريبية تعليمية (سم²/غ) وليست بيانات تصميمية.
"""
from __future__ import annotations

import math

try:
    from .engine import (RNG, ask, ask_float, ask_int, bad, good, header, note, pause,
                    plot, rel_err, seed, step, table, warn)
except ImportError:  # تشغيل مباشر: python3 sims/01_decay_lab.py
    from engine import (RNG, ask, ask_float, ask_int, bad, good, header, note, pause,
                    plot, rel_err, seed, step, table, warn)

# كثافة (غ/سم³) ومعامل التوهين الكتلي للفوتونات (سم²/غ) عند طاقتين شائعتين
MATERIALS = {
    "رصاص":   {"rho": 11.35, "mu_over_rho": {0.662: 0.1106, 1.25: 0.0589}, "cost": 3.0},
    "حديد":   {"rho": 7.87,  "mu_over_rho": {0.662: 0.0735, 1.25: 0.0535}, "cost": 1.0},
    "خرسانة": {"rho": 2.30,  "mu_over_rho": {0.662: 0.0770, 1.25: 0.0570}, "cost": 0.15},
    "ماء":    {"rho": 1.00,  "mu_over_rho": {0.662: 0.0856, 1.25: 0.0630}, "cost": 0.01},
}
SOURCES = {
    "سيزيوم-137": {"E": 0.662, "dose_const": 3.3e-3},   # mSv/h لكل GBq على 1 م (تقريبي تعليمي)
    "كوبالت-60":  {"E": 1.25,  "dose_const": 1.3e-2},
}


def buildup(mux: float) -> float:
    """معامل تراكم تقريبي (Berger-like): B ≈ 1 + a·(μx)·e^(b·μx)."""
    return 1.0 + 0.9 * mux * math.exp(0.15 * min(mux, 20.0))


def dose_rate(activity_gbq, dist_m, material, thickness_cm, energy):
    src = SOURCES[
        "سيزيوم-137" if abs(energy - 0.662) < 0.05 else "كوبالت-60"]
    d0 = activity_gbq * src["dose_const"] / max(dist_m, 0.05) ** 2   # mSv/h بلا درع
    mu = MATERIALS[material]["mu_over_rho"][energy] * MATERIALS[material]["rho"]
    x = max(thickness_cm, 0.0)
    return d0 * buildup(mu * x) * math.exp(-mu * x), d0, mu


def run():
    header("المختبر 03 — مختبر التدريع والجرعة",
           "صمّم درعاً يصل بمعدل الجرعة إلى الهدف — وحاسب الوزن والتكلفة")

    _s = ask("رقم البذرة العشوائية (فارغ = عشوائي)", "")
    seed(int(_s) if _s.strip().lstrip("-").isdigit() else None)

    sname = list(SOURCES)[ask_int("المصدر: 1) سيزيوم-137   2) كوبالت-60", 1, 1, 2) - 1]
    energy = SOURCES[sname]["E"]
    A = ask_float("نشاط المصدر (GBq)", 10.0, 0.001, 1e6)
    r = ask_float("المسافة إلى نقطة العمل (م)", 2.0, 0.05, 100.0)
    hours = ask_float("ساعات العمل الأسبوعية عند تلك النقطة", 10.0, 0.1, 168.0)
    target = ask_float("الهدف: معدل جرعة لا يتجاوز (mSv/ساعة)", 0.01, 1e-6)

    _, d0, _ = dose_rate(A, r, "رصاص", 0.0, energy)
    header("الحالة بلا أي درع", "")
    print(f"  معدل الجرعة على بُعد {r:g} م = {d0:.3e} mSv/ساعة")
    print(f"  الجرعة الأسبوعية = {d0*hours:.3e} mSv/أسبوع")
    note("للمقارنة: الحد المهني الشائع ≈ 20 mSv/سنة (مرجع: توصيات ICRP ولوائح وطنية — راجع بلدك).")
    print(f"  ⇒ بلا درع تتجاوز الحد السنوي في {20.0/(d0*hours*52):.3g} أسبوع إن واصل العمل.")

    step("صفحة التصميم: اختر المادة والسماكة")
    print("  المواد المتاحة: 1) رصاص  2) حديد  3) خرسانة  4) ماء")
    mkey = list(MATERIALS)[ask_int("رقم المادة", 3, 1, 4) - 1]
    mat = MATERIALS[mkey]

    step("مسح للسماكة (لترى المنحنى قبل أن تختار)")
    xs, ys = [], []
    for i in range(41):
        x = i * 0.5
        d, _, _ = dose_rate(A, r, mkey, x, energy)
        xs.append(x); ys.append(d)
    plot(xs, [math.log10(max(v, 1e-12)) for v in ys],
         title=f"لوغاريتم معدل الجرعة مقابل سماكة {mkey} (سم)", ylabel="السماكة (سم)")
    note("لاحظ: المنحنى ليس خطاً مستقيماً تماماً بسبب معامل التراكم B عند السماكات الكبيرة.")

    x = ask_float(f"سماكة {mkey} (سم)", 5.0, 0.0, 200.0)
    d, d0, mu = dose_rate(A, r, mkey, x, energy)
    area_m2 = 1.0  # نعتبر درعاً بمساحة 1 م² للمقارنة
    volume_cm3 = area_m2 * 1e4 * x
    mass_kg = volume_cm3 * mat["rho"] / 1000.0
    cost = mass_kg * mat["cost"]

    header("نتيجة تصميمك", "")
    table([("بلا درع", f"{d0:.3e}", "—"),
           (f"{mkey} {x:g} سم", f"{d:.3e}", f"تخفيض ×{d0/max(d,1e-30):.3g}")],
          ["الحالة", "mSv/ساعة", "عامل التخفيض"], aligns=["<", ">", ">"])
    print(f"\n  الكتلة التقريبية لدرع بمساحة 1 م²: {mass_kg:,.0f} كجم")
    print(f"  مؤشر التكلفة النسبية: {cost:,.0f} (وحدات نسبية)")
    print(f"  الجرعة الأسبوعية بعد التدريع: {d*hours:.3e} mSv")

    if d <= target:
        good(f"نجحت: {d:.3e} ≤ الهدف {target:g} mSv/ساعة.")
        # هل هناك تصميم أخف؟
        best = None
        for mk, mv in MATERIALS.items():
            lo, hi = 0.0, 400.0
            for _ in range(60):
                mid = (lo + hi) / 2
                dd, _, _ = dose_rate(A, r, mk, mid, energy)
                if dd > target:
                    lo = mid
                else:
                    hi = mid
            vol = 1e4 * hi
            mass = vol * mv["rho"] / 1000.0
            if best is None or mass < best[1]:
                best = (mk, mass, hi)
        note(f"أخف تصميم يصل للهدف: {best[0]} بسماكة ≈ {best[2]:.1f} سم "
             f"(كتلة ≈ {best[1]:,.0f} كجم)")
    else:
        warn(f"لم تصل للهدف: تحتاج سماكة أكبر، أو مسافة أكبر، أو وقت أقل.")
        need_t = 20.0 / 52.0 / max(d * hours, 1e-30)
        note("تذكّر مبادئ الحماية الثلاثة: **الزمن · المسافة · التدريع** — "
             "الدرع ليس الخيار الوحيد.")
        print(f"  لو قلّصت الزمن إلى {min(hours, hours/ (d/target)):.2f} ساعة/أسبوع لبلغت الهدف.")

    step("دروس هذا المختبر")
    note("• التوهين أُسّي: كل «طبقة نصفية قيمة» تضاعف التخفيض — لهذا تدرّع بالطبقات لا بالسماكة وحدها.")
    note("• معامل التراكم يعني أن الأشعة المتشتتة لا تختفي: لا تثق بالحساب البسيط عند السماكات الكبيرة.")
    note("• المسافة سلاح مجاني: مضاعفة المسافة = ربع الجرعة (قانون التربيع العكسي).")
    note("• الزمن عامل مباشر في الجرعة المتراكمة: الجرعة = المعدل × الزمن.")
    note("• القيم هنا تعليمية؛ التصميم الحقيقي يحتاج كود انتقال إشعاعي ومراجعة مختص حماية.")
    print()


def main():
    run()


if __name__ == "__main__":
    main()
