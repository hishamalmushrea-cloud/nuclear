# -*- coding: utf-8 -*-
"""عقد المجالات التي اكتشفها الفريق بنفسه (X.12 وما بعده) — قائمة مفتوحة تتوسع."""
from .schema import N

N("disc.neutronimaging", "تصوير النيوترونات", "Neutron imaging", "disc", 8, "specialized", 4, 25,
  prereqs=["nuc.neutronsci", "rad.detectors"],
  concepts=["التباين المختلف عن الأشعة السينية (العناصر الخفيفة)",
            "التصوير المقطعي النيوتروني والطنيني",
            "تصوير الوقود والمواد والآلات", "القيود والحجم"],
  apps=["مراقبة غير إتلافية", "بحث المواد"],
  tags=["مكتشف"])

N("disc.ads", "الأنظمة المدفوعة بالمسرعات (ADS)", "Accelerator-driven systems", "disc", 8, "advanced", 5, 30,
  prereqs=["part.accel", "rx.criticality", "fuel.reprocessing"],
  concepts=["الأنظمة دون الحرجة المدفوعة بمصدر نيوترونات خارجي",
            "k_eff < 1 ومكاسب المصدر",
            "التحويل (transmutation) كمفهوم",
            "التحديات: موثوقية المسرع ونافذة الشعاع"],
  apps=["دراسات دورة الوقود", "مصادر نيوترونات قوية"],
  tags=["مكتشف", "متقدم"])

N("disc.transmutation", "التحويل النووي للأكتينيدات الثانوية", "Transmutation of minor actinides",
  "disc", 8, "advanced", 5, 30,
  prereqs=["fuel.reprocessing", "nuc.reactions"],
  concepts=["مخزون الأكتينيدات الثانوية وطويلة العمر",
            "التحويل بالنيوترونات السريعة أو المدفوعة",
            "أثره على المستودع الجيولوجي", "الاقتصاد والتقنية"],
  apps=["أبحاث دورة الوقود المتقدمة"],
  tags=["مكتشف", "بحثي"])

N("disc.theranostics", "الثيرانوستكس (تشخيص+علاج بنظيرين)", "Theranostics", "disc", 9, "advanced", 4, 30,
  prereqs=["med.isotopes", "med.therapy", "med.imaging"],
  concepts=["الزوج التشخيصي/العلاجي (مثل Ga-68/Lu-177 وTb-155/Tb-161)",
            "الطب الشخصي والجرعات الفردية",
            "سلاسل توريد النظائر الناشئة (Ac-225)", "التحديات التنظيمية"],
  apps=["تطوير أدوية مشعة", "تحليل السوق الصحي"],
  sources=["McGuireWoods-2026", "IAEA-TECDOC-2057"],
  tags=["مكتشف", "حديث"])

N("disc.space", "الطاقة النووية الفضائية", "Space nuclear power & propulsion", "disc", 9, "specialized", 4, 30,
  prereqs=["rx.types", "nuc.decay"],
  concepts=["مولدات النظائر الحرارية (RTG) ومبادئها",
            "مفاعلات الانشطار الفضائية (كيلوباور ونظائرها)",
            "الدفع النووي الحراري والكهربائي",
            "السلامة عند الإطلاق وإعادة الدخول"],
  apps=["بعثات الفضاء العميق", "الطاقة على القمر والمريخ"],
  tags=["مكتشف"])

N("disc.hydrogen", "الهيدروجين والحرارة الصناعية النووية", "Nuclear hydrogen & industrial heat",
  "disc", 8, "advanced", 4, 30,
  prereqs=["rx.thermo_power", "rx.gen4", "chem.phys"],
  concepts=["التحليل الكهربائي عالي الحرارة والدورات الكيميائية الحرارية (S-I وCu-Cl)",
            "الحرارة الصناعية عالية الدرجة وتطبيقاتها",
            "الاقتران مع المفاعلات عالية الحرارة", "الاقتصاد والبنية التحتية"],
  apps=["إزالة الكربون الصناعي", "الأسمدة والصلب"],
  tags=["مكتشف", "حديث"])

N("disc.desal", "التحلية النووية", "Nuclear desalination", "disc", 8, "supporting", 3, 20,
  prereqs=["rx.thermo_power", "rx.economics"],
  concepts=["التقطير متعدد التأثير والتناضح العكسي",
            "الاقتران الحراري والكهربائي",
            "الاعتبارات الاقتصادية والبيئية", "الخبرة الدولية"],
  apps=["المياه في المناطق الجافة"],
  tags=["مكتشف"])

N("disc.digitaltwin", "التوأم الرقمي للمفاعلات", "Digital twins for nuclear systems", "disc", 9, "advanced", 5, 35,
  prereqs=["rx.multiphysics", "cs.vv", "rx.instr"],
  concepts=["مكوّنات التوأم: نموذج فيزيائي + بيانات + تحديث بايزي",
            "النماذج البديلة (surrogates) والتعلم العميق العامل (DeepONet)",
            "التحكم الصحي-الواعي والصيانة التنبؤية",
            "القبول الرقابي للتوأم الرقمي", "أمثلة بحثية حديثة"],
  apps=["الصيانة التنبؤية", "التحكم المتقدم", "التدريب"],
  sources=["Nature-SciRep-DT", "ArXiv-GenIV-DT"],
  tags=["مكتشف", "حديث", "بحثي"])

