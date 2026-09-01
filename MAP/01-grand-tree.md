# MAP/01 — الشجرة الكبرى للعلوم والتكنولوجيا النووية

المصدر الوحيد للحقيقة: `tools/kg/nodes_*.py` → `graph/knowledge_graph.json`.

> ⚙️ **هذا ملف مولّد آلياً.** لا تعدّله يدوياً: عدّل البيانات في `tools/kg/nodes_*.py` ثم نفّذ `python3 tools/build.py`.


## إحصاءات الخريطة

- عدد العقد (الموضوعات): **244**
- عدد المجالات: **22**
- إجمالي الساعات التقديرية لكل الخريطة: **9,530 ساعة**
- الساعات للمواد **الأساسية (core)** فقط: **5,490 ساعة** (≈ 3 سنوات دراسة بدوام كامل)
- أطول سلسلة شرط مسبق (عمق الرسم): **31** مستوى

## الشجرة بحسب المجال

### الرياضيات — `math` (Mathematics)
*20 موضوع · 830 ساعة تقديرية*

- **الأساس الحسابي والجبري التمهيدي** · *Pre-algebra & numeric fluency* · `math.pre`  
  المرحلة 0 (مقدمة عامة) · صعوبة 1/5 · 25 ساعة · 🔵 أساسي · الشروط: —
- **الجبر** · *Algebra* · `math.algebra`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.pre`
- **الدوال** · *Functions* · `math.functions`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 30 ساعة · 🔵 أساسي · الشروط: `math.algebra`
- **الهندسة** · *Geometry* · `math.geometry`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 25 ساعة · ⚪ مساند · الشروط: `math.pre`
- **المثلثات** · *Trigonometry* · `math.trig`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 25 ساعة · ⚪ مساند · الشروط: `math.geometry`
- **التفاضل** · *Differential calculus* · `math.calc1`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.functions`
- **التكامل** · *Integral calculus* · `math.calc2`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.calc1`
- **الجبر الخطي** · *Linear algebra* · `math.linalg`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.algebra`
- **المعادلات التفاضلية العادية** · *Ordinary differential equations* · `math.ode`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 3/5 · 50 ساعة · 🔵 أساسي · الشروط: `math.calc2`
- **تحليل المتجهات (حساب المتجهات)** · *Vector calculus* · `math.vectors`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 3/5 · 40 ساعة · 🔵 أساسي · الشروط: `math.calc2`, `math.linalg`
- **الأعداد المركبة** · *Complex numbers* · `math.complex`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 2/5 · 25 ساعة · ⚪ مساند · الشروط: `math.algebra`, `math.trig`
- **التحليل العددي وطرق الحل العددي** · *Numerical analysis* · `math.nummethods`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 50 ساعة · 🔵 أساسي · الشروط: `math.calc2`, `math.linalg`
- **الاحتمالات** · *Probability* · `math.prob`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 40 ساعة · 🔵 أساسي · الشروط: `math.calc2`
- **الإحصاء** · *Statistics* · `math.stat`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.prob`
- **التحليل الرياضي** · *Mathematical analysis* · `math.analysis`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 50 ساعة · 🟣 متقدم · الشروط: `math.calc2`
- **المعادلات التفاضلية الجزئية** · *Partial differential equations* · `math.pde`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 60 ساعة · 🟣 متقدم · الشروط: `math.ode`, `math.vectors`
- **رياضيات متقدمة للعلوم النووية** · *Advanced methods for nuclear science* · `math.advanced`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 60 ساعة · 🟣 متقدم · الشروط: `math.pde`, `math.analysis`, `math.complex`
- **نظرية الزمر والتماثل** · *Group theory & symmetry* · `math.grouptheory`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 45 ساعة · 🟠 تخصصي · الشروط: `math.linalg`
- **التحسين والبحث العملياتي** · *Optimization & operations research* · `math.optimization`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · ⚪ مساند · الشروط: `math.linalg`, `math.calc1`
- **طرق مونتي كارلو** · *Monte Carlo methods* · `math.mc`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.prob`, `math.stat`, `cs.python`

### تاريخ العلوم النووية — `hist` (History of Nuclear Science)
*3 موضوع · 85 ساعة تقديرية*

- **الخط الزمني للعلوم النووية** · *Timeline of nuclear science* · `hist.timeline`  
  المرحلة 0 (مقدمة عامة) · صعوبة 2/5 · 25 ساعة · 🔵 أساسي · الشروط: —
- **تاريخ المشاريع والمؤسسات الكبرى** · *History of major projects & institutions* · `hist.projects`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `hist.timeline`
- **تاريخ الحوادث والسلامة** · *History of accidents & safety evolution* · `hist.accidents_hist`  
  المرحلة 8 (السلامة النووية) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `hist.timeline`, `safe.accidents`

### الحوسبة العلمية والبرمجة — `comp` (Scientific Computing)
*6 موضوع · 230 ساعة تقديرية*

