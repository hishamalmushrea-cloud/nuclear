# -*- coding: utf-8 -*-
"""عقد هندسة المفاعلات (F) + دورة الوقود والنفايات (G) + المواد (P)."""
from .schema import N

# =============================================== هندسة المفاعلات (F) ========
N("rx.principles", "مبادئ المفاعل النووي", "Nuclear reactor principles", "rx", 5, "core", 3, 35,
  prereqs=["nuc.fission", "nuc.neutron"],
  concepts=["المكوّنات الأساسية: القلب، المبرد، المهدّئ، التحكم، الاحتواء",
            "التبريد مقابل التهدئة", "أنواع الوقود والهندسة", "توازن الطاقة"],
  apps=["فهم أي مفاعل من أي جيل"],
  sources=["Lamarsh"],
  tags=["بوابة"])

N("rx.neutroncycle", "دورة النيوترونات", "The neutron cycle", "rx", 5, "core", 4, 35,
  prereqs=["rx.principles"],
  concepts=["النيوترونات السريعة والتباطؤ", "الامتصاف الطفيلي والتسريب",
            "عامل التضاعف اللانهائي والفعال", "ميزان النيوترونات"],
  eqs=["k_∞ = η f p ε (أربعة عوامل)", "k_eff = k_∞ P_NL P_TNL (ستة عوامل)"],
  apps=["تفسير أثر أي تغيير في التصميم على الحرجية"],
  sources=["Lamarsh", "Duderstadt"],
  tags=["مفتاح"])

N("rx.chain", "التفاعل المتسلسل", "Chain reaction", "rx", 5, "core", 3, 20,
  prereqs=["nuc.fission", "nuc.neutron"],
  concepts=["النيوترونات الفورية والمتأخرة", "الجيل الواحد وزمن الجيل",
            "التفاعل المتسلسل المستدام والخامد والمفرط"],
  eqs=["N_{n+1} = k N_n"],
  apps=["أساس التحكم في المفاعل"],
  tags=["مفتاح"])

N("rx.criticality", "الحرجية والأنظمة دون/فوق الحرجة", "Criticality", "rx", 5, "core", 4, 40,
  prereqs=["rx.neutroncycle", "rx.chain"],
  concepts=["k_eff والسموم والتفاعلية ρ", "الكتلة الحرجة ومعاملات هندسية",
            "الأنظمة دون الحرجة والأنظمة المدفوعة",
            "هامش التفاعلية والإيقاف البارد"],
  eqs=["ρ = (k-1)/k", "بuckling هندسي = buckling مادي"],
  apps=["سلامة التخزين والنقل", "تصميم القلب", "نقدية العمليات"],
  sources=["Duderstadt", "IAEA-NDS"],
  tags=["مفتاح", "جوهري"])

N("rx.kinetics", "حركية المفاعل", "Reactor kinetics", "rx", 6, "core", 4, 50,
  prereqs=["rx.criticality", "math.ode", "cs.numpy"],
  concepts=["حركية النقطة مع ست مجموعات متأخرة",
            "زمن الجيل المطوّل ومعامل الدولارات",
            "خطوة التفاعلية واستجابة القفزة", "تسمم الزينون والساماريوم"],
  eqs=["dn/dt = (ρ-β)/Λ n + Σ λ_i C_i",
       "dC_i/dt = β_i n/Λ - λ_i C_i",
       "ρ ≈ (β_eff - β)/β (دولار)"],
  apps=["بدء التشغيل والإيقاف", "مناورة القدرة", "تحليل الحوادث"],
  sources=["Duderstadt", "Stacey"],
  tags=["مفتاح", "جوهري"])

N("rx.control", "التحكم في المفاعل", "Reactor control", "rx", 6, "core", 4, 40,
  prereqs=["rx.kinetics"],
  concepts=["قضبان التحكم وقيمتها", "السموم القابلة للاحتراق والسموم الكيميائية",
            "تتبع الحمل والمناورة", "أنظمة الحماية والإيقاف السريع (SCRAM)",
            "معاملات التفاعلية (درجة الحرارة، الفراغ)"],
  eqs=["α_T = dρ/dT", "قيمة القضيب ρ_worth"],
  apps=["تشغيل آمن", "تصميم أنظمة التحكم"],
  sources=["Lamarsh", "Stacey"],
  tags=["مفتاح"])