N("disc.ml_nuclear", "تعلم الآلة في العلوم النووية", "Machine learning in nuclear science",
  "disc", 8, "advanced", 5, 40,
  prereqs=["cs.uq", "nuc.data", "cs.numpy"],
  concepts=["النماذج البديلة والتعلم الفيزيائي-الموجّه (PINN)",
            "الاكتشاف في بيانات المقاطع العرضية وتقييم البيانات",
            "تحليل صور الكواشف والطيف", "القلق: الانجراف خارج توزيع التدريب",
            "V&V للنماذج المعتمدة على البيانات"],
  apps=["تسريع المحاكاة", "تحليل البيانات الضخمة"],
  sources=["ArXiv-Nucl", "ArXiv-GenIV-DT"],
  tags=["مكتشف", "حديث", "بحثي"])

N("disc.advancedmanufacturing", "التصنيع المتقدم للمكونات النووية", "Advanced manufacturing (AM) for nuclear",
  "disc", 8, "advanced", 4, 30,
  prereqs=["mat.metals", "mat.characterization"],
  concepts=["الطباعة ثلاثية الأبعاد للمعادن والسيراميك",
            "المؤهل والاعتماد (qualification) للمكونات النووية",
            "المسامية والبنية المجهرية والتشطيب", "التحديات التنظيمية"],
  apps=["قطع الغيار", "المكونات المعقدة", "تقليل المهل"],
  tags=["مكتشف"])

N("disc.quantum", "الحوسبة والاستشعار الكمومي في المجال النووي", "Quantum computing & sensing in nuclear science",
  "disc", 9, "research", 5, 30,
  prereqs=["phys.qm2", "cs.uq", "rx.transport"],
  concepts=["خوارزميات كمومية لمسائل القيم الذاتية والأنظمة الخطية",
            "محاكاة النظم النووية ذات عدة أجسام",
            "الاستشعار الكمومي للمجالات والجرعات",
            "الواقع الحالي مقابل الوعود"],
  apps=["بحث متقدم", "تقييم الوعود التقنية"],
  tags=["مكتشف", "بحثي", "ناشئ"])

N("disc.microreactors", "المفاعلات الميكروية والتطبيقات غير الكهربائية",
  "Microreactors & non-electric applications", "disc", 8, "advanced", 4, 25,
  prereqs=["rx.smr", "rx.cooling"],
  concepts=["مفاعلات <20 MWe للمنشآت النائية والقواعد",
            "التشغيل المستقل والأتمتة", "الأمن والحماية المادية",
            "الحرارة الصناعية والدفاع والمجتمعات النائية"],
  apps=["تخطيط الطاقة", "تقييم حالات الاستخدام"],
  sources=["SMR-Intel-2026"],
  tags=["مكتشف", "حديث"])

N("disc.nuclear_analytics", "التحليلات النووية للبيانات الضخمة والمراقبة",
  "Nuclear analytics & monitoring networks", "disc", 8, "specialized", 4, 25,
  prereqs=["env.dispersion", "meas.monitoring", "cs.data"],
  concepts=["شبكات المراقبة الإشعاعية واستيعاب البيانات",
            "الكشف عن الشذوذ والتوطين العكسي للمصدر",
            "دمج قياسات الأقمار والمحطات", "جودة البيانات والتنبيهات الكاذبة"],
  apps=["الاستجابة للطوارئ", "المراقبة البيئية"],
  tags=["مكتشف"])

N("disc.humanfactors_org", "السلامة التنظيمية والتعلم المؤسسي", "Organisational safety & learning",
  "disc", 8, "advanced", 4, 30,
  prereqs=["safe.culture", "safe.human"],
  concepts=["التعلم من الأحداث الطفيفة",
            "الأنظمة العالية الموثوقية (HRO)",
            "قياس الثقافة ومؤشراتها", "المرونة الهندسية والتنظيمية",
            "مخاطر التعقيد والترابط"],
  apps=["إدارة السلامة", "بحوث الإدارة"],
  tags=["مكتشف", "غالباً يُنسى"])

N("disc.education", "تعليم العلوم النووية ومحاكاة التدريب", "Nuclear education & simulation-based training",
  "disc", 6, "supporting", 3, 20,
  prereqs=["res.writing", "rx.principles"],
  concepts=["المحاكيات التدريبية لغرف التحكم",
            "المختبرات الافتراضية والواقع المعزز",
            "تصميم مناهج قائمة على الكفايات", "تقييم التعلم"],
  apps=["التدريس", "التدريب الصناعي"],
  tags=["مكتشف"])

N("disc.economics_risk", "اقتصاديات المخاطر والتأمين والتمويل النووي",
  "Risk economics, insurance & nuclear project finance", "disc", 8, "advanced", 4, 30,
  prereqs=["rx.economics", "safe.risk", "pol.law"],
  concepts=["تسعير المخاطر وأثر الحوادث على التكلفة",
            "نماذج التمويل (RAB، عقود الفروق، PPA)",
            "تأمين المسؤولية النووية", "مخاطر الجدولة والوحدة الأولى"],
  apps=["تحليل المشاريع", "السياسات الصناعية"],
  sources=["SMR-Intel-2026", "GRS-2026"],
  tags=["مكتشف"])

N("disc.ai_governance", "حوكمة الذكاء الاصطناعي في النظم النووية", "AI governance in nuclear systems",
  "disc", 9, "research", 4, 25,
  prereqs=["disc.ml_nuclear", "rx.instr", "pol.regulatory"],
  concepts=["الموثوقية وقابلية التفسير في الأنظمة الرقمية",
            "متطلبات القبول الرقابي للذكاء الاصطناعي",
            "الأمن السيبراني وتسمم البيانات", "المسؤولية القانونية"],
  apps=["تصميم أنظمة التحكم", "الرقابة"],
  tags=["مكتشف", "ناشئ"])