- **NumPy وSciPy وMatplotlib** · *NumPy / SciPy / Matplotlib* · `cs.numpy`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 40 ساعة · 🔵 أساسي · الشروط: `cs.python`, `math.linalg`
- **البرمجة العلمية بـ Python** · *Scientific programming with Python* · `cs.python`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 40 ساعة · 🔵 أساسي · الشروط: `math.pre`
- **تحليل البيانات وإدارتها** · *Data analysis & management* · `cs.data`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 2/5 · 35 ساعة · 🔵 أساسي · الشروط: `cs.numpy`, `math.stat`
- **كمّنة عدم اليقين (UQ)** · *Uncertainty quantification* · `cs.uq`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.stat`, `math.mc`, `cs.numpy`
- **التحقق والتحقق من الصحة (V&V)** · *Verification & validation* · `cs.vv`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `cs.uq`, `math.nummethods`
- **الحوسبة عالية الأداء** · *High-performance computing* · `cs.hpc`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 35 ساعة · ⚪ مساند · الشروط: `cs.python`

### الفيزياء الأساسية — `phys` (Core Physics)
*15 موضوع · 680 ساعة تقديرية*

- **الطاقة والزخم والزخم الزاوي** · *Energy, momentum & angular momentum* · `phys.energy`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 35 ساعة · 🔵 أساسي · الشروط: `phys.mech`
- **الجاذبية والحركة المدارية** · *Gravitation & orbital motion* · `phys.grav`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 20 ساعة · ⚪ مساند · الشروط: `phys.mech`
- **الميكانيكا الكلاسيكية** · *Classical mechanics* · `phys.mech`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 55 ساعة · 🔵 أساسي · الشروط: `math.calc1`, `math.vectors`
- **الموجات والبصريات** · *Waves & optics* · `phys.waves`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 40 ساعة · ⚪ مساند · الشروط: `math.trig`, `phys.mech`
- **الكهرباء والمغناطيسية** · *Electricity & magnetism* · `phys.em`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 3/5 · 55 ساعة · 🔵 أساسي · الشروط: `math.vectors`, `phys.mech`
- **الفيزياء الذرية** · *Atomic physics* · `phys.atomic`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `phys.qm1`
- **النسبية الخاصة** · *Special relativity* · `phys.relativity`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 40 ساعة · 🔵 أساسي · الشروط: `phys.mech`, `phys.emi`
- **الديناميكا الحرارية** · *Thermodynamics* · `phys.thermo`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 50 ساعة · 🔵 أساسي · الشروط: `math.calc1`, `phys.energy`
- **الكهرومغناطيسية ومعادلات ماكسويل** · *Electromagnetism & Maxwell's equations* · `phys.emi`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `phys.em`, `math.vectors`
- **ميكانيكا الكم (مستوى جامعي)** · *Quantum mechanics (undergraduate)* · `phys.qm1`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 4/5 · 70 ساعة · 🔵 أساسي · الشروط: `math.ode`, `math.linalg`, `math.complex`, `phys.emi`, `phys.relativity`
- **الفيزياء الجزيئية** · *Molecular physics* · `phys.molecular`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `phys.atomic`
- **الفيزياء الإحصائية** · *Statistical physics* · `phys.statmech`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `phys.thermo`, `math.prob`
- **أساسيات المسرعات** · *Accelerator basics* · `phys.accel_basics`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 3/5 · 35 ساعة · ⚪ مساند · الشروط: `phys.em`, `phys.relativity`
- **فيزياء المادة المكثفة** · *Condensed matter physics* · `phys.condmat`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 45 ساعة · ⚪ مساند · الشروط: `phys.qm1`, `phys.statmech`
- **ميكانيكا الكم المتقدمة ونظرية التشتت** · *Advanced QM & scattering theory* · `phys.qm2`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 60 ساعة · 🟣 متقدم · الشروط: `phys.qm1`, `math.advanced`

### الكيمياء — `chem` (Chemistry)
*13 موضوع · 555 ساعة تقديرية*

- **الكيمياء العامة** · *General chemistry* · `chem.general`  
  المرحلة 1 (رياضيات + فيزياء + كيمياء أساسية) · صعوبة 2/5 · 50 ساعة · 🔵 أساسي · الشروط: `math.pre`
- **الروابط الكيميائية** · *Chemical bonding* · `chem.bonding`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 2/5 · 35 ساعة · 🔵 أساسي · الشروط: `chem.structure`
- **البنية الذرية والجدول الدوري** · *Atomic structure & periodic table* · `chem.structure`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 2/5 · 35 ساعة · 🔵 أساسي · الشروط: `chem.general`, `phys.atomic`
- **الكيمياء التحليلية** · *Analytical chemistry* · `chem.analytical`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `chem.general`, `math.stat`
- **الكيمياء الفيزيائية** · *Physical chemistry* · `chem.phys`  
  المرحلة 2 (فيزياء ذرية وميكانيكا الكم) · صعوبة 3/5 · 50 ساعة · 🔵 أساسي · الشروط: `chem.general`, `phys.thermo`, `phys.qm1`
- **الكيمياء غير العضوية** · *Inorganic chemistry* · `chem.inorganic`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `chem.bonding`, `chem.structure`
- **الكيمياء العضوية** · *Organic chemistry* · `chem.organic`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 45 ساعة · ⚪ مساند · الشروط: `chem.bonding`
- **كيمياء المواد** · *Materials chemistry* · `chem.materials`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 3/5 · 35 ساعة · ⚪ مساند · الشروط: `chem.bonding`, `phys.condmat`
- **سلوك النظائر وفصلها** · *Isotope behaviour & separation science* · `chem.isotope`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 45 ساعة · 🟣 متقدم · الشروط: `chem.phys`, `nuc.isotopes`
- **الكيمياء النووية** · *Nuclear chemistry* · `chem.nuclear`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `chem.radiochemistry`, `nuc.reactions`
- **الكيمياء الإشعاعية** · *Radiochemistry* · `chem.radiochemistry`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `chem.inorganic`, `nuc.decay`, `rad.interaction`
- **تقنيات الخلايا الساخنة والمناولة عن بُعد** · *Hot cells & remote handling* · `chem.hotcells`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · 🟠 تخصصي · الشروط: `chem.radiochemistry`, `prot.principles`
- **الكيمياء الإشعاعية البيئية** · *Environmental radiochemistry* · `chem.envradio`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🟠 تخصصي · الشروط: `chem.radiochemistry`, `env.tracers`

### فيزياء الجسيمات — `part` (Particle Physics)
*9 موضوع · 390 ساعة تقديرية*

- **القوى الأساسية الأربع** · *Fundamental forces* · `part.forces`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `part.intro`
- **الجسيمات الأولية: مقدمة** · *Elementary particles: introduction* · `part.intro`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `phys.qm1`, `phys.relativity`
- **كواشف الجسيمات** · *Particle detectors* · `part.detectors`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 40 ساعة · 🟠 تخصصي · الشروط: `part.quarks`, `rad.detectors`
- **الكواركات واللبتونات والبوزونات** · *Quarks, leptons & bosons* · `part.quarks`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `part.intro`
- **فيزياء النيوترينو** · *Neutrino physics* · `part.neutrino`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 40 ساعة · 🟣 متقدم · الشروط: `part.sm`, `nuc.decay`
- **النموذج القياسي** · *The Standard Model* · `part.sm`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 50 ساعة · 🔵 أساسي · الشروط: `part.intro`, `math.grouptheory`, `phys.qm2`
- **فيزياء المسرعات** · *Accelerator physics* · `part.accel`  
  المرحلة 5 (الهندسة النووية) · صعوبة 5/5 · 45 ساعة · 🟠 تخصصي · الشروط: `phys.accel_basics`, `phys.emi`
- **التفاعلات عالية الطاقة** · *High-energy interactions* · `part.hep`  
  المرحلة 5 (الهندسة النووية) · صعوبة 5/5 · 40 ساعة · 🟠 تخصصي · الشروط: `part.sm`, `part.detectors`
- **نظرية الحقول الكمومية** · *Quantum field theory* · `part.qft`  
  المرحلة 5 (الهندسة النووية) · صعوبة 5/5 · 80 ساعة · 🔬 بحثي · الشروط: `part.sm`, `phys.qm2`, `math.advanced`

### الفيزياء النووية — `nuc` (Nuclear Physics)
*23 موضوع · 940 ساعة تقديرية*

- **عمر النصف وقانون التحلل والنشاط** · *Half-life, decay law & activity* · `nuc.halflife`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 2/5 · 30 ساعة · 🔵 أساسي · الشروط: `nuc.decay`, `math.ode`
- **النظائر والنويدات وخريطة النويدات** · *Isotopes, nuclides & the chart of nuclides* · `nuc.isotopes`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 2/5 · 25 ساعة · 🔵 أساسي · الشروط: `phys.atomic`, `chem.structure`
- **الطاقة الرابطة ونقص الكتلة** · *Binding energy & mass defect* · `nuc.binding`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `nuc.isotopes`, `phys.relativity`
- **التحلل الإشعاعي وأنواعه** · *Radioactive decay modes* · `nuc.decay`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 50 ساعة · 🔵 أساسي · الشروط: `nuc.stability`, `phys.qm1`
- **مقدمة الفيزياء النووية** · *Introduction to nuclear physics* · `nuc.intro`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 40 ساعة · 🔵 أساسي · الشروط: `phys.atomic`, `phys.relativity`, `nuc.isotopes`
- **النيوكليونات والقوة النووية** · *Nucleons & the nuclear force* · `nuc.nucleons`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `nuc.intro`, `part.forces`
- **الاستقرار النووي وخط الاستقرار** · *Nuclear stability & the valley of stability* · `nuc.stability`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `nuc.binding`, `nuc.isotopes`
- **المقاطع العرضية** · *Cross sections* · `nuc.crosssection`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `nuc.reactions`, `math.prob`
- **الانشطار النووي** · *Nuclear fission* · `nuc.fission`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `nuc.binding`, `nuc.reactions`
- **الاندماج النووي: الأساس الفيزيائي** · *Nuclear fusion: physical basis* · `nuc.fusion_basics`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `nuc.binding`, `nuc.reactions`, `phys.statmech`
- **التفاعلات النووية والـ Q-value** · *Nuclear reactions & Q-values* · `nuc.reactions`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `nuc.binding`, `phys.energy`, `phys.relativity`
- **البيانات النووية (Nuclear Data)** · *Nuclear data* · `nuc.data`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `nuc.crosssection`, `cs.data`
- **الكتل النووية وجداول الكتل** · *Nuclear masses & mass tables* · `nuc.mass`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 3/5 · 20 ساعة · ⚪ مساند · الشروط: `nuc.binding`
- **الامتصاص والرنين والنماذج النووية للتفاعل** · *Absorption, resonances & reaction models* · `nuc.absorption`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 40 ساعة · 🟣 متقدم · الشروط: `nuc.crosssection`, `nuc.scattering`
- **الفيزياء النووية التجريبية** · *Experimental nuclear physics* · `nuc.exp`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 50 ساعة · 🟣 متقدم · الشروط: `nuc.decay`, `meas.detectors`, `math.stat`
- **فيزياء النيوترونات** · *Neutron physics* · `nuc.neutron`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `nuc.crosssection`, `nuc.absorption`
- **التشتت النووي** · *Nuclear scattering* · `nuc.scattering`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 40 ساعة · 🟣 متقدم · الشروط: `nuc.crosssection`, `phys.qm2`
- **سلاسل التحلل والتوازن الإشعاعي** · *Decay chains & secular equilibrium* · `nuc.series`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `nuc.halflife`, `math.ode`
- **نماذج النواة** · *Nuclear models* · `nuc.models`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 60 ساعة · 🟣 متقدم · الشروط: `phys.qm2`, `nuc.stability`
- **بنية النواة المتقدمة** · *Advanced nuclear structure* · `nuc.structure`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 45 ساعة · 🟣 متقدم · الشروط: `nuc.models`
- **الفيزياء النووية النظرية** · *Theoretical nuclear physics* · `nuc.theory`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 5/5 · 60 ساعة · 🟣 متقدم · الشروط: `nuc.models`, `phys.qm2`
- **الفيزياء النووية الفلكية والتخليق النووي** · *Nuclear astrophysics & nucleosynthesis* · `nuc.astro`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 40 ساعة · 🟠 تخصصي · الشروط: `nuc.fusion_basics`, `nuc.reactions`
- **علم النيوترونات (مصادر وتشتت)** · *Neutron science (sources & scattering)* · `nuc.neutronsci`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 40 ساعة · 🟠 تخصصي · الشروط: `nuc.neutron`, `phys.condmat`

### الإشعاع والقياس — `rad` (Radiation & Measurement)
*12 موضوع · 510 ساعة تقديرية*

- **مصادر الإشعاع** · *Radiation sources* · `rad.sources`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 2/5 · 25 ساعة · 🔵 أساسي · الشروط: `rad.types`, `nuc.halflife`
- **أنواع الإشعاع** · *Types of ionizing radiation* · `rad.types`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 2/5 · 25 ساعة · 🔵 أساسي · الشروط: `nuc.decay`, `phys.atomic`
- **التلوث الإشعاعي والتعرض** · *Contamination & exposure* · `rad.contamination`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `rad.types`, `rad.sources`
- **كواشف الإشعاع** · *Radiation detectors* · `rad.detectors`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 60 ساعة · 🔵 أساسي · الشروط: `rad.interaction`, `phys.em`, `meas.electronics`
- **الجرعة: الممتصة والمكافئة والفعالة** · *Dosimetry: absorbed, equivalent & effective dose* · `rad.dosimetry`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `rad.interaction`, `rad.transport`
- **تفاعل الإشعاع مع المادة** · *Radiation interactions with matter* · `rad.interaction`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 55 ساعة · 🔵 أساسي · الشروط: `rad.types`, `phys.atomic`, `phys.emi`
- **التدريع** · *Radiation shielding* · `rad.shielding`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `rad.transport`, `rad.interaction`
- **التحليل الطيفي الإشعاعي** · *Radiation spectroscopy* · `rad.spectroscopy`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `rad.detectors`, `meas.signal`, `math.stat`
- **انتقال الإشعاع والتوهين** · *Radiation transport & attenuation* · `rad.transport`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `rad.interaction`, `math.ode`
- **علم الأحياء الإشعاعي والتأثيرات البيولوجية** · *Radiobiology & biological effects* · `rad.bio`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 55 ساعة · 🔵 أساسي · الشروط: `rad.dosimetry`, `chem.radiochemistry`
- **قياسات الإشعاع والقياسات المرجعية (Metrology)** · *Radiation metrology & standards* · `rad.metrology`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `rad.dosimetry`, `meas.calibration`
- **التنشيط النيوتروني وتحليله (NAA)** · *Neutron activation & NAA* · `rad.activation`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `nuc.crosssection`, `rad.spectroscopy`, `rx.research`

### مناهج البحث العلمي — `res` (Research Methodology)
*10 موضوع · 310 ساعة تقديرية*

- **قراءة الأوراق ومراجعة الأدبيات** · *Reading papers & literature review* · `res.literature`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `cs.python`
- **تقييم المصادر ومدقق المصادر** · *Source evaluation & auditing* · `res.sources`  
  المرحلة 3 (فيزياء نووية أساسية) · صعوبة 3/5 · 25 ساعة · 🔵 أساسي · الشروط: `res.literature`
- **إدارة البيانات وإتاحتها** · *Data management & FAIR principles* · `res.data`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 25 ساعة · ⚪ مساند · الشروط: `cs.data`, `res.design`
- **تصميم التجارب الآمن** · *Safe experimental design* · `res.design`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `res.question`, `prot.principles`, `math.stat`
- **صياغة سؤال بحث والفرضيات** · *Formulating research questions & hypotheses* · `res.question`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 30 ساعة · 🔵 أساسي · الشروط: `res.literature`, `res.sources`
- **الإحصاء التطبيقي للباحث النووي** · *Applied statistics for nuclear research* · `res.stats`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `math.stat`, `cs.uq`
- **التكرارية والحوسبة القابلة للتكرار** · *Reproducibility & reproducible computing* · `res.reproducibility`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `cs.python`, `res.data`, `cs.vv`
- **الكتابة العلمية والنشر** · *Scientific writing & publishing* · `res.writing`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `res.literature`, `res.stats`
- **مراجعة الأقران والنقد العلمي** · *Peer review & scientific critique* · `res.peerreview`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 20 ساعة · ⚪ مساند · الشروط: `res.writing`
- **المسائل المفتوحة وكيف تختار موضوع بحث** · *Open problems & choosing a topic* · `res.openproblems`  
  المرحلة 9 (التطبيقات الطبية والصناعية والبيئية) · صعوبة 4/5 · 30 ساعة · 🔵 أساسي · الشروط: `res.question`, `res.literature`, `res.reproducibility`

### الأجهزة والكشف — `meas` (Instrumentation & Detection)
*6 موضوع · 220 ساعة تقديرية*

- **معايرة الأجهزة ومصادر الخطأ** · *Instrument calibration & error sources* · `meas.calibration`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.spectroscopy`, `math.stat`
- **تقنيات الكواشف: نظرة هندسية** · *Detector technologies: engineering view* · `meas.detectors`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.interaction`
- **الإلكترونيات النووية** · *Nuclear electronics* · `meas.electronics`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `phys.em`, `math.complex`
- **معالجة الإشارات والحصول على البيانات** · *Signal processing & data acquisition* · `meas.signal`  
  المرحلة 4 (فيزياء نووية متقدمة) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `meas.electronics`, `math.analysis`, `cs.numpy`
- **المسح الإشعاعي وتوصيف المواقع** · *Radiological surveying & site characterization* · `meas.monitoring`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · 🟠 تخصصي · الشروط: `rad.spectroscopy`, `env.tracers`
- **التحليل الطيفي المتقدم** · *Advanced spectroscopy* · `meas.spectroscopy`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `rad.spectroscopy`

### هندسة المفاعلات — `rx` (Reactor Engineering)
*24 موضوع · 1030 ساعة تقديرية*

- **التفاعل المتسلسل** · *Chain reaction* · `rx.chain`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 20 ساعة · 🔵 أساسي · الشروط: `nuc.fission`, `nuc.neutron`
- **مبادئ المفاعل النووي** · *Nuclear reactor principles* · `rx.principles`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `nuc.fission`, `nuc.neutron`
- **الديناميكا الحرارية لمحطات القدرة** · *Power-plant thermodynamics* · `rx.thermo_power`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 40 ساعة · ⚪ مساند · الشروط: `phys.thermo`
- **أنواع المفاعلات** · *Reactor types* · `rx.types`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 45 ساعة · 🔵 أساسي · الشروط: `rx.principles`
- **الحرجية والأنظمة دون/فوق الحرجة** · *Criticality* · `rx.criticality`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `rx.neutroncycle`, `rx.chain`
- **ميكانيكا الموائع** · *Fluid mechanics* · `rx.fluids`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `math.pde`, `phys.mech`
- **انتقال الحرارة** · *Heat transfer* · `rx.heat`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 55 ساعة · 🔵 أساسي · الشروط: `math.pde`, `phys.thermo`
- **دورة النيوترونات** · *The neutron cycle* · `rx.neutroncycle`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `rx.principles`
- **اقتصاديات الطاقة النووية** · *Nuclear energy economics* · `rx.economics`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 35 ساعة · ⚪ مساند · الشروط: `rx.thermo_power`, `math.stat`
- **المفاعلات البحثية واستخداماتها** · *Research reactors & their uses* · `rx.research`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `rx.types`
- **التحكم في المفاعل** · *Reactor control* · `rx.control`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `rx.kinetics`
- **أنظمة التبريد وأنواع المبردات** · *Cooling systems & coolants* · `rx.cooling`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `rx.thermalhyd`
- **نظرية انتشار النيوترونات** · *Neutron diffusion theory* · `rx.diffusion`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `nuc.neutron`, `math.pde`, `math.vectors`
- **وقود المفاعلات** · *Reactor fuel* · `rx.fuel`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `rx.principles`, `mat.intro`
- **أنظمة القياس والتحكم (I&C)** · *Instrumentation & control* · `rx.instr`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `meas.detectors`, `rx.kinetics`, `phys.em`
- **حركية المفاعل** · *Reactor kinetics* · `rx.kinetics`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `rx.criticality`, `math.ode`, `cs.numpy`
- **مواد المفاعلات** · *Reactor materials* · `rx.materials`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `mat.intro`, `mat.damage`
- **مفاعلات القدرة: الجيل الثاني والثالث** · *Power reactors: Gen II & Gen III/III+* · `rx.power`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `rx.types`, `rx.thermalhyd`, `safe.did`
- **المفاعلات الصغيرة والمعيارية والميكروية** · *SMRs, modular & microreactors* · `rx.smr`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🟣 متقدم · الشروط: `rx.gen4`, `safe.did`, `pol.regulatory`
- **تصميم القلب وإدارة الوقود** · *Core design & fuel management* · `rx.core`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 50 ساعة · 🟣 متقدم · الشروط: `rx.transport`, `rx.thermalhyd`, `rx.fuel`
- **المفاعلات المتقدمة والجيل الرابع** · *Advanced reactors & Gen-IV* · `rx.gen4`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 50 ساعة · 🟣 متقدم · الشروط: `rx.types`, `rx.fuel`, `mat.hightemp`
- **المحاكاة متعددة الفيزياء** · *Multiphysics simulation* · `rx.multiphysics`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 50 ساعة · 🟣 متقدم · الشروط: `rx.transport`, `rx.thermalhyd`, `mat.fuels`, `cs.vv`
- **الحراريات المائية للمفاعلات** · *Reactor thermal-hydraulics* · `rx.thermalhyd`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 55 ساعة · 🔵 أساسي · الشروط: `rx.heat`, `rx.fluids`
- **معادلة الانتقال والطرائق العددية** · *Transport equation & numerical methods* · `rx.transport`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 60 ساعة · 🔵 أساسي · الشروط: `rx.diffusion`, `math.mc`, `nuc.data`

### دورة الوقود والنفايات — `fuel` (Fuel Cycle & Waste)
*11 موضوع · 400 ساعة تقديرية*

- **مصادر المواد النووية** · *Nuclear material resources* · `fuel.resources`  
  المرحلة 5 (الهندسة النووية) · صعوبة 2/5 · 25 ساعة · ⚪ مساند · الشروط: `fuel.intro`, `chem.inorganic`
- **دورة الوقود النووي: نظرة شاملة** · *The nuclear fuel cycle: overview* · `fuel.intro`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `nuc.fission`, `chem.inorganic`
- **تحويل وتخصيب وتصنيع الوقود** · *Conversion, enrichment & fuel fabrication* · `fuel.fabrication`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 35 ساعة · ⚪ مساند · الشروط: `fuel.resources`, `chem.isotope`
- **التخزين المؤقت: الرطب والجاف** · *Interim storage: wet & dry* · `fuel.storage`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `fuel.spent`, `rad.shielding`
- **نقل المواد المشعة** · *Transport of radioactive material* · `fuel.transport`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 25 ساعة · ⚪ مساند · الشروط: `rad.shielding`, `pol.regulatory`
- **تفكيك المنشآت وإزالة التخصيص** · *Decommissioning & decommissioning planning* · `fuel.decommissioning`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🟠 تخصصي · الشروط: `fuel.waste`, `meas.monitoring`, `safe.systems`
- **الوقود المستهلك** · *Spent nuclear fuel* · `fuel.spent`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `fuel.intro`, `nuc.series`
- **إدارة النفايات المشعة** · *Radioactive waste management* · `fuel.waste`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `fuel.spent`, `rad.types`, `pol.regulatory`
- **التخلص النهائي الجيولوجي** · *Geological disposal* · `fuel.disposal`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 45 ساعة · 🟣 متقدم · الشروط: `fuel.waste`, `chem.envradio`, `env.hydrology`
- **أداء الوقود داخل المفاعل** · *In-reactor fuel performance* · `fuel.inreactor`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 45 ساعة · 🟣 متقدم · الشروط: `rx.fuel`, `mat.damage`, `rx.thermalhyd`
- **إعادة المعالجة: مفهوم علمي وسياساتي** · *Reprocessing: science & policy* · `fuel.reprocessing`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 40 ساعة · 🟣 متقدم · الشروط: `fuel.spent`, `chem.radiochemistry`, `sec.nonprolif`

### المواد النووية — `mat` (Nuclear Materials)
*10 موضوع · 370 ساعة تقديرية*

- **المواد النووية: مقدمة** · *Introduction to nuclear materials* · `mat.intro`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `phys.condmat`, `chem.materials`
- **السيراميك والوقود السيراميكي** · *Ceramics & ceramic fuels* · `mat.ceramics`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 35 ساعة · ⚪ مساند · الشروط: `mat.intro`, `chem.materials`
- **توصيف المواد** · *Materials characterization* · `mat.characterization`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🟠 تخصصي · الشروط: `phys.condmat`, `meas.spectroscopy`
- **المواد المركّبة (SiC/SiC وC/C)** · *Composites (SiC/SiC, C/C)* · `mat.composites`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 30 ساعة · 🟠 تخصصي · الشروط: `mat.ceramics`
- **التآكل والتعب والتشقق** · *Corrosion, fatigue & cracking* · `mat.corrosion`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `mat.metals`, `chem.phys`
- **مواد درجات الحرارة العالية** · *High-temperature materials* · `mat.hightemp`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 30 ساعة · 🟠 تخصصي · الشروط: `mat.metals`, `mat.ceramics`
- **العمر الافتراضي والموثوقية** · *Lifetime & reliability engineering* · `mat.lifetime`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 35 ساعة · 🔵 أساسي · الشروط: `mat.damage`, `mat.corrosion`, `safe.human`
- **المعادن والسبائك النووية** · *Metals & nuclear alloys* · `mat.metals`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · ⚪ مساند · الشروط: `mat.intro`
- **التلف الإشعاعي** · *Radiation damage in materials* · `mat.damage`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 50 ساعة · 🔵 أساسي · الشروط: `mat.intro`, `rad.interaction`, `phys.condmat`
- **مواد الوقود المتقدمة** · *Advanced fuel materials* · `mat.fuels`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 40 ساعة · 🟣 متقدم · الشروط: `mat.ceramics`, `rx.fuel`

### الحماية من الإشعاع — `prot` (Radiation Protection)
*6 موضوع · 210 ساعة تقديرية*

- **المراقبة وقياس الجرعات** · *Monitoring & dosimetry services* · `prot.monitoring`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `prot.principles`, `rad.detectors`
- **الوقاية المهنية والصحة المهنية** · *Occupational radiation protection* · `prot.occupational`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `prot.monitoring`, `rad.contamination`
- **مبادئ الحماية الإشعاعية** · *Principles of radiation protection* · `prot.principles`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.dosimetry`, `rad.bio`
- **السلامة في المختبرات الإشعاعية** · *Radiation laboratory safety* · `prot.lab`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `prot.principles`, `chem.hotcells`
- **الاستجابة للطوارئ الإشعاعية** · *Radiological emergency response & preparedness* · `prot.emergency`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `prot.principles`, `safe.accidents`, `env.dispersion`
- **الحماية الإشعاعية في الطب** · *Radiation protection in medicine* · `prot.medical`  
  المرحلة 9 (التطبيقات الطبية والصناعية والبيئية) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `prot.principles`, `med.imaging`, `med.therapy`

