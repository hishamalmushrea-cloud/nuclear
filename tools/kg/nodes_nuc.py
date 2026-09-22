# -*- coding: utf-8 -*-
"""عقد الفيزياء النووية (D) والبيانات النووية وعلم النيوترونات."""
from .schema import N

N("nuc.intro", "مقدمة الفيزياء النووية", "Introduction to nuclear physics", "nuc", 3, "core", 3, 40,
  prereqs=["phys.atomic", "phys.relativity", "nuc.isotopes"],
  concepts=["مقاييس الطول والطاقة النووية", "النواة مقابل الذرة",
            "النويدات وخريطة النويدات", "وحدات الطاقة (eV..MeV)"],
  eqs=["1 MeV = 1.602×10⁻¹³ J", "1 fm = 10⁻¹⁵ m"],
  apps=["قراءة كل ما يلي في المجال النووي"],
  tags=["بوابة"])

N("nuc.nucleons", "النيوكليونات والقوة النووية", "Nucleons & the nuclear force", "nuc", 3, "core", 3, 35,
  prereqs=["nuc.intro", "part.forces"],
  concepts=["البروتون والنيوترون وخصائصهما", "الطبيعة المتبقية للقوة القوية (Yukawa)",
            "الاعتماد على الغزل والمدى القصير", "الإشباع والتنافر في المدى القصير جداً"],
  eqs=["V(r) ~ -g² e^{-r/r₀}/r"],
  apps=["تفسير استقرار النواة", "نماذج القوة النووية الفعالة"],
  tags=["مفتاح"])

N("nuc.isotopes", "النظائر والنويدات وخريطة النويدات", "Isotopes, nuclides & the chart of nuclides",
  "nuc", 3, "core", 2, 25,
  prereqs=["phys.atomic", "chem.structure"],
  concepts=["التدوين ^A_Z X", "النظائر/المتساويات النيوترونية/الإيزوبارات",
            "النويدات المستقرة والمشعة", "الوفرة الطبيعية"],
  eqs=["A = Z + N"],
  apps=["اختيار النظائر للتطبيقات", "قراءة LiveChart وNuDat"],
  sources=["IAEA-NDS", "Krane"],
  tags=["أساس", "مفتاح"])

N("nuc.binding", "الطاقة الرابطة ونقص الكتلة", "Binding energy & mass defect", "nuc", 3, "core", 3, 35,
  prereqs=["nuc.isotopes", "phys.relativity"],
  concepts=["طاقة الارتباط والكتلة", "طاقة الارتباط لكل نيوكليون",
            "الصيغة شبه التجريبية للكتلة (Weizsäcker)", "حدود الاستقرار"],
  eqs=["B = [Z m_p + N m_n - M(A,Z)]c²",
       "B = a_v A - a_s A^{2/3} - a_c Z(Z-1)/A^{1/3} - a_a (A-2Z)²/A ± δ"],
  apps=["لماذا يطلق الانشطار طاقة", "لماذا يطلق الاندماج طاقة", "حساب Q للتفاعلات"],
  sources=["Krane"],
  tags=["مفتاح", "جوهري"])

N("nuc.mass", "الكتل النووية وجداول الكتل", "Nuclear masses & mass tables", "nuc", 4, "supporting", 3, 20,
  prereqs=["nuc.binding"],
  concepts=["تقييمات الكتل الذرية (AME)", "وحدة الكتلة الذرية",
            "قياس الكتل بمطيافية الكتلة والترددات (Penning trap)"],
  eqs=["1 u = 931.494 MeV/c²"],
  apps=["حساب Q-values دقيقة", "حساب طاقة الارتباط"],
  sources=["NIST", "NNDC"],
  tags=["دعم"])

N("nuc.stability", "الاستقرار النووي وخط الاستقرار", "Nuclear stability & the valley of stability",
  "nuc", 3, "core", 3, 30,
  prereqs=["nuc.binding", "nuc.isotopes"],
  concepts=["نسبة N/Z والاستقرار", "خطوط التنقيط وحدودها",
            "طاقة الفصل للنيوترون والبروتون", "النويدات السحرية"],
  eqs=["N/Z ≈ 1 للخفيفة ويزداد للثقيلة"],
  apps=["التنبؤ بنمط التحلل", "فهم النويدات بعيدة عن الاستقرار"],
  tags=["مفتاح"])

