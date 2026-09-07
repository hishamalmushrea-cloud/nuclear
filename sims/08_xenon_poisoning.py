# -*- coding: utf-8 -*-
"""
08 — مختبر تسمّم الزينون وحفرة اليود (Xenon-135 poisoning & iodine pit)

الفيزياء — منظومة معادلتين تفاضليتين مقترنتين (بلا أي تبسيط):

    dI/dt = γ_I · Σ_f · Φ − λ_I · I                        (اليود-135)
    dX/dt = γ_X · Σ_f · Φ + λ_I · I − λ_X · X − σ_X · Φ·X   (الزينون-135)

    ρ_Xe(t) = − (σ_X · X(t)) / Σ_a_core            (قيمة التفاعلية بالـ Δk/k)

الثوابت (منشورة):
    λ_I  = 2.87×10⁻⁵ s⁻¹   (T½ = 6.58 h)   γ_I  = 0.0639
    λ_X  = 2.09×10⁻⁵ s⁻¹   (T½ = 9.17 h)   γ_X  = 0.00237
    σ_X  = 2.65×10⁻¹⁸ cm²  = 2.65×10⁶ b    (أكبر مقطع امتصاص حراري معروف تقريباً)

لماذا هذا المختبر مهم؟
    لأن Xe-135 **يصنعه الاضمحلال بعد الإيقاف**: يتوقف المفاعل، فيتوقف «حرق»
    الزينون بالنيوترونات (الحد σ_X Φ X)، بينما يستمر اليود المتراكم يتحلّل
    إلى زينون. فيرتفع السمّ ساعات بعد الإيقاف — **حفرة اليود** — وتصبح
    إعادة التشغيل مستحيلة مؤقتاً إن لم تكن لك تفاعلية فائضة كافية.
    هذا ليس تفصيلاً: هو سبب قيود تشغيل حقيقية (وله دور معروف في تشيرنوبل).

المحاكاة: تكامل RK4 بخطوة ثابتة (مستقر لهذه الثوابت)، والتحقق من حالة
الاستقرار التحليلية قبل الإيقاف.
"""
from __future__ import annotations

import math

try:
    from .engine import (header, step, note, warn, good, bad, ask, ask_float,
                         ask_int, pause, plot, table, rel_err)
except ImportError:
    from engine import header, step, note, warn, good, bad, ask, ask_float, ask_int, \
        pause, plot, table, rel_err


LAM_I = 2.87e-5      # s⁻¹ — ثابت تحلل I-135
LAM_X = 2.09e-5      # s⁻¹ — ثابت تحلل Xe-135
GAM_I = 0.0639       # ناتج الانشطار لسلسلة I-135
GAM_X = 0.00237      # ناتج الانشطار المباشر لـ Xe-135
SIG_X = 2.65e-18     # cm² — مقطع امتصاص Xe-135 الحراري (2.65 مليون barn)
BETA = 0.0065        # كسر النيوترونات المتأخرة (تمثيلي)


def xe_eq(flux, sigma_f, gam_i=GAM_I, gam_x=GAM_X):
    """الزينون عند الاستقرار: X = (γ_I+γ_X)Σ_fΦ / (λ_X + σ_X Φ)."""
    fx = sigma_f * flux
    return (gam_i + gam_x) * fx / (LAM_X + SIG_X * flux)


def i_eq(flux, sigma_f, gam_i=GAM_I):
    return gam_i * sigma_f * flux / LAM_I


def worth(Xe, sigma_a_core):
    """قيمة التفاعلية السالبة للزينون: Δk/k."""
    return -(SIG_X * Xe) / sigma_a_core


def rhs(I, X, flux, sigma_f):
    fx = sigma_f * flux
    dI = GAM_I * fx - LAM_I * I
    dX = GAM_X * fx + LAM_I * I - LAM_X * X - SIG_X * flux * X
    return dI, dX