### السلامة النووية والحوادث — `safe` (Nuclear Safety & Accidents)
*11 موضوع · 475 ساعة تقديرية*

- **الدفاع في العمق** · *Defence in depth* · `safe.did`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.dosimetry`, `rx.principles`
- **ثقافة السلامة والحوكمة** · *Safety culture & governance* · `safe.culture`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · 🔵 أساسي · الشروط: `safe.did`
- **التقييم الحتمي للسلامة** · *Deterministic safety analysis* · `safe.dsa`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 45 ساعة · 🔵 أساسي · الشروط: `safe.systems`, `rx.thermalhyd`, `math.nummethods`
- **تحليل المخاطر وتحديد الأحداث البادئة** · *Hazard analysis & initiating events* · `safe.hazard`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `safe.systems`, `math.prob`
- **العوامل البشرية والموثوقية البشرية** · *Human factors & human reliability* · `safe.human`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `safe.culture`, `math.stat`
- **أنظمة الأمان والتصنيف** · *Safety systems & classification* · `safe.systems`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `safe.did`, `rx.control`
- **التقييم الاحتمالي للسلامة (PSA/PRA)** · *Probabilistic safety assessment* · `safe.psa`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 60 ساعة · 🔵 أساسي · الشروط: `safe.hazard`, `math.prob`, `safe.human`
- **الحوادث النووية التاريخية: تحليل** · *Historical nuclear accidents: analysis* · `safe.accidents`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `safe.severe`, `safe.human`, `hist.timeline`
- **الرقابة والترخيص والتفتيش** · *Regulation, licensing & inspection* · `safe.reg`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `safe.did`, `pol.regulatory`
- **إدارة المخاطر واتخاذ القرار** · *Risk management & decision making* · `safe.risk`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `safe.psa`, `safe.dsa`, `cs.uq`
- **تحليل الحوادث الشديدة** · *Severe accident analysis* · `safe.severe`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 5/5 · 55 ساعة · 🟣 متقدم · الشروط: `safe.dsa`, `safe.psa`, `fuel.inreactor`

### الاندماج والبلازما — `fus` (Fusion & Plasma)
*13 موضوع · 580 ساعة تقديرية*

- **فيزياء البلازما: الأساس** · *Plasma physics: fundamentals* · `fus.plasma`  
  المرحلة 5 (الهندسة النووية) · صعوبة 4/5 · 55 ساعة · 🔵 أساسي · الشروط: `phys.emi`, `phys.statmech`, `math.vectors`
- **تسخين البلازما والتيار المدفوع** · *Plasma heating & current drive* · `fus.heating`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🟣 متقدم · الشروط: `fus.plasma`, `phys.emi`
- **الحبس المغناطيسي** · *Magnetic confinement* · `fus.magnetic`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `fus.plasma`, `fus.mhd`
- **المغناطيسية الهيدروديناميكية (MHD)** · *Magnetohydrodynamics (MHD)* · `fus.mhd`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 5/5 · 50 ساعة · 🟣 متقدم · الشروط: `fus.plasma`, `rx.fluids`
- **مفاهيم حبس بديلة ومتوسطة الكثافة** · *Alternative & magneto-inertial concepts* · `fus.alt`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `fus.magnetic`, `fus.inertial`
- **التوكاماك** · *Tokamaks* · `fus.tokamak`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `fus.magnetic`, `fus.heating`
- **تشخيص البلازما** · *Plasma diagnostics* · `fus.diagnostics`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 5/5 · 45 ساعة · 🟠 تخصصي · الشروط: `fus.plasma`, `meas.detectors`, `meas.signal`
- **الحبس بالقصور الذاتي (ICF)** · *Inertial confinement fusion* · `fus.inertial`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 5/5 · 45 ساعة · 🔵 أساسي · الشروط: `nuc.fusion_basics`, `phys.emi`, `phys.statmech`
- **الستيلاراتور** · *Stellarators* · `fus.stellarator`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 5/5 · 45 ساعة · 🟠 تخصصي · الشروط: `fus.magnetic`
- **البطانية وتكاثر التريتيوم** · *Blankets & tritium breeding* · `fus.blanket`  
  المرحلة 8 (السلامة النووية) · صعوبة 5/5 · 45 ساعة · 🟣 متقدم · الشروط: `fus.neutronics`, `chem.isotope`
- **هندسة الاندماج واقتصادياته** · *Fusion engineering & economics* · `fus.engineering`  
  المرحلة 8 (السلامة النووية) · صعوبة 5/5 · 40 ساعة · 🟣 متقدم · الشروط: `fus.tokamak`, `fus.materials`, `rx.economics`
- **مواد الاندماج** · *Fusion materials* · `fus.materials`  
  المرحلة 8 (السلامة النووية) · صعوبة 5/5 · 45 ساعة · 🟣 متقدم · الشروط: `mat.damage`, `mat.hightemp`
- **نيوترونيات الاندماج** · *Fusion neutronics* · `fus.neutronics`  
  المرحلة 8 (السلامة النووية) · صعوبة 5/5 · 45 ساعة · 🟣 متقدم · الشروط: `rx.transport`, `nuc.fusion_basics`

### التنظيم والسياسات والحوكمة — `pol` (Regulation, Policy & Governance)
*6 موضوع · 195 ساعة تقديرية*

- **الهيئات الرقابية والمعايير** · *Regulatory bodies & standards* · `pol.regulatory`  
  المرحلة 5 (الهندسة النووية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.dosimetry`, `safe.did`
