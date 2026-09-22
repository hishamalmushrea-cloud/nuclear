# -*- coding: utf-8 -*-
"""عقد التطبيقات الطبية (M) والصناعية (N) والبيئية والزراعية (O)."""
from .schema import N

# ================================================= الطب النووي (M) ==========
N("med.nucmed", "الطب النووي: مقدمة", "Nuclear medicine: introduction", "med", 6, "core", 3, 35,
  prereqs=["rad.types", "nuc.halflife", "rad.dosimetry"],
  concepts=["مبدأ النظير المشع كدواء أو كاشف",
            "التشخيص مقابل العلاج", "اختيار النظير: نوع الإشعاع وعمر النصف والكيمياء",
            "مسار المستحضر في الجسم (pharmacokinetics)", "الجودة والصيدلة الإشعاعية"],
  apps=["التصوير الوظيفي", "العلاج الموجّه"],
  tags=["بوابة"])

N("med.imaging", "التصوير: SPECT وPET وSPECT/CT", "Imaging: SPECT, PET, hybrid", "med", 6, "core", 4, 50,
  prereqs=["med.nucmed", "rad.detectors", "meas.signal"],
  concepts=["كواشف غاما والكوليماتور والتصوير المقطعي بالإصدار",
            "PET والإصدار البوزيتروني والتصديق المتزامن (coincidence) وTOF",
            "التصحيحات: التوهين، التشتت، الزمن الميت، إعادة البناء",
            "الأنظمة الهجينة SPECT/CT وPET/CT وPET/MR",
            "مقاييس الجودة: الحساسية، الدقة، التباين"],
  eqs=["تخفيف: I = I₀ e^{-μx} وتصحيح التوهين", "SNR ∝ √(عدد العدّات)"],
  apps=["علم الأورام، القلب، الأعصاب"],
  tags=["مفتاح", "عملي"])

N("med.therapy", "العلاج الإشعاعي والعلاج بالنظائر", "Radiotherapy & radionuclide therapy",
  "med", 7, "core", 4, 55,
  prereqs=["rad.bio", "rad.dosimetry", "med.nucmed"],
  concepts=["العلاج الخارجي (LINAC, IMRT, VMAT, proton)",
            "المعالجة الكثبية (brachytherapy)",
            "العلاج بالنظائر المستهدفة (Lu-177 وAc-225 وRa-223 وI-131)",
            "مبادئ الجرعة والنمذجة الحيوية (BED, EUD)",
            "حساب الجرعة الداخلية (MIRD)"],
  eqs=["BED = nd(1 + d/(α/β))", "D = Ã × S (MIRD)"],
  apps=["علاج السرطان", "أمراض الغدة الدرقية", "تسكين آلام العظام"],
  tags=["مفتاح"])

N("med.isotopes", "إنتاج النظائر الطبية", "Medical isotope production", "med", 7, "core", 4, 40,
  prereqs=["nuc.reactions", "rx.research", "chem.radiochemistry"],
  concepts=["الإنتاج بالمفاعلات (n,γ) والانشطار (Mo-99)",
            "الإنتاج بالمسرعات (Cyclotron: F-18 وGa-68)",
            "المولّدات (Mo-99/Tc-99m، Ge-68/Ga-68، Ac-225/Bi-213)",
            "سلاسل التوريد والاضطرابات", "النظائر الناشئة: Ac-225 وLu-177 وTb-161 وCu-67"],
  apps=["تأمين الإمداد", "تطوير علاجات جديدة"],
  sources=["IAEA-TECDOC-2057", "McGuireWoods-2026"],
  tags=["مفتاح", "حديث"])

N("med.dosimetry_plan", "تخطيط الجرعات والفيزياء الطبية", "Treatment planning & medical physics",
  "med", 7, "specialized", 5, 50,
  prereqs=["med.therapy", "math.mc", "cs.data"],
  concepts=["خوارزميات حساب الجرعة (CCC، MC)",
            "تخطيط العلاج وتحسينه", "ضمان الجودة والمعايرة",
            "إدارة الحركة والتصوير الموجّه (IGRT)", "التحقق من الجرعة"],
  apps=["العمل كفيزيائي طبي", "بحث في الجرعات"],
  tags=["تخصصي", "عملي"])

N("med.rp", "الحماية الإشعاعية في المؤسسات الطبية", "Radiation protection in healthcare",
  "med", 7, "specialized", 3, 30,
  prereqs=["prot.principles", "med.nucmed"],
  concepts=["تصميم غرف النظائر والعلاج",
            "إدارة النفايات والمصادر", "جرعات المرضى والمرافقين",
            "حوادث التعرض والتعلم منها", "التدريب والترخيص"],
  apps=["برامج الحماية في المستشفيات"],
  tags=["تخصصي"])

