# -*- coding: utf-8 -*-
"""
06 — مختبر انتشار النيوترونات والحرجية (Neutron Diffusion & Criticality)

الفيزياء (مستوى جامعي متقدم — بلا أي تبسيط):

مجموعتان (سريعة 1، حرارية 2)، انتشار في لوح (slab) بسماكة a، بشرط حدود مفرّغ
عند «البعد المُستنبط» (extrapolated boundary) δ = 0.7104 λ_tr = 0.7104·3D:

  -D₁ φ₁'' + (Σa₁ + Σr) φ₁ = (1/k)(ν₁Σf₁ φ₁ + ν₂Σf₂ φ₂)
  -D₂ φ₂'' + Σa₂ φ₂                = Σr φ₁

الحل التحليلي للنمط الأساسي (φ ~ cos Bx):

  k(B²) = ν₂Σf₂·Σr / [(Σa₂ + D₂B₂²)(Σa₁ + Σr + D₁B₁²)]  +  ν₁Σf₁ / (Σa₁ + Σr + D₁B₁²)

  مع B_g = π / a_g  ,  a_g = a + 2δ_g  (لكل مجموعة بُعدها المستنبط)

وصيغة المفاعل mالتي يعرفها كل مهندس نووي:

  k_eff = k_∞ / [(1 + L²B²)(1 + τB²)]       ,  L² = D₂/Σa₂  ,  τ = D₁/(Σa₁+Σr)

الحل العددي هنا: تفاضلات محدودة على شبكة + تكرار القدرة (power iteration)
مع حل ثلاثي القطر (Thomas algorithm) — أي أننا نوجد k_eff دون افتراض شكل الجيب،
ثم نقارن الحلين. هذا هو قلب «نيوترونيات المفاعل» كما تُدرَّس في
Duderstadt & Hamilton و Lamarsh — لا علاقة له بأي تصميم عسكري.

المتعلّم يخمّن «السماكة الحرجة» قبل أن يكشفها المختبر.
"""
from __future__ import annotations

import math

try:
    from .engine import header, step, note, warn, good, bad, ask, ask_float, ask_choice, pause, plot, table, rel_err
except ImportError:
    from engine import header, step, note, warn, good, bad, ask, ask_float, ask_choice, pause, plot, table, rel_err


# ثوابت مجموعتين «تمثيلية تعليمية» — قيم مضافة/مولّدة لأغراض التدريس،
# ليست بيانات تصميم لأي مفاعل حقيقي. الوحدات: cm و cm⁻¹.
PRESETS = [
    {
        "name": "ماء خفيف + أكسيد يورانيوم (شبيه PWR)",
        "D1": 1.13, "Sa1": 0.0034, "Sr": 0.0132, "nuF1": 0.0025,
        "D2": 0.16, "Sa2": 0.0850, "nuF2": 0.1110,
    },
    {
        "name": "جرافيت + يورانيوم (معتدل كبير)",
        "D1": 1.00, "Sa1": 0.0009, "Sr": 0.0025, "nuF1": 0.0002,
        "D2": 0.90, "Sa2": 0.0036, "nuF2": 0.0060,
    },
    {
        "name": "نظام سريع (بلا مُهدّئ — مجموعة واحدة فعلياً)",
        "D1": 1.50, "Sa1": 0.0025, "Sr": 0.0, "nuF1": 0.0045,
        "D2": 0.0, "Sa2": 0.0, "nuF2": 0.0,
    },
]

N_NODES = 161          # عدد عقد الشبكة (فردي ليكون المنتصف عقدة)
MAX_ITER = 4000
TOL = 1e-10


# ------------------------------------------------------------ حل عدددي -----
def _thomas(a_lo, a_diag, a_up, rhs):
    """حل منظومة ثلاثية القطر (Thomas algorithm)."""
    n = len(a_diag)
    c = [0.0] * n
    d = [0.0] * n
    c[0] = a_up[0] / a_diag[0]
    d[0] = rhs[0] / a_diag[0]
    for i in range(1, n):
        m = a_diag[i] - a_lo[i - 1] * c[i - 1]
        c[i] = a_up[i] / m if i < n - 1 else 0.0
        d[i] = (rhs[i] - a_lo[i - 1] * d[i - 1]) / m
    x = [0.0] * n
    x[-1] = d[-1]
    for i in range(n - 2, -1, -1):
        x[i] = d[i] - c[i] * x[i + 1]
    return x


def _map_to(grid, other):
    """نقل فيض من شبكة إلى أخرى بالإحداثي المُطبَّع u∈[0,1] (اللوح متناظر)."""
    n = len(grid)
    out = []
    for i in range(n):
        u = i / (n - 1.0)
        p = u * (n - 1.0)
        j = int(p)
        if j >= n - 1:
            out.append(grid[-1])
        else:
            f = p - j
            out.append(grid[j] * (1 - f) + grid[j + 1] * f)
    del other
    return out