- **أخلاقيات العلم النووي والتواصل العام** · *Ethics & public communication* · `pol.ethics`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 25 ساعة · ⚪ مساند · الشروط: `safe.accidents`, `res.literature`
- **الحوكمة النووية وإدارة البرامج** · *Nuclear governance & programme management* · `pol.governance`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `pol.regulatory`, `safe.culture`
- **القانون النووي والمسؤولية المدنية** · *Nuclear law & liability* · `pol.law`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `pol.regulatory`
- **الاتفاقيات والنظام الدولي** · *Treaties & the international regime* · `pol.treaties`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `pol.regulatory`, `sec.nonprolif`
- **الضمانات النووية** · *IAEA safeguards* · `pol.safeguards`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `pol.regulatory`, `fuel.intro`, `sec.nonprolif`

### التطبيقات الطبية — `med` (Medical Applications)
*6 موضوع · 260 ساعة تقديرية*

- **الطب النووي: مقدمة** · *Nuclear medicine: introduction* · `med.nucmed`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.types`, `nuc.halflife`, `rad.dosimetry`
- **التصوير: SPECT وPET وSPECT/CT** · *Imaging: SPECT, PET, hybrid* · `med.imaging`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 50 ساعة · 🔵 أساسي · الشروط: `med.nucmed`, `rad.detectors`, `meas.signal`
- **الحماية الإشعاعية في المؤسسات الطبية** · *Radiation protection in healthcare* · `med.rp`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 30 ساعة · 🟠 تخصصي · الشروط: `prot.principles`, `med.nucmed`
- **إنتاج النظائر الطبية** · *Medical isotope production* · `med.isotopes`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `nuc.reactions`, `rx.research`, `chem.radiochemistry`
- **العلاج الإشعاعي والعلاج بالنظائر** · *Radiotherapy & radionuclide therapy* · `med.therapy`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 55 ساعة · 🔵 أساسي · الشروط: `rad.bio`, `rad.dosimetry`, `med.nucmed`
- **تخطيط الجرعات والفيزياء الطبية** · *Treatment planning & medical physics* · `med.dosimetry_plan`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 5/5 · 50 ساعة · 🟠 تخصصي · الشروط: `med.therapy`, `math.mc`, `cs.data`

### التطبيقات الصناعية — `ind` (Industrial Applications)
*7 موضوع · 200 ساعة تقديرية*

- **القياسات النووية الصناعية** · *Nuclear gauges & process measurements* · `ind.gauges`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 2/5 · 25 ساعة · ⚪ مساند · الشروط: `rad.transport`
- **الفحص غير الإتلافي** · *Non-destructive testing (NDT)* · `ind.ndt`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.transport`, `ind.radiography`
- **التصوير الإشعاعي الصناعي** · *Industrial radiography* · `ind.radiography`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `rad.sources`, `rad.shielding`, `prot.principles`
- **التعقيم الإشعاعي وحفظ الأغذية** · *Radiation sterilization & food irradiation* · `ind.sterilization`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 25 ساعة · ⚪ مساند · الشروط: `rad.bio`, `rad.dosimetry`
- **المتتبعات النظائرية الصناعية** · *Industrial radiotracers* · `ind.tracers`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 25 ساعة · ⚪ مساند · الشروط: `rad.detectors`, `chem.isotope`
- **تسجيل الآبار النووي والجيوفيزياء** · *Nuclear well logging* · `ind.welllogging`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 25 ساعة · 🟠 تخصصي · الشروط: `rad.detectors`, `env.hydrology`
- **تحليل المواد بالتنشيط** · *Activation analysis of materials* · `ind.activation_analysis`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 30 ساعة · 🟠 تخصصي · الشروط: `rad.activation`

