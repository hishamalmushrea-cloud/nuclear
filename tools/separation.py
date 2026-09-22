#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
separation — حاسبة «نظرية الفصل» (Separation Theory) على مستوى الأدبيات المفتوحة.

ما هذا؟
    رياضيات فصل النظائر كما ترد في Benedict & Pigford / Lamarsh / Cohen:
    دالة القيمة، الشغل الفصلي (SWU)، ميزان SWU، الشلال المثالي،
    والحد الأدنى الديناميكي الحراري لعملية الفصل (إنتروبيا الخلط العكسيّة).

ما هذا ليس؟
    ليس مواصفات آلة، ولا مخطط تدفق تشغيلية، ولا معاملات تشغيل، ولا عامل فصل
    لأي جهاز بعينه. عامل الفصل α يُدخله المستخدم بنفسه؛ نحن نحسب ما يترتب عليه
    رياضياً فقط. (راجع MAP/18 و MAP/19: العلم مفتوح، النقل التنفيذي ممتنع.)

الأوامر:
    python3 tools/separation.py demo
    python3 tools/separation.py swu     --xf 0.00711 --xp 0.045 --xt 0.0025 --p 1000
    python3 tools/separation.py cascade --alpha 1.15 --xf 0.00711 --xp 0.045 --xt 0.0025
    python3 tools/separation.py sweep   --xf 0.00711 --xp 0.045 --tmin 0.001 --tmax 0.005
    python3 tools/separation.py         # وضع تفاعلي
"""
from __future__ import annotations

import argparse
import math
import sys

R = 8.314462618          # J/(mol·K)
M_URANIUM = 0.238        # kg/mol (تقريب: كتلة U الطبيعي)
T_REF = 300.0            # K — درجة حرارة مرجعية لحساب الشغل الأدنى


# ------------------------------------------------------------ النظرية ------
def value_function(x: float) -> float:
    """دالة القيمة V(x) = (2x−1)·ln(x/(1−x)) — أساس الشغل الفصلي."""
    if not 0.0 < x < 1.0:
        raise ValueError("النسبة x يجب أن تكون بين 0 و1 (حصراً).")
    return (2.0 * x - 1.0) * math.log(x / (1.0 - x))


def mix_entropy_term(x: float) -> float:
    """h(x) = x·ln x + (1−x)·ln(1−x)  (≤ 0) — إنتروبيا الخلط المولية بدون البعد."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 0.0
    return x * math.log(x) + (1.0 - x) * math.log(1.0 - x)


def balance(xf: float, xp: float, xt: float, p: float = 1.0):
    """ميزان الكتلة والنظير: يعيد (F, T) لكمية منتج P.
       F = P·(xp−xt)/(xf−xt)   ,   T = P·(xp−xf)/(xf−xt)"""
    if not (xt < xf < xp):
        raise ValueError("يجب أن يكون: xt (المخلف) < xf (اللقيم) < xp (المنتج).")
    f = p * (xp - xt) / (xf - xt)
    t = p * (xp - xf) / (xf - xt)
    return f, t


def swu(xf: float, xp: float, xt: float, p: float = 1.0) -> float:
    """الشغل الفصلي: SWU = P·V(xp) + T·V(xt) − F·V(xf)."""
    f, t = balance(xf, xp, xt, p)
    return p * value_function(xp) + t * value_function(xt) - f * value_function(xf)


def min_work(xf: float, xp: float, xt: float, p: float = 1.0,
             temp: float = T_REF) -> float:
    """الحد الأدنى للشغل (ديناميكا حرارية عكوسية): W = RT·[P·h(xp)+T·h(xt)−F·h(xf)]."""
    f, t = balance(xf, xp, xt, p)
    n_p = p / M_URANIUM
    n_f = f / M_URANIUM
    n_t = t / M_URANIUM
    s = n_p * mix_entropy_term(xp) + n_t * mix_entropy_term(xt) - n_f * mix_entropy_term(xf)
    return R * temp * s


def ideal_cascade_stages(alpha: float, xf: float, xp: float, xt: float):
    """عدد مراحل الشلال المثالي (تقريب α−1 صغير، صيغة لامارش):
         N_إثراء = 2/(α−1) · ln(R_P/R_F) − 1
         N_تجريد = 2/(α−1) · ln(R_F/R_W) − 1
       مع R = x/(1−x). α عامل فصل عنصر واحد (مدخل من المستخدم، لا نقدّمه نحن)."""
    if alpha <= 1.0:
        raise ValueError("عامل الفصل α يجب أن يكون أكبر من 1.")
    ratio = lambda x: x / (1.0 - x)  # noqa: E731
    n_en = 2.0 / (alpha - 1.0) * math.log(ratio(xp) / ratio(xf)) - 1.0
    n_st = 2.0 / (alpha - 1.0) * math.log(ratio(xf) / ratio(xt)) - 1.0
    return max(0.0, n_en), max(0.0, n_st)


