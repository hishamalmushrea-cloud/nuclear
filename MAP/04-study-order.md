# MAP/04 — ترتيب الدراسة (Topological Study Order)

الترتيب مولّد طوبولوجياً: لا يظهر موضوع قبل كل شروطه المسبقة. الترتيب داخل المرحلة استرشادي (بالصعوبة ثم المجال).

> ⚙️ **هذا ملف مولّد آلياً.** لا تعدّله يدوياً: عدّل البيانات في `tools/kg/nodes_*.py` ثم نفّذ `python3 tools/build.py`.


## العمود الفقري: أطول مسار زمني في الخريطة

**1,345 ساعة** عبر 31 موضوعاً:

`math.pre` → `math.algebra` → `math.functions` → `math.calc1` → `math.calc2` → `math.vectors` → `phys.mech` → `phys.em` → `phys.emi` → `phys.relativity` → `phys.qm1` → `phys.atomic` → `chem.structure` → `nuc.isotopes` → `nuc.binding` → `nuc.reactions` → `nuc.crosssection` → `nuc.scattering` → `nuc.absorption` → `nuc.neutron` → `rx.principles` → `rx.neutroncycle` → `rx.criticality` → `rx.kinetics` → `rx.control` → `safe.systems` → `safe.hazard` → `safe.psa` → `safe.severe` → `safe.accidents` → `prot.emergency`

هذا المسار هو «الحد الأدنى المتصل» من الأساسيات حتى موضوع بحثي.

## الترتيب بحسب المرحلة

### المرحلة 0: مقدمة عامة
*2 موضوع · 50 ساعة · المجموع التراكمي: 50 ساعة*

1. **الأساس الحسابي والجبري التمهيدي** (`math.pre`) — صعوبة 1/5 · 25 ساعة · الشروط: —
2. **الخط الزمني للعلوم النووية** (`hist.timeline`) — صعوبة 2/5 · 25 ساعة · الشروط: —

### المرحلة 1: رياضيات + فيزياء + كيمياء أساسية
*17 موضوع · 685 ساعة · المجموع التراكمي: 735 ساعة*

1. **الكيمياء العامة** (`chem.general`) — صعوبة 2/5 · 50 ساعة · الشروط: `math.pre`
2. **البرمجة العلمية بـ Python** (`cs.python`) — صعوبة 2/5 · 40 ساعة · الشروط: `math.pre`
3. **الجبر** (`math.algebra`) — صعوبة 2/5 · 45 ساعة · الشروط: `math.pre`
4. **الهندسة** (`math.geometry`) — صعوبة 2/5 · 25 ساعة · الشروط: `math.pre`
5. **الدوال** (`math.functions`) — صعوبة 2/5 · 30 ساعة · الشروط: `math.algebra`
6. **المثلثات** (`math.trig`) — صعوبة 2/5 · 25 ساعة · الشروط: `math.geometry`
7. **الجبر الخطي** (`math.linalg`) — صعوبة 3/5 · 45 ساعة · الشروط: `math.algebra`
8. **NumPy وSciPy وMatplotlib** (`cs.numpy`) — صعوبة 2/5 · 40 ساعة · الشروط: `cs.python`, `math.linalg`
9. **التفاضل** (`math.calc1`) — صعوبة 3/5 · 45 ساعة · الشروط: `math.functions`
10. **التكامل** (`math.calc2`) — صعوبة 3/5 · 45 ساعة · الشروط: `math.calc1`
11. **المعادلات التفاضلية العادية** (`math.ode`) — صعوبة 3/5 · 50 ساعة · الشروط: `math.calc2`
12. **تحليل المتجهات (حساب المتجهات)** (`math.vectors`) — صعوبة 3/5 · 40 ساعة · الشروط: `math.calc2`, `math.linalg`
13. **الميكانيكا الكلاسيكية** (`phys.mech`) — صعوبة 2/5 · 55 ساعة · الشروط: `math.calc1`, `math.vectors`
14. **الطاقة والزخم والزخم الزاوي** (`phys.energy`) — صعوبة 2/5 · 35 ساعة · الشروط: `phys.mech`
15. **الجاذبية والحركة المدارية** (`phys.grav`) — صعوبة 2/5 · 20 ساعة · الشروط: `phys.mech`
16. **الموجات والبصريات** (`phys.waves`) — صعوبة 2/5 · 40 ساعة · الشروط: `math.trig`, `phys.mech`
17. **الكهرباء والمغناطيسية** (`phys.em`) — صعوبة 3/5 · 55 ساعة · الشروط: `math.vectors`, `phys.mech`

### المرحلة 2: فيزياء ذرية وميكانيكا الكم
*14 موضوع · 615 ساعة · المجموع التراكمي: 1,350 ساعة*