### البيئة والزراعة والنظائر — `env` (Environment, Agriculture & Isotopes)
*8 موضوع · 295 ساعة تقديرية*

- **التطبيقات الزراعية للنظائر والإشعاع** · *Agricultural applications* · `env.agriculture`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `env.tracers`, `rad.bio`
- **التأريخ بالنظائر** · *Radioisotope dating* · `env.dating`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `nuc.halflife`, `meas.spectroscopy`, `math.stat`
- **انتشار المواد في الغلاف الجوي والماء** · *Atmospheric & aquatic dispersion* · `env.dispersion`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `rx.fluids`, `math.pde`, `env.radioecology`
- **النظائر في الهيدرولوجيا والمياه** · *Isotope hydrology* · `env.hydrology`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🟠 تخصصي · الشروط: `env.tracers`, `rx.fluids`
- **الإيكولوجيا الإشعاعية** · *Radioecology* · `env.radioecology`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `chem.envradio`, `rad.bio`
- **النظائر البيئية كمتتبعات** · *Environmental isotopes as tracers* · `env.tracers`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 4/5 · 40 ساعة · 🔵 أساسي · الشروط: `chem.isotope`, `rad.spectroscopy`, `math.stat`
- **النظائر في الدراسات المناخية** · *Isotopes in climate & paleo studies* · `env.climate`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `env.tracers`, `env.dating`
- **معالجة المواقع الملوثة وإعادة تأهيلها** · *Site remediation & restoration* · `env.remediation`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `meas.monitoring`, `env.radioecology`, `fuel.decommissioning`

