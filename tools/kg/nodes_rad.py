# -*- coding: utf-8 -*-
"""عقد الإشعاع والقياس (H) + الحماية (I) + السلامة والحوادث (J)."""
from .schema import N

# ================================================= الإشعاع والقياس (H) ======
N("rad.types", "أنواع الإشعاع", "Types of ionizing radiation", "rad", 3, "core", 2, 25,
  prereqs=["nuc.decay", "phys.atomic"],
  concepts=["الإشعاع المؤين مقابل غير المؤين",
            "ألفا وبيتا وغاما والأشعة السينية",
            "النيوترونات", "الجسيمات الثقيلة المشحونة",
            "القدرة على التأين (LET مباشر وغير مباشر)"],
  apps=["تحديد مخاطر المصدر", "اختيار الكاشف والتدريع"],
  sources=["Turner", "Knoll"],
  tags=["أساس", "مفتاح"])

N("rad.sources", "مصادر الإشعاع", "Radiation sources", "rad", 3, "core", 2, 25,
  prereqs=["rad.types", "nuc.halflife"],
  concepts=["المصادر الطبيعية (الكوزمية والأرضية والرادون)",
            "المصادر الصناعية والمصادر المختومة",
            "المولّدات (Mo-99/Tc-99m)", "مصادر النيوترونات (Ra-Be, Cf-252، أنابيب D-T)",
            "الإشعاع الطبيعي التشغيلي (NORM)"],
  apps=["تصنيف المصادر وترخيصها", "حساب الجرعات"],
  sources=["UNSCEAR", "IAEA-GSR-Part3"],
  tags=["أساس"])

N("rad.interaction", "تفاعل الإشعاع مع المادة", "Radiation interactions with matter",
  "rad", 4, "core", 4, 55,
  prereqs=["rad.types", "phys.atomic", "phys.emi"],
  concepts=["الجسيمات المشحونة: فقد الطاقة (Bethe-Bloch) والمدى",
            "الفوتونات: التأثير الكهروضوئي، كومبتون، إنتاج الزوج",
            "النيوترونات: التشتت والامتصاص والتفاعلات النووية",
            "الطاقة الخطية النقل LET", "التوقف النسبي والتشتت المتعدد"],
  eqs=["-dE/dx ∝ (z²/v²) n ln(2m_ev²/I)",
       "μ/ρ = τ + σ_coh + σ_incoh + κ"],
  apps=["اختيار الكواشف", "حساب التدريع", "قياس الجرعة"],
  sources=["Attix", "Knoll"],
  tags=["مفتاح", "جوهري"])

N("rad.transport", "انتقال الإشعاع والتوهين", "Radiation transport & attenuation", "rad", 4, "core", 4, 45,
  prereqs=["rad.interaction", "math.ode"],
  concepts=["التوهين الأسي وطبقة القيمة النصفية",
            "معامل التوهين الكتلي والتراكم (buildup)",
            "انتقال النيوترونات والفوتونات", "الحلول التحليلية والعددية"],
  eqs=["I = I₀ e^{-μx}", "I = B I₀ e^{-μx}", "HVL = ln2/μ"],
  apps=["تصميم التدريع", "تصحيح الهندسة في القياس"],
  sources=["Attix", "Turner"],
  tags=["مفتاح"])

N("rad.dosimetry", "الجرعة: الممتصة والمكافئة والفعالة", "Dosimetry: absorbed, equivalent & effective dose",
  "rad", 4, "core", 4, 50,
  prereqs=["rad.interaction", "rad.transport"],
  concepts=["الجرعة الممتصة D (Gy)",
            "الجرعة المكافئة H_T = w_R D_T (Sv)",
            "الجرعة الفعالة E = Σ w_T H_T",
            "الكيرما والتعرض والجرعة العميقة",
            "مقادير الحماية التشغيلية (Hp(10), Hp(0.07))"],
  eqs=["D = dĒ/dm", "H_T = w_R · D_T", "E = Σ_T w_T H_T"],
  apps=["الامتثال للحدود", "الوقاية المهنية", "التواصل العام"],
  sources=["ICRP-103", "ICRU-85"],
  tags=["مفتاح", "جوهري", "غالباً يُنسى"])