def solve_keff(m, a_ext1, a_ext2):
    """تكرار القدرة على منظومة المجموعتين (تفاضلات محدودة، φ=0 على الحدّين)."""
    n = N_NODES
    m_int = n - 2
    h1 = a_ext1 / (n - 1.0)
    h2 = a_ext2 / (n - 1.0)
    two = m["Sr"] > 0 and (m["nuF2"] > 0 or m["D2"] > 0)

    def build(D, Sigma, h):
        lo = [-D / h / h] * (m_int - 1)
        up = [-D / h / h] * (m_int - 1)
        diag = [2 * D / h / h + Sigma] * m_int
        return lo, diag, up

    lo1, d1, up1 = build(m["D1"], m["Sa1"] + m["Sr"], h1)
    if two:
        lo2, d2, up2 = build(m["D2"], m["Sa2"], h2)

    phi1 = [math.sin(math.pi * (i + 1) / (n - 1)) for i in range(m_int)]
    phi2 = [0.0] * m_int if two else None
    k = 1.0

    for _ in range(MAX_ITER):
        # مصدر الانشطار من التخمين الحالي
        src1 = [m["nuF1"] * phi1[i] + (m["nuF2"] * phi2[i] if two else 0.0)
                for i in range(m_int)]
        tot_old = sum(src1)

        # 1) A1 φ1 = مصدر/k
        rhs = [s / k for s in src1]
        phi1_new = _thomas(lo1, d1, up1, rhs)

        if two:
            # 2) A2 φ2 = Σr φ1  (بعد نقل φ1 إلى شبكة المجموعة الحرارية)
            phi1_on2_pts = [0.0] + _map_to([0.0] + phi1_new + [0.0], None)[1:-1] + [0.0]
            rhs2 = [m["Sr"] * phi1_on2_pts[i + 1] for i in range(m_int)]
            phi2_new = _thomas(lo2, d2, up2, rhs2)
        else:
            phi2_new = None

        src_new = [m["nuF1"] * phi1_new[i] +
                   (m["nuF2"] * phi2_new[i] if two else 0.0) for i in range(m_int)]
        tot_new = sum(src_new)
        if tot_old <= 0:
            break
        k_new = k * tot_new / tot_old

        diff = max(abs(src_new[i] - src1[i]) for i in range(m_int)) / max(1e-30, tot_new)
        phi1, phi2, k = phi1_new, phi2_new, k_new
        if diff < TOL:
            break

    flux1 = [0.0] + phi1 + [0.0]
    flux2 = ([0.0] + phi2 + [0.0]) if two else None
    return k, flux1, flux2, h1, h2


def k_of_thickness(m, a):
    d1 = 0.7104 * 3 * m["D1"]
    d2 = 0.7104 * 3 * m["D2"] if m["D2"] > 0 else 0.0
    k, _, _, _, _ = solve_keff(m, a + 2 * d1, a + 2 * d2)
    return k


def k_analytic(m, a):
    d1 = 0.7104 * 3 * m["D1"]
    d2 = 0.7104 * 3 * m["D2"] if m["D2"] > 0 else 0.0
    B1 = math.pi / (a + 2 * d1)
    den1 = m["Sa1"] + m["Sr"] + m["D1"] * B1 * B1
    k = m["nuF1"] / den1
    if m["Sr"] > 0 and m["D2"] > 0:
        B2 = math.pi / (a + 2 * d2)
        den2 = m["Sa2"] + m["D2"] * B2 * B2
        k += m["nuF2"] * m["Sr"] / (den2 * den1)
    return k


def k_inf(m):
    den1 = m["Sa1"] + m["Sr"]
    k = m["nuF1"] / den1
    if m["Sr"] > 0 and m["Sa2"] > 0:
        k += m["nuF2"] * m["Sr"] / (m["Sa2"] * den1)
    return k


def critical_thickness(m, lo=1.0, hi=4000.0):
    """قسمة ثنائية لإيجاد السماكة التي تجعل k=1."""
    if k_of_thickness(m, lo) >= 1.0:
        return None
    if k_of_thickness(m, hi) < 1.0:
        return None
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if k_of_thickness(m, mid) < 1.0:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-6:
            break
    return 0.5 * (lo + hi)


