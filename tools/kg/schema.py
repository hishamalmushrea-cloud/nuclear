# -*- coding: utf-8 -*-
"""
نواة «خريطة المعرفة النووية الكبرى» (Nuclear Knowledge Graph).

هذا الملف يعرّف:
  * DOMAINS   : المجالات الكبرى (22 مجالاً).
  * SOURCES   : سجل المصادر (مستوى A/B/C/D حسب نظام مدقق المصادر X.3).
  * Node / N  : بنية العقدة المعرفية ودالة إنشائها المختصرة.
  * load_nodes: تجميع كل العقد من ملفات nodes_*.py.

الفلسفة (X.6): كل موضوع عقدة في رسم موجّه غير دوري (DAG)، وكل حافة = شرط مسبق.
لا تُدرس المواضيع كجزر منفصلة: الروابط تُحسب تلقائياً من تقاسم الشروط المسبقة
ومن المجال، ثم تُعرض في المستندات المولّدة.

الاستخدام:
    from .schema import N
    N("math.calc1", "التفاضل", "Differential calculus", "math", 1, "core", 2, 40,
      prereqs=["math.functions"],
      concepts=["المشتقة", "معدل التغير", "قواعد الاشتقاق", "التفاضل الضمني"])
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

# ----------------------------------------------------------------------------
# 1) المجالات الكبرى
# ----------------------------------------------------------------------------
DOMAINS: Dict[str, Dict[str, str]] = {
    "math": {"ar": "الرياضيات", "en": "Mathematics"},
    "comp": {"ar": "الحوسبة العلمية والبرمجة", "en": "Scientific Computing"},
    "phys": {"ar": "الفيزياء الأساسية", "en": "Core Physics"},
    "chem": {"ar": "الكيمياء", "en": "Chemistry"},
    "nuc":  {"ar": "الفيزياء النووية", "en": "Nuclear Physics"},
    "part": {"ar": "فيزياء الجسيمات", "en": "Particle Physics"},
    "rx":   {"ar": "هندسة المفاعلات", "en": "Reactor Engineering"},
    "fuel": {"ar": "دورة الوقود والنفايات", "en": "Fuel Cycle & Waste"},
    "rad":  {"ar": "الإشعاع والقياس", "en": "Radiation & Measurement"},
    "prot": {"ar": "الحماية من الإشعاع", "en": "Radiation Protection"},
    "safe": {"ar": "السلامة النووية والحوادث", "en": "Nuclear Safety & Accidents"},
    "fus":  {"ar": "الاندماج والبلازما", "en": "Fusion & Plasma"},
    "med":  {"ar": "التطبيقات الطبية", "en": "Medical Applications"},
    "ind":  {"ar": "التطبيقات الصناعية", "en": "Industrial Applications"},
    "env":  {"ar": "البيئة والزراعة والنظائر", "en": "Environment, Agriculture & Isotopes"},
    "mat":  {"ar": "المواد النووية", "en": "Nuclear Materials"},
    "meas": {"ar": "الأجهزة والكشف", "en": "Instrumentation & Detection"},
    "pol":  {"ar": "التنظيم والسياسات والحوكمة", "en": "Regulation, Policy & Governance"},
    "sec":  {"ar": "الأمن وعدم الانتشار والتاريخ العسكري", "en": "Security, Non-proliferation & Military History"},
    "hist": {"ar": "تاريخ العلوم النووية", "en": "History of Nuclear Science"},
    "res":  {"ar": "مناهج البحث العلمي", "en": "Research Methodology"},
    "disc": {"ar": "مجالات مكتشفة/nاشئة", "en": "Discovered & Emerging Fields"},
}

# مستويات العمق (X.5)
DEPTHS = {
    "core": "أساسي إلزامي لكل المسارات",
    "supporting": "مساند: يُطلب لفهم مسار أو أكثر بعمق",
    "advanced": "متقدم: بعد إتقان الأساس",
    "specialized": "تخصصي: لمسار محدد",
    "research": "بحثي: قراءة أدبيات وأسئلة مفتوحة",
}

# المراحل (النظام المكوّن من 0..14)
STAGES: Dict[int, str] = {
    0: "مقدمة عامة",
    1: "رياضيات + فيزياء + كيمياء أساسية",
    2: "فيزياء ذرية وميكانيكا الكم",
    3: "فيزياء نووية أساسية",
    4: "فيزياء نووية متقدمة",
    5: "الهندسة النووية",
    6: "المفاعلات والحراريات والمواد",
    7: "الإشعاع والكواشف والحماية",
    8: "السلامة النووية",
    9: "التطبيقات الطبية والصناعية والبيئية",
    10: "الاندماج والبلازما",
    11: "الحوسبة والمحاكاة",
    12: "الأبحاث النووية المتقدمة",
    13: "السياسات والأمن وعدم الانتشار والتاريخ العسكري",
    14: "مستوى الباحث",
}

# ----------------------------------------------------------------------------
# 2) سجل المصادر — تصنيف مدقق المصادر (X.3)
#    A = ورقة محكّمة/كتاب أكاديمي/وثيقة رسمية/مؤسسة علمية أو تنظيمية
#    B = جامعة أو مؤسسة بحثية موثوقة
#    C = مصدر تعليمي ثانوي جيد
#    D = مصدر عام (لا يُبنى عليه حكم علمي مهم)
# ----------------------------------------------------------------------------
SOURCES: Dict[str, Dict[str, str]] = {
    # --- مستوى A: مؤسسات تنظيمية ومعايير ---
    "IAEA-SSR2/1": {"level": "A", "ar": "IAEA SSR-2/1 (Rev.1): السلامة في تصميم محطات القدرة النووية",
                    "url": "https://www.iaea.org/publications/11088/safety-of-nuclear-power-plants-design"},
    "IAEA-SF1": {"level": "A", "ar": "IAEA SF-1: أساسيات السلامة النووية",
                 "url": "https://www.iaea.org/publications/6990/fundamental-safety-principles"},
    "IAEA-GSR-Part3": {"level": "A", "ar": "IAEA GSR Part 3: الحماية من الإشعاع وسلامة المصادر",
                       "url": "https://www.iaea.org/publications/15302/radiation-protection-and-safety-of-radiation-sources-international-basic-safety-standards"},
    "IAEA-SSG-46": {"level": "A", "ar": "IAEA SSG-46: تقييم الدفاع في العمق",
                    "url": "https://www-pub.iaea.org/MTCD/Publications/PDF/p15147-PUB2008_web.pdf"},
    "IAEA-NDS": {"level": "A", "ar": "خدمات البيانات النووية للوكالة (ENDF/EXFOR/ENSDF/LiveChart)",
                 "url": "https://nds.iaea.org/"},
    "IAEA-PRIS": {"level": "A", "ar": "نظام معلومات مفاعلات القدرة PRIS",
                  "url": "https://pris.iaea.org/pris/"},
    "IAEA-TECDOC-2057": {"level": "A", "ar": "IAEA TECDOC-2057: إنتاج Ac-225 وجودته",
                         "url": "https://www-pub.iaea.org/MTCD/publications/PDF/TE-2057web.pdf"},
    "ICRP-103": {"level": "A", "ar": "ICRP 103: توصيات اللجنة الدولية للوقاية من الإشعاع (2007)",
                 "url": "https://www.icrp.org/publication.asp?id=ICRP%20Publication%20103"},
    "ICRU-85": {"level": "A", "ar": "ICRU 85/85a: الكميات والوحدات في قياس الجرعات",
                "url": "https://www.icru.org/"},
    "UNSCEAR": {"level": "A", "ar": "UNSCEAR: تقارير آثار الإشعاع المؤين",
                "url": "https://www.unscear.org/"},
    "NUREG-0800": {"level": "A", "ar": "NUREG-0800: الفصل المرجعي للتقييم القياسي (NRC)",
                   "url": "https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr0800/"},
    "NUREG-1150": {"level": "A", "ar": "NUREG-1150: تقييم المخاطر الاحتمالية لمحطات القدرة",
                   "url": "https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr1150/"},
    "NRC-10CFR20": {"level": "A", "ar": "10 CFR Part 20: معايير الحماية من الإشعاع",
                    "url": "https://www.nrc.gov/reading-rm/doc-collections/cfr/part020/"},
    "NPT-Text": {"level": "A", "ar": "نص معاهدة عدم الانتشار النووي (NPT)",
                 "url": "https://www.un.org/disarmament/wmd/nuclear/npt/"},
    "UN-Press-DC3912": {"level": "A", "ar": "بيان الأمم المتحدة: المؤتمر الحادي عشر لمراجعة NPT انتهى دون توافق (22 مايو 2026)",
                        "url": "https://press.un.org/en/2026/dc3912.doc.htm"},
    "ITER-NewBaseline": {"level": "A", "ar": "ITER: خط الأساس الجديد 2024 (بدء التشغيل البحثي 2034، D-T 2039)",
                         "url": "https://www.iter.org/node/20687/new-baseline-prioritize-robust-start-exploitation"},
    "LLNL-Ignition": {"level": "A", "ar": "LLNL/NIF: سجلّات الاشتعال الاندماجي (8.6 MJ أبريل 2025)",
                      "url": "https://lasers.llnl.gov/science/achieving-fusion-ignition"},
    "IPP-W7X": {"level": "A", "ar": "Max-Planck-IPP: أرقام قياسية لـ Wendelstein 7-X (مايو 2025)",
                "url": "https://www.ipp.mpg.de/5532945/w7x"},
    "CFS-SPARC": {"level": "B", "ar": "Commonwealth Fusion Systems: تقدم SPARC (مصادقة DOE على المغناطيس 2025)",
                  "url": "https://cfs.energy/news-and-media/"},
    "DOE-FRIB": {"level": "A", "ar": "DOE/FRIB: اكتشاف خمس نظائر جديدة (2026)",
                 "url": "https://www.energy.gov/science/np/articles/facility-rare-isotope-beams-observes-five-never-seen-isotopes"},
    "STUK-Onkalo": {"level": "A", "ar": "STUK/Posiva: تقييم أمان مستودع Onkalo الفنلندي (2026)",
                    "url": "https://www.stuk.fi/"},
    "NIST": {"level": "A", "ar": "NIST: الثوابت الفيزيائية وبيانات القياس",
             "url": "https://physics.nist.gov/"},
    "CODATA": {"level": "A", "ar": "CODATA: الثوابت الفيزيائية الأساسية الموصى بها",
               "url": "https://codata.org/"},
    # --- مستوى A: كتب أكاديمية مرجعية ---
    "Krane": {"level": "A", "ar": "Krane, Introductory Nuclear Physics (Wiley)", "url": ""},
    "Lamarsh": {"level": "A", "ar": "Lamarsh & Baratta, Introduction to Nuclear Engineering", "url": ""},
    "LamarshTheory": {"level": "A", "ar": "Lamarsh, Introduction to Nuclear Reactor Theory", "url": ""},
    "Duderstadt": {"level": "A", "ar": "Duderstadt & Hamilton, Nuclear Reactor Analysis", "url": ""},
    "Stacey": {"level": "A", "ar": "Stacey, Nuclear Reactor Physics (Wiley)", "url": ""},
    "StaceyFusion": {"level": "A", "ar": "Stacey, Fusion Plasma Physics / Fusion: An Introduction", "url": ""},
    "Todreas": {"level": "A", "ar": "Todreas & Kazimi, Nuclear Systems (thermal-hydraulics/fuel)", "url": ""},
    "Choppin": {"level": "A", "ar": "Choppin, Liljenzin & Rydberg, Radiochemistry and Nuclear Chemistry", "url": ""},
    "Knoll": {"level": "A", "ar": "Knoll, Radiation Detection and Measurement", "url": ""},
    "Attix": {"level": "A", "ar": "Attix, Introduction to Radiological Physics and Radiation Dosimetry", "url": ""},
    "Turner": {"level": "A", "ar": "Turner, Atoms, Radiation, and Radiation Protection", "url": ""},
    "Griffiths-QM": {"level": "A", "ar": "Griffiths, Introduction to Quantum Mechanics", "url": ""},
    "Sakurai": {"level": "A", "ar": "Sakurai & Napolitano, Modern Quantum Mechanics", "url": ""},
    "Serway": {"level": "A", "ar": "Serway/Jewett: Physics for Scientists and Engineers", "url": ""},
    "Cengel": {"level": "A", "ar": "Çengel & Ghajar, Heat and Mass Transfer", "url": ""},
    "White-Fluid": {"level": "A", "ar": "White, Fluid Mechanics", "url": ""},
    "NRL-Materials": {"level": "A", "ar": "Olander/Was: مواد المفاعلات وأساسيات التلف الإشعاعي", "url": ""},
    "Was": {"level": "A", "ar": "Was, Fundamentals of Radiation Materials Science", "url": ""},
    "Freiesleben": {"level": "A", "ar": "Frei & Esleben: فيزياء الإشعاع والقياس", "url": ""},
    "IAEA-TECDOC-Transport": {"level": "A", "ar": "IAEA: نقل المواد المشعة ومراجع الحماية", "url": ""},
    # --- مستوى B: جامعات ومؤسسات بحثية ---
    "MIT-OCW": {"level": "B", "ar": "MIT OpenCourseWare: الفيزياء النووية والهندسة النووية (22.02 / 22.05…)",
                "url": "https://ocw.mit.edu/"},
    "NNSA": {"level": "A", "ar": "NNSA/مختبرات DOE: برامج العلوم النووية", "url": "https://www.energy.gov/nnsa"},
    "NEA-Databank": {"level": "A", "ar": "OECD/NEA Data Bank وJANIS", "url": "https://www.oecd-nea.org/janis/"},
    "NNDC": {"level": "A", "ar": "NNDC (Brookhaven): ENDF/B وNuDat وNSR", "url": "https://www.nndc.bnl.gov/"},
    "SMR-Intel-2026": {"level": "C", "ar": "تقرير سنوي عن حالة SMR (2026) — مصدر صناعي ثانوي",
                       "url": "https://smrintel.com/state-of-smr-2026/"},
    "WorldNuclear": {"level": "B", "ar": "World Nuclear Association: تقارير وتقنيات دورة الوقود",
                     "url": "https://world-nuclear.org/"},
    "SIPRI": {"level": "B", "ar": "SIPRI: التسلح ونزع السلاح والأمن الدولي", "url": "https://www.sipri.org/"},
    "BASIC": {"level": "B", "ar": "BASIC: تحليل مؤتمر مراجعة NPT 2026", "url": "https://basicint.org/"},
    "CSS-ETH": {"level": "B", "ar": "CSS/ETH Zurich: تحليل انهيار مفاوضات NPT 2026",
                "url": "https://css.ethz.ch/"},
    "ArXiv-Nucl": {"level": "B", "ar": "arXiv: فيزياء نووية/تجريبية ونظرية وحوسبة",
                   "url": "https://arxiv.org/list/nucl-ex/recent"},
    "Nature-SciRep-DT": {"level": "A", "ar": "Sci. Reports: DeepONet للتوأم الرقمي في النظم النووية (2024)",
                         "url": "https://www.nature.com/articles/s41598-024-51984-x"},
    "ArXiv-GenIV-DT": {"level": "B", "ar": "arXiv 2506.17258: إطار توأم رقمي لمفاعلات الجيل الرابع",
                       "url": "https://arxiv.org/html/2506.17258v1"},
    "McGuireWoods-2026": {"level": "C", "ar": "ملخص صناعي: تحديث قطاع المستحضرات الصيدلانية الإشعاعية (Q1 2026)",
                          "url": "https://www.mcguirewoods.com/client-resources/alerts/2026/4/radiopharmaceutical-industry-update-q1-2026/"},
    "GRS-2026": {"level": "B", "ar": "GRS: الطاقة النووية عالمياً 2026",
                 "url": "https://www.grs.de/en/news/nuclear-energy-worldwide-2026"},
    "IAEA-Trends-2025": {"level": "A", "ar": "IAEA: ستة اتجاهات عالمية في الطاقة النووية (حالة 2025)",
                         "url": "https://www.iaea.org/newscenter/news/six-global-trends-in-nuclear-power-you-should-know"},
}

# مصادر افتراضية لكل مجال (تُستخدم إن لم تحدد العقدة مصادرها)
DOMAIN_DEFAULT_SOURCES: Dict[str, List[str]] = {
    "math": ["Serway"],
    "comp": ["ArXiv-Nucl"],
    "phys": ["Serway", "Griffiths-QM"],
    "chem": ["Choppin"],
    "nuc":  ["Krane", "IAEA-NDS"],
    "part": ["Krane"],
    "rx":   ["Lamarsh", "Duderstadt", "Stacey"],
    "fuel": ["Choppin", "WorldNuclear"],
    "rad":  ["Knoll", "Attix", "Turner"],
    "prot": ["ICRP-103", "IAEA-GSR-Part3", "Turner"],
    "safe": ["IAEA-SF1", "IAEA-SSR2/1", "IAEA-SSG-46"],
    "fus":  ["StaceyFusion", "ITER-NewBaseline"],
    "med":  ["IAEA-TECDOC-2057"],
    "ind":  ["IAEA-NDS"],
    "env":  ["UNSCEAR"],
    "mat":  ["Was", "NRL-Materials"],
    "meas": ["Knoll"],
    "pol":  ["IAEA-SF1"],
    "sec":  ["NPT-Text", "SIPRI"],
    "hist": ["IAEA-SF1"],
    "res":  ["ArXiv-Nucl"],
    "disc": ["ArXiv-Nucl", "IAEA-NDS"],
}

# أدوات برمجية لكل مجال (تُستخدم في MAP/10 وتُعرض في العارض)
DOMAIN_TOOLS: Dict[str, List[str]] = {
    "math": ["SymPy", "NumPy", "Matplotlib"],
    "comp": ["Python", "NumPy", "SciPy", "Matplotlib", "pandas", "Jupyter", "Git"],
    "phys": ["Python", "SymPy"],
    "chem": ["Python", "pandas"],
    "nuc":  ["IAEA LiveChart", "JANIS (NEA)", "ENDF/B", "EXFOR", "ENSDF", "Python"],
    "part": ["Geant4", "ROOT", "Python"],
    "rx":   ["OpenMC", "Serpent", "MCNP", "SCALE", "NJOY", "MOOSE", "RELAP5/TRACE", "Python"],
    "fuel": ["ORIGEN/SCALE", "Python"],
    "rad":  ["Geant4", "FLUKA", "PHITS", "PENELOPE", "Python"],
    "prot": ["MicroShield (تجاري)", "Python", "Geant4"],
    "safe": ["SAPHIRE", "RiskSpectrum", "MAAP/MELCOR", "Python"],
    "fus":  ["TRANSP", "MHD/ gyrokinetic codes", "OpenMC", "Python"],
    "med":  ["GATE (Geant4)", "SIMIND", "Python", "DICOM toolkits"],
    "ind":  ["Geant4", "Python"],
    "env":  ["Python", "QGIS", "pandas"],
    "mat":  ["LAMMPS", "MOOSE/BISON", "Python", "SRIM (تجاري)"],
    "meas": ["ROOT", "Python", "GNU Radio? لا", "CAEN/الإلكترونيات النووية"],
    "pol":  ["وثائق IAEA/NRC", "قواعد بيانات قانونية"],
    "sec":  ["وثائق IAEA وNPT وSIPRI"],
    "hist": ["أرشيفات IAEA وDOE"],
    "res":  ["arXiv", "INSPIRE-HEP", " Scopus/Web of Science", "Zotero", "Jupyter", "Git"],
    "disc": ["Python", "OpenMC", "MOOSE", "arXiv"],
}


# ----------------------------------------------------------------------------
# 4) المستويات الخمسة عشر (0..14) — تصنيف موضوعاتي للمراحل كما طلب المستخدم.
#    ملاحظة منهجية: هذا التصنيف «موضوعاتي» (thematic)، أما الترتيب الفعلي
#    للدراسة فهو الترتيب الطوبولوجي المولّد في MAP/04.
# ----------------------------------------------------------------------------
LEVELS_0_14: Dict[int, str] = {
    0: "مقدمة عامة",
    1: "رياضيات + فيزياء + كيمياء أساسية",
    2: "فيزياء ذرية وميكانيكا الكم",
    3: "فيزياء نووية أساسية",
    4: "الفيزياء النووية المتقدمة",
    5: "الهندسة النووية",
    6: "المفاعلات والحراريات والمواد",
    7: "الإشعاع والكواشف والحماية",
    8: "السلامة النووية",
    9: "التطبيقات الطبية والصناعية والبيئية",
    10: "الاندماج والبلازما",
    11: "الحوسبة والمحاكاة",
    12: "الأبحاث النووية المتقدمة",
    13: "السياسات والأمن وعدم الانتشار والتاريخ العسكري",
    14: "مستوى الباحث",
}

# المستوى الافتراضي لكل مجال
LEVEL_DEFAULT: Dict[str, int] = {
    "math": 1, "comp": 11, "phys": 2, "chem": 2, "nuc": 3, "part": 3,
    "rx": 5, "fuel": 6, "rad": 7, "prot": 7, "safe": 8, "fus": 10,
    "med": 9, "ind": 9, "env": 9, "mat": 6, "meas": 7, "pol": 13,
    "sec": 13, "hist": 13, "res": 14, "disc": 12,
}

# استثناءات محددة
LEVEL_OVERRIDE: Dict[str, int] = {
    "math.pre": 0,
    "hist.timeline": 0,
    "phys.mech": 1, "phys.energy": 1, "phys.grav": 1, "phys.em": 1,
    "phys.waves": 1, "phys.thermo": 1, "chem.general": 1,
    "cs.python": 1, "cs.numpy": 1, "cs.data": 1,
    "math.analysis": 4, "math.advanced": 4, "math.grouptheory": 4,
    "phys.condmat": 4, "phys.qm2": 4, "phys.accel_basics": 4,
    "part.sm": 4, "part.neutrino": 4, "part.detectors": 4,
    "part.accel": 4, "part.hep": 4, "part.qft": 4,
    "chem.materials": 4, "chem.organic": 3, "chem.envradio": 9,
    "chem.hotcells": 7,
    "math.mc": 11, "math.optimization": 11,
    "rx.multiphysics": 11, "disc.ml_nuclear": 11, "disc.digitaltwin": 11,
    "rad.metrology": 7,
    "rx.diffusion": 6, "rx.transport": 6, "rx.kinetics": 6, "rx.control": 6,
    "rx.heat": 6, "rx.fluids": 6, "rx.thermalhyd": 6, "rx.power": 6,
    "mat.intro": 6, "mat.fuels": 6,
    "res.literature": 3, "res.sources": 3, "res.question": 5,
    "res.design": 5, "res.stats": 5, "res.data": 5,
    "res.reproducibility": 11, "res.writing": 11, "res.peerreview": 14,
    "res.openproblems": 14,
    "disc.education": 14,
    "nuc.theory": 12, "nuc.models": 12, "nuc.structure": 12,
    "nuc.astro": 12, "nuc.neutronsci": 12,
    "sec.forensics": 13, "sec.geopolitics": 13,
}


def user_level(node: "Node") -> int:
    return LEVEL_OVERRIDE.get(node.id, LEVEL_DEFAULT.get(node.domain, 3))


# ----------------------------------------------------------------------------
# 3) العقدة المعرفية
# ----------------------------------------------------------------------------
@dataclass
class Node:
    id: str
    ar: str
    en: str
    domain: str
    stage: int
    depth: str
    diff: int                       # 1..5
    hours: int                      # وقت تقديري للدراسة الجادة
    prereqs: List[str] = field(default_factory=list)
    concepts: List[str] = field(default_factory=list)
    eqs: List[str] = field(default_factory=list)
    apps: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = {
            "id": self.id,
            "ar": self.ar,
            "en": self.en,
            "domain": self.domain,
            "domain_ar": DOMAINS[self.domain]["ar"],
            "stage": self.stage,
            "stage_ar": STAGES[self.stage],
            "depth": self.depth,
            "depth_ar": DEPTHS[self.depth],
            "difficulty": self.diff,
            "hours": self.hours,
            "prereqs": list(self.prereqs),
            "concepts": list(self.concepts),
            "equations": list(self.eqs),
            "applications": list(self.apps),
            "sources": list(self.sources),
            "tags": list(self.tags),
            "tools": DOMAIN_TOOLS.get(self.domain, []),
        }
        return d


_NODES: List[Node] = []


def N(  # noqa: E741  (اسم مختصر متعمّد لسهولة كتابة البيانات)
    id: str,
    ar: str,
    en: str,
    domain: str,
    stage: int,
    depth: str,
    diff: int,
    hours: int,
    prereqs: Optional[List[str]] = None,
    concepts: Optional[List[str]] = None,
    eqs: Optional[List[str]] = None,
    apps: Optional[List[str]] = None,
    sources: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
) -> Node:
    """إنشاء عقدة وإضافتها إلى السجل العام."""
    if domain not in DOMAINS:
        raise ValueError(f"مجال غير معروف: {domain} (العقدة {id})")
    if depth not in DEPTHS:
        raise ValueError(f"عمق غير معروف: {depth} (العقدة {id})")
    if stage not in STAGES:
        raise ValueError(f"مرحلة غير معروفة: {stage} (العقدة {id})")
    if not (1 <= diff <= 5):
        raise ValueError(f"صعوبة خارج النطاق 1..5: {diff} (العقدة {id})")
    node = Node(
        id=id, ar=ar, en=en, domain=domain, stage=stage, depth=depth,
        diff=diff, hours=hours,
        prereqs=list(prereqs or []),
        concepts=list(concepts or []),
        eqs=list(eqs or []),
        apps=list(apps or []),
        sources=list(sources or DOMAIN_DEFAULT_SOURCES.get(domain, [])),
        tags=list(tags or []),
    )
    _NODES.append(node)
    return node


def load_nodes() -> List[Node]:
    """استيراد كل وحدات العقد لملء السجل، ثم إرجاعه."""
    if _NODES:
        return _NODES
    import importlib
    mods = [
        "nodes_math", "nodes_phys", "nodes_chem", "nodes_nuc",
        "nodes_rx", "nodes_rad", "nodes_fus", "nodes_app",
        "nodes_pol", "nodes_res", "nodes_disc",
    ]
    pkg = __name__.rsplit(".", 1)[0] if "." in __name__ else "kg"
    for m in mods:
        importlib.import_module(f"{pkg}.{m}")
    return _NODES


def registry() -> Dict[str, Node]:
    return {n.id: n for n in load_nodes()}