### مجالات مكتشفة/nاشئة — `disc` (Discovered & Emerging Fields)
*17 موضوع · 485 ساعة تقديرية*

- **تعليم العلوم النووية ومحاكاة التدريب** · *Nuclear education & simulation-based training* · `disc.education`  
  المرحلة 6 (المفاعلات والحراريات والمواد) · صعوبة 3/5 · 20 ساعة · ⚪ مساند · الشروط: `res.writing`, `rx.principles`
- **التحلية النووية** · *Nuclear desalination* · `disc.desal`  
  المرحلة 8 (السلامة النووية) · صعوبة 3/5 · 20 ساعة · ⚪ مساند · الشروط: `rx.thermo_power`, `rx.economics`
- **التصنيع المتقدم للمكونات النووية** · *Advanced manufacturing (AM) for nuclear* · `disc.advancedmanufacturing`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 30 ساعة · 🟣 متقدم · الشروط: `mat.metals`, `mat.characterization`
- **اقتصاديات المخاطر والتأمين والتمويل النووي** · *Risk economics, insurance & nuclear project finance* · `disc.economics_risk`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 30 ساعة · 🟣 متقدم · الشروط: `rx.economics`, `safe.risk`, `pol.law`
- **السلامة التنظيمية والتعلم المؤسسي** · *Organisational safety & learning* · `disc.humanfactors_org`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 30 ساعة · 🟣 متقدم · الشروط: `safe.culture`, `safe.human`
- **الهيدروجين والحرارة الصناعية النووية** · *Nuclear hydrogen & industrial heat* · `disc.hydrogen`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 30 ساعة · 🟣 متقدم · الشروط: `rx.thermo_power`, `rx.gen4`, `chem.phys`
- **المفاعلات الميكروية والتطبيقات غير الكهربائية** · *Microreactors & non-electric applications* · `disc.microreactors`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 25 ساعة · 🟣 متقدم · الشروط: `rx.smr`, `rx.cooling`
- **تصوير النيوترونات** · *Neutron imaging* · `disc.neutronimaging`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 25 ساعة · 🟠 تخصصي · الشروط: `nuc.neutronsci`, `rad.detectors`
- **التحليلات النووية للبيانات الضخمة والمراقبة** · *Nuclear analytics & monitoring networks* · `disc.nuclear_analytics`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 25 ساعة · 🟠 تخصصي · الشروط: `env.dispersion`, `meas.monitoring`, `cs.data`
- **الأنظمة المدفوعة بالمسرعات (ADS)** · *Accelerator-driven systems* · `disc.ads`  
  المرحلة 8 (السلامة النووية) · صعوبة 5/5 · 30 ساعة · 🟣 متقدم · الشروط: `part.accel`, `rx.criticality`, `fuel.reprocessing`
