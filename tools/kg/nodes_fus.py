# -*- coding: utf-8 -*-
"""عقد الاندماج والبلازما (L) + الأجهزة والكشف (R)."""
from .schema import N

# =================================================== الأجهزة والكشف (R) =====
N("meas.electronics", "الإلكترونيات النووية", "Nuclear electronics", "meas", 4, "core", 4, 45,
  prereqs=["phys.em", "math.complex"],
  concepts=["مضخمات الشحنة الحساسة والمضخمات التماثلية",
            "تشكيل النبضة والتفاضل والتكامل",
            "المقارنات والمحللات متعددة القنوات (MCA)",
            "مصادر الجهد العالي والضجيج والتأريض والتدريع الكهربائي",
            "التحويل الرقمي (ADC) والزمن الميت"],
  eqs=["V_out = Q/C_f", "FWHM ∝ √EN C"],
  apps=["بناء أي نظام قياس إشعاعي", "تطوير الكواشف"],
  sources=["Knoll"],
  tags=["مفتاح", "عملي"])

N("meas.signal", "معالجة الإشارات والحصول على البيانات", "Signal processing & data acquisition",
  "meas", 4, "core", 4, 40,
  prereqs=["meas.electronics", "math.analysis", "cs.numpy"],
  concepts=["الترشيح الرقمي وتشكيل النبضة الرقمي",
            "تمييز النيوترون/غاما (PSD)",
            "التحليل الطيفي المتعدد والاصطفاف",
            "أنظمة الاستحواذ (DAQ) والتشغيل المتوازي",
            "تحليل عدم يقين القياس"],
  apps=["أنظمة القياس الحديثة", "تحليل الإشارات المعقدة"],
  sources=["Knoll"],
  tags=["مفتاح", "عملي"])

N("meas.calibration", "معايرة الأجهزة ومصادر الخطأ", "Instrument calibration & error sources",
  "meas", 4, "core", 3, 35,
  prereqs=["rad.spectroscopy", "math.stat"],
  concepts=["معايرة الطاقة والكفاءة والزمن", "المصادر المرجعية المعتمدة",
            "مصادر الخطأ: إحصائي، منهجي، هندسي، تراكمي",
            "تجميع عدم اليقين (Type A و Type B)",
            "الاستقرار طويل الأمد وضبط الجودة"],
  eqs=["u_c = √(Σ u_i²)", "U = k u_c"],
  apps=["أي قياس موثوق", "الاعتماد المخبري"],
  sources=["Knoll", "ICRU-85"],
  tags=["مفتاح", "غالباً يُنسى"])

N("meas.detectors", "تقنيات الكواشف: نظرة هندسية", "Detector technologies: engineering view",
  "meas", 4, "core", 3, 35,
  prereqs=["rad.interaction"],
  concepts=["مفاضلات اختيار الكاشف",
            "الكفاءة، الدقة، الزمن الميت، المتانة",
            "الكواشف المحمولة والثابتة والشبكية",
            "أنظمة المراقبة البيئية", "تقنيات التصوير الإشعاعي"],
  apps=["تصميم أنظمة القياس"],
  sources=["Knoll"],
  tags=["مفتاح"])

N("meas.monitoring", "المسح الإشعاعي وتوصيف المواقع", "Radiological surveying & site characterization",
  "meas", 6, "specialized", 3, 30,
  prereqs=["rad.spectroscopy", "env.tracers"],
  concepts=["تخطيط المسح وأخذ العينات",
            "المسح الجوي والمركبات والمسيرات",
            "رسم الخرائط الإشعاعية (GIS)",
            "التحليل الإحصائي للمسح (MARSSIM)",
            "توثيق نتائج التحرر (release criteria)"],
  apps=["التفكيك", "الاستجابة للطوارئ", "المواقع الملوثة"],
  tags=["تخصصي", "عملي"])

N("meas.spectroscopy", "التحليل الطيفي المتقدم", "Advanced spectroscopy", "meas", 6, "specialized", 4, 35,
  prereqs=["rad.spectroscopy"],
  concepts=["مطيافية غاما-غاما والترابط الزمني",
            "مطيافية ألفا وبيتا ومطيافية الكتلة (ICP-MS, TIMS, AMS)",
            "مطيافية النيوترونات", "تقنيات الخلفية المنخفضة (تحت الأرض)"],
  apps=["التحليل الجنائي النووي", "القياسات فائقة الحساسية", "التأريخ"],
  tags=["تخصصي"])