N("rad.detectors", "كواشف الإشعاع", "Radiation detectors", "rad", 4, "core", 4, 60,
  prereqs=["rad.interaction", "phys.em", "meas.electronics"],
  concepts=["غرف الغاز (التأين والتناسب وغايغر)",
            "الكواشف الوميضية وأشباه الموصلات (HPGe, Si, CdTe)",
            "كواشف النيوترونات (He-3, BF₃, اللوّام السائلة)",
            "المنشّطات الحرارية واللمعانية (TLD/OSL) والأفلام",
            "الكفاءة والزمن الميت والاستجابة للطاقة"],
  eqs=["كفاءة مطلقة = عدد النبضات/عدد الجسيمات المنبعثة"],
  apps=["القياس المخبري والميداني", "التحليل الطيفي", "مراقبة المناطق"],
  sources=["Knoll"],
  tags=["مفتاح", "عملي"])

N("rad.spectroscopy", "التحليل الطيفي الإشعاعي", "Radiation spectroscopy", "rad", 4, "core", 4, 50,
  prereqs=["rad.detectors", "meas.signal", "math.stat"],
  concepts=["أطياف غاما: القمم الكاملة والطرود الفوتونية",
            "الدقة والكفاءة والمعايرة بالطاقة",
            "تحديد المنطقة الصافية والحد الأدنى للكشف (MDA)",
            "التكديس والزمن الميت", "التوهين الذاتي والتطابق"],
  eqs=["FWHM = √(a + bE + cE²)", "MDA = 2.71 + 4.65√B"],
  apps=["تحديد النويدات كمياً", "مراقبة البيئة", "قياس النشاط"],
  sources=["Knoll"],
  tags=["مفتاح", "عملي"])

N("rad.shielding", "التدريع", "Radiation shielding", "rad", 4, "core", 4, 45,
  prereqs=["rad.transport", "rad.interaction"],
  concepts=["مواد التدريع للفوتونات (Pb, W, خرسانة)",
            "تدريع النيوترونات: التباطؤ ثم الامتصاص",
            "الدرع المركّب والسموم النيوترونية (B, Li)",
            "التسخين في الدرع والإشعاع الثانوي", "فتحات ومرور الأنابيب (streaming)"],
  apps=["تصميم المنشآت والحاويات", "حماية العاملين"],
  sources=["Turner", "Attix"],
  tags=["مفتاح"])

N("rad.contamination", "التلوث الإشعاعي والتعرض", "Contamination & exposure", "rad", 4, "core", 3, 30,
  prereqs=["rad.types", "rad.sources"],
  concepts=["التلوث مقابل التشعيع", "التلوث السطحي والهوائي",
            "مسارات الدخول (استنشاق، ابتلاع، جلد، جرح)",
            "الاحتواء وإزالة التلوث", "قياس التلوث"],
  apps=["العمل في المختبرات", "الاستجابة للحوادث"],
  tags=["مفتاح"])

N("rad.bio", "علم الأحياء الإشعاعي والتأثيرات البيولوجية", "Radiobiology & biological effects",
  "rad", 5, "core", 4, 55,
  prereqs=["rad.dosimetry", "chem.radiochemistry"],
  concepts=["التفاعلات على المستوى الجزيئي والخلوي",
            "تلف DNA والإصلاح", "التأثيرات الحتمية والاحتمالية (stochastic)",
            "النماذج: خطي بلا عتبة (LNT) والنقاش حوله",
            "التأثيرات الحادة والمزمنة والوراثية",
            "عوامل الفعالية النسبية RBE والأكسجين OER"],
  eqs=["نموذج خطي-تربيعي: S = exp(-αD - βD²)"],
  apps=["تحديد الحدود", "الطب النووي والعلاج", "التواصل عن المخاطر"],
  sources=["UNSCEAR", "ICRP-103"],
  tags=["مفتاح", "متنازع عليه جزئياً"])

N("rad.metrology", "قياسات الإشعاع والقياسات المرجعية (Metrology)", "Radiation metrology & standards",
  "rad", 5, "specialized", 4, 35,
  prereqs=["rad.dosimetry", "meas.calibration"],
  concepts=["التتبّع إلى المعايير الوطنية (NMI/PTB/NIST/NPL)",
            "غرف الجرعة المرجعية والقياس المعياري",
            "مقارنات دولية (BIPM/CCRI)", "شهادات المعايرة"],
  apps=["معايرة الأجهزة", "الامتثال القانوني"],
  sources=["ICRU-85", "NIST"],
  tags=["تخصصي", "غالباً يُنسى"])