N("rx.diffusion", "نظرية انتشار النيوترونات", "Neutron diffusion theory", "rx", 6, "core", 4, 45,
  prereqs=["nuc.neutron", "math.pde", "math.vectors"],
  concepts=["قانون فيك للنيوترونات", "معادلة الانتشار والشرط الحدّي",
            "طول الانتشار والbuckling", "حلول لقلب بسيط"],
  eqs=["-D∇²φ + Σ_a φ = S", "L = √(D/Σ_a)"],
  apps=["حساب توزيع الفيض في القلب", "تقدير التسريب"],
  sources=["Duderstadt", "Stacey"],
  tags=["مفتاح"])

N("rx.transport", "معادلة الانتقال والطرائق العددية", "Transport equation & numerical methods",
  "rx", 6, "core", 5, 60,
  prereqs=["rx.diffusion", "math.mc", "nuc.data"],
  concepts=["معادلة بولتزمان للانتقال (الزمن، الزاوية، الطاقة، المكان)",
            "طرق S_N و P_N وطريقة التصادمات",
            "مونتي كارلو للأنظمة المستمرة والمتعددة المجموعات",
            "تجميع المجموعات والتماثل", "التقارب والإحصاء"],
  eqs=["(1/v)∂ψ/∂t + Ω·∇ψ + Σ_t ψ = ∫Σ_s ψ' dΩ' dE' + S",
       "σ_relative ≈ 1/√N"],
  apps=["كل حسابات النيوترونيات الحديثة", "تدريع، حرجية، مخزون", "تحليل الكواشف"],
  sources=["Duderstadt", "Stacey"],
  tags=["مفتاح", "متقدم"])

N("rx.heat", "انتقال الحرارة", "Heat transfer", "rx", 5, "core", 4, 55,
  prereqs=["math.pde", "phys.thermo"],
  concepts=["التوصيل والحمل والإشعاع",
            "التوصيل في الوقود ذي التوليد الداخلي",
            "الحمل القسري والطبيعي ومعاملات الانتقال",
            "الغليان وأزمة الغليان (CHF/DNB)", "المبادلات الحرارية"],
  eqs=["q'' = -k ∇T (قانون فورييه)", "Nu = f(Re, Pr)", "DNBR = q''_CHF / q''_عامل"],
  apps=["تبريد الوقود", "تصميم المبادلات", "هوامش الأمان الحراري"],
  sources=["Cengel", "Todreas"],
  tags=["مفتاح", "جوهري"])

N("rx.fluids", "ميكانيكا الموائع", "Fluid mechanics", "rx", 5, "core", 4, 50,
  prereqs=["math.pde", "phys.mech"],
  concepts=["معادلات نافييه-ستوكس والاستمرارية",
            "فقد الضغط والاحتكاك", "الجريان المضغوط وغير المضغوط",
            "الجريان ثنائي الطور", "الدوران الطبيعي"],
  eqs=["ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + ρg"],
  apps=["تبريد القلب", "تحليل فقد المبرد (LOCA)", "مضخات وأنابيب"],
  sources=["White-Fluid", "Todreas"],
  tags=["مفتاح"])

N("rx.thermalhyd", "الحراريات المائية للمفاعلات", "Reactor thermal-hydraulics", "rx", 6, "core", 5, 55,
  prereqs=["rx.heat", "rx.fluids"],
  concepts=["قنوات الوقود وتوزيع التدفق",
            "الجريان ثنائي الطور والفراغ", "أزمة الغليان ونسبة DNBR",
            "الدوران الطبيعي والتبريد السلبي", "الاستقرار الحراري المائي"],
  eqs=["DNBR = q''_CHF / q''_عمل", "ΔP = f(L/D)(ρv²/2)"],
  apps=["ترخيص التصميم", "تحليل الحوادث", "تحسين الأداء"],
  sources=["Todreas", "NUREG-0800"],
  tags=["مفتاح", "جوهري"])

N("rx.thermo_power", "الديناميكا الحرارية لمحطات القدرة", "Power-plant thermodynamics",
  "rx", 5, "supporting", 3, 40,
  prereqs=["phys.thermo"],
  concepts=["دورة رانكن والبخار", "إعادة التسخين والتسخين المسبق",
            "دورات الغاز وبرايتون", "الكفاءة والحدود العملية"],
  eqs=["η_th = W_net/Q_in", "η_حد أقصى كارنو"],
  apps=["تقييم أداء المحطات", "مقارنة تقنيات المفاعلات", "الاقتران مع التحلية/الحرارة الصناعية"],
  tags=["دعم"])