# ================================================ التطبيقات الصناعية (N) =====
N("ind.ndt", "الفحص غير الإتلافي", "Non-destructive testing (NDT)", "ind", 6, "core", 3, 35,
  prereqs=["rad.transport", "ind.radiography"],
  concepts=["الراديوغرافي، فوق الصوتي، التيار الدوامي، الجسيمات، التصوير المقطعي الصناعي",
            "مقارنة الطرائق ومجالات استخدامها",
            "الجودة والمؤشرات (IQIs)"],
  apps=["اللحامات، الصب، الطيران، الأنابيب"],
  tags=["مفتاح"])

N("ind.radiography", "التصوير الإشعاعي الصناعي", "Industrial radiography", "ind", 6, "core", 3, 35,
  prereqs=["rad.sources", "rad.shielding", "prot.principles"],
  concepts=["مصادر غاما (Ir-192, Se-75, Co-60) وأنابيب الأشعة السينية",
            "التصوير بالأفلام والرقمي والتصوير المقطعي الصناعي",
            "جودة الصورة والتباين والضجيج",
            "السلامة: المنطقة المحظورة والدرع"],
  apps=["فحص اللحامات والسباكة", "مكافحة التهريب (حاويات)"],
  tags=["مفتاح", "عملي"])

N("ind.gauges", "القياسات النووية الصناعية", "Nuclear gauges & process measurements",
  "ind", 6, "supporting", 2, 25,
  prereqs=["rad.transport"],
  concepts=["قياس المستوى والكثافة والسماكة والرطوبة",
            "التوهين والانتشار العكسي", "مزاياها وقيودها"],
  apps=["الصناعات الورقية والصلب والأسمنت والنفط"],
  tags=["دعم"])

N("ind.tracers", "المتتبعات النظائرية الصناعية", "Industrial radiotracers", "ind", 6, "supporting", 3, 25,
  prereqs=["rad.detectors", "chem.isotope"],
  concepts=["اختيار المتتبع ومدة التجربة",
            "قياس التدفق والتسرب والتآكل", "نمذجة الاستجابة"],
  apps=["شبكات الأنابيب، الخزانات، التآكل"],
  tags=["دعم"])

N("ind.sterilization", "التعقيم الإشعاعي وحفظ الأغذية", "Radiation sterilization & food irradiation",
  "ind", 6, "supporting", 3, 25,
  prereqs=["rad.bio", "rad.dosimetry"],
  concepts=["جرعات التعقيم للأجهزة الطبية",
            "تشعيع الأغذية: الأهداف والجرعات والقبول",
            "كيمياء الأغذية المشععة", "اللوائح ووسم المنتجات"],
  apps=["التعقيم الصناعي", "الحجر الزراعي"],
  tags=["دعم"])

N("ind.activation_analysis", "تحليل المواد بالتنشيط", "Activation analysis of materials",
  "ind", 6, "specialized", 4, 30,
  prereqs=["rad.activation"],
  concepts=["NAA وPGNAA وتنشيط الجسيمات المشحونة",
            "تحليل أشباه الموصلات والمعادن", "التحليل في الموقع"],
  apps=["مراقبة الجودة", "الجيولوجيا", "الآثار"],
  tags=["تخصصي"])

N("ind.welllogging", "تسجيل الآبار النووي والجيوفيزياء", "Nuclear well logging", "ind", 6, "specialized", 3, 25,
  prereqs=["rad.detectors", "env.hydrology"],
  concepts=["قياس المسامية والكثافة والتكوين",
            "مصادر النيوترونات وغاما في الآبار", "السلامة في الحقول"],
  apps=["استكشاف النفط والغاز والمياه"],
  tags=["تخصصي"])

# ============================================== البيئة والزراعة (O) =========
N("env.tracers", "النظائر البيئية كمتتبعات", "Environmental isotopes as tracers", "env", 6, "core", 4, 40,
  prereqs=["chem.isotope", "rad.spectroscopy", "math.stat"],
  concepts=["النظائر المستقرة (O-18, D, C-13, N-15) والمشعة (H-3, C-14, Pb-210, Cs-137)",
            "التوقيع النظائري والتجزئة",
            "نماذج الخلط وصناديق الاختلاط", "أخذ العينات والتحليل"],
  eqs=["δ¹⁸O = [(R_sample/R_std) - 1] × 1000 ‰"],
  apps=["مصادر المياه والمسارات", "مصادر التلوث"],
  tags=["مفتاح"])