# =============================================== الاندماج والبلازما (L) ======
N("fus.plasma", "فيزياء البلازما: الأساس", "Plasma physics: fundamentals", "fus", 5, "core", 4, 55,
  prereqs=["phys.emi", "phys.statmech", "math.vectors"],
  concepts=["البلازما كحالة رابعة وشرط الحياد الكهربائي",
            "طول ديباي وتردد البلازما ومعامل الاقتران",
            "الحركة المنجرفة للجسيمات في المجالات (E×B، الانجراف المغناطيسي)",
            "الحركة الجيروسكوبية والأديابات",
            "معدلات الاصطدام والتوصيل"],
  eqs=["λ_D = √(ε₀ k T_e / n e²)", "ω_p = √(n e²/ε₀ m)", "r_L = m v_⊥/(qB)"],
  apps=["أساس كل طرق الحبس", "تشخيص البلازما"],
  sources=["StaceyFusion"],
  tags=["مفتاح", "بوابة"])

N("fus.mhd", "المغناطيسية الهيدروديناميكية (MHD)", "Magnetohydrodynamics (MHD)", "fus", 6, "advanced", 5, 50,
  prereqs=["fus.plasma", "rx.fluids"],
  concepts=["معادلات MHD أحادية السوائل",
            "التجميد المغناطيسي وبيتا",
            "توازن الغراد-شافرانوف",
            "الاستقرار المثالي والمقاومي (kink, tearing, ballooning)",
            "الاضطرابات (disruptions) والتخفيف منها"],
  eqs=["β = p/(B²/2μ₀)", "Δ*ψ = -μ₀ r² dp/dψ - F dF/dψ"],
  apps=["تصميم التوكاماك", "التحكم في الاضطرابات"],
  sources=["StaceyFusion", "ITER-NewBaseline"],
  tags=["متقدم"])

N("fus.heating", "تسخين البلازما والتيار المدفوع", "Plasma heating & current drive", "fus", 6, "advanced", 4, 40,
  prereqs=["fus.plasma", "phys.emi"],
  concepts=["التسخين الأومي وحدوده",
            "تسخين بالرنين الأيوني/الإلكتروني السيكلوتروني (ICRH/ECRH)",
            "حقن الحزمة المحايدة (NBI)",
            "التيار المدفوع والتيار البوتسترابي", "التسخين الألفا في البلازما المشتعلة"],
  apps=["الوصول إلى درجات الحرارة الاندماجية"],
  sources=["StaceyFusion", "ITER-NewBaseline"],
  tags=["متقدم"])

N("fus.magnetic", "الحبس المغناطيسي", "Magnetic confinement", "fus", 6, "core", 4, 40,
  prereqs=["fus.plasma", "fus.mhd"],
  concepts=["الهندسات المغلقة ومشكلة النهايات",
            "الوقت المحصور ونقل الحرارة الشاذ",
            "الحبس في الحقل المعكوس والمرايا",
            "مقاييس الحبس (H-mode و L-mode و scaling laws)"],
  eqs=["τ_E ~ scaling (I_p, B, n, P, R, a)", "H-factor = τ_E/τ_{ITER98}"],
  apps=["مقارنة مقاربات الحبس"],
  sources=["StaceyFusion"],
  tags=["مفتاح"])

N("fus.tokamak", "التوكاماك", "Tokamaks", "fus", 7, "core", 4, 50,
  prereqs=["fus.magnetic", "fus.heating"],
  concepts=["الهندسة الطورية والتيار الحلقي والحقل القطبي",
            "تيار البلازما والتحكم في الشكل",
            "التباعد والـ divertor و X-point",
            "حدود الكثافة (Greenwald) وحدود بيتا (Troyon)",
            "ITU و ITER و SPARC و JT-60SA و JET",
            "الموصلات فائقة التوصيل (LTS/HTS)"],
  eqs=["q = a B_t/(R B_p) ≥ 2", "n_G = I_p/(π a²)"],
  apps=["فهم الطريق السائد للاندماج"],
  sources=["ITER-NewBaseline", "CFS-SPARC", "StaceyFusion"],
  tags=["مفتاح", "حديث"])

N("fus.stellarator", "الستيلاراتور", "Stellarators", "fus", 7, "specialized", 5, 45,
  prereqs=["fus.magnetic"],
  concepts=["التحسين ثلاثي الأبعاد للحقل المغناطيسي",
            "غياب التيار الحلقي = تشغيل مستمر أسهل",
            "التحدي: تصنيع الملفات المعقدة",
            "Wendelstein 7-X ونتائجه القياسية",
            "التحسين (quasi-symmetry, omnigenity)"],
  apps=["تقييم المسار البديل"],
  sources=["IPP-W7X"],
  tags=["تخصصي", "حديث"])