N("rx.cooling", "أنظمة التبريد وأنواع المبردات", "Cooling systems & coolants", "rx", 6, "core", 4, 35,
  prereqs=["rx.thermalhyd"],
  concepts=["الماء الخفيف والثقيل", "الغاز (He, CO₂)", "الصوديوم والرصاص والبيسموت",
            "الأملاح المنصهرة", "المصرف النهائي للحرارة (ultimate heat sink)"],
  apps=["اختيار تقنية المفاعل", "تحليل السلامة"],
  tags=["مفتاح"])

N("rx.fuel", "وقود المفاعلات", "Reactor fuel", "rx", 6, "core", 4, 40,
  prereqs=["rx.principles", "mat.intro"],
  concepts=["UO₂ والوقود المعدني وTRISO وMOX",
            "التخصيب ومفهوم الحرق (burnup)",
            "تغليف الوقود وتفاعلات الغلاف", "سلوك الغازات الانشطارية"],
  eqs=["حرق: MWd/kgU", "الاستهلاك والتحويل (breeding ratio)"],
  apps=["تصميم الوقود", "تحليل دورة الحياة"],
  sources=["Lamarsh", "Todreas"],
  tags=["مفتاح"])

N("rx.materials", "مواد المفاعلات", "Reactor materials", "rx", 6, "core", 4, 40,
  prereqs=["mat.intro", "mat.damage"],
  concepts=["الغلاف (Zircaloy) والسبائك المتقدمة",
            "الفولاذات وأوعية الضغط", "الخرسانة والجرافيت",
            "معايير التصميم الميكانيكي (ASME)", "التقادم وإدارة الحياة"],
  apps=["تصميم المكونات", "تمديد العمر", "تحليل السلامة"],
  sources=["Was", "NRL-Materials"],
  tags=["مفتاح"])

N("rx.instr", "أنظمة القياس والتحكم (I&C)", "Instrumentation & control", "rx", 6, "core", 4, 45,
  prereqs=["meas.detectors", "rx.kinetics", "phys.em"],
  concepts=["قياس الفيض والقدرة (مجاميع النيوترونات)",
            "قياس الحرارة والضغط والتدفق", "أنظمة الحماية والتشابكات",
            "التحكم الرقمي والأمن السيبراني", "الموثوقية والتكرار"],
  apps=["تشغيل المفاعل", "السلامة الوظيفية", "التحديث الرقمي"],
  tags=["مفتاح", "غالباً يُنسى"])

N("rx.types", "أنواع المفاعلات", "Reactor types", "rx", 5, "core", 3, 45,
  prereqs=["rx.principles"],
  concepts=["PWR وBWR وPHWR (CANDU)",
            "HTGR وRBMK وLWGR", "المفاعلات السريعة (SFR, LFR)",
            "مفاعلات الأملاح المنصهرة", "المفاعلات البحثية والمجمّعات"],
  apps=["اختيار السياق التكنولوجي", "قراءة الأدبيات"],
  sources=["Lamarsh", "IAEA-PRIS"],
  tags=["مفتاح"])

N("rx.research", "المفاعلات البحثية واستخداماتها", "Research reactors & their uses",
  "rx", 6, "supporting", 3, 30,
  prereqs=["rx.types"],
  concepts=["المفاعلات من نوع حوض ومجمع ومفاعلات تدفق",
            "إنتاج النظائر", "التنشيط النيوتروني",
            "حيود النيوترونات", "تحليل المواد وتجارب التشعيع"],
  apps=["الطب والصناعة والبحث", "تدريب الكوادر"],
  tags=["دعم"])

N("rx.power", "مفاعلات القدرة: الجيل الثاني والثالث", "Power reactors: Gen II & Gen III/III+",
  "rx", 6, "core", 4, 45,
  prereqs=["rx.types", "rx.thermalhyd", "safe.did"],
  concepts=["الأنظمة السلبية والنشطة", "الاحتواء المزدوج ومصائد الحطام",
            "مفاعلات الماء المضغوط والمغلي المتقدمة", "السلامة بعد فوكوشيما"],
  apps=["فهم الأسطول الحالي", "تقييم المشاريع الجديدة"],
  sources=["IAEA-SSR2/1", "NUREG-0800"],
  tags=["مفتاح"])