- **تعلم الآلة في العلوم النووية** · *Machine learning in nuclear science* · `disc.ml_nuclear`  
  المرحلة 8 (السلامة النووية) · صعوبة 5/5 · 40 ساعة · 🟣 متقدم · الشروط: `cs.uq`, `nuc.data`, `cs.numpy`
- **التحويل النووي للأكتينيدات الثانوية** · *Transmutation of minor actinides* · `disc.transmutation`  
  المرحلة 8 (السلامة النووية) · صعوبة 5/5 · 30 ساعة · 🟣 متقدم · الشروط: `fuel.reprocessing`, `nuc.reactions`
- **حوكمة الذكاء الاصطناعي في النظم النووية** · *AI governance in nuclear systems* · `disc.ai_governance`  
  المرحلة 9 (التطبيقات الطبية والصناعية والبيئية) · صعوبة 4/5 · 25 ساعة · 🔬 بحثي · الشروط: `disc.ml_nuclear`, `rx.instr`, `pol.regulatory`
- **الطاقة النووية الفضائية** · *Space nuclear power & propulsion* · `disc.space`  
  المرحلة 9 (التطبيقات الطبية والصناعية والبيئية) · صعوبة 4/5 · 30 ساعة · 🟠 تخصصي · الشروط: `rx.types`, `nuc.decay`