N("rad.activation", "التنشيط النيوتروني وتحليله (NAA)", "Neutron activation & NAA", "rad", 6, "specialized", 4, 35,
  prereqs=["nuc.crosssection", "rad.spectroscopy", "rx.research"],
  concepts=["معدل التنشيط والتشبع",
            "الطرق: بطيء نسبياً، مؤقت، سريع",
            "مقارنة بمعيار (comparator method) و k₀",
            "التداخلات والتصحيحات"],
  eqs=["A = N σ Φ (1 - e^{-λt})", "R = N σ Φ S D C"],
  apps=["تحليل العناصر النزرة", "علم الآثار والبيئة", "مراقبة المواد"],
  tags=["تخصصي", "عملي"])

# ================================================ الحماية من الإشعاع (I) =====
N("prot.principles", "مبادئ الحماية الإشعاعية", "Principles of radiation protection",
  "prot", 5, "core", 3, 35,
  prereqs=["rad.dosimetry", "rad.bio"],
  concepts=["المبادئ الثلاثة: التبرير، التحسين (ALARA)، تحديد الجرعة",
            "الزمن والمسافة والتدريع", "قانون التربيع العكسي",
            "حدود الجرعة للعاملين والجمهور", "تصنيف المناطق والإشراف"],
  eqs=["D ∝ 1/r²", "H = H₀ e^{-μx} (r₀/r)²"],
  apps=["كل عمل مع الإشعاع", "تصميم المختبرات والمواقع"],
  sources=["ICRP-103", "IAEA-GSR-Part3", "NRC-10CFR20"],
  tags=["مفتاح", "جوهري"])

N("prot.monitoring", "المراقبة وقياس الجرعات", "Monitoring & dosimetry services", "prot", 5, "core", 3, 35,
  prereqs=["prot.principles", "rad.detectors"],
  concepts=["قياس الجرعات الشخصية (TLD, OSL, إلكترونية)",
            "مراقبة منطقة العمل والهواء", "مراقبة الجسم كله والمسح",
            "سجلات الجرعة والاحتفاظ بها", "مستويات التحقيق"],
  apps=["برامج الوقاية المهنية", "الامتثال"],
  sources=["IAEA-GSR-Part3"],
  tags=["مفتاح"])

N("prot.occupational", "الوقاية المهنية والصحة المهنية", "Occupational radiation protection",
  "prot", 5, "core", 3, 35,
  prereqs=["prot.monitoring", "rad.contamination"],
  concepts=["تصنيف العاملين", "معدات الوقاية الشخصية",
            "إجراءات العمل الآمنة وتصريح العمل",
            "المراقبة الطبية", "حماية الأجنة والعاملات الحوامل"],
  apps=["إدارة برامج الحماية", "التدريب"],
  tags=["مفتاح"])

N("prot.lab", "السلامة في المختبرات الإشعاعية", "Radiation laboratory safety", "prot", 6, "core", 3, 30,
  prereqs=["prot.principles", "chem.hotcells"],
  concepts=["تصميم المختبر وتدفق العمل", "الاحتواء والتهوية والترشيح",
            "إدارة المصادر وجردها", "التعامل مع الانسكابات",
            "نقل المصادر والتخلص"],
  apps=["العمل العملي الآمن", "التدريب الجامعي"],
  tags=["مفتاح", "عملي"])

N("prot.emergency", "الاستجابة للطوارئ الإشعاعية", "Radiological emergency response & preparedness",
  "prot", 7, "core", 4, 40,
  prereqs=["prot.principles", "safe.accidents", "env.dispersion"],
  concepts=["مستويات الطوارئ وتصنيفها",
            "مناطق التخطيط (UPZ, EPZ) والإيواء والإخلاء",
            "حبوب اليود المستقر (KI)",
            "القياس الميداني وتخطيط الجرعة", "التواصل مع الجمهور"],
  apps=["خطط الطوارئ الوطنية والمحلية", "التمارين"],
  sources=["IAEA-GSR-Part3", "IAEA-SF1"],
  tags=["مفتاح"])