N("nuc.decay", "التحلل الإشعاعي وأنواعه", "Radioactive decay modes", "nuc", 3, "core", 3, 50,
  prereqs=["nuc.stability", "phys.qm1"],
  concepts=["تحلل ألفا (نفق كمومي)", "تحلل بيتا (β⁻, β⁺, التقاط إلكترون)",
            "انبعاث غاما والتحويل الداخلي", "الانشطار التلقائي وانبعاث العناقيد",
            "قواعد اختيار الانتقالات ومخططات المستويات"],
  eqs=["P ≈ exp[-2∫√(2m(V-E))/ħ dr]", "Q_β⁻ = [M(A,Z) - M(A,Z+1)]c²"],
  apps=["تحديد نمط التحلل", "قراءة مخططات التحلل (decay schemes)", "حساب النشاط"],
  sources=["Krane", "IAEA-NDS"],
  tags=["مفتاح", "جوهري"])

N("nuc.halflife", "عمر النصف وقانون التحلل والنشاط", "Half-life, decay law & activity",
  "nuc", 3, "core", 2, 30,
  prereqs=["nuc.decay", "math.ode"],
  concepts=["ثابت التحلل وعمر النصف وعمر المتوسط",
            "النشاط والوحدات (Bq, Ci)", "النشاط النوعي",
            "نمو الابن والاضمحلال المتسلسل"],
  eqs=["N(t) = N₀ e^{-λt}", "T_{1/2} = ln2 / λ", "A = λN"],
  apps=["حساب نشاط مصدر", "التأريخ الإشعاعي", "جرعات المريض في الطب النووي"],
  tags=["مفتاح", "جوهري"])

N("nuc.series", "سلاسل التحلل والتوازن الإشعاعي", "Decay chains & secular equilibrium",
  "nuc", 4, "core", 4, 35,
  prereqs=["nuc.halflife", "math.ode"],
  concepts=["معادلات Bateman للسلاسل", "التوازن المؤقت والمستقر",
            "سلاسل U-238 وU-235 وTh-232", "نمو الابن المتراكم"],
  eqs=["dN_i/dt = λ_{i-1}N_{i-1} - λ_i N_i",
       "توازن مستقر: λ₁N₁ = λ₂N₂"],
  apps=["جرعات الرادون وأبنائه", "تأريخ U-Pb", "تقييم النفايات طويلة العمر"],
  tags=["مفتاح"])

N("nuc.reactions", "التفاعلات النووية والـ Q-value", "Nuclear reactions & Q-values", "nuc", 3, "core", 4, 45,
  prereqs=["nuc.binding", "phys.energy", "phys.relativity"],
  concepts=["التدوين A(a,b)B", "حساب Q من الكتل", "طاقة العتبة",
            "حركية المختبر مقابل مركز الكتلة", "أنواع التفاعلات (التقاط، تشتت، نقل)"],
  eqs=["Q = (M_أولية - M_نهائية)c²", "E_th = -Q (m_a + m_A)/m_A"],
  apps=["حساب طاقة النواتج", "اختيار تفاعلات إنتاج النظائر"],
  sources=["Krane"],
  tags=["مفتاح"])

N("nuc.crosssection", "المقاطع العرضية", "Cross sections", "nuc", 3, "core", 4, 45,
  prereqs=["nuc.reactions", "math.prob"],
  concepts=["تعريف المقطع العرضي (1 barn = 10⁻²⁸ m²)",
            "الاعتماد على الطاقة: 1/v، الرنين، العتبة",
            "المقاطع المجهرية والمجهرية-الكبرية", "معدل التفاعل R = Φ σ N"],
  eqs=["σ = (# أحداث)/(# جسيمات ساقطة × # ذرات/المساحة)", "Σ = N σ"],
  apps=["كل حسابات النيوترونيات", "تصميم الوقود والتدريع"],
  sources=["Krane", "IAEA-NDS"],
  tags=["مفتاح", "جوهري"])

