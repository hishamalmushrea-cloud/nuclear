# -*- coding: utf-8 -*-
"""
المختبر 02 — محاكي عدّاد غايغر/ميولر التفاعلي.

يتعلّم فيه المستخدم ثلاث حقائق لا تُرى في الكتب بوضوح:
  1. الجهاز لا يرى كل شيء: الكفاءة × الهندسة (قانون التربيع العكسي).
  2. هناك خلفية دائماً يجب طرحها.
  3. للجهاز «زمن ميت»: عند المعدلات العالية يسرق نبضات، فيجب التصحيح.

المطلوب منك: قِس، صحّح، ثم استنتج النشاط الحقيقي للمصدر.
"""
from __future__ import annotations

import math

try:
    from .engine import (RNG, ask, ask_float, ask_int, bad, good, header, note, pause,
                    poisson, rel_err, seed, step, table, warn)
except ImportError:  # تشغيل مباشر: python3 sims/01_decay_lab.py
    from engine import (RNG, ask, ask_float, ask_int, bad, good, header, note, pause,
                    poisson, rel_err, seed, step, table, warn)

DET_AREA_CM2 = 8.0  # مساحة نافذة الكاشف (سم²)

SOURCES = [
    ("أمريسيوم-241", "Am-241", 3.7e4, "ألفا + غاما 59 keV — كواشف الدخان"),
    ("سيزيوم-137", "Cs-137", 1.85e5, "غاما 662 keV — معايرة",),
    ("كوبالت-60", "Co-60", 9.25e3, "غاما 1.17 و1.33 MeV"),
    ("سترونتيوم-90", "Sr-90", 2.2e4, "بيتا خالص تقريباً"),
]


def geometry(r_cm: float) -> float:
    """كسر الفضاء الذي تراه نافذة الكاشف على بُعد r من مصدر نقطي."""
    return DET_AREA_CM2 / (4.0 * math.pi * r_cm ** 2)


def measure(true_rate, live_time, dead_time, background):
    """محاكاة قياس حقيقي: خلفية + ضجيج بواسون + زمن ميت غير مشلّ."""
    gross_true = true_rate + background
    n = poisson(gross_true * live_time)          # ما «كان يجب» أن يُعدّ
    # نموذج غير مشلّ (non-paralyzable): m = n / (1 + n·τ/t)
    m = n / (1.0 + n * dead_time / live_time) if dead_time > 0 else n
    return int(m)


def correct(counts, live_time, dead_time, background):
    """تصحيح الزمن الميت (إعادة بناء n من m) ثم طرح الخلفية."""
    m_rate = counts / live_time
    n_rate = m_rate / (1.0 - m_rate * dead_time) if (1.0 - m_rate * dead_time) > 0 else float("inf")
    return n_rate - background