def stage_profile(alpha: float, xf: float, xp: float, xt: float, n: int = 40):
    """مسار النسبة على طول الشلال المثالي: R يرتفع بمقدار α كل نصف-مرحلة تقريباً."""
    n_en, n_st = ideal_cascade_stages(alpha, xf, xp, xt)
    total = n_en + n_st
    if total <= 0:
        return [], [], 0.0, 0.0
    r_f = xf / (1 - xf)
    xs, ys = [], []
    for i in range(n + 1):
        stage = -n_st + total * i / n        # من قاع التجريد إلى رأس الإثراء
        r = r_f * alpha ** (0.5 * stage)
        x = r / (1 + r)
        xs.append(stage)
        ys.append(x)
    return xs, ys, n_en, n_st


# -------------------------------------------------------------- العرض -------
def hr(t=""):
    print("\n" + "═" * 64)
    if t:
        print("  " + t)
        print("═" * 64)


def show_swu(xf, xp, xt, p):
    f, t = balance(xf, xp, xt, p)
    s = swu(xf, xp, xt, p)
    hr("ميزان الفصل والشغل الفصلي (SWU)")
    print(f"  اللقيم F  = {f:,.2f} كجم  (نسبة {xf*100:.4g}٪)")
    print(f"  المنتج P  = {p:,.2f} كجم  (نسبة {xp*100:.4g}٪)")
    print(f"  المخلف T  = {t:,.2f} كجم  (نسبة {xt*100:.4g}٪)")
    print()
    print(f"  دالة القيمة:  V(xp) = {value_function(xp):.4f} · "
          f"V(xf) = {value_function(xf):.4f} · V(xt) = {value_function(xt):.4f}")
    print(f"  SWU = P·V(xp) + T·V(xt) − F·V(xf)")
    print(f"      = {s:,.3f} كجم SWU")
    print(f"      = {s/max(p,1e-12):,.4f} كجم SWU لكل كجم منتج")

    w_min = min_work(xf, xp, xt, p)
    print()
    print(f"  الحد الأدنى الديناميكي الحراري (فصل عكوسي T={T_REF:.0f} K):")
    print(f"      W_min = RT·[P·h(xp) + T·h(xt) − F·h(xf)] = {w_min/1000:,.4f} كيلوجول"
          f"  ({w_min/max(p,1e-12)/1000:,.4f} kJ/كجم منتج)")
    print(f"      = {w_min/3.6e6:,.3e} kWh")
    print()
    print("  للمقارنة (قيم منشورة، ثقة متوسطة، تختلف بحسب المحطة):")
    for name, kwh in (("انتشار غازي (تاريخي)", 2400.0),
                      ("طرد مركزي (حديث)", 60.0)):
        real = s * kwh * 3.6e6
        eff = (w_min / real) if real > 0 else float("nan")
        print(f"      {name}: {kwh:,.0f} kWh/SWU → {real/1e9:,.2f} GJ للدفعة · "
              f"الكفاءة مقابل الحد الأدنى ≈ {eff:.2e}")
    print("\n  ملاحظة منهجية: هذا التباين بسبعة إلى ثمانية أضعاف ليس هدراً هندسياً،")
    print("  بل هو ثمن «الاستقلال عن طبيعة النظيرين»: الفصل الميكانيكي يضرب كل")
    print("  جزيء ليعرف كتلته، بينما الحد الأدنى يفترض معرفة مسبقة تامة.")


def show_cascade(alpha, xf, xp, xt):
    n_en, n_st = ideal_cascade_stages(alpha, xf, xp, xt)
    hr("الشلال المثالي (مدخل α من المستخدم)")
    print(f"  عامل الفصل لكل عنصر: α = {alpha:.4f}  (α−1 = {alpha-1:.4g})")
    print(f"  مراحل الإثراء  N_en = {n_en:,.1f}")
    print(f"  مراحل التجريد  N_st = {n_st:,.1f}")
    print(f"  المجموع            = {n_en + n_st:,.1f} مرحلة")
    print()
    print("  ملاحظة: هذه مراحل «مثالية» بمعنى أن تيارَي الرأس والذيل لكل مرحلة")
    print("  يُدمجان فقط عندما تتساوى نسبتهما — شرط رياضي يقلّل التدفق الداخلي")
    print("  (ومعه الشغل المفقود) إلى أدنى حد. α نفسه خاصية العنصر الفاصل،")
    print("  ولا ندخله نحن: هو مدخل تفرضه أنت.")

    xs, ys, _, _ = stage_profile(alpha, xf, xp, xt)
    if xs:
        lo, hi = min(ys), max(ys)
        print()
        print("  مسار النسبة على طول الشلال (لوغاريتمي):")
        h = 12
        grid = [[" "] * 60 for _ in range(h)]
        for i, y in enumerate(ys):
            col = int(i * 59 / (len(ys) - 1))
            row = int((math.log10(y) - math.log10(lo)) /
                      max(1e-12, math.log10(hi) - math.log10(lo)) * (h - 1))
            grid[h - 1 - row][col] = "█"
        for r_i, row in enumerate(grid):
            val = 10 ** (math.log10(hi) - r_i / (h - 1) * (math.log10(hi) - math.log10(lo)))
            print(f"{val*100:9.4g}٪ │{''.join(row)}")
        print(f"{'':9s} └" + "─" * 60)
        print(f"{'':9s}  {xs[0]:+.1f} (قاع التجريد){'':>22s}{xs[-1]:+.1f} (رأس الإثراء)")