1. **الأعداد المركبة** (`math.complex`) — صعوبة 2/5 · 25 ساعة · الشروط: `math.algebra`, `math.trig`
2. **التحليل العددي وطرق الحل العددي** (`math.nummethods`) — صعوبة 3/5 · 50 ساعة · الشروط: `math.calc2`, `math.linalg`
3. **الاحتمالات** (`math.prob`) — صعوبة 3/5 · 40 ساعة · الشروط: `math.calc2`
4. **الإحصاء** (`math.stat`) — صعوبة 3/5 · 45 ساعة · الشروط: `math.prob`
5. **تحليل البيانات وإدارتها** (`cs.data`) — صعوبة 2/5 · 35 ساعة · الشروط: `cs.numpy`, `math.stat`
6. **الكيمياء التحليلية** (`chem.analytical`) — صعوبة 3/5 · 45 ساعة · الشروط: `chem.general`, `math.stat`
7. **الديناميكا الحرارية** (`phys.thermo`) — صعوبة 3/5 · 50 ساعة · الشروط: `math.calc1`, `phys.energy`
8. **الكهرومغناطيسية ومعادلات ماكسويل** (`phys.emi`) — صعوبة 4/5 · 50 ساعة · الشروط: `phys.em`, `math.vectors`
9. **النسبية الخاصة** (`phys.relativity`) — صعوبة 3/5 · 40 ساعة · الشروط: `phys.mech`, `phys.emi`
10. **ميكانيكا الكم (مستوى جامعي)** (`phys.qm1`) — صعوبة 4/5 · 70 ساعة · الشروط: `math.ode`, `math.linalg`, `math.complex`, `phys.emi`, `phys.relativity`
11. **الكيمياء الفيزيائية** (`chem.phys`) — صعوبة 3/5 · 50 ساعة · الشروط: `chem.general`, `phys.thermo`, `phys.qm1`
12. **الفيزياء الذرية** (`phys.atomic`) — صعوبة 3/5 · 45 ساعة · الشروط: `phys.qm1`
13. **البنية الذرية والجدول الدوري** (`chem.structure`) — صعوبة 2/5 · 35 ساعة · الشروط: `chem.general`, `phys.atomic`
14. **الروابط الكيميائية** (`chem.bonding`) — صعوبة 2/5 · 35 ساعة · الشروط: `chem.structure`

### المرحلة 3: فيزياء نووية أساسية
*22 موضوع · 795 ساعة · المجموع التراكمي: 2,145 ساعة*

1. **تاريخ المشاريع والمؤسسات الكبرى** (`hist.projects`) — صعوبة 3/5 · 30 ساعة · الشروط: `hist.timeline`
2. **قراءة الأوراق ومراجعة الأدبيات** (`res.literature`) — صعوبة 3/5 · 35 ساعة · الشروط: `cs.python`
3. **تقييم المصادر ومدقق المصادر** (`res.sources`) — صعوبة 3/5 · 25 ساعة · الشروط: `res.literature`
4. **الفيزياء الإحصائية** (`phys.statmech`) — صعوبة 4/5 · 50 ساعة · الشروط: `phys.thermo`, `math.prob`
5. **الجسيمات الأولية: مقدمة** (`part.intro`) — صعوبة 3/5 · 30 ساعة · الشروط: `phys.qm1`, `phys.relativity`
6. **القوى الأساسية الأربع** (`part.forces`) — صعوبة 3/5 · 30 ساعة · الشروط: `part.intro`
7. **الفيزياء الجزيئية** (`phys.molecular`) — صعوبة 3/5 · 30 ساعة · الشروط: `phys.atomic`
8. **النظائر والنويدات وخريطة النويدات** (`nuc.isotopes`) — صعوبة 2/5 · 25 ساعة · الشروط: `phys.atomic`, `chem.structure`
9. **الكيمياء غير العضوية** (`chem.inorganic`) — صعوبة 3/5 · 45 ساعة · الشروط: `chem.bonding`, `chem.structure`
10. **الكيمياء العضوية** (`chem.organic`) — صعوبة 3/5 · 45 ساعة · الشروط: `chem.bonding`
11. **الطاقة الرابطة ونقص الكتلة** (`nuc.binding`) — صعوبة 3/5 · 35 ساعة · الشروط: `nuc.isotopes`, `phys.relativity`
12. **مقدمة الفيزياء النووية** (`nuc.intro`) — صعوبة 3/5 · 40 ساعة · الشروط: `phys.atomic`, `phys.relativity`, `nuc.isotopes`
13. **النيوكليونات والقوة النووية** (`nuc.nucleons`) — صعوبة 3/5 · 35 ساعة · الشروط: `nuc.intro`, `part.forces`
14. **الاستقرار النووي وخط الاستقرار** (`nuc.stability`) — صعوبة 3/5 · 30 ساعة · الشروط: `nuc.binding`, `nuc.isotopes`
15. **التفاعلات النووية والـ Q-value** (`nuc.reactions`) — صعوبة 4/5 · 45 ساعة · الشروط: `nuc.binding`, `phys.energy`, `phys.relativity`
16. **التحلل الإشعاعي وأنواعه** (`nuc.decay`) — صعوبة 3/5 · 50 ساعة · الشروط: `nuc.stability`, `phys.qm1`
17. **المقاطع العرضية** (`nuc.crosssection`) — صعوبة 4/5 · 45 ساعة · الشروط: `nuc.reactions`, `math.prob`
18. **الانشطار النووي** (`nuc.fission`) — صعوبة 4/5 · 50 ساعة · الشروط: `nuc.binding`, `nuc.reactions`
19. **الاندماج النووي: الأساس الفيزيائي** (`nuc.fusion_basics`) — صعوبة 4/5 · 40 ساعة · الشروط: `nuc.binding`, `nuc.reactions`, `phys.statmech`
20. **عمر النصف وقانون التحلل والنشاط** (`nuc.halflife`) — صعوبة 2/5 · 30 ساعة · الشروط: `nuc.decay`, `math.ode`
21. **أنواع الإشعاع** (`rad.types`) — صعوبة 2/5 · 25 ساعة · الشروط: `nuc.decay`, `phys.atomic`
22. **مصادر الإشعاع** (`rad.sources`) — صعوبة 2/5 · 25 ساعة · الشروط: `rad.types`, `nuc.halflife`

### المرحلة 4: فيزياء نووية متقدمة
*36 موضوع · 1625 ساعة · المجموع التراكمي: 3,770 ساعة*