def integrate(I0, X0, flux, sigma_f, t_end, dt=60.0):
    """تكامل RK4 للمنظومة — يعيد قائمة (t, I, X) بخطوة زمنية للتسجيل."""
    I, X = I0, X0
    out = [(0.0, I, X)]
    n = int(t_end / dt)
    record_every = max(1, n // 720)
    for k in range(1, n + 1):
        k1i, k1x = rhs(I, X, flux, sigma_f)
        k2i, k2x = rhs(I + 0.5 * dt * k1i, X + 0.5 * dt * k1x, flux, sigma_f)
        k3i, k3x = rhs(I + 0.5 * dt * k2i, X + 0.5 * dt * k2x, flux, sigma_f)
        k4i, k4x = rhs(I + dt * k3i, X + dt * k3x, flux, sigma_f)
        I += dt / 6.0 * (k1i + 2 * k2i + 2 * k3i + k4i)
        X += dt / 6.0 * (k1x + 2 * k2x + 2 * k3x + k4x)
        if k % record_every == 0 or k == n:
            out.append((k * dt, I, X))
    return out


def run():
    header("مختبر تسمّم الزينون وحفرة اليود",
           "أوقف المفاعل… ثم شاهد السمّ يرتفع بعد أن أطفأته")

    step("المنظومة:")
    print("""
    dI/dt = γ_I·Σ_f·Φ − λ_I·I
    dX/dt = γ_X·Σ_f·Φ + λ_I·I − λ_X·X − σ_X·Φ·X
    ρ_Xe  = −σ_X·X / Σ_a قلب

    λ_I = 2.87e-5 s⁻¹ (6.58 س)   γ_I = 6.39٪
    λ_X = 2.09e-5 s⁻¹ (9.17 س)   γ_X = 0.24٪
    σ_X = 2.65e6 barn  ← أكبر مقطع امتصاص حراري معروف تقريباً
""")
    note("الحد الحاسم في المعادلة الثانية هو **σ_X·Φ·X**: المفاعل وهو يعمل "
         "يحرق الزينون بالنيوترونات. أوقفه فيختفي هذا الحد… واليود لا يزال يصنع زينوناً.")

    flux = ask_float("؟ فيض النيوترونات الحرارية Φ (ن/سم²·ث) — PWR نموذجي 3e13: ",
                     3e13, 1e8, 1e16)
    sigma_f = ask_float("؟ المقطع الفصلي الماكروسكوبي Σ_f (cm⁻¹) — نموذجي 0.10: ",
                        0.10, 0.001, 5.0)
    sigma_a = ask_float("؟ Σ_a الفعّال للقلب (cm⁻¹) لتحويل السمّ إلى تفاعلية — نموذجي 0.20: ",
                        0.20, 0.01, 5.0)
    hours_op = ask_float("؟ ساعات التشغيل قبل الإيقاف (يكفي 300 س للوصول للاستقرار): ",
                         400.0, 1.0, 5000.0)

    step("أُشغّل المفاعل حتى الاستقرار…")
    steady = integrate(0.0, 0.0, flux, sigma_f, hours_op * 3600.0, dt=120.0)
    t_op, I0, X0 = steady[-1]
    X_analytic = xe_eq(flux, sigma_f)
    I_analytic = i_eq(flux, sigma_f)
    print(f"  بعد {hours_op:.0f} ساعة تشغيل:")
    print(f"    I-135 = {I0:.4e} ذرة/سم³   (تحليلي {I_analytic:.4e})")
    print(f"    Xe-135 = {X0:.4e} ذرة/سم³  (تحليلي {X_analytic:.4e}) — "
          f"فرق {abs(X0-X_analytic)/X_analytic*100:.3f}٪")
    r_eq = worth(X0, sigma_a)
    print(f"    قيمة الزينون عند التشغيل: ρ = {r_eq*1e5:.0f} pcm = "
          f"{r_eq/BETA:.1f} $   (أي يأكل {abs(r_eq)*100:.2f}٪ من k)")
    note("هذه هي «الضريبة» التي يدفعها أي مفاعل يعمل: جزء من التفاعلية محجوز دائماً للزينون.")

    print()
    guess_h = ask_float("؟ بعد الإيقاف: كم ساعة تمضي حتى يبلغ الزينون ذروته؟ ", 10.0, 0.1, 200.0)
    guess_rho = ask_float("؟ كم تتوقع أن تكون قيمة الزينون عند الذروة (pcm، القيمة مطلقة)؟ ",
                          abs(r_eq) * 1.6 * 1e5, 1.0, 1e6)

    step("أوقف المفاعل في t=0 وأتابع المنظومة 72 ساعة…")
    traj = integrate(I0, X0, 0.0, sigma_f, 72 * 3600.0, dt=60.0)

    peak_t, peak_x = max(((t, x) for t, _, x in traj), key=lambda p: p[1])
    peak_h = peak_t / 3600.0
    rho_peak = worth(peak_x, sigma_a)
    ratio = peak_x / X0 if X0 > 0 else float("inf")

    good(f"الذروة بعد **{peak_h:.1f} ساعة** من الإيقاف")
    print(f"  Xe عند الذروة = {peak_x:.4e} ذرة/سم³ = **{ratio:.2f}×** قيمته عند التشغيل")
    print(f"  التفاعلية عند الذروة: ρ = {rho_peak*1e5:.0f} pcm = {rho_peak/BETA:.1f} $ "
          f"(أي {abs(rho_peak)*100:.2f}٪ من k)")

    e_h = rel_err(guess_h, peak_h)
    e_r = rel_err(guess_rho, abs(rho_peak) * 1e5)
    print(f"\n  تخمينك للزمن: {guess_h:.1f} س (خطأ {e_h:.1f}٪) · "
          f"للقيمة: {guess_rho:.0f} pcm (خطأ {e_r:.1f}٪)")
    if e_h < 15 and e_r < 25:
        good("ممتاز — تفهم حفرة اليود فهماً تشغيلياً.")
    else:
        note("السبب الفيزيائي: بعد الإيقاف يتوقف «الحرق» σ_XΦX، ويستمر اليود (6.58 س) "
             "يغذّي الزينون (9.17 س). الذروة حيث يتقاطع الإنتاج مع التحلل.")

    step("جدول زمني بعد الإيقاف:")
    rows = []
    for h in (0, 2, 5, 8, 10, 12, 15, 20, 24, 36, 48, 72):
        t = h * 3600.0
        best = min(traj, key=lambda p: abs(p[0] - t))
        _, Ii, Xx = best
        rows.append((f"{h:>3d}", f"{Ii:.3e}", f"{Xx:.3e}",
                     f"{worth(Xx, sigma_a)*1e5:>7.0f}",
                     f"{worth(Xx, sigma_a)/BETA:>6.1f}"))
    table(rows, ["الساعة", "I-135", "Xe-135", "ρ (pcm)", "ρ ($)"],
          aligns=[">", ">", ">", ">", ">"])

    step("منحنى الزينون بعد الإيقاف:")
    ts = [t / 3600.0 for t, _, _ in traj]
    xs = [x for _, _, x in traj]
    plot(ts, xs, title="تركيز Xe-135 مقابل الزمن بعد الإيقاف (ساعات)",
         ylabel="الزمن (ساعة) — لاحظ الذروة ثم الهبوط البطيء")

    step("التفاعلية الفائضة: هل تستطيع إعادة التشغيل؟")
    excess = ask_float(f"؟ كم تفاعلية فائضة يملك قضيبك (pcm)؟ (الزينون عند الذروة "
                       f"{abs(rho_peak)*1e5:.0f} pcm): ", 4000.0, 0.0, 20000.0)
    need = abs(rho_peak) * 1e5
    # نافذة إعادة التشغيل: الفترات التي يكون فيها السمّ أقل من التفاعلية الفائضة
    times = [t / 3600.0 for t, _, x in traj if abs(worth(x, sigma_a)) * 1e5 <= excess]
    if excess > need:
        good(f"نعم: {excess:.0f} > {need:.0f} pcm — يمكنك إعادة التشغيل في أي وقت، "
             f"حتى عند ذروة السمّ.")
    else:
        bad(f"لا عند الذروة: تحتاج {need:.0f} pcm وتملك {excess:.0f} pcm — "
            f"حفرة يود عمقها {need - excess:.0f} pcm.")
        # أول لحظة يدخل فيها السمّ في الحفرة، وأول لحظة يخرج منها
        t_enter = t_exit = None
        prev_ok = abs(worth(traj[0][2], sigma_a)) * 1e5 <= excess
        for t, _, x in traj[1:]:
            ok = abs(worth(x, sigma_a)) * 1e5 <= excess
            if prev_ok and not ok and t_enter is None:
                t_enter = t / 3600.0
            if not prev_ok and ok and t_enter is not None and t_exit is None:
                t_exit = t / 3600.0
            prev_ok = ok
        if t_enter is None:
            print("  السمّ تحت فائضك طوال الـ72 ساعة — لا حفرة تمنعك.")
        else:
            print(f"  نافذتك الآن مفتوحة لكنها **تُغلق بعد ≈ {t_enter:.1f} ساعة** "
                  f"(حين يتجاوز السمّ {excess:.0f} pcm).")
            if t_exit is not None:
                print(f"  ثم لا يمكنك إعادة التشغيل حتى ≈ **{t_exit:.1f} ساعة** بعد الإيقاف "
                      f"(≈ {t_exit - t_enter:.1f} ساعة من الحفرة).")
            else:
                print("  ولا تُفتح النافذة مجدداً خلال 72 ساعة من الإيقاف.")
        note("هذه ظاهرة حقيقية حاكمة: بعد إيقاف مفاعل عالي الفيض، قد لا تستطيع "
             "إعادة تشغيله بعد ساعات **ولو أردت** — حتى مع كل القضبان مرفوعة. "
             "ولهذا تُخطَّط فترات التوقف و«هوامش الزينون» مسبقاً.")

    step("العب: كيف تتغيّر الذروة مع الفيض؟ (الفيض العالي = حفرة أعمق)")
    rows = []
    for f in (0.1, 0.5, 1.0, 2.0, 4.0):
        fl = flux * f
        x_eqf = xe_eq(fl, sigma_f)
        st = integrate(0.0, 0.0, fl, sigma_f, 400 * 3600.0, dt=180.0)
        I_0f, X_0f = st[-1][1], st[-1][2]
        tj = integrate(I_0f, X_0f, 0.0, sigma_f, 72 * 3600.0, dt=120.0)
        pt, px = max(((t, x) for t, _, x in tj), key=lambda p: p[1])
        rows.append((f"{fl:.2e}", f"{x_eqf:.3e}", f"{pt/3600:.1f}",
                     f"{px/X_0f:.2f}×", f"{abs(worth(px, sigma_a))*1e5:>7.0f}"))
    table(rows, ["الفيض", "Xe استقرار", "زمن الذروة (س)", "نسبة الذروة", "ρ الذروة (pcm)"],
          aligns=[">", ">", ">", ">", ">"])
    note("لاحظ: الفيض العالي ⇒ زينون استقرار أعلى (يشتغل المفاعل وهو «مسمّم» أكثر)، "
         "وحفرة أعمق بعد الإيقاف. وفي فيض منخفض جداً لا تكاد توجد حفرة.")

    note("""
ما وراء هذا المختبر (مفتوح بالكامل في الخريطة):
  السموم الأخرى: Sm-149 (مستقر، لا يتحلل بعد الإيقاف) و Gd · تسمّم متأخر
  · توزّع الزينون **المكاني** وتذبذباته (xenon oscillations) في القلوب الكبيرة
  · اقتران النيوترونيات بالحرارة (feedback loops) واستقرار القلب
  · تسمّم الزينون في الإيقاف البارد مقابل الحمل المتغيّر (load-follow)
  · دوره في حادثة تشيرنوبل (1986): مفاعل أُبقي تحت الطاقة ساعات، فتراكم اليود،
    ثم محاولة إعادة تشغيل من حفرة — اقرأ `safe.accidents` للتفصيل التقني.""")
    pause()


if __name__ == "__main__":
    run()