N("nuc.scattering", "التشتت النووي", "Nuclear scattering", "nuc", 4, "advanced", 4, 40,
  prereqs=["nuc.crosssection", "phys.qm2"],
  concepts=["التشتت المرن وغير المرن", "التشتت الكمومي (الأطوار الجزئية)",
            "صيغة برايت-فينر للرنين", "التشتت النيوتروني وحيود النيوترونات"],
  eqs=["σ_l = (4π/k²)(2l+1) sin²δ_l",
       "σ(E) = (π/k²) g Γ²/((E-E_r)² + Γ²/4)"],
  apps=["تحليل بيانات التجارب", "علم النيوترونات", "قياس البنية"],
  tags=["متقدم"])

N("nuc.absorption", "الامتصاص والرنين والنماذج النووية للتفاعل",
  "Absorption, resonances & reaction models", "nuc", 4, "advanced", 4, 40,
  prereqs=["nuc.crosssection", "nuc.scattering"],
  concepts=["نموذج النواة المركبة", "عروض الرنين وتأثير دوبلر",
            "التفاعلات المباشرة وما قبل التوازن", "التكاملات الرنينية"],
  eqs=["σ(E) مع توسّع دوبلر", "قاعدة بورتر-توماس للعروض"],
  apps=["توليد البيانات النووية المقيّمة", "فهم مناطق الرنين في U-238"],
  tags=["متقدم"])

N("nuc.neutron", "فيزياء النيوترونات", "Neutron physics", "nuc", 4, "core", 4, 50,
  prereqs=["nuc.crosssection", "nuc.absorption"],
  concepts=["النيوترونات الحرارية والسريعة والبطيئة",
            "التباطؤ والإعتاق (moderation)", "طيف فيرمي وطيف ماكسويل",
            "النيوترونات المتأخرة في الانشطار", "النيوترونات الباردة وفائقة البرودة"],
  eqs=["E' ≈ αE مع α = ((A-1)/(A+1))²", "⟨ξ⟩ = 1 + α ln α/(1-α)"],
  apps=["أساس المفاعلات الحرارية", "مصادر النيوترونات للبحث", "تحليل التنشيط"],
  sources=["Lamarsh", "Duderstadt"],
  tags=["مفتاح", "جوهري"])

N("nuc.fission", "الانشطار النووي", "Nuclear fission", "nuc", 3, "core", 4, 50,
  prereqs=["nuc.binding", "nuc.reactions"],
  concepts=["نموذج القطرة السائلة والانشطار",
            "حاجز الانشطار والحالة السرجية", "توزيع كتل النواتج",
            "النيوترونات الفورية والمتأخرة", "طاقة الانشطار وتوزيعها",
            "الانشطار المستحث والذاتي"],
  eqs=["~200 MeV لكل انشطار", "ν̄ ≈ 2.4 لـ U-235 الحراري"],
  apps=["كل مفاعلات الانشطار", "إنتاج النظائر الانشطارية (Mo-99)"],
  sources=["Krane", "Lamarsh"],
  tags=["مفتاح", "جوهري"])

N("nuc.fusion_basics", "الاندماج النووي: الأساس الفيزيائي", "Nuclear fusion: physical basis",
  "nuc", 3, "core", 4, 40,
  prereqs=["nuc.binding", "nuc.reactions", "phys.statmech"],
  concepts=["تفاعلات D-T وD-D وD-He3", "حاجز كولومب والنفق الكمومي",
            "معامل غاموف ومعدلات التفاعل ⟨σv⟩", "شرط لوسون ومعامل الثلاثية"],
  eqs=["⟨σv⟩ = ∫ σ(v) v f(v) d³v", "n T τ_E ≥ 3×10²¹ keV·s/m³ (شرط لوسون لـ D-T)"],
  apps=["أساس الاندماج كمصدر طاقة", "التخليق النووي في النجوم"],
  sources=["StaceyFusion"],
  tags=["مفتاح"])

N("nuc.models", "نماذج النواة", "Nuclear models", "nuc", 4, "advanced", 5, 60,
  prereqs=["phys.qm2", "nuc.stability"],
  concepts=["نموذج القطرة السائلة", "نموذج القشرة المستقل والأعداد السحرية",
            "النموذج الجماعي (الاهتزاز والدوران)", "النموذج الموحد والنموذج البيني",
            "نماذج ab initio والتفاعلات الفعالة الحديثة"],
  eqs=["V(r) + (l·s) للقشرة مع اقتران الغزل-المدار"],
  apps=["تفسير مستويات النواة", "التنبؤ بخصائص النويدات البعيدة",
        "تقييم البيانات النووية"],
  sources=["Krane", "ArXiv-Nucl"],
  tags=["متقدم", "بحثي"])