def run():
    header("المختبر 02 — عدّاد غايغر: كفاءة، خلفية، وزمن ميت",
           "قِس مصدراً مجهولاً واستنتج نشاطه الحقيقي بالـ Bq")

    _s = ask("رقم البذرة العشوائية (فارغ = عشوائي)", "")
    seed(int(_s) if _s.strip().lstrip("-").isdigit() else None)

    print("\nاختر المصدر (أو 0 للمفاجأة):")
    for i, (nm, sy, act, cm) in enumerate(SOURCES, 1):
        print(f"   {i}) {nm} ({sy}) — {cm}")
    ch = ask_int("رقم المصدر", 0, 0, len(SOURCES))
    name, sym, true_activity, comment = (RNG.choice(SOURCES) if ch == 0 else SOURCES[ch - 1])

    eff = ask_float("كفاءة الكاشف لهذا الإشعاع (0–1)", 0.05, 0.0001, 1.0)
    tau = ask_float("الزمن الميت للجهاز (ثانية) — 0 لجهاز مثالي", 1.0e-4, 0.0, 1e-2)
    bkg = ask_float("معدل الخلفية (عدد/ثانية)", 0.5, 0.0)

    step("الخطوة 1: قياس الخلفية وحدها (بدون المصدر)")
    tb = ask_float("زمن قياس الخلفية (ثانية)", 300.0, 1.0)
    cb = poisson(bkg * tb)
    print(f"  عدّدت {cb} نبضة في {tb:g} ث ⇒ معدل الخلفية المقاس = {cb/tb:.3f} عدد/ث")
    note(f"عدم يقين الخلفية ≈ √{cb}/{tb:g} = {math.sqrt(cb)/tb:.3f} عدد/ث "
         f"(±{100*math.sqrt(cb)/max(cb,1):.1f}٪)")

    step("الخطوة 2: قياس المصدر على مسافة تختارها")
    r = ask_float("بُعد الكاشف عن المصدر (سم)", 20.0, 0.5, 500.0)
    t = ask_float("زمن القياس (ثانية)", 60.0, 1.0)

    geo = geometry(r)
    true_signal_rate = true_activity * eff * geo
    m = measure(true_signal_rate, t, tau, bkg)

    header("نتيجة القياس", "")
    table([("الخلفية", f"{cb}", f"{cb/tb:.3f} عدد/ث"),
           ("المصدر + الخلفية", f"{m}", f"{m/t:.3f} عدد/ث")],
          ["القياس", "النبضات", "المعدل"], aligns=["<", ">", ">"])
    note(f"الهندسة: مساحة النافذة {DET_AREA_CM2:g} سم² على بُعد {r:g} سم ⇒ كسر = {geo:.3e}")

    step("الخطوة 3: صحّح ثم استنتج النشاط")
    print("  أ) اطرح الخلفية من معدل المصدر.")
    print("  ب) صحّح الزمن الميت: n = m / (1 − m·τ)   (m, n بالمعدل لا بالعدد)")
    net_rate = (m / t) - (cb / tb)
    dead_ok = (1.0 - (m / t) * tau) > 0
    corrected_rate = correct(m, t, tau, cb / tb)
    print(f"\n  الصافي قبل تصحيح الزمن الميت: {net_rate:.3f} عدد/ث")
    if dead_ok:
        print(f"  بعد تصحيح الزمن الميت:        {corrected_rate:.3f} عدد/ث "
              f"(فرق {100*abs(corrected_rate-net_rate)/max(net_rate,1e-9):.1f}٪)")
    else:
        warn("معدل العدّ أعلى من قدرة الجهاز (m·τ ≥ 1): القياس غير صالح — ابتعد أكثر!")

    step("الخطوة 4: ما نشاط المصدر الحقيقي؟ (Bq)")
    print("  العلاقة:  المعدل الصافي = النشاط × الكفاءة × الهندسة")
    print("  ⇒ النشاط = المعدل الصافي / (الكفاءة × الهندسة)")
    guess = ask_float("اكتب تقديرك للنشاط بالـ Bq",
                      max(corrected_rate, 0.0) / (eff * geo), 0.0)

    header("الكشف", "")
    print(f"  المصدر: {name} ({sym}) — {comment}")
    print(f"  النشاط الحقيقي: {true_activity:.4g} Bq")
    err = rel_err(guess, true_activity)
    print(f"  تقديرك: {guess:.4g} Bq — خطأ {err:.1f}٪")
    if err < 10:
        good("ممتاز.")
    elif err < 30:
        warn("قريب — راجع تصحيح الخلفية أو الزمن الميت.")
    else:
        warn("بعيد — تحقّق: هل استخدمت الهندسة الصحيحة؟ هل قسّمت على الكفاءة؟")

    step("دروس هذا المختبر")
    note("• الكفاءة والهندسة هما ما يحوّلان «نبضات» إلى «بكريل». النبضة ليست نشاطاً.")
    note("• الخلفية تُقاس وتُطرح؛ عدم يقينها ينتقل إلى النتيجة.")
    note("• الزمن الميت يحني العلاقة عند المعدلات العالية: العدّ ينمو أبطأ من الحقيقة.")
    note("• إهمال أيٍّ من هذه التصحيحات يعطي رقماً «دقيقاً» خاطئاً — وهذا أسوأ من رقم تقريبي صادق.")
    print()


def main():
    run()


if __name__ == "__main__":
    main()