N("prot.medical", "الحماية الإشعاعية في الطب", "Radiation protection in medicine", "prot", 9, "specialized", 4, 35,
  prereqs=["prot.principles", "med.imaging", "med.therapy"],
  concepts=["التبرير والتحسين في التصوير والعلاج",
            "مستويات المرجعية التشخيصية (DRL)",
            "جرعات المرضى والحوادث في العلاج الإشعاعي",
            "حماية العاملين في الأشعة التداخلية"],
  apps=["برامج الجودة في المستشفيات"],
  sources=["ICRP-103"],
  tags=["تخصصي"])

# ============================================= السلامة والحوادث (J) ==========
N("safe.culture", "ثقافة السلامة والحوكمة", "Safety culture & governance", "safe", 6, "core", 3, 30,
  prereqs=["safe.did"],
  concepts=["خصائص ثقافة السلامة (IAEA)",
            "القيادة والمسؤولية", "الإبلاغ عن الأحداث والتعلم",
            "ثقافة الإنصاف (just culture)", "المؤشرات والتقييم الذاتي"],
  apps=["إدارة المنشآت", "المراجعات الرقابية"],
  sources=["IAEA-SF1"],
  tags=["مفتاح", "غالباً يُنسى"])

N("safe.did", "الدفاع في العمق", "Defence in depth", "safe", 5, "core", 3, 35,
  prereqs=["rad.dosimetry", "rx.principles"],
  concepts=["المستويات الخمسة للدفاع في العمق",
            "الحواجز المتعددة (الوقود، الغلاف، الاحتواء)",
            "الاستقلال والتنوع والتكرار",
            "الإقصاء العملي للتسريبات المبكرة أو الكبيرة",
            "ظروف التصميم الممتدة (DEC)"],
  apps=["كل تحليل سلامة", "التصميم والترخيص"],
  sources=["IAEA-SSR2/1", "IAEA-SSG-46"],
  tags=["مفتاح", "جوهري"])

N("safe.systems", "أنظمة الأمان والتصنيف", "Safety systems & classification", "safe", 6, "core", 4, 40,
  prereqs=["safe.did", "rx.control"],
  concepts=["أنظمة الأمان والتحكم والحماية",
            "التصنيف: سلامة وأهمية للأمان", "التكرار والتنوع والعزل المادي",
            "الإيقاف الآمن والتبريد المتبقي", "الاحتواء"],
  apps=["التصميم والترخيص", "تحليل الموثوقية"],
  sources=["IAEA-SSR2/1", "NUREG-0800"],
  tags=["مفتاح"])

N("safe.hazard", "تحليل المخاطر وتحديد الأحداث البادئة", "Hazard analysis & initiating events",
  "safe", 6, "core", 4, 40,
  prereqs=["safe.systems", "math.prob"],
  concepts=["المخاطر الداخلية والخارجية",
            "تحديد الأحداث البادئة (PIE) وتجميعها",
            "طرق: HAZOP وFMEA وأشجار الأخطاء",
            "تحليل المخاطر الخارجية (زلازل، فيضانات، طقس)"],
  apps=["أساس التحليل الحتمي والاحتمالي"],
  sources=["IAEA-SSR2/1"],
  tags=["مفتاح"])

N("safe.psa", "التقييم الاحتمالي للسلامة (PSA/PRA)", "Probabilistic safety assessment",
  "safe", 6, "core", 5, 60,
  prereqs=["safe.hazard", "math.prob", "safe.human"],
  concepts=["المستويات 1 و2 و3",
            "أشجار الأحداث وأشجار الأخطاء",
            "التردد الأساسي لتلف القلب CDF وتردد التسريب المبكر LERF",
            "أهمية القياس (Fussell-Vesely)",
            "الاعتماديات والسبب المشترك (CCF)",
            "PSA الحيّ وإدارة المخاطر الموجّهة بالrisk"],
  eqs=["CDF = Σ_j f_j · P(فشل|j)", "P(شجرة أخطاء OR/AND)"],
  apps=["الترخيص الحديث", "تحديد أولويات التحسينات"],
  sources=["NUREG-1150", "IAEA-SSG-46"],
  tags=["مفتاح", "متقدم"])