N("nuc.exp", "الفيزياء النووية التجريبية", "Experimental nuclear physics", "nuc", 4, "advanced", 4, 50,
  prereqs=["nuc.decay", "meas.detectors", "math.stat"],
  concepts=["تجهيز التجربة والهدف والحزمة", "قياس المقاطع العرضية",
            "مطيافية غاما وأشعة بيتا", "فصل النواتج وقياس عمر النصف",
            "مصادر الخطأ والتصحيحات"],
  apps=["توليد بيانات جديدة", "قياسات دقيقة للأعمار والكتل"],
  tags=["متقدم", "عملي"])

N("nuc.theory", "الفيزياء النووية النظرية", "Theoretical nuclear physics", "nuc", 4, "advanced", 5, 60,
  prereqs=["nuc.models", "phys.qm2"],
  concepts=["مشكلة عدة أجسام النووية", "طرق الهيكل: Hartree-Fock, shell model, DFT نووية",
            "نماذج التفاعل: R-matrix, Hauser-Feshbach", "الرياضيات العددية للحل"],
  apps=["التنبؤ بالبيانات المفقودة", "تفسير النتائج", "تقييم البيانات"],
  sources=["ArXiv-Nucl"],
  tags=["متقدم", "بحثي"])

N("nuc.data", "البيانات النووية (Nuclear Data)", "Nuclear data", "nuc", 4, "core", 3, 35,
  prereqs=["nuc.crosssection", "cs.data"],
  concepts=["مكتبات مقيّمة: ENDF/B وJEFF وJENDL وTENDL وCENDL",
            "بيانات تجريبية: EXFOR", "بنية واضمحلال: ENSDF وNuDat",
            "المعالجة: NJOY وPREPRO", "مصفوفات التغاير وعدم اليقين"],
  apps=["كل محاكاة نووية تبدأ من هنا", "التحقق والمقارنة"],
  sources=["IAEA-NDS", "NNDC", "NEA-Databank"],
  tags=["مفتاح", "غالباً يُنسى"])

N("nuc.neutronsci", "علم النيوترونات (مصادر وتشتت)", "Neutron science (sources & scattering)",
  "nuc", 5, "specialized", 4, 40,
  prereqs=["nuc.neutron", "phys.condmat"],
  concepts=["مصادر النيوترونات: مفاعلات، تشظية، تشتت",
            "حيود النيوترونات والتشتت غير المرن", "تصوير النيوترونات",
            "النيوترونات الباردة وفائقة البرودة"],
  apps=["دراسة المواد والمغناطيسية", "تحليل الإجهاد", "علوم الحياة"],
  sources=["DOE-FRIB", "IAEA-NDS"],
  tags=["تخصصي"])

N("nuc.astro", "الفيزياء النووية الفلكية والتخليق النووي", "Nuclear astrophysics & nucleosynthesis",
  "nuc", 5, "specialized", 4, 40,
  prereqs=["nuc.fusion_basics", "nuc.reactions"],
  concepts=["التخليق في الانفجار العظيم والنجوم والمستعرات",
            "عمليات s وr وp", "معدلات التفاعل في البلازما النجمية",
            "النويدات بعيدة عن الاستقرار وخطوط الانتظار"],
  apps=["تفسير وفرة العناصر", "دور المنشآت الحديثة (FRIB وFAIR)"],
  sources=["DOE-FRIB"],
  tags=["تخصصي"])

N("nuc.structure", "بنية النواة المتقدمة", "Advanced nuclear structure", "nuc", 4, "advanced", 5, 45,
  prereqs=["nuc.models"],
  concepts=["الأنوية المشوهة والدوران فائق الدوران", "الإثارة الجماعية والرنينات العملاقة",
            "الأنوية الهالية وحدود التنقيط", "النويدات الثقيلة جداً وجزيرة الاستقرار"],
  apps=["بحث بنيوي", "قياسات بالمنشآت الراديوية"],
  sources=["ArXiv-Nucl", "DOE-FRIB"],
  tags=["متقدم", "بحثي"])