def show_sweep(xf, xp, tmin, tmax, steps=12):
    hr("أثر نسبة المخلف على الشغل الفصلي")
    print("  كلما انخفضت نسبة المخلف توفّرت مادة اللقيم… وكلف شغل فصلي أكثر.")
    print()
    print("   نسبة المخلف٪   كجم SWU/كجم منتج   كجم لقيم/كجم منتج")
    print("   ────────────   ────────────────   ─────────────────")
    for i in range(steps + 1):
        xt = tmin + (tmax - tmin) * i / steps
        if not (0 < xt < xf):
            continue
        s = swu(xf, xp, xt, 1.0)
        f, _ = balance(xf, xp, xt, 1.0)
        print(f"   {xt*100:11.4f}٪   {s:16.4f}   {f:17.4f}")
    print()
    print("  هذا هو المفاضلة الاقتصادية الحقيقية: سعر اللقيم مقابل سعر الشغل.")
    print("  النقطة المثلى ليست حيث يقلّ SWU، بل حيث تقلّ التكلفة الكلية.")


def interactive():
    hr("حاسبة نظرية الفصل — وضع تفاعلي")
    try:
        xf = float(input("؟ نسبة اللقيم xf (مثال 0.00711 لليورانيوم الطبيعي): ") or 0.00711)
        xp = float(input("؟ نسبة المنتج xp (مثال 0.045): ") or 0.045)
        xt = float(input("؟ نسبة المخلف xt (مثال 0.0025): ") or 0.0025)
        p = float(input("؟ كمية المنتج بالكجم [1]: ") or 1.0)
    except (EOFError, KeyboardInterrupt, ValueError):
        print("\n  (خروج)")
        return
    try:
        show_swu(xf, xp, xt, p)
        a = input("\n؟ عامل فصل α لحساب مراحل الشلال المثالي (اتركه فارغاً للتخطي): ").strip()
        if a:
            show_cascade(float(a), xf, xp, xt)
    except ValueError as e:
        print(f"  ⚠️  {e}")


def main() -> int:
    ap = argparse.ArgumentParser(description="نظرية الفصل: SWU + الشلال المثالي + الحد الأدنى")
    sub = ap.add_subparsers(dest="cmd")

    p1 = sub.add_parser("swu", help="ميزان الكتلة + الشغل الفصلي + الحد الأدنى")
    p1.add_argument("--xf", type=float, default=0.00711)
    p1.add_argument("--xp", type=float, default=0.045)
    p1.add_argument("--xt", type=float, default=0.0025)
    p1.add_argument("--p", type=float, default=1.0)

    p2 = sub.add_parser("cascade", help="عدد مراحل الشلال المثالي")
    p2.add_argument("--alpha", type=float, required=True)
    p2.add_argument("--xf", type=float, default=0.00711)
    p2.add_argument("--xp", type=float, default=0.045)
    p2.add_argument("--xt", type=float, default=0.0025)

    p3 = sub.add_parser("sweep", help="أثر نسبة المخلف")
    p3.add_argument("--xf", type=float, default=0.00711)
    p3.add_argument("--xp", type=float, default=0.045)
    p3.add_argument("--tmin", type=float, default=0.001)
    p3.add_argument("--tmax", type=float, default=0.005)

    sub.add_parser("demo", help="مثال جاهز")
    args = ap.parse_args()

    try:
        if args.cmd == "swu":
            show_swu(args.xf, args.xp, args.xt, args.p)
        elif args.cmd == "cascade":
            show_cascade(args.alpha, args.xf, args.xp, args.xt)
        elif args.cmd == "sweep":
            show_sweep(args.xf, args.xp, args.tmin, args.tmax)
        elif args.cmd == "demo":
            show_swu(0.00711, 0.045, 0.0025, 1000.0)
            show_cascade(1.15, 0.00711, 0.045, 0.0025)
            show_sweep(0.00711, 0.045, 0.001, 0.005)
        else:
            interactive()
    except ValueError as e:
        print(f"⚠️  {e}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