N("safe.dsa", "التقييم الحتمي للسلامة", "Deterministic safety analysis", "safe", 6, "core", 4, 45,
  prereqs=["safe.systems", "rx.thermalhyd", "math.nummethods"],
  concepts=["تصنيف حالات المحطة",
            "مبادئ المحافظة والهوامش",
            "الأكواد الحتمية (RELAP, TRACE, ATHLET, CATHARE)",
            "معايير القبول (مثل درجة حرارة الغلاف)",
            "النهج الأفضل-التقدير مع عدم اليقين (BEPU)"],
  apps=["الترخيص", "تحليل الحوادث"],
  sources=["NUREG-0800", "IAEA-SSG-46"],
  tags=["مفتاح"])

N("safe.severe", "تحليل الحوادث الشديدة", "Severe accident analysis", "safe", 7, "advanced", 5, 55,
  prereqs=["safe.dsa", "safe.psa", "fuel.inreactor"],
  concepts=["تسلسل الحوادث الشديدة وتدهور القلب",
            "أكسدة الزركونيوم والهيدروجين", "تفاعل الحطام المنصهر والخرسانة (MCCI)",
            "الاحتواء والتسخين المباشر والتفجيرات", "أكواد مثل MELCOR وMAAP",
            "إدارة الحوادث والاستراتيجيات"],
  apps=["إدارة الحوادث", "تصميم ما بعد فوكوشيما"],
  sources=["NUREG-1150", "IAEA-SSR2/1"],
  tags=["متقدم", "جوهري"])

N("safe.human", "العوامل البشرية والموثوقية البشرية", "Human factors & human reliability",
  "safe", 6, "core", 4, 40,
  prereqs=["safe.culture", "math.stat"],
  concepts=["تحليل الموثوقية البشرية (THERP, SPAR-H)",
            "أنماط الخطأ وأشكال الأداء",
            "تصميم غرف التحكم والواجهات", "التدريب والمحاكاة",
            "التنظيم والضغط الزمني"],
  apps=["PSA", "التحقيق في الحوادث"],
  sources=["NUREG-1150"],
  tags=["مفتاح", "غالباً يُنسى"])

N("safe.risk", "إدارة المخاطر واتخاذ القرار", "Risk management & decision making", "safe", 7, "core", 4, 40,
  prereqs=["safe.psa", "safe.dsa", "cs.uq"],
  concepts=["القرارات الموجّهة بالمخاطر (risk-informed)",
            "معايير القبول والمقايضات", "تحليل التكلفة-الفائدة",
            "مخاطر متعددة الوحدات والمواقع", "التواصل عن المخاطر"],
  apps=["الرقابة والتشغيل", "السياسات"],
  tags=["مفتاح"])

N("safe.accidents", "الحوادث النووية التاريخية: تحليل", "Historical nuclear accidents: analysis",
  "safe", 7, "core", 4, 50,
  prereqs=["safe.severe", "safe.human", "hist.timeline"],
  concepts=["Three Mile Island-2 (1979): فقد المبرد الصغير والاحتواء",
            "تشرنوبل-4 (1986): التصميم والاختبار والثقافة",
            "فوكوشيما دايتشي (2011): الفيضان وفقد الطاقة والمصرف الحراري",
            "حوادث الإشعاع الصناعية والطبية (غويانيا، ليثيوم، …)",
            "منهجية التحليل: ماذا حدث، لماذا، ماذا تغير"],
  apps=["الاستفادة من الدروس", "السلامة المقارنة"],
  sources=["IAEA-SF1", "IAEA-SSR2/1"],
  tags=["مفتاح", "جوهري"])

N("safe.reg", "الرقابة والترخيص والتفتيش", "Regulation, licensing & inspection", "safe", 7, "core", 4, 40,
  prereqs=["safe.did", "pol.regulatory"],
  concepts=["الهيئات الرقابية واستقلالها", "عملية الترخيص خطوة بخطوة",
            "التفتيش والتنفيذ", "المراجعات الدورية للسلامة (PSR)",
            "المشاركة العامة والشفافية"],
  apps=["فهم الإطار التنظيمي"],
  sources=["NUREG-0800", "IAEA-SF1"],
  tags=["مفتاح"])