N("rx.gen4", "المفاعلات المتقدمة والجيل الرابع", "Advanced reactors & Gen-IV", "rx", 6, "advanced", 5, 50,
  prereqs=["rx.types", "rx.fuel", "mat.hightemp"],
  concepts=["أهداف الجيل الرابع (استدامة، اقتصاد، سلامة، مقاومة انتشار)",
            "ستة مفاهيم: SFR, LFR, GFR, VHTR, SCWR, MSR",
            "الوقود عالي التحمل (ATF) و HALEU", "التحديات التنظيمية والاقتصادية"],
  apps=["تقييم التقنيات الناشئة", "قراءة تقارير GIF"],
  sources=["Stacey", "SMR-Intel-2026"],
  tags=["متقدم"])

N("rx.smr", "المفاعلات الصغيرة والمعيارية والميكروية", "SMRs, modular & microreactors",
  "rx", 6, "advanced", 4, 40,
  prereqs=["rx.gen4", "safe.did", "pol.regulatory"],
  concepts=["تعريف SMR وmicroreactor", "التصنيع المعياري والمصنعي",
            "السلامة بالتصميم والأنظمة السلبية", "اقتصاديات الوحدة الأولى FOAK مقابل NOAK",
            "الترخيص للمصنع المتعدد"],
  apps=["قراءة السوق الحالي", "تحليل المشاريع"],
  sources=["SMR-Intel-2026", "IAEA-PRIS"],
  tags=["متقدم", "حديث"])

N("rx.core", "تصميم القلب وإدارة الوقود", "Core design & fuel management", "rx", 6, "advanced", 5, 50,
  prereqs=["rx.transport", "rx.thermalhyd", "rx.fuel"],
  concepts=["نماذج إعادة التحميل (out-in, low-leakage)",
            "توزيع الطاقة وعوامل الذروة", "الحرق وتراكم السموم",
            "تحسين التحميل", "القيود الحرارية والنيوترونية"],
  apps=["تخطيط الدورة التشغيلية", "التحسين الاقتصادي"],
  sources=["Stacey", "Todreas"],
  tags=["متقدم"])

N("rx.multiphysics", "المحاكاة متعددة الفيزياء", "Multiphysics simulation", "rx", 6, "advanced", 5, 50,
  prereqs=["rx.transport", "rx.thermalhyd", "mat.fuels", "cs.vv"],
  concepts=["اقتران النيوترونيات بالحراريات المائية والهيكل والوقود",
            "الأنماط: Picard وJacobian-Free Newton-Krylov",
            "المقاييس الزمنية والمكانية", "التحقق والمعايير المرجعية"],
  apps=["محاكاة دقيقة للقلب", "تحليل الحوادث"],
  sources=["ArXiv-GenIV-DT", "Stacey"],
  tags=["متقدم", "حديث"])

N("rx.economics", "اقتصاديات الطاقة النووية", "Nuclear energy economics", "rx", 6, "supporting", 3, 35,
  prereqs=["rx.thermo_power", "math.stat"],
  concepts=["CAPEX وOPEX وLCOE", "مخاطر الوحدة الأولى وتكلفة رأس المال",
            "أثر التنظيم والجدولة", "مقارنة بمصادر أخرى", "القيمة المرنة والحرارة"],
  apps=["تقييم الجدوى", "قراءة تقارير الطاقة"],
  sources=["SMR-Intel-2026", "GRS-2026"],
  tags=["دعم", "غالباً يُنسى"])

# ============================================ دورة الوقود والنفايات (G) ======
N("fuel.intro", "دورة الوقود النووي: نظرة شاملة", "The nuclear fuel cycle: overview",
  "fuel", 5, "core", 3, 35,
  prereqs=["nuc.fission", "chem.inorganic"],
  concepts=["الدورة المفتوحة والمغلقة", "الواجهة الأمامية والخلفية",
            "مخزون المواد الانشطارية", "مفهوم الاستدامة والجيل الرابع"],
  apps=["قراءة السياسات النووية", "تقييم خيارات الدول"],
  sources=["WorldNuclear", "IAEA-PRIS"],
  tags=["مفتاح"])