N("env.hydrology", "النظائر في الهيدرولوجيا والمياه", "Isotope hydrology", "env", 6, "specialized", 4, 40,
  prereqs=["env.tracers", "rx.fluids"],
  concepts=["دورة المياه وتوقيعاتها النظائرية",
            "التأريخ بالمياه الجوفية (H-3, C-14, Kr-81, Cl-36)",
            "تغذية المياه الجوفية والتفاعل مع الصخور", "نمذجة المستودعات"],
  apps=["إدارة المياه", "تقييم مواقع التخلص"],
  sources=["IAEA-NDS"],
  tags=["تخصصي"])

N("env.climate", "النظائر في الدراسات المناخية", "Isotopes in climate & paleo studies",
  "env", 7, "specialized", 4, 35,
  prereqs=["env.tracers", "env.dating"],
  concepts=["النظائر في الجليد والرواسب والكهوف",
            "مقاييس درجات الحرارة القديمة", "دورات الميلانكوفيتش",
            "النيوترونات الكوزموجينية (Be-10, C-14)"],
  apps=["إعادة بناء المناخ", "التحقق من النماذج"],
  tags=["تخصصي"])

N("env.dating", "التأريخ بالنظائر", "Radioisotope dating", "env", 6, "core", 3, 35,
  prereqs=["nuc.halflife", "meas.spectroscopy", "math.stat"],
  concepts=["الكربون-14 ومعايرته",
            "U-Pb وK-Ar وAr-Ar وRb-Sr",
            "التأريخ بالنيوكلويدات الكوزموجينية",
            "الافتراضات ومصادر الخطأ", "التقويم المعاير"],
  eqs=["t = (1/λ) ln(N₀/N)", "عمر C-14 = 5730 سنة"],
  apps=["الآثار والجيولوجيا والطب الشرعي"],
  tags=["مفتاح"])

N("env.radioecology", "الإيكولوجيا الإشعاعية", "Radioecology", "env", 6, "core", 4, 40,
  prereqs=["chem.envradio", "rad.bio"],
  concepts=["الانتقال في السلاسل الغذائية",
            "معاملات التركيز والانتقال", "التعرض للحيوانات والبشر",
            "نماذج التقييم (ERICA, RESRAD)", "المناطق الملوثة وإدارتها"],
  apps=["تقييم الأثر", "إدارة ما بعد الحوادث"],
  sources=["UNSCEAR"],
  tags=["مفتاح"])

N("env.dispersion", "انتشار المواد في الغلاف الجوي والماء", "Atmospheric & aquatic dispersion",
  "env", 6, "core", 4, 40,
  prereqs=["rx.fluids", "math.pde", "env.radioecology"],
  concepts=["معادلة النقل-الانتشار (advection-diffusion)",
            "نماذج الغاوسي واللاغرانجي",
            "الترسب الجاف والرطب", "نقل المياه السطحية والجوفية",
            "التحقق من النماذج والبيانات"],
  eqs=["∂C/∂t + u·∇C = ∇·(K∇C) - λC + S"],
  apps=["الاستجابة للطوارئ", "تقييم الأثر", "مراقبة المعاهدات"],
  tags=["مفتاح"])

N("env.agriculture", "التطبيقات الزراعية للنظائر والإشعاع", "Agricultural applications", "env", 6, "supporting", 3, 30,
  prereqs=["env.tracers", "rad.bio"],
  concepts=["تسميد النيتروجين-15 وقياس كفاءة الأسمدة",
            "تحسين المحاصيل بالتشعيع (mutation breeding)",
            "تقنية الحشرة العقيمة (SIT)", "إدارة المياه والتربة"],
  apps=["الأمن الغذائي", "المكافحة المتكاملة للآفات"],
  tags=["دعم"])

N("env.remediation", "معالجة المواقع الملوثة وإعادة تأهيلها", "Site remediation & restoration",
  "env", 7, "specialized", 4, 35,
  prereqs=["meas.monitoring", "env.radioecology", "fuel.decommissioning"],
  concepts=["توصيف الموقع ونموذج الحالة المفهومية",
            "خيارات المعالجة وإزالة التلوث",
            "إدارة النفايات الناتجة", "معايير التحرر والمراقبة اللاحقة",
            "المشاركة المجتمعية"],
  apps=["برامج التطهير", "إعادة استخدام الأراضي"],
  tags=["تخصصي"])
