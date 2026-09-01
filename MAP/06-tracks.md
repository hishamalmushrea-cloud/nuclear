# MAP/06 — المسارات التخصصية (A → N)

كل مسار بأربع طبقات: **المشترك → التخصص → التخصص الفرعي → البحث**.
«المشترك» = ما يجب إتقانه قبل دخول أي مسار (≈ المراحل 0–3 + الحوسبة الأساسية).

---

## المشترك لكل المسارات (Core commun)

```
math.pre → math.algebra → math.functions → math.calc1 → math.calc2 → math.ode
math.linalg → math.vectors · math.prob → math.stat · math.nummethods
cs.python → cs.numpy → cs.data
phys.mech → phys.energy → phys.em → phys.emi → phys.relativity → phys.qm1 → phys.atomic
phys.thermo → phys.statmech
chem.general → chem.structure → chem.bonding → chem.inorganic
nuc.isotopes → nuc.binding → nuc.decay → nuc.halflife → nuc.reactions → nuc.crosssection
nuc.fission · nuc.fusion_basics
rad.types → rad.sources → rad.interaction → rad.transport → rad.dosimetry
res.literature → res.sources
```
≈ **2,300 ساعة**. بعده تتفرّع المسارات.

---

## A — الفيزياء النووية
**التخصص:** `phys.qm2` · `nuc.nucleons` · `nuc.stability` · `nuc.series` · `nuc.scattering`
· `nuc.absorption` · `nuc.neutron` · `nuc.models` · `nuc.structure` · `nuc.data`
· `nuc.exp` · `nuc.theory` · `part.intro` · `part.forces` · `part.quarks` · `part.sm`
· `math.advanced` · `math.grouptheory`
**تخصص فرعي:** `nuc.astro` · `nuc.neutronsci` · `part.neutrino` · `part.qft` · `part.accel` · `part.hep`
**بحث:** `res.question` · `res.stats` · `res.openproblems`
**مشاريع مميزة:** بناء جدول نويدات محلي من ENSDF؛ محاكاة تشتت نيوترون-نواة بنموذج بسيط؛
مراجعة قياسات عمر نصف حديثة في EXFOR.

## B — الهندسة النووية
**التخصص:** `rx.principles` · `rx.neutroncycle` · `rx.criticality` · `rx.kinetics`
· `rx.diffusion` · `rx.transport` · `rx.heat` · `rx.fluids` · `rx.thermalhyd`
· `rx.thermo_power` · `rx.fuel` · `rx.instr` · `rx.types` · `math.pde` · `math.mc`
**تخصص فرعي:** `rx.core` · `rx.multiphysics` · `rx.gen4` · `rx.smr` · `rx.economics`
· `mat.intro` · `mat.damage` · `mat.corrosion` · `mat.lifetime`
**بحث:** `cs.uq` · `cs.vv` · `res.design` · `res.openproblems`

## C — فيزياء وهندسة المفاعلات
**التخصص:** كل ما في B + `rx.control` · `rx.cooling` · `rx.power` · `rx.research`
· `rx.materials` · `mat.metals` · `mat.fuels`
**تخصص فرعي:** `fuel.inreactor` · `safe.systems` · `safe.dsa` · `safe.severe` · `disc.digitaltwin`
**بحث:** `rx.multiphysics` · `res.openproblems`
**مشاريع:** محاكاة حركية نقطية مع ست مجموعات متأخرة وسموم الزينون؛ نموذج قناة وقود
بحساب DNBR؛ مقارنة نتائج مجموعة انتشار ثنائية المجموعة مع مرجع منشور.

## D — الإشعاع والحماية الإشعاعية
**التخصص:** `rad.detectors` · `rad.spectroscopy` · `rad.shielding` · `rad.contamination`
· `rad.bio` · `meas.electronics` · `meas.signal` · `meas.calibration` · `meas.detectors`
· `prot.principles` · `prot.monitoring` · `prot.occupational` · `prot.lab`
**تخصص فرعي:** `rad.metrology` · `rad.activation` · `meas.monitoring` · `meas.spectroscopy`
· `prot.emergency` · `prot.medical` · `env.dispersion` · `env.radioecology`
**بحث:** `cs.uq` · `disc.nuclear_analytics`
**مشاريع:** معايرة طاقة وكفاءة لكاشف ومقارنة النتيجة بمصدر معتمد (محاكاةً إن لم تتوفر معدات)؛
حساب درع متعدد الطبقات؛ تحليل طيف افتراضي وتحديد MDA.

## E — الكيمياء النووية والإشعاعية
**التخصص:** `chem.phys` · `chem.analytical` · `chem.radiochemistry` · `chem.nuclear`
· `chem.isotope` · `chem.hotcells` · `rad.activation`
**تخصص فرعي:** `chem.envradio` · `env.tracers` · `fuel.reprocessing` · `sec.forensics`
· `med.isotopes`
**بحث:** `res.stats` · `res.openproblems`

## F — الاندماج والبلازما
**التخصص:** `fus.plasma` · `fus.mhd` · `fus.heating` · `fus.magnetic` · `fus.tokamak`
· `fus.inertial` · `fus.neutronics` · `fus.diagnostics`
**تخصص فرعي:** `fus.stellarator` · `fus.alt` · `fus.materials` · `fus.blanket` · `fus.engineering`
**بحث:** `disc.ml_nuclear` · `res.openproblems`
**مشاريع:** حساب شرط لوسون لثلاثة أنظمة؛ نموذج بسيط لتوازن الطاقة في البلازما؛
مقارنة بين W7-X وITER من حيث الأهداف الفيزيائية (بحث مصدري).