- **الثيرانوستكس (تشخيص+علاج بنظيرين)** · *Theranostics* · `disc.theranostics`  
  المرحلة 9 (التطبيقات الطبية والصناعية والبيئية) · صعوبة 4/5 · 30 ساعة · 🟣 متقدم · الشروط: `med.isotopes`, `med.therapy`, `med.imaging`
- **التوأم الرقمي للمفاعلات** · *Digital twins for nuclear systems* · `disc.digitaltwin`  
  المرحلة 9 (التطبيقات الطبية والصناعية والبيئية) · صعوبة 5/5 · 35 ساعة · 🟣 متقدم · الشروط: `rx.multiphysics`, `cs.vv`, `rx.instr`
- **الحوسبة والاستشعار الكمومي في المجال النووي** · *Quantum computing & sensing in nuclear science* · `disc.quantum`  
  المرحلة 9 (التطبيقات الطبية والصناعية والبيئية) · صعوبة 5/5 · 30 ساعة · 🔬 بحثي · الشروط: `phys.qm2`, `cs.uq`, `rx.transport`

### الأمن وعدم الانتشار والتاريخ العسكري — `sec` (Security, Non-proliferation & Military History)
*8 موضوع · 280 ساعة تقديرية*

- **عدم الانتشار النووي** · *Nuclear non-proliferation* · `sec.nonprolif`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `hist.timeline`, `fuel.intro`
- **الأمن النووي وحماية المنشآت** · *Nuclear security & facility protection* · `sec.security`  
  المرحلة 7 (الإشعاع والكواشف والحماية) · صعوبة 3/5 · 35 ساعة · 🔵 أساسي · الشروط: `sec.nonprolif`, `pol.regulatory`
- **الجغرافيا السياسية النووية** · *Nuclear geopolitics* · `sec.geopolitics`  
  المرحلة 8 (السلامة النووية) · صعوبة 3/5 · 30 ساعة · ⚪ مساند · الشروط: `sec.nonprolif`, `pol.treaties`, `rx.economics`
- **التاريخ العسكري النووي** · *Nuclear military history* · `sec.history`  
  المرحلة 8 (السلامة النووية) · صعوبة 3/5 · 40 ساعة · ⚪ مساند · الشروط: `hist.timeline`
- **الحد من التسلح والتحقق** · *Arms control & verification* · `sec.armscontrol`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 35 ساعة · ⚪ مساند · الشروط: `sec.nonprolif`, `pol.treaties`
- **الردع والاستراتيجية النووية** · *Deterrence & nuclear strategy* · `sec.deterrence`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 35 ساعة · ⚪ مساند · الشروط: `sec.nonprolif`, `sec.history`
- **آثار الانفجارات النووية** · *Effects of nuclear detonations* · `sec.effects`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 35 ساعة · ⚪ مساند · الشروط: `rad.interaction`, `rad.bio`, `rad.transport`
- **التحليل الجنائي النووي** · *Nuclear forensics* · `sec.forensics`  
  المرحلة 8 (السلامة النووية) · صعوبة 4/5 · 35 ساعة · 🟠 تخصصي · الشروط: `meas.spectroscopy`, `chem.analytical`, `nuc.data`

