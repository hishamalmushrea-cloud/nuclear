# -*- coding: utf-8 -*-
"""
محرّك المحاكاة التفاعلية: يجعل التجربة «كأنها حقيقية» دون أي مصدر إشعاع حقيقي.

المبدأ: كل محاكاة تعمل كـ«مختبر افتراضي»:
  - تعطيك بيانات فيها ضجيج إحصائي واقعي (إحصاء بواسون، خلفية، زمن ميت).
  - تُخفي الحقيقة حتى تقيسها أنت.
  - تطلب منك تقديراً، ثم تكشف القيمة الحقيقية وتشرح الفرق.

لا يتعامل هذا الكود مع أي مادة أو جهاز مشعّ حقيقي.
"""
from __future__ import annotations

import math
import random
import sys

# ------------------------------------------------------------------ أدوات --
RNG = random.Random()


def seed(s=None):
    """تثبيت البذرة من أجل نتائج قابلة للتكرار (X.19)."""
    global RNG
    RNG = random.Random(s)
    return RNG


def header(title: str, sub: str = ""):
    w = 68
    print("\n" + "═" * w)
    print(f"  {title}")
    if sub:
        print(f"  {sub}")
    print("═" * w)


def step(txt: str):
    print(f"\n▸ {txt}")


def note(txt: str):
    print(f"  · {txt}")


def warn(txt: str):
    print(f"  ⚠ {txt}")


def good(txt: str):
    print(f"  ✅ {txt}")


def bad(txt: str):
    print(f"  ❌ {txt}")


def ask(prompt: str, default: str = "") -> str:
    d = f" [{default}]" if default else ""
    try:
        v = input(f"\n؟ {prompt}{d}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return default
    return v or default


def ask_float(prompt: str, default: float, lo: float = None, hi: float = None) -> float:
    while True:
        raw = ask(prompt, f"{default:g}")
        try:
            v = float(raw.replace(",", ".").replace("×10^", "e").replace("^", "e"))
        except ValueError:
            bad("أدخل رقماً صالحاً (مثال: 3.5 أو 2e3)")
            continue
        if lo is not None and v < lo:
            bad(f"القيمة أصغر من الحد المسموح ({lo:g})")
            continue
        if hi is not None and v > hi:
            bad(f"القيمة أكبر من الحد المسموح ({hi:g})")
            continue
        return v


def ask_int(prompt: str, default: int, lo: int = None, hi: int = None) -> int:
    return int(ask_float(prompt, default, lo, hi))


def ask_choice(prompt: str, options: list) -> int:
    for i, o in enumerate(options, 1):
        print(f"   {i}) {o}")
    while True:
        v = ask_int(prompt, 1, 1, len(options))
        return int(v) - 1


def pause():
    try:
        input("\n… اضغط Enter للمتابعة …")
    except (EOFError, KeyboardInterrupt):
        print()


# --------------------------------------------------------------- إحصاء -----
def poisson(lam: float) -> int:
    """عينة من توزيع بواسون (Knuth للقيم الصغيرة، تقريب غاوسي للكبيرة).

    يستخدمه المحاكي ليحاكي «عدّ النبضات» كما في الحياة الواقعية:
    حتى لو كان المعدل الحقيقي ثابتاً، فإن العدّ يتذبذب.
    """
    lam = max(lam, 0.0)
    if lam < 30:
        if lam == 0:
            return 0
        L = math.exp(-lam)
        k, p = 0, 1.0
        while True:
            p *= RNG.random()
            if p <= L:
                return k
            k += 1
    g = RNG.gauss(lam, math.sqrt(lam))
    return max(0, int(round(g)))


def gauss(mu: float, sigma: float) -> float:
    return RNG.gauss(mu, sigma)


# --------------------------------------------------------------- رسوم -----
def plot(xs, ys, title="", ylabel="", height=14, width=64, symbol="█"):
    """رسم نصي بسيط يعمل في أي طرفية."""
    if not ys:
        return
    lo, hi = min(ys), max(ys)
    if hi - lo < 1e-12:
        hi = lo + 1.0
    grid = [[" "] * width for _ in range(height)]
    n = len(ys)
    for i in range(width):
        j = int(i * (n - 1) / max(1, width - 1)) if n > 1 else 0
        row = int((ys[j] - lo) / (hi - lo) * (height - 1))
        grid[height - 1 - row][i] = symbol
    print()
    if title:
        print(f"  {title}")
    for r_i, row in enumerate(grid):
        val = hi - (r_i / (height - 1)) * (hi - lo)
        print(f"{val:10.3g} │{''.join(row)}")
    print(f"{'':10s} └" + "─" * width)
    print(f"{'':10s}  {xs[0]:<10.4g}{'':{max(0,width-24)}s}{xs[-1]:>10.4g}")
    if ylabel:
        print(f"{'':10s}  {ylabel}")


def table(rows, headers, aligns=None):
    cols = len(headers)
    widths = [len(str(h)) for h in headers]
    for r in rows:
        for i in range(cols):
            widths[i] = max(widths[i], len(str(r[i])))
    aligns = aligns or ["<"] * cols
    line = "  " + "  ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers))
    print(line)
    print("  " + "  ".join("─" * widths[i] for i in range(cols)))
    for r in rows:
        cells = []
        for i in range(cols):
            s = str(r[i])
            cells.append(s.rjust(widths[i]) if aligns[i] == ">" else s.ljust(widths[i]))
        print("  " + "  ".join(cells))


def rel_err(measured: float, true: float) -> float:
    if true == 0:
        return float("inf")
    return abs(measured - true) / abs(true) * 100.0
