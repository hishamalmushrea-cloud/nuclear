# -*- coding: utf-8 -*-
"""
المختبر 01 — مختبر الاضمحلال الإشعاعي (تفاعلي، بلا أي مصدر حقيقي).

ما تفعله:
  1. يختار لك «نظيراً مجهولاً» ويعطيك عينة افتراضية منه.
  2. يقلّد لك عدّاداً: في كل قياس يعطيك عدداً فيه ضجيج بواسون + خلفية.
  3. تطلب منك تقدير عمر النصف من بياناتك (بيانياً أو بحساب).
  4. يكشف القيمة الحقيقية، ويحسب خطأك، ويشرح مصدره.

الدرس الفيزيائي: النشاط يتبع قانوناً أُسّيّاً، لكن **القياس** يتبع إحصاء بواسون؛
الفصل بين الاثنين هو جوهر العمل التجريبي النووي.
"""
from __future__ import annotations

import math

try:
    from .engine import (RNG, ask, ask_float, ask_int, good, header, note, pause,
                    plot, poisson, rel_err, seed, step, table, warn)
except ImportError:  # تشغيل مباشر: python3 sims/01_decay_lab.py
    from engine import (RNG, ask, ask_float, ask_int, good, header, note, pause,
                    plot, poisson, rel_err, seed, step, table, warn)

# قاعدة بيانات صغيرة (عمر النصف بالثواني) — قيم حقيقية معروفة
LIBRARY = [
    # (الاسم، الرمز، عمر النصف بالثواني، تعليق)
    ("فوسفور-32", "P-32", 1.23e6, "نظير شائع في الأبحاث الحيوية"),
    ("صوديوم-24", "Na-24", 5.4e4, "يُنتج بالتنشيط النيوتروني"),
    ("يود-131", "I-131", 6.93e5, "يستخدم في الطب النووي"),
    ("تكنيشيوم-99m", "Tc-99m", 2.16e4, "الأكثر استخداماً في التصوير الطبي"),
    ("رادون-222", "Rn-222", 3.30e5, "غاز طبيعي مهم صحياً"),
    ("كوبالت-60", "Co-60", 1.66e8, "مصدر غاما صناعي شائع"),
    ("سيزيوم-137", "Cs-137", 9.51e8, "ناتج انشطار طويل العمر"),
    ("بولونيوم-210", "Po-210", 1.194e6, "ألفا، سام جداً إشعاعياً"),
]


def counts_in(A0, lam, t, dt, background_rate):
    """عدد النبضات المتوقّع خلال نافذة قياس dt عند اللحظة t (مع خلفية)."""
    expected = A0 * math.exp(-lam * t) * dt + background_rate * dt
    return poisson(expected)