def run():
    header("الوحدة: انتشار النيوترونات والحرجية (مجموعتان)",
           "السؤال: ما أقل سماكة للوح تجعله «حرجاً» (k = 1)؟")

    step("نظرية في ثلاثة أسطر (بلا تبسيط):")
    print("""
  معادلة الانتشار (مجموعتان، لوح بسماكة a، حدود مفرّغة):
     -D₁ φ₁'' + (Σa₁+Σr) φ₁ = (1/k)(ν₁Σf₁ φ₁ + ν₂Σf₂ φ₂)
     -D₂ φ₂'' + Σa₂ φ₂        = Σr φ₁
  النمط الأساسي φ ~ cos(Bx) مع B = π/(a+2δ) و δ = 0.7104·3D (البعد المُستنبط)،
  فيُكتب الشرط الحرج:
     k = ν₂Σf₂·Σr /[(Σa₂+D₂B₂²)(Σa₁+Σr+D₁B₁²)] + ν₁Σf₁/(Σa₁+Σr+D₁B₁²)
  وهو يكافئ صيغة المفاعل الشهيرة:  k_eff = k_∞ /[(1+L²B²)(1+τB²)]
     L² = D₂/Σa₂ (مساحة الانتشار الحراري) · τ = D₁/(Σa₁+Σr) (عمر فيرمي)
  الملاحظة الحاسمة: التسرب يزداد كلما صغُر الحجم (B² ~ 1/a²)،
  لذلك يوجد حجم أدنى للحراجة، وتحتَه يستحيل استمرار السلسلة مهما كانت المادة.
""")

    print("  اختر وسطاً (القيم تمثيلية تعليمية، ليست بيانات تصميم):")
    try:
        idx = ask_choice("؟ الوسط: ", [p["name"] for p in PRESETS] + ["إدخال يدوي"])
    except (EOFError, KeyboardInterrupt):
        return
    if idx == 3:
        m = {}
        m["name"] = "مخصص"
        m["D1"] = ask_float("  D₁ (cm)", 1.13, 0.01, 50)
        m["Sa1"] = ask_float("  Σa₁ (cm⁻¹)", 0.0034, 0.0, 1)
        m["Sr"] = ask_float("  Σr (cm⁻¹، إزالة سريع→حراري)", 0.0132, 0.0, 1)
        m["nuF1"] = ask_float("  νΣf₁ (cm⁻¹)", 0.0025, 0.0, 1)
        m["D2"] = ask_float("  D₂ (cm)", 0.16, 0.0, 50)
        m["Sa2"] = ask_float("  Σa₂ (cm⁻¹)", 0.085, 0.0, 1)
        m["nuF2"] = ask_float("  νΣf₂ (cm⁻¹)", 0.111, 0.0, 1)
    else:
        m = dict(PRESETS[idx])

    k_inf_val = k_inf(m)
    L2 = (m["D2"] / m["Sa2"]) if m["Sa2"] > 0 else 0.0
    tau = (m["D1"] / (m["Sa1"] + m["Sr"])) if (m["Sa1"] + m["Sr"]) > 0 else 0.0
    step("ثوابت الوسط المختار:")
    table([(f"{m['D1']:.4g}", f"{m['Sa1']:.4g}", f"{m['Sr']:.4g}", f"{m['nuF1']:.4g}",
            f"{m['D2']:.4g}", f"{m['Sa2']:.4g}", f"{m['nuF2']:.4g}")],
          ["D₁", "Σa₁", "Σr", "νΣf₁", "D₂", "Σa₂", "νΣf₂"], aligns=[">"] * 7)
    print(f"\n  معامل التضاعف اللانهائي: k_∞ = {k_inf_val:.5f}")
    print(f"  مساحة الانتشار: L² = {L2:.2f} cm² · عمر فيرمي: τ = {tau:.2f} cm²"
          f" · مساحة الترحال: M² = {L2 + tau:.2f} cm²")
    if k_inf_val <= 1.0:
        bad("هذا الوسط k_∞ ≤ 1: السلسلة تنطفئ في أي حجم — لا يوجد حجم حرج.")
        pause()
        return
    note(f"بما أن k_∞ = {k_inf_val:.4f} > 1، فالحرجية ممكنة إذا أصبح التسرب صغيراً كفاية.")

    print()
    guess = ask_float("؟ خمّن السماكة الحرجة a_c (سم) للوح العاري (k=1): ", 60.0, 0.1, 100000.0)

    step("أحلّ المنظومة عددياً (تفاضلات محدودة + تكرار قدرة) لأجد a_c…")
    a_c = critical_thickness(m)
    if a_c is None:
        bad("لم أجد حلاً في المدى المدروس (1–4000 سم).")
        pause()
        return

    err = rel_err(guess, a_c)
    good(f"السماكة الحرجة الحقيقية: a_c = {a_c:.2f} سم")
    print(f"  تخمينك: {guess:.2f} سم → خطأ نسبي {err:.1f}٪")
    if err < 5:
        good("ممتاز — هذه دقة مهندس نيوترونيات.")
    elif err < 20:
        note("قريب. تذكّر: k_eff يتحسّن بسرعة أولاً ثم يقترب من k_∞ ببطء (B² ~ 1/a²).")
    else:
        note("راجع: كلما كبُر الحجم قلّ التسرب، لكن العائد يتناقص (سلوك 1/a²).")

    k_num = k_of_thickness(m, a_c)
    k_ana = k_analytic(m, a_c)
    print(f"\n  تحقّق مزدوج عند a_c:  k_عددي = {k_num:.6f}  ·  k_تحليلي (نمط أساسي) = {k_ana:.6f}")
    print(f"  الفرق بين الطريقتين: {abs(k_num - k_ana)*1e5:.2f} pcm   (pcm = 10⁻⁵ Δk/k)")

    step("كيف يتغيّر k مع السماكة؟")
    rows = []
    for f in (0.25, 0.5, 0.75, 0.9, 1.0, 1.25, 1.5, 3.0):
        a = a_c * f
        rows.append((f"{f:.2f}×", f"{a:.1f}", f"{k_of_thickness(m, a):.5f}",
                     f"{k_analytic(m, a):.5f}"))
    table(rows, ["نسبة من a_c", "السماكة (سم)", "k_eff عددي", "k_eff تحليلي"],
          aligns=[">", ">", ">", ">"])
    note("عند 3×a_c يقترب k_eff من k_∞: اللوح السميك يفقد أثر الحدود.")

    step("شكل الفيض عند الحجم الحرج (φ يصفَر عند «البعد المستنبط»، لا عند حدّ المادة):")
    d1 = 0.7104 * 3 * m["D1"]
    d2 = 0.7104 * 3 * m["D2"] if m["D2"] > 0 else 0.0
    _, f1, f2, h1, h2 = solve_keff(m, a_c + 2 * d1, a_c + 2 * d2)
    xs1 = [i * h1 for i in range(len(f1))]
    plot(xs1, f1, title="الفيض السريع φ₁(x) — يجب أن يشبه نصف جيب",
         ylabel="الموضع (سم، من الحد المستنبط إلى الآخر)")
    if f2:
        xs2 = [i * h2 for i in range(len(f2))]
        plot(xs2, f2, title="الفيض الحراري φ₂(x) — هو الذي يحدّد القدرة",
             ylabel="الموضع (سم)")

    # ---- لعب: إضافة سمّ نيوتروني (كما يُفعل بالبورون في ماء التبريد) ----
    step("العب: أضف سماً نيوترونياً (امتصاص إضافي ΔΣa₂) وشاهد k ينهار إلى ما دون 1")
    try:
        dsa = ask_float("؟ ΔΣa₂ (cm⁻¹، جرّب 0.01): ", 0.01, 0.0, 5.0)
    except (EOFError, KeyboardInterrupt):
        return
    if dsa > 0:
        m2 = dict(m)
        m2["Sa2"] = m["Sa2"] + dsa
        kn = k_of_thickness(m2, a_c)
        print(f"\n  بعد ΔΣa₂ = {dsa:.4g} cm⁻¹ يصبح k_eff = {kn:.5f} عند نفس السماكة")
        if kn < 1:
            bad("أصبح تحت الحرج — هكذا يعمل البورون المذاب وقضبان التحكم فيزيائياً.")
        else:
            note("ما زال فوق الحرج: زِد التركيز.")
        new_ac = critical_thickness(m2, lo=a_c, hi=40000.0)
        if new_ac:
            print(f"  السماكة الحرجة الجديدة: {new_ac:.1f} سم (كانت {a_c:.1f} سم)")
        react = (kn - 1.0) / kn
        beta = 0.0065
        print(f"  التفاعلية ρ = (k−1)/k = {react*1e5:.0f} pcm = {react/beta:.2f} $ "
              f"(β_eff = {beta} تمثيلي)")
        if abs(react) > beta:
            warn("|ρ| > β: انتقال يتجاوز حيّز النيوترونات المتأخرة — "
                 "هنا تفقد سيطرة قضبان التحكم معناها الزمني المعتاد.")

    note("""
ما وراء هذا المختبر (مفتوح بالكامل في الخريطة):
  نقل بولتزمان S_N و P_N · نظرية النقل ومعادلة النقل التكاملية · مونتي-كارلو
  (تتبّع تاريخ النيوترون، تقدير k_eff بـ Shannon-entropy، Shannon jitter)
  · مجموعات متعددة ومعالجة الرنين (Nordheim، Bondarenko) · نظرية الاضطراب
  لحساب معاملات التفاعل · حرق الوقود ومعادلات Bateman · نيوترونيات الزمن
  (kinetics، مصفوفة النقاط) · سلامة الحراجة (criticality safety) في كل مكان
  تُعالَج فيه مواد انشطارية · الحراجة الحرجة والسموم (Xe-135، Sm-149).""")
    pause()


if __name__ == "__main__":
    run()
