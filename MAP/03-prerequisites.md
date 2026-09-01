# MAP/03 — جدول المتطلبات السابقة (Prerequisites)

لكل موضوع: ما يجب إتقانه قبله، وما يفتحه لاحقاً.

> ⚙️ **هذا ملف مولّد آلياً.** لا تعدّله يدوياً: عدّل البيانات في `tools/kg/nodes_*.py` ثم نفّذ `python3 tools/build.py`.


| المعرّف | الموضوع | المجال | المرحلة | الشروط المسبقة | يفتح الطريق إلى | صعوبة | ساعات |
|---|---|---|---|---|---|---|---|
| `hist.timeline` | الخط الزمني للعلوم النووية | تاريخ العلوم النووية | 0 | — | `hist.accidents_hist`, `hist.projects`, `safe.accidents`, `sec.history`, `sec.nonprolif` | 2/5 | 25 |
| `math.pre` | الأساس الحسابي والجبري التمهيدي | الرياضيات | 0 | — | `chem.general`, `cs.python`, `math.algebra`, `math.geometry` | 1/5 | 25 |
| `chem.general` | الكيمياء العامة | الكيمياء | 1 | `math.pre` | `chem.analytical`, `chem.phys`, `chem.structure` | 2/5 | 50 |
| `cs.numpy` | NumPy وSciPy وMatplotlib | الحوسبة العلمية والبرمجة | 1 | `cs.python`, `math.linalg` | `cs.data`, `cs.uq`, `disc.ml_nuclear`, `meas.signal`, `rx.kinetics` | 2/5 | 40 |
| `cs.python` | البرمجة العلمية بـ Python | الحوسبة العلمية والبرمجة | 1 | `math.pre` | `cs.hpc`, `cs.numpy`, `math.mc`, `res.literature`, `res.reproducibility` | 2/5 | 40 |
| `math.algebra` | الجبر | الرياضيات | 1 | `math.pre` | `math.complex`, `math.functions`, `math.linalg` | 2/5 | 45 |
| `math.calc1` | التفاضل | الرياضيات | 1 | `math.functions` | `math.calc2`, `math.optimization`, `phys.mech`, `phys.thermo` | 3/5 | 45 |
| `math.calc2` | التكامل | الرياضيات | 1 | `math.calc1` | `math.analysis`, `math.nummethods`, `math.ode`, `math.prob`, `math.vectors` | 3/5 | 45 |
| `math.functions` | الدوال | الرياضيات | 1 | `math.algebra` | `math.calc1` | 2/5 | 30 |
| `math.geometry` | الهندسة | الرياضيات | 1 | `math.pre` | `math.trig` | 2/5 | 25 |
| `math.linalg` | الجبر الخطي | الرياضيات | 1 | `math.algebra` | `cs.numpy`, `math.grouptheory`, `math.nummethods`, `math.optimization`, `math.vectors`, `phys.qm1` | 3/5 | 45 |
| `math.ode` | المعادلات التفاضلية العادية | الرياضيات | 1 | `math.calc2` | `math.pde`, `nuc.halflife`, `nuc.series`, `phys.qm1`, `rad.transport`, `rx.kinetics` | 3/5 | 50 |
| `math.trig` | المثلثات | الرياضيات | 1 | `math.geometry` | `math.complex`, `phys.waves` | 2/5 | 25 |
| `math.vectors` | تحليل المتجهات (حساب المتجهات) | الرياضيات | 1 | `math.calc2`, `math.linalg` | `fus.plasma`, `math.pde`, `phys.em`, `phys.emi`, `phys.mech`, `rx.diffusion` | 3/5 | 40 |
| `phys.em` | الكهرباء والمغناطيسية | الفيزياء الأساسية | 1 | `math.vectors`, `phys.mech` | `meas.electronics`, `phys.accel_basics`, `phys.emi`, `rad.detectors`, `rx.instr` | 3/5 | 55 |
| `phys.energy` | الطاقة والزخم والزخم الزاوي | الفيزياء الأساسية | 1 | `phys.mech` | `nuc.reactions`, `phys.thermo` | 2/5 | 35 |
| `phys.grav` | الجاذبية والحركة المدارية | الفيزياء الأساسية | 1 | `phys.mech` | — | 2/5 | 20 |
| `phys.mech` | الميكانيكا الكلاسيكية | الفيزياء الأساسية | 1 | `math.calc1`, `math.vectors` | `phys.em`, `phys.energy`, `phys.grav`, `phys.relativity`, `phys.waves`, `rx.fluids` | 2/5 | 55 |
| `phys.waves` | الموجات والبصريات | الفيزياء الأساسية | 1 | `math.trig`, `phys.mech` | — | 2/5 | 40 |
| `chem.analytical` | الكيمياء التحليلية | الكيمياء | 2 | `chem.general`, `math.stat` | `sec.forensics` | 3/5 | 45 |
| `chem.bonding` | الروابط الكيميائية | الكيمياء | 2 | `chem.structure` | `chem.inorganic`, `chem.materials`, `chem.organic` | 2/5 | 35 |
| `chem.phys` | الكيمياء الفيزيائية | الكيمياء | 2 | `chem.general`, `phys.thermo`, `phys.qm1` | `chem.isotope`, `disc.hydrogen`, `mat.corrosion` | 3/5 | 50 |
| `chem.structure` | البنية الذرية والجدول الدوري | الكيمياء | 2 | `chem.general`, `phys.atomic` | `chem.bonding`, `chem.inorganic`, `nuc.isotopes` | 2/5 | 35 |
| `cs.data` | تحليل البيانات وإدارتها | الحوسبة العلمية والبرمجة | 2 | `cs.numpy`, `math.stat` | `disc.nuclear_analytics`, `med.dosimetry_plan`, `nuc.data`, `res.data` | 2/5 | 35 |
| `math.complex` | الأعداد المركبة | الرياضيات | 2 | `math.algebra`, `math.trig` | `math.advanced`, `meas.electronics`, `phys.qm1` | 2/5 | 25 |
| `math.nummethods` | التحليل العددي وطرق الحل العددي | الرياضيات | 2 | `math.calc2`, `math.linalg` | `cs.vv`, `safe.dsa` | 3/5 | 50 |
| `math.prob` | الاحتمالات | الرياضيات | 2 | `math.calc2` | `math.mc`, `math.stat`, `nuc.crosssection`, `phys.statmech`, `safe.hazard`, `safe.psa` | 3/5 | 40 |
| `math.stat` | الإحصاء | الرياضيات | 2 | `math.prob` | `chem.analytical`, `cs.data`, `cs.uq`, `env.dating`, `env.tracers`, `math.mc` (+7) | 3/5 | 45 |
| `phys.atomic` | الفيزياء الذرية | الفيزياء الأساسية | 2 | `phys.qm1` | `chem.structure`, `nuc.intro`, `nuc.isotopes`, `phys.molecular`, `rad.interaction`, `rad.types` | 3/5 | 45 |
| `phys.emi` | الكهرومغناطيسية ومعادلات ماكسويل | الفيزياء الأساسية | 2 | `phys.em`, `math.vectors` | `fus.heating`, `fus.inertial`, `fus.plasma`, `part.accel`, `phys.qm1`, `phys.relativity` (+1) | 4/5 | 50 |
| `phys.qm1` | ميكانيكا الكم (مستوى جامعي) | الفيزياء الأساسية | 2 | `math.ode`, `math.linalg`, `math.complex`, `phys.emi`, `phys.relativity` | `chem.phys`, `nuc.decay`, `part.intro`, `phys.atomic`, `phys.condmat`, `phys.qm2` | 4/5 | 70 |
| `phys.relativity` | النسبية الخاصة | الفيزياء الأساسية | 2 | `phys.mech`, `phys.emi` | `nuc.binding`, `nuc.intro`, `nuc.reactions`, `part.intro`, `phys.accel_basics`, `phys.qm1` | 3/5 | 40 |
| `phys.thermo` | الديناميكا الحرارية | الفيزياء الأساسية | 2 | `math.calc1`, `phys.energy` | `chem.phys`, `phys.statmech`, `rx.heat`, `rx.thermo_power` | 3/5 | 50 |
| `chem.inorganic` | الكيمياء غير العضوية | الكيمياء | 3 | `chem.bonding`, `chem.structure` | `chem.radiochemistry`, `fuel.intro`, `fuel.resources` | 3/5 | 45 |
| `chem.organic` | الكيمياء العضوية | الكيمياء | 3 | `chem.bonding` | — | 3/5 | 45 |
| `hist.projects` | تاريخ المشاريع والمؤسسات الكبرى | تاريخ العلوم النووية | 3 | `hist.timeline` | — | 3/5 | 30 |
| `nuc.binding` | الطاقة الرابطة ونقص الكتلة | الفيزياء النووية | 3 | `nuc.isotopes`, `phys.relativity` | `nuc.fission`, `nuc.fusion_basics`, `nuc.mass`, `nuc.reactions`, `nuc.stability` | 3/5 | 35 |
| `nuc.crosssection` | المقاطع العرضية | الفيزياء النووية | 3 | `nuc.reactions`, `math.prob` | `nuc.absorption`, `nuc.data`, `nuc.neutron`, `nuc.scattering`, `rad.activation` | 4/5 | 45 |
| `nuc.decay` | التحلل الإشعاعي وأنواعه | الفيزياء النووية | 3 | `nuc.stability`, `phys.qm1` | `chem.radiochemistry`, `disc.space`, `nuc.exp`, `nuc.halflife`, `part.neutrino`, `rad.types` | 3/5 | 50 |
| `nuc.fission` | الانشطار النووي | الفيزياء النووية | 3 | `nuc.binding`, `nuc.reactions` | `fuel.intro`, `rx.chain`, `rx.principles` | 4/5 | 50 |
| `nuc.fusion_basics` | الاندماج النووي: الأساس الفيزيائي | الفيزياء النووية | 3 | `nuc.binding`, `nuc.reactions`, `phys.statmech` | `fus.inertial`, `fus.neutronics`, `nuc.astro` | 4/5 | 40 |
| `nuc.halflife` | عمر النصف وقانون التحلل والنشاط | الفيزياء النووية | 3 | `nuc.decay`, `math.ode` | `env.dating`, `med.nucmed`, `nuc.series`, `rad.sources` | 2/5 | 30 |
| `nuc.intro` | مقدمة الفيزياء النووية | الفيزياء النووية | 3 | `phys.atomic`, `phys.relativity`, `nuc.isotopes` | `nuc.nucleons` | 3/5 | 40 |
| `nuc.isotopes` | النظائر والنويدات وخريطة النويدات | الفيزياء النووية | 3 | `phys.atomic`, `chem.structure` | `chem.isotope`, `nuc.binding`, `nuc.intro`, `nuc.stability` | 2/5 | 25 |
| `nuc.nucleons` | النيوكليونات والقوة النووية | الفيزياء النووية | 3 | `nuc.intro`, `part.forces` | — | 3/5 | 35 |
| `nuc.reactions` | التفاعلات النووية والـ Q-value | الفيزياء النووية | 3 | `nuc.binding`, `phys.energy`, `phys.relativity` | `chem.nuclear`, `disc.transmutation`, `med.isotopes`, `nuc.astro`, `nuc.crosssection`, `nuc.fission` (+1) | 4/5 | 45 |
| `nuc.stability` | الاستقرار النووي وخط الاستقرار | الفيزياء النووية | 3 | `nuc.binding`, `nuc.isotopes` | `nuc.decay`, `nuc.models` | 3/5 | 30 |
| `part.forces` | القوى الأساسية الأربع | فيزياء الجسيمات | 3 | `part.intro` | `nuc.nucleons` | 3/5 | 30 |
| `part.intro` | الجسيمات الأولية: مقدمة | فيزياء الجسيمات | 3 | `phys.qm1`, `phys.relativity` | `part.forces`, `part.quarks`, `part.sm` | 3/5 | 30 |
| `phys.molecular` | الفيزياء الجزيئية | الفيزياء الأساسية | 3 | `phys.atomic` | — | 3/5 | 30 |
| `phys.statmech` | الفيزياء الإحصائية | الفيزياء الأساسية | 3 | `phys.thermo`, `math.prob` | `fus.inertial`, `fus.plasma`, `nuc.fusion_basics`, `phys.condmat` | 4/5 | 50 |
| `rad.sources` | مصادر الإشعاع | الإشعاع والقياس | 3 | `rad.types`, `nuc.halflife` | `ind.radiography`, `rad.contamination` | 2/5 | 25 |
| `rad.types` | أنواع الإشعاع | الإشعاع والقياس | 3 | `nuc.decay`, `phys.atomic` | `fuel.waste`, `med.nucmed`, `rad.contamination`, `rad.interaction`, `rad.sources` | 2/5 | 25 |
| `res.literature` | قراءة الأوراق ومراجعة الأدبيات | مناهج البحث العلمي | 3 | `cs.python` | `pol.ethics`, `res.openproblems`, `res.question`, `res.sources`, `res.writing` | 3/5 | 35 |
| `res.sources` | تقييم المصادر ومدقق المصادر | مناهج البحث العلمي | 3 | `res.literature` | `res.question` | 3/5 | 25 |
| `chem.isotope` | سلوك النظائر وفصلها | الكيمياء | 4 | `chem.phys`, `nuc.isotopes` | `env.tracers`, `fuel.fabrication`, `fus.blanket`, `ind.tracers` | 4/5 | 45 |
| `chem.materials` | كيمياء المواد | الكيمياء | 4 | `chem.bonding`, `phys.condmat` | `mat.ceramics`, `mat.intro` | 3/5 | 35 |
| `chem.nuclear` | الكيمياء النووية | الكيمياء | 4 | `chem.radiochemistry`, `nuc.reactions` | — | 4/5 | 50 |
| `chem.radiochemistry` | الكيمياء الإشعاعية | الكيمياء | 4 | `chem.inorganic`, `nuc.decay`, `rad.interaction` | `chem.envradio`, `chem.hotcells`, `chem.nuclear`, `fuel.reprocessing`, `med.isotopes`, `rad.bio` | 4/5 | 50 |
| `math.advanced` | رياضيات متقدمة للعلوم النووية | الرياضيات | 4 | `math.pde`, `math.analysis`, `math.complex` | `part.qft`, `phys.qm2` | 5/5 | 60 |
| `math.analysis` | التحليل الرياضي | الرياضيات | 4 | `math.calc2` | `math.advanced`, `meas.signal` | 4/5 | 50 |
| `math.grouptheory` | نظرية الزمر والتماثل | الرياضيات | 4 | `math.linalg` | `part.sm` | 5/5 | 45 |
| `math.pde` | المعادلات التفاضلية الجزئية | الرياضيات | 4 | `math.ode`, `math.vectors` | `env.dispersion`, `math.advanced`, `rx.diffusion`, `rx.fluids`, `rx.heat` | 4/5 | 60 |
| `meas.calibration` | معايرة الأجهزة ومصادر الخطأ | الأجهزة والكشف | 4 | `rad.spectroscopy`, `math.stat` | `rad.metrology` | 3/5 | 35 |
| `meas.detectors` | تقنيات الكواشف: نظرة هندسية | الأجهزة والكشف | 4 | `rad.interaction` | `fus.diagnostics`, `nuc.exp`, `rx.instr` | 3/5 | 35 |
| `meas.electronics` | الإلكترونيات النووية | الأجهزة والكشف | 4 | `phys.em`, `math.complex` | `meas.signal`, `rad.detectors` | 4/5 | 45 |
| `meas.signal` | معالجة الإشارات والحصول على البيانات | الأجهزة والكشف | 4 | `meas.electronics`, `math.analysis`, `cs.numpy` | `fus.diagnostics`, `med.imaging`, `rad.spectroscopy` | 4/5 | 40 |
| `nuc.absorption` | الامتصاص والرنين والنماذج النووية للتفاعل | الفيزياء النووية | 4 | `nuc.crosssection`, `nuc.scattering` | `nuc.neutron` | 4/5 | 40 |
| `nuc.data` | البيانات النووية (Nuclear Data) | الفيزياء النووية | 4 | `nuc.crosssection`, `cs.data` | `disc.ml_nuclear`, `rx.transport`, `sec.forensics` | 3/5 | 35 |
| `nuc.exp` | الفيزياء النووية التجريبية | الفيزياء النووية | 4 | `nuc.decay`, `meas.detectors`, `math.stat` | — | 4/5 | 50 |
| `nuc.mass` | الكتل النووية وجداول الكتل | الفيزياء النووية | 4 | `nuc.binding` | — | 3/5 | 20 |
| `nuc.models` | نماذج النواة | الفيزياء النووية | 4 | `phys.qm2`, `nuc.stability` | `nuc.structure`, `nuc.theory` | 5/5 | 60 |
| `nuc.neutron` | فيزياء النيوترونات | الفيزياء النووية | 4 | `nuc.crosssection`, `nuc.absorption` | `nuc.neutronsci`, `rx.chain`, `rx.diffusion`, `rx.principles` | 4/5 | 50 |
| `nuc.scattering` | التشتت النووي | الفيزياء النووية | 4 | `nuc.crosssection`, `phys.qm2` | `nuc.absorption` | 4/5 | 40 |
| `nuc.series` | سلاسل التحلل والتوازن الإشعاعي | الفيزياء النووية | 4 | `nuc.halflife`, `math.ode` | `fuel.spent` | 4/5 | 35 |
| `nuc.structure` | بنية النواة المتقدمة | الفيزياء النووية | 4 | `nuc.models` | — | 5/5 | 45 |
| `nuc.theory` | الفيزياء النووية النظرية | الفيزياء النووية | 4 | `nuc.models`, `phys.qm2` | — | 5/5 | 60 |
| `part.detectors` | كواشف الجسيمات | فيزياء الجسيمات | 4 | `part.quarks`, `rad.detectors` | `part.hep` | 4/5 | 40 |
| `part.neutrino` | فيزياء النيوترينو | فيزياء الجسيمات | 4 | `part.sm`, `nuc.decay` | — | 5/5 | 40 |
| `part.quarks` | الكواركات واللبتونات والبوزونات | فيزياء الجسيمات | 4 | `part.intro` | `part.detectors` | 4/5 | 35 |
| `part.sm` | النموذج القياسي | فيزياء الجسيمات | 4 | `part.intro`, `math.grouptheory`, `phys.qm2` | `part.hep`, `part.neutrino`, `part.qft` | 5/5 | 50 |
| `phys.accel_basics` | أساسيات المسرعات | الفيزياء الأساسية | 4 | `phys.em`, `phys.relativity` | `part.accel` | 3/5 | 35 |
| `phys.condmat` | فيزياء المادة المكثفة | الفيزياء الأساسية | 4 | `phys.qm1`, `phys.statmech` | `chem.materials`, `mat.characterization`, `mat.damage`, `mat.intro`, `nuc.neutronsci` | 4/5 | 45 |
| `phys.qm2` | ميكانيكا الكم المتقدمة ونظرية التشتت | الفيزياء الأساسية | 4 | `phys.qm1`, `math.advanced` | `disc.quantum`, `nuc.models`, `nuc.scattering`, `nuc.theory`, `part.qft`, `part.sm` | 5/5 | 60 |
| `rad.contamination` | التلوث الإشعاعي والتعرض | الإشعاع والقياس | 4 | `rad.types`, `rad.sources` | `prot.occupational` | 3/5 | 30 |
| `rad.detectors` | كواشف الإشعاع | الإشعاع والقياس | 4 | `rad.interaction`, `phys.em`, `meas.electronics` | `disc.neutronimaging`, `ind.tracers`, `ind.welllogging`, `med.imaging`, `part.detectors`, `prot.monitoring` (+1) | 4/5 | 60 |
| `rad.dosimetry` | الجرعة: الممتصة والمكافئة والفعالة | الإشعاع والقياس | 4 | `rad.interaction`, `rad.transport` | `ind.sterilization`, `med.nucmed`, `med.therapy`, `pol.regulatory`, `prot.principles`, `rad.bio` (+2) | 4/5 | 50 |
| `rad.interaction` | تفاعل الإشعاع مع المادة | الإشعاع والقياس | 4 | `rad.types`, `phys.atomic`, `phys.emi` | `chem.radiochemistry`, `mat.damage`, `meas.detectors`, `rad.detectors`, `rad.dosimetry`, `rad.shielding` (+2) | 4/5 | 55 |
| `rad.shielding` | التدريع | الإشعاع والقياس | 4 | `rad.transport`, `rad.interaction` | `fuel.storage`, `fuel.transport`, `ind.radiography` | 4/5 | 45 |
| `rad.spectroscopy` | التحليل الطيفي الإشعاعي | الإشعاع والقياس | 4 | `rad.detectors`, `meas.signal`, `math.stat` | `env.tracers`, `meas.calibration`, `meas.monitoring`, `meas.spectroscopy`, `rad.activation` | 4/5 | 50 |
| `rad.transport` | انتقال الإشعاع والتوهين | الإشعاع والقياس | 4 | `rad.interaction`, `math.ode` | `ind.gauges`, `ind.ndt`, `rad.dosimetry`, `rad.shielding`, `sec.effects` | 4/5 | 45 |
| `cs.uq` | كمّنة عدم اليقين (UQ) | الحوسبة العلمية والبرمجة | 5 | `math.stat`, `math.mc`, `cs.numpy` | `cs.vv`, `disc.ml_nuclear`, `disc.quantum`, `res.stats`, `safe.risk` | 4/5 | 45 |
| `cs.vv` | التحقق والتحقق من الصحة (V&V) | الحوسبة العلمية والبرمجة | 5 | `cs.uq`, `math.nummethods` | `disc.digitaltwin`, `res.reproducibility`, `rx.multiphysics` | 4/5 | 35 |
| `fuel.fabrication` | تحويل وتخصيب وتصنيع الوقود | دورة الوقود والنفايات | 5 | `fuel.resources`, `chem.isotope` | — | 4/5 | 35 |
| `fuel.intro` | دورة الوقود النووي: نظرة شاملة | دورة الوقود والنفايات | 5 | `nuc.fission`, `chem.inorganic` | `fuel.resources`, `fuel.spent`, `pol.safeguards`, `sec.nonprolif` | 3/5 | 35 |
| `fuel.resources` | مصادر المواد النووية | دورة الوقود والنفايات | 5 | `fuel.intro`, `chem.inorganic` | `fuel.fabrication` | 2/5 | 25 |
| `fus.plasma` | فيزياء البلازما: الأساس | الاندماج والبلازما | 5 | `phys.emi`, `phys.statmech`, `math.vectors` | `fus.diagnostics`, `fus.heating`, `fus.magnetic`, `fus.mhd` | 4/5 | 55 |
| `mat.intro` | المواد النووية: مقدمة | المواد النووية | 5 | `phys.condmat`, `chem.materials` | `mat.ceramics`, `mat.damage`, `mat.metals`, `rx.fuel`, `rx.materials` | 3/5 | 30 |
| `math.mc` | طرق مونتي كارلو | الرياضيات | 5 | `math.prob`, `math.stat`, `cs.python` | `cs.uq`, `med.dosimetry_plan`, `rx.transport` | 4/5 | 45 |
| `math.optimization` | التحسين والبحث العملياتي | الرياضيات | 5 | `math.linalg`, `math.calc1` | — | 3/5 | 35 |
| `nuc.astro` | الفيزياء النووية الفلكية والتخليق النووي | الفيزياء النووية | 5 | `nuc.fusion_basics`, `nuc.reactions` | — | 4/5 | 40 |
| `nuc.neutronsci` | علم النيوترونات (مصادر وتشتت) | الفيزياء النووية | 5 | `nuc.neutron`, `phys.condmat` | `disc.neutronimaging` | 4/5 | 40 |
| `part.accel` | فيزياء المسرعات | فيزياء الجسيمات | 5 | `phys.accel_basics`, `phys.emi` | `disc.ads` | 5/5 | 45 |
| `part.hep` | التفاعلات عالية الطاقة | فيزياء الجسيمات | 5 | `part.sm`, `part.detectors` | — | 5/5 | 40 |
| `part.qft` | نظرية الحقول الكمومية | فيزياء الجسيمات | 5 | `part.sm`, `phys.qm2`, `math.advanced` | — | 5/5 | 80 |
| `pol.regulatory` | الهيئات الرقابية والمعايير | التنظيم والسياسات والحوكمة | 5 | `rad.dosimetry`, `safe.did` | `disc.ai_governance`, `fuel.transport`, `fuel.waste`, `pol.governance`, `pol.law`, `pol.safeguards` (+4) | 3/5 | 35 |
| `prot.monitoring` | المراقبة وقياس الجرعات | الحماية من الإشعاع | 5 | `prot.principles`, `rad.detectors` | `prot.occupational` | 3/5 | 35 |
| `prot.occupational` | الوقاية المهنية والصحة المهنية | الحماية من الإشعاع | 5 | `prot.monitoring`, `rad.contamination` | — | 3/5 | 35 |
| `prot.principles` | مبادئ الحماية الإشعاعية | الحماية من الإشعاع | 5 | `rad.dosimetry`, `rad.bio` | `chem.hotcells`, `ind.radiography`, `med.rp`, `prot.emergency`, `prot.lab`, `prot.medical` (+2) | 3/5 | 35 |
| `rad.bio` | علم الأحياء الإشعاعي والتأثيرات البيولوجية | الإشعاع والقياس | 5 | `rad.dosimetry`, `chem.radiochemistry` | `env.agriculture`, `env.radioecology`, `ind.sterilization`, `med.therapy`, `prot.principles`, `sec.effects` | 4/5 | 55 |
| `rad.metrology` | قياسات الإشعاع والقياسات المرجعية (Metrology) | الإشعاع والقياس | 5 | `rad.dosimetry`, `meas.calibration` | — | 4/5 | 35 |
| `res.data` | إدارة البيانات وإتاحتها | مناهج البحث العلمي | 5 | `cs.data`, `res.design` | `res.reproducibility` | 3/5 | 25 |
| `res.design` | تصميم التجارب الآمن | مناهج البحث العلمي | 5 | `res.question`, `prot.principles`, `math.stat` | `res.data` | 4/5 | 35 |
| `res.question` | صياغة سؤال بحث والفرضيات | مناهج البحث العلمي | 5 | `res.literature`, `res.sources` | `res.design`, `res.openproblems` | 4/5 | 30 |
| `res.stats` | الإحصاء التطبيقي للباحث النووي | مناهج البحث العلمي | 5 | `math.stat`, `cs.uq` | `res.writing` | 4/5 | 45 |
| `rx.chain` | التفاعل المتسلسل | هندسة المفاعلات | 5 | `nuc.fission`, `nuc.neutron` | `rx.criticality` | 3/5 | 20 |
| `rx.criticality` | الحرجية والأنظمة دون/فوق الحرجة | هندسة المفاعلات | 5 | `rx.neutroncycle`, `rx.chain` | `disc.ads`, `rx.kinetics` | 4/5 | 40 |
| `rx.fluids` | ميكانيكا الموائع | هندسة المفاعلات | 5 | `math.pde`, `phys.mech` | `env.dispersion`, `env.hydrology`, `fus.mhd`, `rx.thermalhyd` | 4/5 | 50 |
| `rx.heat` | انتقال الحرارة | هندسة المفاعلات | 5 | `math.pde`, `phys.thermo` | `rx.thermalhyd` | 4/5 | 55 |
| `rx.neutroncycle` | دورة النيوترونات | هندسة المفاعلات | 5 | `rx.principles` | `rx.criticality` | 4/5 | 35 |
| `rx.principles` | مبادئ المفاعل النووي | هندسة المفاعلات | 5 | `nuc.fission`, `nuc.neutron` | `disc.education`, `rx.fuel`, `rx.neutroncycle`, `rx.types`, `safe.did` | 3/5 | 35 |
| `rx.thermo_power` | الديناميكا الحرارية لمحطات القدرة | هندسة المفاعلات | 5 | `phys.thermo` | `disc.desal`, `disc.hydrogen`, `rx.economics` | 3/5 | 40 |
| `rx.types` | أنواع المفاعلات | هندسة المفاعلات | 5 | `rx.principles` | `disc.space`, `rx.gen4`, `rx.power`, `rx.research` | 3/5 | 45 |
| `safe.did` | الدفاع في العمق | السلامة النووية والحوادث | 5 | `rad.dosimetry`, `rx.principles` | `pol.regulatory`, `rx.power`, `rx.smr`, `safe.culture`, `safe.reg`, `safe.systems` | 3/5 | 35 |
| `chem.envradio` | الكيمياء الإشعاعية البيئية | الكيمياء | 6 | `chem.radiochemistry`, `env.tracers` | `env.radioecology`, `fuel.disposal` | 4/5 | 40 |
| `chem.hotcells` | تقنيات الخلايا الساخنة والمناولة عن بُعد | الكيمياء | 6 | `chem.radiochemistry`, `prot.principles` | `prot.lab` | 3/5 | 30 |
| `cs.hpc` | الحوسبة عالية الأداء | الحوسبة العلمية والبرمجة | 6 | `cs.python` | — | 4/5 | 35 |
| `disc.education` | تعليم العلوم النووية ومحاكاة التدريب | مجالات مكتشفة/nاشئة | 6 | `res.writing`, `rx.principles` | — | 3/5 | 20 |
| `env.agriculture` | التطبيقات الزراعية للنظائر والإشعاع | البيئة والزراعة والنظائر | 6 | `env.tracers`, `rad.bio` | — | 3/5 | 30 |
| `env.dating` | التأريخ بالنظائر | البيئة والزراعة والنظائر | 6 | `nuc.halflife`, `meas.spectroscopy`, `math.stat` | `env.climate` | 3/5 | 35 |
| `env.dispersion` | انتشار المواد في الغلاف الجوي والماء | البيئة والزراعة والنظائر | 6 | `rx.fluids`, `math.pde`, `env.radioecology` | `disc.nuclear_analytics`, `prot.emergency` | 4/5 | 40 |
| `env.hydrology` | النظائر في الهيدرولوجيا والمياه | البيئة والزراعة والنظائر | 6 | `env.tracers`, `rx.fluids` | `fuel.disposal`, `ind.welllogging` | 4/5 | 40 |
| `env.radioecology` | الإيكولوجيا الإشعاعية | البيئة والزراعة والنظائر | 6 | `chem.envradio`, `rad.bio` | `env.dispersion`, `env.remediation` | 4/5 | 40 |
| `env.tracers` | النظائر البيئية كمتتبعات | البيئة والزراعة والنظائر | 6 | `chem.isotope`, `rad.spectroscopy`, `math.stat` | `chem.envradio`, `env.agriculture`, `env.climate`, `env.hydrology`, `meas.monitoring` | 4/5 | 40 |
| `fuel.decommissioning` | تفكيك المنشآت وإزالة التخصيص | دورة الوقود والنفايات | 6 | `fuel.waste`, `meas.monitoring`, `safe.systems` | `env.remediation` | 4/5 | 40 |
| `fuel.disposal` | التخلص النهائي الجيولوجي | دورة الوقود والنفايات | 6 | `fuel.waste`, `chem.envradio`, `env.hydrology` | — | 5/5 | 45 |
| `fuel.inreactor` | أداء الوقود داخل المفاعل | دورة الوقود والنفايات | 6 | `rx.fuel`, `mat.damage`, `rx.thermalhyd` | `safe.severe` | 5/5 | 45 |
| `fuel.spent` | الوقود المستهلك | دورة الوقود والنفايات | 6 | `fuel.intro`, `nuc.series` | `fuel.reprocessing`, `fuel.storage`, `fuel.waste` | 4/5 | 35 |
| `fuel.storage` | التخزين المؤقت: الرطب والجاف | دورة الوقود والنفايات | 6 | `fuel.spent`, `rad.shielding` | — | 3/5 | 30 |
| `fuel.transport` | نقل المواد المشعة | دورة الوقود والنفايات | 6 | `rad.shielding`, `pol.regulatory` | — | 3/5 | 25 |
| `fuel.waste` | إدارة النفايات المشعة | دورة الوقود والنفايات | 6 | `fuel.spent`, `rad.types`, `pol.regulatory` | `fuel.decommissioning`, `fuel.disposal` | 4/5 | 45 |
| `fus.heating` | تسخين البلازما والتيار المدفوع | الاندماج والبلازما | 6 | `fus.plasma`, `phys.emi` | `fus.tokamak` | 4/5 | 40 |
| `fus.magnetic` | الحبس المغناطيسي | الاندماج والبلازما | 6 | `fus.plasma`, `fus.mhd` | `fus.alt`, `fus.stellarator`, `fus.tokamak` | 4/5 | 40 |
| `fus.mhd` | المغناطيسية الهيدروديناميكية (MHD) | الاندماج والبلازما | 6 | `fus.plasma`, `rx.fluids` | `fus.magnetic` | 5/5 | 50 |
| `ind.activation_analysis` | تحليل المواد بالتنشيط | التطبيقات الصناعية | 6 | `rad.activation` | — | 4/5 | 30 |
| `ind.gauges` | القياسات النووية الصناعية | التطبيقات الصناعية | 6 | `rad.transport` | — | 2/5 | 25 |
| `ind.ndt` | الفحص غير الإتلافي | التطبيقات الصناعية | 6 | `rad.transport`, `ind.radiography` | — | 3/5 | 35 |
| `ind.radiography` | التصوير الإشعاعي الصناعي | التطبيقات الصناعية | 6 | `rad.sources`, `rad.shielding`, `prot.principles` | `ind.ndt` | 3/5 | 35 |
| `ind.sterilization` | التعقيم الإشعاعي وحفظ الأغذية | التطبيقات الصناعية | 6 | `rad.bio`, `rad.dosimetry` | — | 3/5 | 25 |
| `ind.tracers` | المتتبعات النظائرية الصناعية | التطبيقات الصناعية | 6 | `rad.detectors`, `chem.isotope` | — | 3/5 | 25 |
| `ind.welllogging` | تسجيل الآبار النووي والجيوفيزياء | التطبيقات الصناعية | 6 | `rad.detectors`, `env.hydrology` | — | 3/5 | 25 |
| `mat.ceramics` | السيراميك والوقود السيراميكي | المواد النووية | 6 | `mat.intro`, `chem.materials` | `mat.composites`, `mat.fuels`, `mat.hightemp` | 4/5 | 35 |
| `mat.characterization` | توصيف المواد | المواد النووية | 6 | `phys.condmat`, `meas.spectroscopy` | `disc.advancedmanufacturing` | 4/5 | 40 |
| `mat.composites` | المواد المركّبة (SiC/SiC وC/C) | المواد النووية | 6 | `mat.ceramics` | — | 4/5 | 30 |
| `mat.corrosion` | التآكل والتعب والتشقق | المواد النووية | 6 | `mat.metals`, `chem.phys` | `mat.lifetime` | 4/5 | 40 |
| `mat.damage` | التلف الإشعاعي | المواد النووية | 6 | `mat.intro`, `rad.interaction`, `phys.condmat` | `fuel.inreactor`, `fus.materials`, `mat.lifetime`, `rx.materials` | 5/5 | 50 |
| `mat.fuels` | مواد الوقود المتقدمة | المواد النووية | 6 | `mat.ceramics`, `rx.fuel` | `rx.multiphysics` | 5/5 | 40 |
| `mat.hightemp` | مواد درجات الحرارة العالية | المواد النووية | 6 | `mat.metals`, `mat.ceramics` | `fus.materials`, `rx.gen4` | 4/5 | 30 |
| `mat.lifetime` | العمر الافتراضي والموثوقية | المواد النووية | 6 | `mat.damage`, `mat.corrosion`, `safe.human` | — | 4/5 | 35 |
| `mat.metals` | المعادن والسبائك النووية | المواد النووية | 6 | `mat.intro` | `disc.advancedmanufacturing`, `mat.corrosion`, `mat.hightemp` | 4/5 | 40 |
| `meas.monitoring` | المسح الإشعاعي وتوصيف المواقع | الأجهزة والكشف | 6 | `rad.spectroscopy`, `env.tracers` | `disc.nuclear_analytics`, `env.remediation`, `fuel.decommissioning` | 3/5 | 30 |
| `meas.spectroscopy` | التحليل الطيفي المتقدم | الأجهزة والكشف | 6 | `rad.spectroscopy` | `env.dating`, `mat.characterization`, `sec.forensics` | 4/5 | 35 |
| `med.imaging` | التصوير: SPECT وPET وSPECT/CT | التطبيقات الطبية | 6 | `med.nucmed`, `rad.detectors`, `meas.signal` | `disc.theranostics`, `prot.medical` | 4/5 | 50 |
| `med.nucmed` | الطب النووي: مقدمة | التطبيقات الطبية | 6 | `rad.types`, `nuc.halflife`, `rad.dosimetry` | `med.imaging`, `med.rp`, `med.therapy` | 3/5 | 35 |
| `prot.lab` | السلامة في المختبرات الإشعاعية | الحماية من الإشعاع | 6 | `prot.principles`, `chem.hotcells` | — | 3/5 | 30 |
| `rad.activation` | التنشيط النيوتروني وتحليله (NAA) | الإشعاع والقياس | 6 | `nuc.crosssection`, `rad.spectroscopy`, `rx.research` | `ind.activation_analysis` | 4/5 | 35 |
| `res.reproducibility` | التكرارية والحوسبة القابلة للتكرار | مناهج البحث العلمي | 6 | `cs.python`, `res.data`, `cs.vv` | `res.openproblems` | 3/5 | 30 |
| `res.writing` | الكتابة العلمية والنشر | مناهج البحث العلمي | 6 | `res.literature`, `res.stats` | `disc.education`, `res.peerreview` | 3/5 | 35 |
| `rx.control` | التحكم في المفاعل | هندسة المفاعلات | 6 | `rx.kinetics` | `safe.systems` | 4/5 | 40 |
| `rx.cooling` | أنظمة التبريد وأنواع المبردات | هندسة المفاعلات | 6 | `rx.thermalhyd` | `disc.microreactors` | 4/5 | 35 |
| `rx.core` | تصميم القلب وإدارة الوقود | هندسة المفاعلات | 6 | `rx.transport`, `rx.thermalhyd`, `rx.fuel` | — | 5/5 | 50 |
| `rx.diffusion` | نظرية انتشار النيوترونات | هندسة المفاعلات | 6 | `nuc.neutron`, `math.pde`, `math.vectors` | `rx.transport` | 4/5 | 45 |
| `rx.economics` | اقتصاديات الطاقة النووية | هندسة المفاعلات | 6 | `rx.thermo_power`, `math.stat` | `disc.desal`, `disc.economics_risk`, `fus.engineering`, `sec.geopolitics` | 3/5 | 35 |
| `rx.fuel` | وقود المفاعلات | هندسة المفاعلات | 6 | `rx.principles`, `mat.intro` | `fuel.inreactor`, `mat.fuels`, `rx.core`, `rx.gen4` | 4/5 | 40 |
| `rx.gen4` | المفاعلات المتقدمة والجيل الرابع | هندسة المفاعلات | 6 | `rx.types`, `rx.fuel`, `mat.hightemp` | `disc.hydrogen`, `rx.smr` | 5/5 | 50 |
| `rx.instr` | أنظمة القياس والتحكم (I&C) | هندسة المفاعلات | 6 | `meas.detectors`, `rx.kinetics`, `phys.em` | `disc.ai_governance`, `disc.digitaltwin` | 4/5 | 45 |
| `rx.kinetics` | حركية المفاعل | هندسة المفاعلات | 6 | `rx.criticality`, `math.ode`, `cs.numpy` | `rx.control`, `rx.instr` | 4/5 | 50 |
| `rx.materials` | مواد المفاعلات | هندسة المفاعلات | 6 | `mat.intro`, `mat.damage` | — | 4/5 | 40 |
| `rx.multiphysics` | المحاكاة متعددة الفيزياء | هندسة المفاعلات | 6 | `rx.transport`, `rx.thermalhyd`, `mat.fuels`, `cs.vv` | `disc.digitaltwin` | 5/5 | 50 |
| `rx.power` | مفاعلات القدرة: الجيل الثاني والثالث | هندسة المفاعلات | 6 | `rx.types`, `rx.thermalhyd`, `safe.did` | — | 4/5 | 45 |
| `rx.research` | المفاعلات البحثية واستخداماتها | هندسة المفاعلات | 6 | `rx.types` | `med.isotopes`, `rad.activation` | 3/5 | 30 |
| `rx.smr` | المفاعلات الصغيرة والمعيارية والميكروية | هندسة المفاعلات | 6 | `rx.gen4`, `safe.did`, `pol.regulatory` | `disc.microreactors` | 4/5 | 40 |
| `rx.thermalhyd` | الحراريات المائية للمفاعلات | هندسة المفاعلات | 6 | `rx.heat`, `rx.fluids` | `fuel.inreactor`, `rx.cooling`, `rx.core`, `rx.multiphysics`, `rx.power`, `safe.dsa` | 5/5 | 55 |
| `rx.transport` | معادلة الانتقال والطرائق العددية | هندسة المفاعلات | 6 | `rx.diffusion`, `math.mc`, `nuc.data` | `disc.quantum`, `fus.neutronics`, `rx.core`, `rx.multiphysics` | 5/5 | 60 |
| `safe.culture` | ثقافة السلامة والحوكمة | السلامة النووية والحوادث | 6 | `safe.did` | `disc.humanfactors_org`, `pol.governance`, `safe.human` | 3/5 | 30 |
| `safe.dsa` | التقييم الحتمي للسلامة | السلامة النووية والحوادث | 6 | `safe.systems`, `rx.thermalhyd`, `math.nummethods` | `safe.risk`, `safe.severe` | 4/5 | 45 |
| `safe.hazard` | تحليل المخاطر وتحديد الأحداث البادئة | السلامة النووية والحوادث | 6 | `safe.systems`, `math.prob` | `safe.psa` | 4/5 | 40 |
| `safe.human` | العوامل البشرية والموثوقية البشرية | السلامة النووية والحوادث | 6 | `safe.culture`, `math.stat` | `disc.humanfactors_org`, `mat.lifetime`, `safe.accidents`, `safe.psa` | 4/5 | 40 |
| `safe.psa` | التقييم الاحتمالي للسلامة (PSA/PRA) | السلامة النووية والحوادث | 6 | `safe.hazard`, `math.prob`, `safe.human` | `safe.risk`, `safe.severe` | 5/5 | 60 |
| `safe.systems` | أنظمة الأمان والتصنيف | السلامة النووية والحوادث | 6 | `safe.did`, `rx.control` | `fuel.decommissioning`, `safe.dsa`, `safe.hazard` | 4/5 | 40 |
| `env.climate` | النظائر في الدراسات المناخية | البيئة والزراعة والنظائر | 7 | `env.tracers`, `env.dating` | — | 4/5 | 35 |
| `env.remediation` | معالجة المواقع الملوثة وإعادة تأهيلها | البيئة والزراعة والنظائر | 7 | `meas.monitoring`, `env.radioecology`, `fuel.decommissioning` | — | 4/5 | 35 |
| `fuel.reprocessing` | إعادة المعالجة: مفهوم علمي وسياساتي | دورة الوقود والنفايات | 7 | `fuel.spent`, `chem.radiochemistry`, `sec.nonprolif` | `disc.ads`, `disc.transmutation` | 4/5 | 40 |
| `fus.alt` | مفاهيم حبس بديلة ومتوسطة الكثافة | الاندماج والبلازما | 7 | `fus.magnetic`, `fus.inertial` | — | 4/5 | 35 |
| `fus.diagnostics` | تشخيص البلازما | الاندماج والبلازما | 7 | `fus.plasma`, `meas.detectors`, `meas.signal` | — | 5/5 | 45 |
| `fus.inertial` | الحبس بالقصور الذاتي (ICF) | الاندماج والبلازما | 7 | `nuc.fusion_basics`, `phys.emi`, `phys.statmech` | `fus.alt` | 5/5 | 45 |
| `fus.stellarator` | الستيلاراتور | الاندماج والبلازما | 7 | `fus.magnetic` | — | 5/5 | 45 |
| `fus.tokamak` | التوكاماك | الاندماج والبلازما | 7 | `fus.magnetic`, `fus.heating` | `fus.engineering` | 4/5 | 50 |
| `med.dosimetry_plan` | تخطيط الجرعات والفيزياء الطبية | التطبيقات الطبية | 7 | `med.therapy`, `math.mc`, `cs.data` | — | 5/5 | 50 |
| `med.isotopes` | إنتاج النظائر الطبية | التطبيقات الطبية | 7 | `nuc.reactions`, `rx.research`, `chem.radiochemistry` | `disc.theranostics` | 4/5 | 40 |
| `med.rp` | الحماية الإشعاعية في المؤسسات الطبية | التطبيقات الطبية | 7 | `prot.principles`, `med.nucmed` | — | 3/5 | 30 |
| `med.therapy` | العلاج الإشعاعي والعلاج بالنظائر | التطبيقات الطبية | 7 | `rad.bio`, `rad.dosimetry`, `med.nucmed` | `disc.theranostics`, `med.dosimetry_plan`, `prot.medical` | 4/5 | 55 |
| `pol.ethics` | أخلاقيات العلم النووي والتواصل العام | التنظيم والسياسات والحوكمة | 7 | `safe.accidents`, `res.literature` | — | 3/5 | 25 |
| `pol.governance` | الحوكمة النووية وإدارة البرامج | التنظيم والسياسات والحوكمة | 7 | `pol.regulatory`, `safe.culture` | — | 3/5 | 30 |
| `pol.law` | القانون النووي والمسؤولية المدنية | التنظيم والسياسات والحوكمة | 7 | `pol.regulatory` | `disc.economics_risk` | 3/5 | 30 |
| `pol.safeguards` | الضمانات النووية | التنظيم والسياسات والحوكمة | 7 | `pol.regulatory`, `fuel.intro`, `sec.nonprolif` | — | 4/5 | 40 |
| `pol.treaties` | الاتفاقيات والنظام الدولي | التنظيم والسياسات والحوكمة | 7 | `pol.regulatory`, `sec.nonprolif` | `sec.armscontrol`, `sec.geopolitics` | 3/5 | 35 |
| `prot.emergency` | الاستجابة للطوارئ الإشعاعية | الحماية من الإشعاع | 7 | `prot.principles`, `safe.accidents`, `env.dispersion` | — | 4/5 | 40 |
| `res.peerreview` | مراجعة الأقران والنقد العلمي | مناهج البحث العلمي | 7 | `res.writing` | — | 3/5 | 20 |
| `safe.accidents` | الحوادث النووية التاريخية: تحليل | السلامة النووية والحوادث | 7 | `safe.severe`, `safe.human`, `hist.timeline` | `hist.accidents_hist`, `pol.ethics`, `prot.emergency` | 4/5 | 50 |
| `safe.reg` | الرقابة والترخيص والتفتيش | السلامة النووية والحوادث | 7 | `safe.did`, `pol.regulatory` | — | 4/5 | 40 |
| `safe.risk` | إدارة المخاطر واتخاذ القرار | السلامة النووية والحوادث | 7 | `safe.psa`, `safe.dsa`, `cs.uq` | `disc.economics_risk` | 4/5 | 40 |
| `safe.severe` | تحليل الحوادث الشديدة | السلامة النووية والحوادث | 7 | `safe.dsa`, `safe.psa`, `fuel.inreactor` | `safe.accidents` | 5/5 | 55 |
| `sec.nonprolif` | عدم الانتشار النووي | الأمن وعدم الانتشار والتاريخ العسكري | 7 | `hist.timeline`, `fuel.intro` | `fuel.reprocessing`, `pol.safeguards`, `pol.treaties`, `sec.armscontrol`, `sec.deterrence`, `sec.geopolitics` (+1) | 3/5 | 35 |
| `sec.security` | الأمن النووي وحماية المنشآت | الأمن وعدم الانتشار والتاريخ العسكري | 7 | `sec.nonprolif`, `pol.regulatory` | — | 3/5 | 35 |
| `disc.ads` | الأنظمة المدفوعة بالمسرعات (ADS) | مجالات مكتشفة/nاشئة | 8 | `part.accel`, `rx.criticality`, `fuel.reprocessing` | — | 5/5 | 30 |
| `disc.advancedmanufacturing` | التصنيع المتقدم للمكونات النووية | مجالات مكتشفة/nاشئة | 8 | `mat.metals`, `mat.characterization` | — | 4/5 | 30 |
| `disc.desal` | التحلية النووية | مجالات مكتشفة/nاشئة | 8 | `rx.thermo_power`, `rx.economics` | — | 3/5 | 20 |
| `disc.economics_risk` | اقتصاديات المخاطر والتأمين والتمويل النووي | مجالات مكتشفة/nاشئة | 8 | `rx.economics`, `safe.risk`, `pol.law` | — | 4/5 | 30 |
| `disc.humanfactors_org` | السلامة التنظيمية والتعلم المؤسسي | مجالات مكتشفة/nاشئة | 8 | `safe.culture`, `safe.human` | — | 4/5 | 30 |
| `disc.hydrogen` | الهيدروجين والحرارة الصناعية النووية | مجالات مكتشفة/nاشئة | 8 | `rx.thermo_power`, `rx.gen4`, `chem.phys` | — | 4/5 | 30 |
| `disc.microreactors` | المفاعلات الميكروية والتطبيقات غير الكهربائية | مجالات مكتشفة/nاشئة | 8 | `rx.smr`, `rx.cooling` | — | 4/5 | 25 |
| `disc.ml_nuclear` | تعلم الآلة في العلوم النووية | مجالات مكتشفة/nاشئة | 8 | `cs.uq`, `nuc.data`, `cs.numpy` | `disc.ai_governance` | 5/5 | 40 |
| `disc.neutronimaging` | تصوير النيوترونات | مجالات مكتشفة/nاشئة | 8 | `nuc.neutronsci`, `rad.detectors` | — | 4/5 | 25 |
| `disc.nuclear_analytics` | التحليلات النووية للبيانات الضخمة والمراقبة | مجالات مكتشفة/nاشئة | 8 | `env.dispersion`, `meas.monitoring`, `cs.data` | — | 4/5 | 25 |
| `disc.transmutation` | التحويل النووي للأكتينيدات الثانوية | مجالات مكتشفة/nاشئة | 8 | `fuel.reprocessing`, `nuc.reactions` | — | 5/5 | 30 |
| `fus.blanket` | البطانية وتكاثر التريتيوم | الاندماج والبلازما | 8 | `fus.neutronics`, `chem.isotope` | — | 5/5 | 45 |
| `fus.engineering` | هندسة الاندماج واقتصادياته | الاندماج والبلازما | 8 | `fus.tokamak`, `fus.materials`, `rx.economics` | — | 5/5 | 40 |
| `fus.materials` | مواد الاندماج | الاندماج والبلازما | 8 | `mat.damage`, `mat.hightemp` | `fus.engineering` | 5/5 | 45 |
| `fus.neutronics` | نيوترونيات الاندماج | الاندماج والبلازما | 8 | `rx.transport`, `nuc.fusion_basics` | `fus.blanket` | 5/5 | 45 |
| `hist.accidents_hist` | تاريخ الحوادث والسلامة | تاريخ العلوم النووية | 8 | `hist.timeline`, `safe.accidents` | — | 3/5 | 30 |
| `sec.armscontrol` | الحد من التسلح والتحقق | الأمن وعدم الانتشار والتاريخ العسكري | 8 | `sec.nonprolif`, `pol.treaties` | — | 4/5 | 35 |
| `sec.deterrence` | الردع والاستراتيجية النووية | الأمن وعدم الانتشار والتاريخ العسكري | 8 | `sec.nonprolif`, `sec.history` | — | 4/5 | 35 |
| `sec.effects` | آثار الانفجارات النووية | الأمن وعدم الانتشار والتاريخ العسكري | 8 | `rad.interaction`, `rad.bio`, `rad.transport` | — | 4/5 | 35 |
| `sec.forensics` | التحليل الجنائي النووي | الأمن وعدم الانتشار والتاريخ العسكري | 8 | `meas.spectroscopy`, `chem.analytical`, `nuc.data` | — | 4/5 | 35 |
| `sec.geopolitics` | الجغرافيا السياسية النووية | الأمن وعدم الانتشار والتاريخ العسكري | 8 | `sec.nonprolif`, `pol.treaties`, `rx.economics` | — | 3/5 | 30 |
| `sec.history` | التاريخ العسكري النووي | الأمن وعدم الانتشار والتاريخ العسكري | 8 | `hist.timeline` | `sec.deterrence` | 3/5 | 40 |
| `disc.ai_governance` | حوكمة الذكاء الاصطناعي في النظم النووية | مجالات مكتشفة/nاشئة | 9 | `disc.ml_nuclear`, `rx.instr`, `pol.regulatory` | — | 4/5 | 25 |
| `disc.digitaltwin` | التوأم الرقمي للمفاعلات | مجالات مكتشفة/nاشئة | 9 | `rx.multiphysics`, `cs.vv`, `rx.instr` | — | 5/5 | 35 |
| `disc.quantum` | الحوسبة والاستشعار الكمومي في المجال النووي | مجالات مكتشفة/nاشئة | 9 | `phys.qm2`, `cs.uq`, `rx.transport` | — | 5/5 | 30 |
| `disc.space` | الطاقة النووية الفضائية | مجالات مكتشفة/nاشئة | 9 | `rx.types`, `nuc.decay` | — | 4/5 | 30 |
| `disc.theranostics` | الثيرانوستكس (تشخيص+علاج بنظيرين) | مجالات مكتشفة/nاشئة | 9 | `med.isotopes`, `med.therapy`, `med.imaging` | — | 4/5 | 30 |
| `prot.medical` | الحماية الإشعاعية في الطب | الحماية من الإشعاع | 9 | `prot.principles`, `med.imaging`, `med.therapy` | — | 4/5 | 35 |
| `res.openproblems` | المسائل المفتوحة وكيف تختار موضوع بحث | مناهج البحث العلمي | 9 | `res.question`, `res.literature`, `res.reproducibility` | — | 4/5 | 30 |