N("fuel.resources", "مصادر المواد النووية", "Nuclear material resources", "fuel", 5, "supporting", 2, 25,
  prereqs=["fuel.intro", "chem.inorganic"],
  concepts=["جيولوجيا اليورانيوم والثوريوم",
            "الاحتياطيات والموارد (Red Book)", "الاستخلاص والمعالجة",
            "المصادر غير التقليدية (البحر، الفوسفات)"],
  apps=["تقييم أمن الإمداد", "النقاشات السياسية"],
  sources=["WorldNuclear"],
  tags=["دعم"])

N("fuel.fabrication", "تحويل وتخصيب وتصنيع الوقود", "Conversion, enrichment & fuel fabrication",
  "fuel", 5, "supporting", 4, 35,
  prereqs=["fuel.resources", "chem.isotope"],
  concepts=["تحويل U₃O₈ إلى UF₆",
            "التخصيب كمفهوم فيزيائي وعملي: فصل النظائر، وحدات العمل SWU",
            "تصنيع الحبيبات والقضبان والمجمّعات",
            "الوقود المتقدم: HALEU و TRISO و MOX",
            "الضمانات والقياسات أثناء التصنيع"],
  eqs=["V(x_p) = (2x_p - 1) ln(x_p/(1-x_p))"],
  apps=["قراءة تقارير سلسلة الإمداد", "فهم قيود HALEU"],
  sources=["WorldNuclear", "SMR-Intel-2026"],
  tags=["دعم", "حساس - معالجة أكاديمية وصفية"])

N("fuel.inreactor", "أداء الوقود داخل المفاعل", "In-reactor fuel performance", "fuel", 6, "advanced", 5, 45,
  prereqs=["rx.fuel", "mat.damage", "rx.thermalhyd"],
  concepts=["درجات حرارة الوقود وهيكل الحبيبات",
            "الانتفاخ والزحف وإطلاق الغازات الانشطارية",
            "تفاعل الغلاف مع الوقود (PCI) والهدرجة",
            "سلوك الوقود في الحوادث", "نمذجة الأداء (BISON)"],
  apps=["تحديد حدود التشغيل", "تقييم الوقود المتسامح مع الحوادث ATF"],
  sources=["Todreas", "NRL-Materials"],
  tags=["متقدم", "بحثي"])

N("fuel.spent", "الوقود المستهلك", "Spent nuclear fuel", "fuel", 6, "core", 4, 35,
  prereqs=["fuel.intro", "nuc.series"],
  concepts=["المخزون النويدي: الأكتينيدات ونواتج الانشطار",
            "الحرارة المتحللة والنشاط المتبقي", "الحرق والتبريد",
            "الخصائص الإشعاعية والحرارية"],
  eqs=["P_decay ≈ 0.066 P₀ [t^{-0.2} - (t+t₀)^{-0.2}]"],
  apps=["تصميم أحواض التبريد والتخزين الجاف", "تصميم المستودعات", "نقل الوقود"],
  tags=["مفتاح"])

N("fuel.storage", "التخزين المؤقت: الرطب والجاف", "Interim storage: wet & dry", "fuel", 6, "core", 3, 30,
  prereqs=["fuel.spent", "rad.shielding"],
  concepts=["أحواض الوقود المستهلك", "الحاويات الجافة والخرسانة",
            "التبريد السلبي والمراقبة", "التمديد طويل الأمد وتقادم المواد"],
  apps=["إدارة المواقع", "السلامة التشغيلية"],
  tags=["مفتاح"])

N("fuel.reprocessing", "إعادة المعالجة: مفهوم علمي وسياساتي", "Reprocessing: science & policy",
  "fuel", 7, "advanced", 4, 40,
  prereqs=["fuel.spent", "chem.radiochemistry", "sec.nonprolif"],
  concepts=["فصل البلوتونيوم واليورانيوم: مبادئ كيميائية عامة (PUREX كمفهوم)",
            "المعالجة البيروميتالورجية", "التقسيم والتحويل (partitioning & transmutation)",
            "الجوانب الاقتصادية وسياسات عدم الانتشار", "خيارات الدول المختلفة"],
  apps=["فهم النقاش السياسي", "تقييم خيارات الدورة المغلقة"],
  sources=["Choppin", "WorldNuclear"],
  tags=["حساس - معالجة وصفية وسياساتية", "متقدم"])