N("fus.inertial", "الحبس بالقصور الذاتي (ICF)", "Inertial confinement fusion", "fus", 7, "core", 5, 45,
  prereqs=["nuc.fusion_basics", "phys.emi", "phys.statmech"],
  concepts=["الضغط بالليزر أو الأشعة السينية (مباشر/غير مباشر)",
            "الهولراوم والانبساط الرشيق",
            "عدم استقرار رايلي-تايلور والمزج",
            "الاشتعال والكسب الهدفي (target gain)",
            "القيود: كفاءة الليزر والقدرة على التكرار"],
  eqs=["G = E_fusion/E_on_target", "ρR > ~0.3 g/cm² للاشتعال"],
  apps=["تقييم NIF والشركات الناشئة"],
  sources=["LLNL-Ignition"],
  tags=["مفتاح", "حديث"])

N("fus.alt", "مفاهيم حبس بديلة ومتوسطة الكثافة", "Alternative & magneto-inertial concepts",
  "fus", 7, "specialized", 4, 35,
  prereqs=["fus.magnetic", "fus.inertial"],
  concepts=["المرايا المغناطيسية وحبس الانعكاس",
            "الحقل المعكوس (FRC) والبينش-Z",
            "الاندماج بالقصور المغناطيسي (MIF)",
            "التركيز الكثيف للبلازما والنهج غير التقليدية",
            "كيفية تقييم الادعاءات علمياً"],
  apps=["قراءة مشهد الشركات الناشئة"],
  tags=["تخصصي"])

N("fus.materials", "مواد الاندماج", "Fusion materials", "fus", 8, "advanced", 5, 45,
  prereqs=["mat.damage", "mat.hightemp"],
  concepts=["أحمال حرارية عالية وتدفق نيوتروني 14 MeV",
            "التنغستن والمواد المبطّنة", "السبائك منخفضة التنشيط (RAFM)",
            "التآكل والترسيب وإعادة الترسيب", "التأثيرات على الموصلات والعزل"],
  apps=["تصميم المكونات المواجهة للبلازما"],
  sources=["Was", "StaceyFusion"],
  tags=["متقدم", "بحثي"])

N("fus.blanket", "البطانية وتكاثر التريتيوم", "Blankets & tritium breeding", "fus", 8, "advanced", 5, 45,
  prereqs=["fus.neutronics", "chem.isotope"],
  concepts=["البطانيات المولّدة (LiPb, Li₂TiO₃/Be)",
            "نسبة تكاثر التريتيوم TBR > 1",
            "استخلاص التريتيوم واحتوائه",
            "مخزون التريتيوم والسلامة", "استخراج الحرارة"],
  eqs=["TBR = إنتاج التريتيوم/استهلاكه"],
  apps=["تصميم محطات الاندماج", "دورة الوقود الذاتية"],
  sources=["StaceyFusion", "ITER-NewBaseline"],
  tags=["متقدم", "بحثي"])

N("fus.neutronics", "نيوترونيات الاندماج", "Fusion neutronics", "fus", 8, "advanced", 5, 45,
  prereqs=["rx.transport", "nuc.fusion_basics"],
  concepts=["طيف نيوترونات 14.1 MeV",
            "التنشيط وتلف المواد (dpa)",
            "التدريع وحماية الملفات",
            "توليد الحرارة الحجمية", "طرق مونتي كارلو للاندماج"],
  apps=["تصميم المحطة", "تحليل السلامة"],
  tags=["متقدم"])

N("fus.diagnostics", "تشخيص البلازما", "Plasma diagnostics", "fus", 7, "specialized", 5, 45,
  prereqs=["fus.plasma", "meas.detectors", "meas.signal"],
  concepts=["قياس الكثافة والحرارة (Thomson scattering, ECE)",
            "التداخل والبولاريمتري", "مطيافية الأشعة السينية والنيوترونات",
            "المجسات المغناطيسية", "التحليل العكسي للبيانات"],
  apps=["تشغيل التجارب", "التحكم"],
  tags=["تخصصي", "عملي"])

N("fus.engineering", "هندسة الاندماج واقتصادياته", "Fusion engineering & economics", "fus", 8, "advanced", 5, 40,
  prereqs=["fus.tokamak", "fus.materials", "rx.economics"],
  concepts=["نظم المغناطيسات والتبريد والموجودات",
            "صيانة عن بُعد وتوفر المحطة",
            "تكلفة الكهرباء المتوقعة والشكوك",
            "المقارنة مع الانشطار والمتجددة",
            "خارطة طريق: ITER → DEMO → محطة تجارية"],
  apps=["تقييم واقعي للجدول والاقتصاد"],
  sources=["ITER-NewBaseline", "CFS-SPARC"],
  tags=["متقدم", "حديث"])