1. **نظرية الزمر والتماثل** (`math.grouptheory`) — صعوبة 5/5 · 45 ساعة · الشروط: `math.linalg`
2. **التحليل الرياضي** (`math.analysis`) — صعوبة 4/5 · 50 ساعة · الشروط: `math.calc2`
3. **المعادلات التفاضلية الجزئية** (`math.pde`) — صعوبة 4/5 · 60 ساعة · الشروط: `math.ode`, `math.vectors`
4. **رياضيات متقدمة للعلوم النووية** (`math.advanced`) — صعوبة 5/5 · 60 ساعة · الشروط: `math.pde`, `math.analysis`, `math.complex`
5. **الإلكترونيات النووية** (`meas.electronics`) — صعوبة 4/5 · 45 ساعة · الشروط: `phys.em`, `math.complex`
6. **معالجة الإشارات والحصول على البيانات** (`meas.signal`) — صعوبة 4/5 · 40 ساعة · الشروط: `meas.electronics`, `math.analysis`, `cs.numpy`
7. **أساسيات المسرعات** (`phys.accel_basics`) — صعوبة 3/5 · 35 ساعة · الشروط: `phys.em`, `phys.relativity`
8. **فيزياء المادة المكثفة** (`phys.condmat`) — صعوبة 4/5 · 45 ساعة · الشروط: `phys.qm1`, `phys.statmech`
9. **ميكانيكا الكم المتقدمة ونظرية التشتت** (`phys.qm2`) — صعوبة 5/5 · 60 ساعة · الشروط: `phys.qm1`, `math.advanced`
10. **الكواركات واللبتونات والبوزونات** (`part.quarks`) — صعوبة 4/5 · 35 ساعة · الشروط: `part.intro`
11. **النموذج القياسي** (`part.sm`) — صعوبة 5/5 · 50 ساعة · الشروط: `part.intro`, `math.grouptheory`, `phys.qm2`
12. **كيمياء المواد** (`chem.materials`) — صعوبة 3/5 · 35 ساعة · الشروط: `chem.bonding`, `phys.condmat`
13. **سلوك النظائر وفصلها** (`chem.isotope`) — صعوبة 4/5 · 45 ساعة · الشروط: `chem.phys`, `nuc.isotopes`
14. **الكتل النووية وجداول الكتل** (`nuc.mass`) — صعوبة 3/5 · 20 ساعة · الشروط: `nuc.binding`
15. **نماذج النواة** (`nuc.models`) — صعوبة 5/5 · 60 ساعة · الشروط: `phys.qm2`, `nuc.stability`
16. **البيانات النووية (Nuclear Data)** (`nuc.data`) — صعوبة 3/5 · 35 ساعة · الشروط: `nuc.crosssection`, `cs.data`
17. **التشتت النووي** (`nuc.scattering`) — صعوبة 4/5 · 40 ساعة · الشروط: `nuc.crosssection`, `phys.qm2`
18. **بنية النواة المتقدمة** (`nuc.structure`) — صعوبة 5/5 · 45 ساعة · الشروط: `nuc.models`
19. **الفيزياء النووية النظرية** (`nuc.theory`) — صعوبة 5/5 · 60 ساعة · الشروط: `nuc.models`, `phys.qm2`
20. **فيزياء النيوترينو** (`part.neutrino`) — صعوبة 5/5 · 40 ساعة · الشروط: `part.sm`, `nuc.decay`
21. **الامتصاص والرنين والنماذج النووية للتفاعل** (`nuc.absorption`) — صعوبة 4/5 · 40 ساعة · الشروط: `nuc.crosssection`, `nuc.scattering`
22. **سلاسل التحلل والتوازن الإشعاعي** (`nuc.series`) — صعوبة 4/5 · 35 ساعة · الشروط: `nuc.halflife`, `math.ode`
23. **تفاعل الإشعاع مع المادة** (`rad.interaction`) — صعوبة 4/5 · 55 ساعة · الشروط: `rad.types`, `phys.atomic`, `phys.emi`
24. **تقنيات الكواشف: نظرة هندسية** (`meas.detectors`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.interaction`
25. **التلوث الإشعاعي والتعرض** (`rad.contamination`) — صعوبة 3/5 · 30 ساعة · الشروط: `rad.types`, `rad.sources`
26. **الكيمياء الإشعاعية** (`chem.radiochemistry`) — صعوبة 4/5 · 50 ساعة · الشروط: `chem.inorganic`, `nuc.decay`, `rad.interaction`
27. **فيزياء النيوترونات** (`nuc.neutron`) — صعوبة 4/5 · 50 ساعة · الشروط: `nuc.crosssection`, `nuc.absorption`
28. **كواشف الإشعاع** (`rad.detectors`) — صعوبة 4/5 · 60 ساعة · الشروط: `rad.interaction`, `phys.em`, `meas.electronics`
29. **انتقال الإشعاع والتوهين** (`rad.transport`) — صعوبة 4/5 · 45 ساعة · الشروط: `rad.interaction`, `math.ode`
30. **الكيمياء النووية** (`chem.nuclear`) — صعوبة 4/5 · 50 ساعة · الشروط: `chem.radiochemistry`, `nuc.reactions`
31. **الفيزياء النووية التجريبية** (`nuc.exp`) — صعوبة 4/5 · 50 ساعة · الشروط: `nuc.decay`, `meas.detectors`, `math.stat`
32. **كواشف الجسيمات** (`part.detectors`) — صعوبة 4/5 · 40 ساعة · الشروط: `part.quarks`, `rad.detectors`
33. **الجرعة: الممتصة والمكافئة والفعالة** (`rad.dosimetry`) — صعوبة 4/5 · 50 ساعة · الشروط: `rad.interaction`, `rad.transport`
34. **التدريع** (`rad.shielding`) — صعوبة 4/5 · 45 ساعة · الشروط: `rad.transport`, `rad.interaction`
35. **التحليل الطيفي الإشعاعي** (`rad.spectroscopy`) — صعوبة 4/5 · 50 ساعة · الشروط: `rad.detectors`, `meas.signal`, `math.stat`
36. **معايرة الأجهزة ومصادر الخطأ** (`meas.calibration`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.spectroscopy`, `math.stat`

### المرحلة 5: الهندسة النووية
*33 موضوع · 1305 ساعة · المجموع التراكمي: 5,075 ساعة*

1. **التحسين والبحث العملياتي** (`math.optimization`) — صعوبة 3/5 · 35 ساعة · الشروط: `math.linalg`, `math.calc1`
2. **صياغة سؤال بحث والفرضيات** (`res.question`) — صعوبة 4/5 · 30 ساعة · الشروط: `res.literature`, `res.sources`
3. **طرق مونتي كارلو** (`math.mc`) — صعوبة 4/5 · 45 ساعة · الشروط: `math.prob`, `math.stat`, `cs.python`
4. **ميكانيكا الموائع** (`rx.fluids`) — صعوبة 4/5 · 50 ساعة · الشروط: `math.pde`, `phys.mech`
5. **كمّنة عدم اليقين (UQ)** (`cs.uq`) — صعوبة 4/5 · 45 ساعة · الشروط: `math.stat`, `math.mc`, `cs.numpy`
6. **الديناميكا الحرارية لمحطات القدرة** (`rx.thermo_power`) — صعوبة 3/5 · 40 ساعة · الشروط: `phys.thermo`
7. **التحقق والتحقق من الصحة (V&V)** (`cs.vv`) — صعوبة 4/5 · 35 ساعة · الشروط: `cs.uq`, `math.nummethods`
8. **الإحصاء التطبيقي للباحث النووي** (`res.stats`) — صعوبة 4/5 · 45 ساعة · الشروط: `math.stat`, `cs.uq`
9. **انتقال الحرارة** (`rx.heat`) — صعوبة 4/5 · 55 ساعة · الشروط: `math.pde`, `phys.thermo`
10. **فيزياء البلازما: الأساس** (`fus.plasma`) — صعوبة 4/5 · 55 ساعة · الشروط: `phys.emi`, `phys.statmech`, `math.vectors`
11. **فيزياء المسرعات** (`part.accel`) — صعوبة 5/5 · 45 ساعة · الشروط: `phys.accel_basics`, `phys.emi`
12. **نظرية الحقول الكمومية** (`part.qft`) — صعوبة 5/5 · 80 ساعة · الشروط: `part.sm`, `phys.qm2`, `math.advanced`
13. **المواد النووية: مقدمة** (`mat.intro`) — صعوبة 3/5 · 30 ساعة · الشروط: `phys.condmat`, `chem.materials`
14. **دورة الوقود النووي: نظرة شاملة** (`fuel.intro`) — صعوبة 3/5 · 35 ساعة · الشروط: `nuc.fission`, `chem.inorganic`
15. **الفيزياء النووية الفلكية والتخليق النووي** (`nuc.astro`) — صعوبة 4/5 · 40 ساعة · الشروط: `nuc.fusion_basics`, `nuc.reactions`
16. **مصادر المواد النووية** (`fuel.resources`) — صعوبة 2/5 · 25 ساعة · الشروط: `fuel.intro`, `chem.inorganic`
17. **تحويل وتخصيب وتصنيع الوقود** (`fuel.fabrication`) — صعوبة 4/5 · 35 ساعة · الشروط: `fuel.resources`, `chem.isotope`
18. **التفاعل المتسلسل** (`rx.chain`) — صعوبة 3/5 · 20 ساعة · الشروط: `nuc.fission`, `nuc.neutron`
19. **مبادئ المفاعل النووي** (`rx.principles`) — صعوبة 3/5 · 35 ساعة · الشروط: `nuc.fission`, `nuc.neutron`
20. **علم النيوترونات (مصادر وتشتت)** (`nuc.neutronsci`) — صعوبة 4/5 · 40 ساعة · الشروط: `nuc.neutron`, `phys.condmat`
21. **أنواع المفاعلات** (`rx.types`) — صعوبة 3/5 · 45 ساعة · الشروط: `rx.principles`
22. **الدفاع في العمق** (`safe.did`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.dosimetry`, `rx.principles`
23. **علم الأحياء الإشعاعي والتأثيرات البيولوجية** (`rad.bio`) — صعوبة 4/5 · 55 ساعة · الشروط: `rad.dosimetry`, `chem.radiochemistry`
24. **دورة النيوترونات** (`rx.neutroncycle`) — صعوبة 4/5 · 35 ساعة · الشروط: `rx.principles`
25. **التفاعلات عالية الطاقة** (`part.hep`) — صعوبة 5/5 · 40 ساعة · الشروط: `part.sm`, `part.detectors`
26. **الهيئات الرقابية والمعايير** (`pol.regulatory`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.dosimetry`, `safe.did`
27. **مبادئ الحماية الإشعاعية** (`prot.principles`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.dosimetry`, `rad.bio`
28. **قياسات الإشعاع والقياسات المرجعية (Metrology)** (`rad.metrology`) — صعوبة 4/5 · 35 ساعة · الشروط: `rad.dosimetry`, `meas.calibration`
29. **الحرجية والأنظمة دون/فوق الحرجة** (`rx.criticality`) — صعوبة 4/5 · 40 ساعة · الشروط: `rx.neutroncycle`, `rx.chain`
30. **المراقبة وقياس الجرعات** (`prot.monitoring`) — صعوبة 3/5 · 35 ساعة · الشروط: `prot.principles`, `rad.detectors`
31. **تصميم التجارب الآمن** (`res.design`) — صعوبة 4/5 · 35 ساعة · الشروط: `res.question`, `prot.principles`, `math.stat`
32. **الوقاية المهنية والصحة المهنية** (`prot.occupational`) — صعوبة 3/5 · 35 ساعة · الشروط: `prot.monitoring`, `rad.contamination`
33. **إدارة البيانات وإتاحتها** (`res.data`) — صعوبة 3/5 · 25 ساعة · الشروط: `cs.data`, `res.design`

### المرحلة 6: المفاعلات والحراريات والمواد
*66 موضوع · 2530 ساعة · المجموع التراكمي: 7,605 ساعة*

1. **الحوسبة عالية الأداء** (`cs.hpc`) — صعوبة 4/5 · 35 ساعة · الشروط: `cs.python`
2. **الكتابة العلمية والنشر** (`res.writing`) — صعوبة 3/5 · 35 ساعة · الشروط: `res.literature`, `res.stats`
3. **اقتصاديات الطاقة النووية** (`rx.economics`) — صعوبة 3/5 · 35 ساعة · الشروط: `rx.thermo_power`, `math.stat`
4. **الحراريات المائية للمفاعلات** (`rx.thermalhyd`) — صعوبة 5/5 · 55 ساعة · الشروط: `rx.heat`, `rx.fluids`
5. **تسخين البلازما والتيار المدفوع** (`fus.heating`) — صعوبة 4/5 · 40 ساعة · الشروط: `fus.plasma`, `phys.emi`
6. **أنظمة التبريد وأنواع المبردات** (`rx.cooling`) — صعوبة 4/5 · 35 ساعة · الشروط: `rx.thermalhyd`
7. **المغناطيسية الهيدروديناميكية (MHD)** (`fus.mhd`) — صعوبة 5/5 · 50 ساعة · الشروط: `fus.plasma`, `rx.fluids`
8. **الحبس المغناطيسي** (`fus.magnetic`) — صعوبة 4/5 · 40 ساعة · الشروط: `fus.plasma`, `fus.mhd`
9. **السيراميك والوقود السيراميكي** (`mat.ceramics`) — صعوبة 4/5 · 35 ساعة · الشروط: `mat.intro`, `chem.materials`
10. **المعادن والسبائك النووية** (`mat.metals`) — صعوبة 4/5 · 40 ساعة · الشروط: `mat.intro`
11. **المواد المركّبة (SiC/SiC وC/C)** (`mat.composites`) — صعوبة 4/5 · 30 ساعة · الشروط: `mat.ceramics`
12. **التآكل والتعب والتشقق** (`mat.corrosion`) — صعوبة 4/5 · 40 ساعة · الشروط: `mat.metals`, `chem.phys`
13. **مواد درجات الحرارة العالية** (`mat.hightemp`) — صعوبة 4/5 · 30 ساعة · الشروط: `mat.metals`, `mat.ceramics`
14. **الوقود المستهلك** (`fuel.spent`) — صعوبة 4/5 · 35 ساعة · الشروط: `fuel.intro`, `nuc.series`
15. **التلف الإشعاعي** (`mat.damage`) — صعوبة 5/5 · 50 ساعة · الشروط: `mat.intro`, `rad.interaction`, `phys.condmat`
16. **القياسات النووية الصناعية** (`ind.gauges`) — صعوبة 2/5 · 25 ساعة · الشروط: `rad.transport`
17. **المتتبعات النظائرية الصناعية** (`ind.tracers`) — صعوبة 3/5 · 25 ساعة · الشروط: `rad.detectors`, `chem.isotope`
18. **نظرية انتشار النيوترونات** (`rx.diffusion`) — صعوبة 4/5 · 45 ساعة · الشروط: `nuc.neutron`, `math.pde`, `math.vectors`
19. **مواد المفاعلات** (`rx.materials`) — صعوبة 4/5 · 40 ساعة · الشروط: `mat.intro`, `mat.damage`
20. **تعليم العلوم النووية ومحاكاة التدريب** (`disc.education`) — صعوبة 3/5 · 20 ساعة · الشروط: `res.writing`, `rx.principles`
21. **التخزين المؤقت: الرطب والجاف** (`fuel.storage`) — صعوبة 3/5 · 30 ساعة · الشروط: `fuel.spent`, `rad.shielding`
22. **الطب النووي: مقدمة** (`med.nucmed`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.types`, `nuc.halflife`, `rad.dosimetry`
23. **النظائر البيئية كمتتبعات** (`env.tracers`) — صعوبة 4/5 · 40 ساعة · الشروط: `chem.isotope`, `rad.spectroscopy`, `math.stat`
24. **التحليل الطيفي المتقدم** (`meas.spectroscopy`) — صعوبة 4/5 · 35 ساعة · الشروط: `rad.spectroscopy`
25. **وقود المفاعلات** (`rx.fuel`) — صعوبة 4/5 · 40 ساعة · الشروط: `rx.principles`, `mat.intro`
26. **معادلة الانتقال والطرائق العددية** (`rx.transport`) — صعوبة 5/5 · 60 ساعة · الشروط: `rx.diffusion`, `math.mc`, `nuc.data`
27. **التطبيقات الزراعية للنظائر والإشعاع** (`env.agriculture`) — صعوبة 3/5 · 30 ساعة · الشروط: `env.tracers`, `rad.bio`
28. **التأريخ بالنظائر** (`env.dating`) — صعوبة 3/5 · 35 ساعة · الشروط: `nuc.halflife`, `meas.spectroscopy`, `math.stat`
29. **التعقيم الإشعاعي وحفظ الأغذية** (`ind.sterilization`) — صعوبة 3/5 · 25 ساعة · الشروط: `rad.bio`, `rad.dosimetry`
30. **المسح الإشعاعي وتوصيف المواقع** (`meas.monitoring`) — صعوبة 3/5 · 30 ساعة · الشروط: `rad.spectroscopy`, `env.tracers`
31. **المفاعلات البحثية واستخداماتها** (`rx.research`) — صعوبة 3/5 · 30 ساعة · الشروط: `rx.types`
32. **ثقافة السلامة والحوكمة** (`safe.culture`) — صعوبة 3/5 · 30 ساعة · الشروط: `safe.did`
33. **الكيمياء الإشعاعية البيئية** (`chem.envradio`) — صعوبة 4/5 · 40 ساعة · الشروط: `chem.radiochemistry`, `env.tracers`
34. **النظائر في الهيدرولوجيا والمياه** (`env.hydrology`) — صعوبة 4/5 · 40 ساعة · الشروط: `env.tracers`, `rx.fluids`
35. **توصيف المواد** (`mat.characterization`) — صعوبة 4/5 · 40 ساعة · الشروط: `phys.condmat`, `meas.spectroscopy`
36. **التصوير: SPECT وPET وSPECT/CT** (`med.imaging`) — صعوبة 4/5 · 50 ساعة · الشروط: `med.nucmed`, `rad.detectors`, `meas.signal`
37. **مفاعلات القدرة: الجيل الثاني والثالث** (`rx.power`) — صعوبة 4/5 · 45 ساعة · الشروط: `rx.types`, `rx.thermalhyd`, `safe.did`
38. **أداء الوقود داخل المفاعل** (`fuel.inreactor`) — صعوبة 5/5 · 45 ساعة · الشروط: `rx.fuel`, `mat.damage`, `rx.thermalhyd`
39. **مواد الوقود المتقدمة** (`mat.fuels`) — صعوبة 5/5 · 40 ساعة · الشروط: `mat.ceramics`, `rx.fuel`
40. **تصميم القلب وإدارة الوقود** (`rx.core`) — صعوبة 5/5 · 50 ساعة · الشروط: `rx.transport`, `rx.thermalhyd`, `rx.fuel`
41. **المفاعلات المتقدمة والجيل الرابع** (`rx.gen4`) — صعوبة 5/5 · 50 ساعة · الشروط: `rx.types`, `rx.fuel`, `mat.hightemp`
42. **تقنيات الخلايا الساخنة والمناولة عن بُعد** (`chem.hotcells`) — صعوبة 3/5 · 30 ساعة · الشروط: `chem.radiochemistry`, `prot.principles`
43. **نقل المواد المشعة** (`fuel.transport`) — صعوبة 3/5 · 25 ساعة · الشروط: `rad.shielding`, `pol.regulatory`
44. **التصوير الإشعاعي الصناعي** (`ind.radiography`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.sources`, `rad.shielding`, `prot.principles`
45. **تسجيل الآبار النووي والجيوفيزياء** (`ind.welllogging`) — صعوبة 3/5 · 25 ساعة · الشروط: `rad.detectors`, `env.hydrology`
46. **الإيكولوجيا الإشعاعية** (`env.radioecology`) — صعوبة 4/5 · 40 ساعة · الشروط: `chem.envradio`, `rad.bio`
47. **إدارة النفايات المشعة** (`fuel.waste`) — صعوبة 4/5 · 45 ساعة · الشروط: `fuel.spent`, `rad.types`, `pol.regulatory`
48. **التنشيط النيوتروني وتحليله (NAA)** (`rad.activation`) — صعوبة 4/5 · 35 ساعة · الشروط: `nuc.crosssection`, `rad.spectroscopy`, `rx.research`
49. **حركية المفاعل** (`rx.kinetics`) — صعوبة 4/5 · 50 ساعة · الشروط: `rx.criticality`, `math.ode`, `cs.numpy`
50. **المفاعلات الصغيرة والمعيارية والميكروية** (`rx.smr`) — صعوبة 4/5 · 40 ساعة · الشروط: `rx.gen4`, `safe.did`, `pol.regulatory`
51. **العوامل البشرية والموثوقية البشرية** (`safe.human`) — صعوبة 4/5 · 40 ساعة · الشروط: `safe.culture`, `math.stat`
52. **المحاكاة متعددة الفيزياء** (`rx.multiphysics`) — صعوبة 5/5 · 50 ساعة · الشروط: `rx.transport`, `rx.thermalhyd`, `mat.fuels`, `cs.vv`
53. **الفحص غير الإتلافي** (`ind.ndt`) — صعوبة 3/5 · 35 ساعة · الشروط: `rad.transport`, `ind.radiography`
54. **السلامة في المختبرات الإشعاعية** (`prot.lab`) — صعوبة 3/5 · 30 ساعة · الشروط: `prot.principles`, `chem.hotcells`
55. **انتشار المواد في الغلاف الجوي والماء** (`env.dispersion`) — صعوبة 4/5 · 40 ساعة · الشروط: `rx.fluids`, `math.pde`, `env.radioecology`
56. **تحليل المواد بالتنشيط** (`ind.activation_analysis`) — صعوبة 4/5 · 30 ساعة · الشروط: `rad.activation`
57. **العمر الافتراضي والموثوقية** (`mat.lifetime`) — صعوبة 4/5 · 35 ساعة · الشروط: `mat.damage`, `mat.corrosion`, `safe.human`
58. **التحكم في المفاعل** (`rx.control`) — صعوبة 4/5 · 40 ساعة · الشروط: `rx.kinetics`
59. **أنظمة القياس والتحكم (I&C)** (`rx.instr`) — صعوبة 4/5 · 45 ساعة · الشروط: `meas.detectors`, `rx.kinetics`, `phys.em`
60. **التخلص النهائي الجيولوجي** (`fuel.disposal`) — صعوبة 5/5 · 45 ساعة · الشروط: `fuel.waste`, `chem.envradio`, `env.hydrology`
61. **التكرارية والحوسبة القابلة للتكرار** (`res.reproducibility`) — صعوبة 3/5 · 30 ساعة · الشروط: `cs.python`, `res.data`, `cs.vv`
62. **أنظمة الأمان والتصنيف** (`safe.systems`) — صعوبة 4/5 · 40 ساعة · الشروط: `safe.did`, `rx.control`
63. **تفكيك المنشآت وإزالة التخصيص** (`fuel.decommissioning`) — صعوبة 4/5 · 40 ساعة · الشروط: `fuel.waste`, `meas.monitoring`, `safe.systems`
64. **التقييم الحتمي للسلامة** (`safe.dsa`) — صعوبة 4/5 · 45 ساعة · الشروط: `safe.systems`, `rx.thermalhyd`, `math.nummethods`
65. **تحليل المخاطر وتحديد الأحداث البادئة** (`safe.hazard`) — صعوبة 4/5 · 40 ساعة · الشروط: `safe.systems`, `math.prob`
66. **التقييم الاحتمالي للسلامة (PSA/PRA)** (`safe.psa`) — صعوبة 5/5 · 60 ساعة · الشروط: `safe.hazard`, `math.prob`, `safe.human`

### المرحلة 7: الإشعاع والكواشف والحماية
*25 موضوع · 980 ساعة · المجموع التراكمي: 8,585 ساعة*

1. **مراجعة الأقران والنقد العلمي** (`res.peerreview`) — صعوبة 3/5 · 20 ساعة · الشروط: `res.writing`
2. **التوكاماك** (`fus.tokamak`) — صعوبة 4/5 · 50 ساعة · الشروط: `fus.magnetic`, `fus.heating`
3. **الستيلاراتور** (`fus.stellarator`) — صعوبة 5/5 · 45 ساعة · الشروط: `fus.magnetic`
4. **الحبس بالقصور الذاتي (ICF)** (`fus.inertial`) — صعوبة 5/5 · 45 ساعة · الشروط: `nuc.fusion_basics`, `phys.emi`, `phys.statmech`
5. **عدم الانتشار النووي** (`sec.nonprolif`) — صعوبة 3/5 · 35 ساعة · الشروط: `hist.timeline`, `fuel.intro`
6. **مفاهيم حبس بديلة ومتوسطة الكثافة** (`fus.alt`) — صعوبة 4/5 · 35 ساعة · الشروط: `fus.magnetic`, `fus.inertial`
7. **إعادة المعالجة: مفهوم علمي وسياساتي** (`fuel.reprocessing`) — صعوبة 4/5 · 40 ساعة · الشروط: `fuel.spent`, `chem.radiochemistry`, `sec.nonprolif`
8. **تشخيص البلازما** (`fus.diagnostics`) — صعوبة 5/5 · 45 ساعة · الشروط: `fus.plasma`, `meas.detectors`, `meas.signal`
9. **العلاج الإشعاعي والعلاج بالنظائر** (`med.therapy`) — صعوبة 4/5 · 55 ساعة · الشروط: `rad.bio`, `rad.dosimetry`, `med.nucmed`
10. **الحماية الإشعاعية في المؤسسات الطبية** (`med.rp`) — صعوبة 3/5 · 30 ساعة · الشروط: `prot.principles`, `med.nucmed`
11. **الحوكمة النووية وإدارة البرامج** (`pol.governance`) — صعوبة 3/5 · 30 ساعة · الشروط: `pol.regulatory`, `safe.culture`
12. **القانون النووي والمسؤولية المدنية** (`pol.law`) — صعوبة 3/5 · 30 ساعة · الشروط: `pol.regulatory`
13. **الاتفاقيات والنظام الدولي** (`pol.treaties`) — صعوبة 3/5 · 35 ساعة · الشروط: `pol.regulatory`, `sec.nonprolif`
14. **الأمن النووي وحماية المنشآت** (`sec.security`) — صعوبة 3/5 · 35 ساعة · الشروط: `sec.nonprolif`, `pol.regulatory`
15. **النظائر في الدراسات المناخية** (`env.climate`) — صعوبة 4/5 · 35 ساعة · الشروط: `env.tracers`, `env.dating`
16. **إنتاج النظائر الطبية** (`med.isotopes`) — صعوبة 4/5 · 40 ساعة · الشروط: `nuc.reactions`, `rx.research`, `chem.radiochemistry`
17. **الضمانات النووية** (`pol.safeguards`) — صعوبة 4/5 · 40 ساعة · الشروط: `pol.regulatory`, `fuel.intro`, `sec.nonprolif`
18. **الرقابة والترخيص والتفتيش** (`safe.reg`) — صعوبة 4/5 · 40 ساعة · الشروط: `safe.did`, `pol.regulatory`
19. **تخطيط الجرعات والفيزياء الطبية** (`med.dosimetry_plan`) — صعوبة 5/5 · 50 ساعة · الشروط: `med.therapy`, `math.mc`, `cs.data`
20. **معالجة المواقع الملوثة وإعادة تأهيلها** (`env.remediation`) — صعوبة 4/5 · 35 ساعة · الشروط: `meas.monitoring`, `env.radioecology`, `fuel.decommissioning`
21. **إدارة المخاطر واتخاذ القرار** (`safe.risk`) — صعوبة 4/5 · 40 ساعة · الشروط: `safe.psa`, `safe.dsa`, `cs.uq`
22. **تحليل الحوادث الشديدة** (`safe.severe`) — صعوبة 5/5 · 55 ساعة · الشروط: `safe.dsa`, `safe.psa`, `fuel.inreactor`
23. **الحوادث النووية التاريخية: تحليل** (`safe.accidents`) — صعوبة 4/5 · 50 ساعة · الشروط: `safe.severe`, `safe.human`, `hist.timeline`
24. **أخلاقيات العلم النووي والتواصل العام** (`pol.ethics`) — صعوبة 3/5 · 25 ساعة · الشروط: `safe.accidents`, `res.literature`
25. **الاستجابة للطوارئ الإشعاعية** (`prot.emergency`) — صعوبة 4/5 · 40 ساعة · الشروط: `prot.principles`, `safe.accidents`, `env.dispersion`

### المرحلة 8: السلامة النووية
*22 موضوع · 730 ساعة · المجموع التراكمي: 9,315 ساعة*

1. **التاريخ العسكري النووي** (`sec.history`) — صعوبة 3/5 · 40 ساعة · الشروط: `hist.timeline`
2. **التحلية النووية** (`disc.desal`) — صعوبة 3/5 · 20 ساعة · الشروط: `rx.thermo_power`, `rx.economics`
3. **تعلم الآلة في العلوم النووية** (`disc.ml_nuclear`) — صعوبة 5/5 · 40 ساعة · الشروط: `cs.uq`, `nuc.data`, `cs.numpy`
4. **الردع والاستراتيجية النووية** (`sec.deterrence`) — صعوبة 4/5 · 35 ساعة · الشروط: `sec.nonprolif`, `sec.history`
5. **مواد الاندماج** (`fus.materials`) — صعوبة 5/5 · 45 ساعة · الشروط: `mat.damage`, `mat.hightemp`
6. **تصوير النيوترونات** (`disc.neutronimaging`) — صعوبة 4/5 · 25 ساعة · الشروط: `nuc.neutronsci`, `rad.detectors`
7. **التحويل النووي للأكتينيدات الثانوية** (`disc.transmutation`) — صعوبة 5/5 · 30 ساعة · الشروط: `fuel.reprocessing`, `nuc.reactions`
8. **هندسة الاندماج واقتصادياته** (`fus.engineering`) — صعوبة 5/5 · 40 ساعة · الشروط: `fus.tokamak`, `fus.materials`, `rx.economics`
9. **آثار الانفجارات النووية** (`sec.effects`) — صعوبة 4/5 · 35 ساعة · الشروط: `rad.interaction`, `rad.bio`, `rad.transport`
10. **التحليل الجنائي النووي** (`sec.forensics`) — صعوبة 4/5 · 35 ساعة · الشروط: `meas.spectroscopy`, `chem.analytical`, `nuc.data`
11. **نيوترونيات الاندماج** (`fus.neutronics`) — صعوبة 5/5 · 45 ساعة · الشروط: `rx.transport`, `nuc.fusion_basics`
12. **التصنيع المتقدم للمكونات النووية** (`disc.advancedmanufacturing`) — صعوبة 4/5 · 30 ساعة · الشروط: `mat.metals`, `mat.characterization`
13. **الهيدروجين والحرارة الصناعية النووية** (`disc.hydrogen`) — صعوبة 4/5 · 30 ساعة · الشروط: `rx.thermo_power`, `rx.gen4`, `chem.phys`
14. **الأنظمة المدفوعة بالمسرعات (ADS)** (`disc.ads`) — صعوبة 5/5 · 30 ساعة · الشروط: `part.accel`, `rx.criticality`, `fuel.reprocessing`
15. **البطانية وتكاثر التريتيوم** (`fus.blanket`) — صعوبة 5/5 · 45 ساعة · الشروط: `fus.neutronics`, `chem.isotope`
16. **الجغرافيا السياسية النووية** (`sec.geopolitics`) — صعوبة 3/5 · 30 ساعة · الشروط: `sec.nonprolif`, `pol.treaties`, `rx.economics`
17. **السلامة التنظيمية والتعلم المؤسسي** (`disc.humanfactors_org`) — صعوبة 4/5 · 30 ساعة · الشروط: `safe.culture`, `safe.human`
18. **المفاعلات الميكروية والتطبيقات غير الكهربائية** (`disc.microreactors`) — صعوبة 4/5 · 25 ساعة · الشروط: `rx.smr`, `rx.cooling`
19. **الحد من التسلح والتحقق** (`sec.armscontrol`) — صعوبة 4/5 · 35 ساعة · الشروط: `sec.nonprolif`, `pol.treaties`
20. **التحليلات النووية للبيانات الضخمة والمراقبة** (`disc.nuclear_analytics`) — صعوبة 4/5 · 25 ساعة · الشروط: `env.dispersion`, `meas.monitoring`, `cs.data`
21. **اقتصاديات المخاطر والتأمين والتمويل النووي** (`disc.economics_risk`) — صعوبة 4/5 · 30 ساعة · الشروط: `rx.economics`, `safe.risk`, `pol.law`
22. **تاريخ الحوادث والسلامة** (`hist.accidents_hist`) — صعوبة 3/5 · 30 ساعة · الشروط: `hist.timeline`, `safe.accidents`

### المرحلة 9: التطبيقات الطبية والصناعية والبيئية
*7 موضوع · 215 ساعة · المجموع التراكمي: 9,530 ساعة*

1. **الطاقة النووية الفضائية** (`disc.space`) — صعوبة 4/5 · 30 ساعة · الشروط: `rx.types`, `nuc.decay`
2. **الحوسبة والاستشعار الكمومي في المجال النووي** (`disc.quantum`) — صعوبة 5/5 · 30 ساعة · الشروط: `phys.qm2`, `cs.uq`, `rx.transport`
3. **الحماية الإشعاعية في الطب** (`prot.medical`) — صعوبة 4/5 · 35 ساعة · الشروط: `prot.principles`, `med.imaging`, `med.therapy`
4. **الثيرانوستكس (تشخيص+علاج بنظيرين)** (`disc.theranostics`) — صعوبة 4/5 · 30 ساعة · الشروط: `med.isotopes`, `med.therapy`, `med.imaging`
5. **حوكمة الذكاء الاصطناعي في النظم النووية** (`disc.ai_governance`) — صعوبة 4/5 · 25 ساعة · الشروط: `disc.ml_nuclear`, `rx.instr`, `pol.regulatory`
6. **التوأم الرقمي للمفاعلات** (`disc.digitaltwin`) — صعوبة 5/5 · 35 ساعة · الشروط: `rx.multiphysics`, `cs.vv`, `rx.instr`
7. **المسائل المفتوحة وكيف تختار موضوع بحث** (`res.openproblems`) — صعوبة 4/5 · 30 ساعة · الشروط: `res.question`, `res.literature`, `res.reproducibility`

