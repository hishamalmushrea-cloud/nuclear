# -*- coding: utf-8 -*-
"""
المختبر 04 — حركية المفاعل النقطية (تفاعلي).

تحرّك «قضيب تحكم» افتراضياً فتتحرك القدرة أمامك. سترى بنفسك:
  • لماذا النيوترونات المتأخرة هي التي تجعل التحكم ممكناً.
  • كيف تعطي خطوة تفاعلية صغيرة «وثبة سريعة» ثم نمواً بطيئاً.
  • ماذا يحدث إن تجاوزت ρ = β (خطر: نمو سريع جداً).
  • كيف يعمل الإيقاف السريع (SCRAM).

النموذج: حركية النقطة بست مجموعات من النيوترونات المتأخرة:
    dn/dt   = (ρ−β)/Λ · n + Σ λᵢ Cᵢ
    dCᵢ/dt  = βᵢ/Λ · n − λᵢ Cᵢ
البيانات: يورانيوم-235 حراري — β = 0.0065، Λ = 2×10⁻⁵ ث (تقريبية تعليمية).
"""
from __future__ import annotations

import math

try:
    from .engine import (ask, ask_float, ask_int, bad, good, header, note, pause, plot,
                    step, table, warn)
except ImportError:  # تشغيل مباشر: python3 sims/01_decay_lab.py
    from engine import (ask, ask_float, ask_int, bad, good, header, note, pause, plot,
                    step, table, warn)

BETA = 0.0065
LAMBDA_GEN = 2.0e-5          # Λ (ث)
BETA_I = [0.033, 0.219, 0.196, 0.395, 0.115, 0.042]      # كسور من β
LAMBDA_I = [0.0124, 0.0305, 0.111, 0.301, 1.14, 3.01]    # ث⁻¹


def steady_precursors(n, beta, lam_gen):
    """التركيز المتوازن للنيوترونات المتأخرة عند قدرة ثابتة."""
    return [(b * beta / lam_gen) * n / l for b, l in zip(BETA_I, LAMBDA_I)]


def simulate(rho_steps, total_time=200.0, dt=1e-3, n0=1.0, scram_at=None):
    """rho_steps: قائمة (زمن_البداية، ρ) — تُطبّق عند تجاوز الزمن."""
    n = n0
    C = steady_precursors(n, BETA, LAMBDA_GEN)
    t = 0.0
    steps = int(total_time / dt)
    rho = rho_steps[0][1] if rho_steps else 0.0
    idx = 0
    ts, powers = [], []
    sample_every = max(1, int(0.5 / dt))
    for k in range(steps):
        while idx < len(rho_steps) and t >= rho_steps[idx][0]:
            rho = rho_steps[idx][1]
            idx += 1
        if scram_at is not None and t >= scram_at:
            rho = -10.0 * BETA  # إيقاف سريع: تفاعلية سالبة كبيرة
        dni = (rho - BETA) / LAMBDA_GEN * n
        for i in range(6):
            dni += LAMBDA_I[i] * C[i]
        n += dt * dni
        for i in range(6):
            C[i] += dt * (BETA_I[i] * BETA / LAMBDA_GEN * n - LAMBDA_I[i] * C[i])
        if n < 1e-30:
            n = 1e-30
        t += dt
        if k % sample_every == 0:
            ts.append(t)
            powers.append(n)
    return ts, powers