## G — المواد النووية
**التخصص:** `mat.intro` · `mat.damage` · `mat.metals` · `mat.ceramics` · `mat.corrosion`
· `mat.lifetime` · `mat.characterization` · `phys.condmat`
**تخصص فرعي:** `mat.composites` · `mat.hightemp` · `mat.fuels` · `fuel.inreactor`
· `fus.materials` · `disc.advancedmanufacturing`
**بحث:** `cs.uq` · `res.openproblems`
**مشاريع:** حساب dpa لتراكض معيّن؛ تحليل بيانات صلابة/انتفاخ منشورة؛ مقارنة مواد الغلاف.

## H — الأجهزة والكشف والقياس
**التخصص:** `meas.electronics` · `meas.signal` · `meas.calibration` · `meas.detectors`
· `rad.detectors` · `rad.spectroscopy` · `rad.metrology`
**تخصص فرعي:** `meas.spectroscopy` · `meas.monitoring` · `part.detectors` · `disc.nuclear_analytics`
**بحث:** `disc.ml_nuclear` · `cs.uq`
**مشاريع:** محاكاة استجابة كاشف ومعالجة النبضات رقمياً؛ تصميم نظام تحليل طيفي على الورق؛
تحليل عدم يقين كامل لقياس نشاط.

## I — الطب النووي
**التخصص:** `med.nucmed` · `med.imaging` · `med.therapy` · `med.isotopes` · `rad.bio`
· `prot.principles`
**تخصص فرعي:** `med.dosimetry_plan` · `med.rp` · `prot.medical` · `disc.theranostics`
· `chem.radiochemistry`
**بحث:** `res.design` · `res.stats`
**مشاريع:** حساب جرعة MIRD لمصدر في عضو؛ خطة إنتاج Tc-99m من مولّد (مفهومياً)؛
تحليل سلسلة توريد Ac-225 من مصادر منشورة.

## J — الحوسبة والمحاكاة
**التخصص:** `math.mc` · `cs.uq` · `cs.vv` · `cs.hpc` · `rx.transport` · `math.nummethods`
· `math.pde` · `nuc.data`
**تخصص فرعي:** `rx.multiphysics` · `disc.ml_nuclear` · `disc.digitaltwin` · `disc.quantum`
· `res.reproducibility`
**بحث:** `res.openproblems`
**مشاريع:** شبكة انتشار 1D بمنهج الفروق المحدودة + تحقق بالتقارب; تكامل مونتي كارلو
لتوهين فوتونات؛ حساب عدم يقين لمخرَج نموذج.

## K — الأمن النووي وعدم الانتشار
**التخصص:** `sec.nonprolif` · `sec.security` · `pol.safeguards` · `pol.treaties`
· `fuel.intro` · `hist.timeline` · `hist.projects`
**تخصص فرعي:** `sec.armscontrol` · `sec.deterrence` · `sec.effects` · `sec.geopolitics`
· `sec.forensics` · `pol.law` · `pol.governance`
**بحث:** `res.sources` · `res.peerreview`

## L — السياسات والاستراتيجية النووية
**التخصص:** `pol.regulatory` · `pol.treaties` · `pol.safeguards` · `pol.governance`
· `sec.nonprolif` · `sec.geopolitics` · `rx.economics`
**تخصص فرعي:** `pol.law` · `pol.ethics` · `sec.armscontrol` · `sec.deterrence`
· `disc.economics_risk` · `disc.ai_governance`
**بحث:** `res.sources` · `res.openproblems`

## M — البيئة والنظائر
**التخصص:** `env.tracers` · `env.radioecology` · `env.dispersion` · `env.dating`
· `chem.envradio` · `rad.spectroscopy`
**تخصص فرعي:** `env.hydrology` · `env.climate` · `env.agriculture` · `env.remediation`
· `meas.monitoring` · `ind.tracers`
**بحث:** `cs.data` · `res.stats`

## N — البحث العلمي (مسار فوقي)
**التخصص:** `res.literature` · `res.sources` · `res.question` · `res.design` · `res.stats`
· `res.data` · `res.reproducibility` · `res.writing`
**تخصص فرعي:** `res.peerreview` · `res.openproblems` · `disc.education`
**بحث:** مشروع مراجعة أدبيات + سؤال بحث أصلي + خطة تحقق.

---

## اختيار المسار (X.29)

بعد إتمام المشترك وثلاثة اختبارات بوابة، نحلّل نتائجك ونقترح مسارين أو ثلاثة **مع
الأسباب**: ما الذي حللته بدقة؟ ما الذي أعدت المحاولة فيه طوعاً؟ أي نوع مسائل يشدّك
(الاشتقاق أم التصميم أم القياس أم السياسة)؟ القرار لك، والاقتراح مبني على بيانات.

## تعدد المسارات

المسارات ليست حصرية؛ المسارات B/C/J تتقاطع بشدة، وD/H كذلك، وK/L كذلك.
أفضل تركيبة للباحث التطبيقي عادةً: **مسار أساسي واحد بعمق L4/L5** +
**مسار ثانٍ حتى L2/L3** + **مسار N دائماً حتى L4**.