def run():
    header("المختبر 01 — مختبر الاضمحلال الإشعاعي",
           "محاكاة كاملة: عينة مجهولة + عدّاد فيه ضجيج + عليك استنتاج عمر النصف")
    note("لا يوجد أي مصدر مشعّ حقيقي هنا؛ كل ما تراه أرقام مولّدة إحصائياً.")

    _s = ask("رقم البذرة العشوائية (اتركه فارغاً لتجربة مختلفة كل مرة)", "")
    seed(int(_s) if _s.strip().lstrip("-").isdigit() else None)

    print("\nاختر النويدة (أو 0 ليختارها المحاكي سراً):")
    for i, (nm, sy, th, cm) in enumerate(LIBRARY, 1):
        print(f"   {i}) {nm} ({sy}) — {cm}")
    choice = ask_int("رقم النويدة", 0, 0, len(LIBRARY))
    if choice == 0:
        name, sym, t_half, comment = RNG.choice(LIBRARY)
    else:
        name, sym, t_half, comment = LIBRARY[choice - 1]

    lam = math.log(2) / t_half

    idx = ask_int("كم عدد نقاط القياس التي تريدها؟", 12, 6, 20)
    # نقترح زمن رصد ≈ 2.5 عمر نصف حتى يظهر الانحدار بوضوح
    gap_sug = 2.5 * t_half / max(1, idx - 1)
    gap = ask_float("الزمن بين بدايات القياسات (ثانية)", round(gap_sug, 3), 0.001)
    dt = ask_float("زمن كل قياس (ثانية)", round(gap / 5, 3), 0.001, gap)
    target = ask_float("عدد النبضات التقريبي في أول قياس (يضبط «قوة» العينة)", 300.0, 10.0)
    # نقترح خلفية ≈ 2٪ من إشارة القياس الأول حتى تكون مسموعة لا طاغية
    bkg = ask_float("معدل الخلفية (عدد/ثانية) — 0 لقياس نظيف", round(0.02 * target / dt, 6), 0.0)
    A0 = target / dt  # نشاط ابتدائي بالـ Bq يكفي لرؤية الإحصاء

    if idx * gap < 0.5 * t_half:
        warn("زمن الرصد الكلي أقصر من نصف عمر النصف: الانحدار سيكون ضعيفاً والخطأ كبيراً.")

    step(f"أعطيتك عينة من نويدة مجهولة. جهازك يعدّ النبضات.")
    note(f"زمن القياس الواحد: {dt:g} ث · الفاصل بين القياسات: {gap:g} ث · "
         f"الخلفية: {bkg:g} عدد/ث")
    pause()

    times, counts = [], []
    header("جدول القياس", "النبضات الخام كما يقرأها الجهاز")
    for i in range(idx):
        t = i * gap
        c = counts_in(A0, lam, t, dt, bkg)
        times.append(t)
        counts.append(c)
    table([(i + 1, f"{times[i]:.0f}", counts[i]) for i in range(idx)],
          ["#", "الزمن (ث)", "النبضات"], aligns=[">", ">", ">"])

    step("الخطوة 1: اطرح الخلفية من كل قراءة (إن وُجدت)، ثم لوغاريتم النتيجة.")
    net = [max(c - bkg * dt, 0.0) for c in counts]
    ln_vals = [math.log(v) if v > 0 else float("nan") for v in net]

    plot(times, ln_vals, title="لوغاريتم العدد الصافي مقابل الزمن (يجب أن يكون خطاً مستقيماً)",
         ylabel="الزمن (ث)")
    note("ميل الخط المستقيم = −λ، ومنه عمر النصف T₁/₂ = ln2 / λ")

    step("الخطوة 2: قدّر الميل بالعين أو بالحساب. (نحسبه هنا بمربعات صغرى بسيطة)")
    xs = [t for t, y in zip(times, ln_vals) if not math.isnan(y)]
    ys = [y for y in ln_vals if not math.isnan(y)]
    n = len(xs)
    if n >= 2:
        mx = sum(xs) / n
        my = sum(ys) / n
        num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        den = sum((x - mx) ** 2 for x in xs)
        slope = num / den if den else 0.0
        lam_fit = -slope
        t_half_fit = math.log(2) / lam_fit if lam_fit > 0 else float("inf")
    else:
        lam_fit, t_half_fit = 0.0, float("inf")

    guess = ask_float("ما تقديرك لعمر النصف بالثواني؟ (اكتبه قبل أن نكشف الحقيقة)",
                      round(t_half_fit, 2), 0.0)

    header("الكشف", "")
    print(f"  النويدة كانت: {name} ({sym})")
    print(f"  عمر النصف الحقيقي: {t_half:.4g} ث")
    print(f"  تقديرك: {guess:.4g} ث — خطأ نسبي {rel_err(guess, t_half):.1f}٪")
    print(f"  تقدير المربعات الصغرى من بياناتك: {t_half_fit:.4g} ث — "
          f"خطأ {rel_err(t_half_fit, t_half):.1f}٪")
    print(f"\n  تعليق: {comment}")

    if rel_err(guess, t_half) < 10:
        good("ممتاز: تقديرك داخل 10٪ من الحقيقة.")
    elif rel_err(guess, t_half) < 30:
        warn("قريب. الفرق سببه الضجيج الإحصائي وقصر زمن القياس.")
    else:
        warn("بعيد. جرّب: قياسات أطول، نقاط أكثر، أو خلفية أقل.")

    step("لماذا يوجد خطأ أصلاً؟")
    note("• ضجيج بواسون: الانحراف المعياري للعدّ N هو √N — لا مفر منه.")
    note("• الخلفية: إن لم تُطرح تُفلِط الميل (خصوصاً عند الأزمنة الطويلة).")
    note("• نافذة القياس القصيرة: عدد أقل ⇒ عدم يقين نسبي أكبر (√N/N = 1/√N).")
    note("• الزمن الميت للجهاز (المختبر 02) يسرق نبضات عند المعدلات العالية.")

    step("تحقق سريع: كم عدم اليقين في قراءتك الأولى؟")
    c0 = counts[0]
    print(f"  القراءة الأولى = {c0} نبضة ⇒ σ ≈ √{c0} ≈ {math.sqrt(c0):.1f} "
          f"⇒ عدم يقين نسبي ≈ {100/math.sqrt(c0):.1f}٪")
    print("\n  هذه هي الفكرة التي سترافقك في كل القياسات النووية:")
    print("  «الرقم الواحد بلا عدم يقين ليس نتيجة علمية.»")
    print()


def main():
    run()


if __name__ == "__main__":
    main()