def run():
    header("المختبر 04 — حركية المفاعل: العب بقضيب التحكم",
           "النيوترونات المتأخرة = سبب أن المفاعل قابل للتحكم أصلاً")

    note(f"β = {BETA:g} · Λ = {LAMBDA_GEN:g} ث · القدرة الابتدائية = 100٪ (نسبة)")
    note("التفاعلية تُكتب عادة بـ«الدولار»: 1$ = ρ/β. أي ρ = β يعني 1$.")
    print("""
  قواعد اللعبة:
   • ρ = 0        ⇒ قدرة ثابتة (حرجية بالضبط).
   • ρ > 0        ⇒ قدرة صاعدة.
   • ρ = β (1$)   ⇒ «الحرجية السريعة»: النمو يعتمد على النيوترونات الفورية وحدها.
   • ρ > β        ⇒ خطر: النمو خلال أجزاء من الثانية.
   • ρ < 0        ⇒ قدرة هابطة.
""")

    step("التجربة 1: خطوة تفاعلية صغيرة")
    dollars = ask_float("كم دولاراً تريد إدخالها؟ (0.1 = آمن، 1.0 = حدّي، >1 = خطر)", 0.1, -5, 1.5)
    rho = dollars * BETA
    T = ask_float("زمن المحاكاة (ثانية)", 120.0, 5.0, 600.0)
    ts, powers = simulate([(0.0, rho)], total_time=T)
    plot(ts, [math.log10(max(p, 1e-12)) for p in powers],
         title=f"لوغاريتم القدرة مقابل الزمن عند ρ = {dollars:g}$", ylabel="الزمن (ث)")
    print(f"  القدرة الابتدائية: {powers[0]:.4g}")
    print(f"  القدرة النهائية:   {powers[-1]:.4g}")
    if dollars > 0:
        # قياس «الفترة» الزمنية e-fold
        if powers[-1] > powers[0]:
            period = T / math.log(powers[-1] / powers[0])
            print(f"  فترة تضاعف الأسّي (e-folding) ≈ {period:.3g} ثانية")
            note("هذه هي «فترة المفاعل»: المقياس العملي الذي يراقبه المشغّل.")
    pause()

    step("التجربة 2: مقارنة ثلاث خطوات")
    rows = []
    for d in (0.1, 0.5, 1.0):
        _, p = simulate([(0.0, d * BETA)], total_time=20.0)
        ratio = p[-1] / p[0]
        rows.append((f"{d:g}$", f"{ratio:.4g}", f"{20.0/max(math.log(ratio),1e-9):.4g}"))
    table(rows, ["التفاعلية", "نسبة القدرة بعد 20 ث", "الفترة (ث)"], aligns=["<", ">", ">"])
    note("لاحظ الفرق الهائل بين 0.1$ و1$: هذا هو هامش الأمان الذي يمنحه تأخّر النيوترونات.")

    step("التجربة 3: الإيقاف السريع (SCRAM)")
    d2 = ask_float("ابدأ بخطوة تفاعلية (دولار)", 0.3, -1, 1.2)
    trig = ask_float("عند أي قدرة (نسبة من الابتدائية) تُفعّل الإيقاف السريع؟", 5.0, 1.01)
    # نحسب زمن الوصول إلى العتبة أولاً
    ts1, p1 = simulate([(0.0, d2 * BETA)], total_time=600.0)
    t_trig = None
    for tt, pp in zip(ts1, p1):
        if pp >= trig:
            t_trig = tt
            break
    if t_trig is None:
        warn("لم تصل القدرة إلى العتبة خلال 600 ث — الخطوة صغيرة جداً.")
    else:
        print(f"  بلغت القدرة {trig:g}× عند t ≈ {t_trig:.1f} ث ⇒ SCRAM")
        ts2, p2 = simulate([(0.0, d2 * BETA)], total_time=t_trig + 60.0, scram_at=t_trig)
        plot(ts2, p2, title="القدرة بعد الإيقاف السريع (SCRAM)", ylabel="الزمن (ث)")
        print(f"  القدرة بعد 60 ث من الإيقاف: {p2[-1]:.4g} (من الذروة {max(p2):.4g})")
        note("القدرة لا تهبط فوراً إلى الصفر: النيوترونات المتأخرة تبقيها «متلاشية» ببطء، "
             "وهذا بالضبط ما يجعل الإيقاف الآمن ممكناً.")

    step("التجربة 4: ماذا لو تجاوزت 1$؟ (فقط للمشاهدة)")
    ts3, p3 = simulate([(0.0, 1.05 * BETA)], total_time=2.0, dt=2e-4)
    print(f"  بعد 2 ثانية فقط: القدرة × {p3[-1]/p3[0]:.3g}")
    warn("عند ρ > β لا ينقذك إلا التصميم (معاملات تفاعلية سالبة) وأنظمة الحماية المستقلة — "
         "وليس ردّ فعل المشغّل. هذه هي الفيزياء التي تقف خلف كل نظام حماية في مفاعل حقيقي.")

    step("دروس هذا المختبر")
    note("• β صغير (0.65٪) لكنه الفارق بين «آلة يمكن قيادتها» و«قنبلة موقوتة».")
    note("• الوثبة السريعة ثم النمو البطيء = توقيع النيوترونات المتأخرة.")
    note("• «فترة المفاعل» هي المقياس العملي، لا ρ وحدها.")
    note("• الإيقاف السريع يضخ تفاعلية سالبة كبيرة؛ القدرة تهبط لكن التسخين المتحلل يبقى (راجع MAP/07).")
    print()


def main():
    run()


if __name__ == "__main__":
    main()