N("fuel.waste", "إدارة النفايات المشعة", "Radioactive waste management", "fuel", 6, "core", 4, 45,
  prereqs=["fuel.spent", "rad.types", "pol.regulatory"],
  concepts=["تصنيف النفايات: منخفضة/متوسطة/عالية المستوى",
            "التقليل والمعالجة والتكييف (vitrification, cementation)",
            "التخزين والتخلص", "المسؤولية والتمويل", "القبول المجتمعي"],
  apps=["السياسات الوطنية", "إدارة المواقع"],
  sources=["IAEA-SF1", "STUK-Onkalo"],
  tags=["مفتاح"])

N("fuel.disposal", "التخلص النهائي الجيولوجي", "Geological disposal", "fuel", 6, "advanced", 5, 45,
  prereqs=["fuel.waste", "chem.envradio", "env.hydrology"],
  concepts=["مبدأ الحواجز المتعددة ( engineered + natural)",
            "السلامة على مدى 10⁴–10⁵ سنة", "النمذجة والسيناريوهات",
            "حالة Onkalo/فنلندا وأمثلة أخرى", "المراقبة وإمكانية الاسترجاع"],
  apps=["تقييم برامج التخلص", "فهم تاريخ الموافقات التنظيمية"],
  sources=["STUK-Onkalo", "IAEA-SF1"],
  tags=["متقدم", "حديث"])

N("fuel.transport", "نقل المواد المشعة", "Transport of radioactive material", "fuel", 6, "supporting", 3, 25,
  prereqs=["rad.shielding", "pol.regulatory"],
  concepts=["لوائح النقل (IAEA SSR-6)", "تصنيف الطرود واختباراتها",
            "الحاويات والوقود المستهلك", "الطوارئ أثناء النقل"],
  apps=["اللوجستيات النووية", "الامتثال التنظيمي"],
  tags=["دعم"])

N("fuel.decommissioning", "تفكيك المنشآت وإزالة التخصيص", "Decommissioning & decommissioning planning",
  "fuel", 6, "specialized", 4, 40,
  prereqs=["fuel.waste", "meas.monitoring", "safe.systems"],
  concepts=["استراتيجيات: الإزالة الفورية، التأجيل الآمن، الدفن في الموقع",
            "المسح الإشعاعي وتوصيف الموقع", "إزالة التلوث والقطع عن بُعد",
            "إدارة النفايات الناتجة", "التكلفة والتمويل"],
  apps=["تخطيط نهاية العمر", "إدارة المواقع التاريخية"],
  tags=["تخصصي", "غالباً يُنسى"])

# ======================================================= المواد (P) =========
N("mat.intro", "المواد النووية: مقدمة", "Introduction to nuclear materials", "mat", 5, "core", 3, 30,
  prereqs=["phys.condmat", "chem.materials"],
  concepts=["لماذا المواد في المفاعل بيئة قاسية",
            "درجة الحرارة، الإشعاع، الإجهاد، التآكل",
            "مؤشرات الأداء (dpa, appm He)", "المواد الهيكلية والوقود"],
  apps=["بوابة لمسار المواد"],
  sources=["Was"],
  tags=["بوابة"])

N("mat.damage", "التلف الإشعاعي", "Radiation damage in materials", "mat", 6, "core", 5, 50,
  prereqs=["mat.intro", "rad.interaction", "phys.condmat"],
  concepts=["تسلسل الاصطدام وشلالات الإزاحة (Norgett-Robinson-Torrens)",
            "dpa والعيوب النقطية والتجمعات",
            "الانتفاخ والزحف الإشعاعي والتقصف", "إنتاج الهيليوم والهيدروجين عبر (n,α) و(n,p)",
            "التأثيرات على الخواص الميكانيكية"],
  eqs=["N_d = 0.8 E_DPA/(2E_d)", "dpa = Φ σ_d t"],
  apps=["تحديد عمر المكونات", "اختيار مواد المفاعلات والاندماج"],
  sources=["Was"],
  tags=["مفتاح", "جوهري"])

N("mat.metals", "المعادن والسبائك النووية", "Metals & nuclear alloys", "mat", 6, "supporting", 4, 40,
  prereqs=["mat.intro"],
  concepts=["الفولاذات المقاومة للزحف والفولاذات الأوستنيتية",
            "سبائك الزركونيوم", "سبائك الألمنيوم للمفاعلات البحثية",
            "الفولاذات المخففة التنشيط (RAFM)",
            "المعالجة الحرارية والبنية المجهرية"],
  apps=["أنابيب الغلاف وأوعية الضغط", "مكونات الاندماج"],
  tags=["دعم"])

N("mat.ceramics", "السيراميك والوقود السيراميكي", "Ceramics & ceramic fuels", "mat", 6, "supporting", 4, 35,
  prereqs=["mat.intro", "chem.materials"],
  concepts=["UO₂ والنتريد والكربيد", "السيراميك كحواجز (SiC, TiC)",
            "التلبيد والبنية الحبيبية", "التوصيل الحراري وتأثير الحرق"],
  apps=["الوقود وطلاءات TRISO", "حواجز النفايات"],
  tags=["دعم"])

N("mat.composites", "المواد المركّبة (SiC/SiC وC/C)", "Composites (SiC/SiC, C/C)", "mat", 6, "specialized", 4, 30,
  prereqs=["mat.ceramics"],
  concepts=["ألياف وواجهات ومصفوفة", "سلوك تحت الإشعاع",
            "تطبيقات الغلاف والقنوات", "تحديات التصنيع والربط"],
  apps=["الوقود المتسامح مع الحوادث", "مكونات درجات الحرارة العالية"],
  tags=["تخصصي"])

N("mat.hightemp", "مواد درجات الحرارة العالية", "High-temperature materials", "mat", 6, "specialized", 4, 30,
  prereqs=["mat.metals", "mat.ceramics"],
  concepts=["الزحف والتعب الحراري", "الأكسدة والكربنة",
            "السبائك فائقة القوة والمركبات", "القيود في المفاعلات المتقدمة"],
  apps=["VHTR وMSR والاندماج"],
  tags=["تخصصي"])

N("mat.corrosion", "التآكل والتعب والتشقق", "Corrosion, fatigue & cracking", "mat", 6, "core", 4, 40,
  prereqs=["mat.metals", "chem.phys"],
  concepts=["التآكل العام والموضعي والتشقق تحت الإجهاد (SCC)",
            "التعب الدوري والحراري", "كيمياء الماء في المفاعل",
            "تأثير الإشعاع على التآكل", "المراقبة والتفتيش"],
  apps=["إدارة التقادم", "تقييم العمر المتبقي"],
  sources=["Was"],
  tags=["مفتاح"])

N("mat.lifetime", "العمر الافتراضي والموثوقية", "Lifetime & reliability engineering", "mat", 6, "core", 4, 35,
  prereqs=["mat.damage", "mat.corrosion", "safe.human"],
  concepts=["إدارة التقادم وإدارة الحياة",
            "الإحصاء في الموثوقية (Weibull، معدلات الفشل)",
            "التفتيش في الخدمة والاختبار غير الإتلافي", "تمديد الترخيص"],
  apps=["تمديد عمر المحطات", "إدارة الأصول"],
  tags=["مفتاح", "غالباً يُنسى"])

N("mat.characterization", "توصيف المواد", "Materials characterization", "mat", 6, "specialized", 4, 40,
  prereqs=["phys.condmat", "meas.spectroscopy"],
  concepts=["المجهر الإلكتروني (SEM/TEM) و EBSD",
            "مسبار الليزر الذري (APT)", "حيود الأشعة السينية والنيوترونات",
            "التحليل الميكانيكي مصغّراً", "تحديات المواد المشعة (خلايا ساخنة)"],
  apps=["البحث في المواد", "تحليل العينات المشععة"],
  tags=["تخصصي", "عملي"])

N("mat.fuels", "مواد الوقود المتقدمة", "Advanced fuel materials", "mat", 6, "advanced", 5, 40,
  prereqs=["mat.ceramics", "rx.fuel"],
  concepts=["TRISO (وقود متعدد الطبقات)",
            "الوقود المعدني والنتريدي", "الوقود المتسامح مع الحوادث ATF (Cr-coated cladding, FeCrAl, SiC)",
            "الوقود عالي التخصيب منخفض التخصيب HALEU",
            "سلوك الوقود في ظروف الحوادث"],
  apps=["مفاعلات الجيل الرابع وSMR", "تحسين السلامة"],
  sources=["SMR-Intel-2026", "Stacey"],
  tags=["متقدم", "حديث"])
