# MAP/09 — المصادر: السجلّ، التصنيف، وكيفية التدقيق (X.3)

> قاعدة: **لا مصدر مخترَع**. كل مدخل هنا إمّا وثيقة مؤسسية يمكن الوصول إليها، أو كتاب
> أكاديمي معروف، أو مجلة/قاعدة بيانات معروفة. ما لم نتحقق منه نُعلّمه بـ«لم نتحقق منه».

---

## 1) تصنيف المصادر

| المستوى | التعريف | متى نستخدمه |
|---|---|---|
| **A** | ورقة محكّمة · كتاب أكاديمي · وثيقة رسمية (IAEA/NRC/ICRP/ICRU/UNSCEAR/NEA/NIST) | بناء الأحكام العلمية والأرقام |
| **B** | جامعة/مختبر وطني/منظمة بحثية (MIT OCW, ORNL, INL, IPP, LANL…) | الشرح والتوسع، مع تأييد بمصدر A |
| **C** | مصدر تعليمي أو صناعي ثانوي جيد | الفهم الأولي والتقريب، لا للأرقام الحسّاسة |
| **D** | منتديات ومواقع عامة | **لا** نبني عليه حكماً مهماً |

عند التعارض: نعرضه، نفحص السبب (اختلاف تعريف؟ سنة؟ نطاق؟ نموذج؟)، ونرجّح الأقوى،
ونعلن ذلك صراحةً. **لا إجماع مخترَع.**

---

## 2) سجل المصادر (مطابق لما في `tools/kg/schema.py`)

### 2.1 معايير ومؤسسات (A)

| المعرّف | المصدر | الرابط |
|---|---|---|
| `IAEA-SSR2/1` | IAEA SSR-2/1 (Rev.1): السلامة في تصميم محطات القدرة النووية | https://www.iaea.org/publications/11088/safety-of-nuclear-power-plants-design |
| `IAEA-SF1` | IAEA SF-1: أساسيات السلامة | https://www.iaea.org/publications/6990/fundamental-safety-principles |
| `IAEA-GSR-Part3` | المعايير الأساسية الدولية للحماية من الإشعاع | https://www.iaea.org/publications/15302/radiation-protection-and-safety-of-radiation-sources-international-basic-safety-standards |
| `IAEA-SSG-46` | تقييم الدفاع في العمق (Safety Reports Series 46 Rev.1) | https://www-pub.iaea.org/MTCD/Publications/PDF/p15147-PUB2008_web.pdf |
| `IAEA-NDS` | خدمات البيانات النووية: ENDF / EXFOR / ENSDF / LiveChart | https://nds.iaea.org/ |
| `IAEA-PRIS` | نظام معلومات مفاعلات القدرة | https://pris.iaea.org/pris/ |
| `IAEA-TECDOC-2057` | إنتاج Ac-225 وضبط جودته | https://www-pub.iaea.org/MTCD/publications/PDF/TE-2057web.pdf |
| `ICRP-103` | توصيات ICRP (2007) | https://www.icrp.org/publication.asp?id=ICRP%20Publication%20103 |
| `ICRU-85` | كميات ووحدات قياس الجرعات | https://www.icru.org/ |
| `UNSCEAR` | تقارير آثار الإشعاع المؤين | https://www.unscear.org/ |
| `NUREG-0800` | الفصل المرجعي للتقييم القياسي (NRC) | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr0800/ |
| `NUREG-1150` | التقييم الاحتمالي للمخاطر لمحطات القدرة | https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr1150/ |
| `NRC-10CFR20` | 10 CFR Part 20: معايير الحماية من الإشعاع | https://www.nrc.gov/reading-rm/doc-collections/cfr/part020/ |
| `NPT-Text` | نص معاهدة عدم الانتشار | https://www.un.org/disarmament/wmd/nuclear/npt/ |
| `UN-Press-DC3912` | بيان الأمم المتحدة: المؤتمر الحادي عشر لمراجعة NPT أنهى أعماله دون وثيقة توافقية (22 مايو 2026) | https://press.un.org/en/2026/dc3912.doc.htm |
| `ITER-NewBaseline` | ITER: خط الأساس الجديد (بدء التشغيل البحثي 2034، D-T 2039) | https://www.iter.org/node/20687/new-baseline-prioritize-robust-start-exploitation |
| `LLNL-Ignition` | LLNL/NIF: سجلّات الاشتعال (ذروة 8.6 MJ في 7 أبريل 2025) | https://lasers.llnl.gov/science/achieving-fusion-ignition |
| `IPP-W7X` | IPP: أرقام W7-X القياسية (مايو 2025) | https://www.ipp.mpg.de/5532945/w7x |
| `DOE-FRIB` | DOE: خمس نظائر جديدة رُصدت لأول مرة في FRIB | https://www.energy.gov/science/np/articles/facility-rare-isotope-beams-observes-five-never-seen-isotopes |
| `STUK-Onkalo` | STUK/Posiva: مستودع Onkalo الفنلندي | https://www.stuk.fi/ |
| `NEA-Databank` | OECD/NEA Data Bank وJANIS | https://www.oecd-nea.org/janis/ |
| `NNDC` | NNDC (Brookhaven): ENDF/B وNuDat وNSR | https://www.nndc.bnl.gov/ |
| `NIST` / `CODATA` | الثوابت الفيزيائية وبيانات القياس | https://physics.nist.gov/ · https://codata.org/ |
| `Nature-SciRep-DT` | DeepONet للتوأم الرقمي في النظم النووية (Sci. Rep. 2024) | https://www.nature.com/articles/s41598-024-51984-x |

### 2.2 كتب مرجعية (A) — بلا روابط (تُعرف من المكتبات الجامعية)

| المجال | المرجع |
|---|---|
| فيزياء نووية | Krane, *Introductory Nuclear Physics* (Wiley) |
| هندسة نووية (مقدمة) | Lamarsh & Baratta, *Introduction to Nuclear Engineering* |
| نظرية المفاعلات | Lamarsh, *Introduction to Nuclear Reactor Theory* · Duderstadt & Hamilton, *Nuclear Reactor Analysis* · Stacey, *Nuclear Reactor Physics* (Wiley) |
| النظم النووية والحراريات | Todreas & Kazimi, *Nuclear Systems* |
| الكيمياء النووية والإشعاعية | Choppin, Liljenzin & Rydberg, *Radiochemistry and Nuclear Chemistry* |
| الكشف والقياس | Knoll, *Radiation Detection and Measurement* |
| الجرعات | Attix, *Introduction to Radiological Physics and Radiation Dosimetry* |
| الحماية | Turner, *Atoms, Radiation, and Radiation Protection* |
| ميكانيكا الكم | Griffiths, *Introduction to Quantum Mechanics* · Sakurai & Napolitano, *Modern Quantum Mechanics* |
| أساسيات | Serway/Jewett, *Physics for Scientists and Engineers* |
| انتقال الحرارة / الموائع | Çengel & Ghajar, *Heat and Mass Transfer* · White, *Fluid Mechanics* |
| مواد | Was, *Fundamentals of Radiation Materials Science* |
| الاندماج | Stacey, *Fusion Plasma Physics* / *Fusion: An Introduction* |

### 2.3 مصادر B وC مستخدمة في هذا المشروع

| المعرّف | المصدر | المستوى |
|---|---|---|
| `MIT-OCW` | مقررات MIT المفتوحة (22.02 مقدمة في الهندسة النووية، 22.05 فيزياء النيوترونات…) | B |
| `ArXiv-Nucl` | arXiv (nucl-ex / nucl-th / physics.comp-ph) | B |
| `ArXiv-GenIV-DT` | arXiv:2506.17258 — إطار توأم رقمي لمفاعلات الجيل الرابع | B |
| `WorldNuclear` | World Nuclear Association (تقارير ودورة الوقود) | B |
| `SIPRI` | معهد ستوكهولم لأبحاث السلام | B |
| `BASIC` / `CSS-ETH` | تحليلات مؤتمر مراجعة NPT 2026 | B |
| `GRS-2026` | GRS: الطاقة النووية عالمياً 2026 | B |
| `IAEA-Trends-2025` | IAEA: ستة اتجاهات عالمية في الطاقة النووية | A |
| `SMR-Intel-2026` | تقرير سنوي عن حالة SMR (2026) | C |
| `McGuireWoods-2026` | ملخص صناعي لقطاع المستحضرات الإشعاعية (Q1 2026) | C |
| `CFS-SPARC` | Commonwealth Fusion Systems: أخبار وتطور SPARC | B |

---

## 3) أين تبحث عن الأوراق؟

| الحاجة | المكان |
|---|---|
| فيزياء نووية/جسيمات (ما قبل النشر) | arXiv: `nucl-ex`, `nucl-th`, `hep-ex`, `physics.acc-ph`, `physics.plasm-ph` |
| بحث bibliografي شامل | INSPIRE-HEP · NSR (NNDC) · INIS (IAEA) |
| مجلات محكّمة رئيسية | *Physical Review C* · *Nuclear Physics A* · *Nuclear Science and Engineering* · *Annals of Nuclear Energy* · *Nuclear Technology* · *Journal of Nuclear Materials* · *Nuclear Fusion* · *Fusion Engineering and Design* · *Nuclear Instruments and Methods in Physics Research A* · *Health Physics* · *Radiation Research* · *Journal of Radiological Protection* · *Radiation Protection Dosimetry* · *IEEE Transactions on Nuclear Science* |
| بيانات تجريبية للتحقق | EXFOR (تفاعلات) · ENSDF (بنية واضمحلال) · ICSBEP (حرجية) · IRPhEP (فيزيا مفاعلات) |
| تقارير تقنية | NUREG (NRC) · IAEA TECDOC · OECD/NEA reports · DOE/INL/ORNL reports |

---

## 4) قائمة تدقيق سريعة قبل الاعتماد على مصدر

1. من الناشر؟ (مؤسسة/مجلة/جامعة/فرد/منتدى)
2. ما تاريخه؟ (هل سبق تغييراً معيارياً معروفاً؟)
3. هل الأرقام مصحوبة بعدم يقين أو منهجية؟
4. هل يتوافق مع معيار/مرجع آخر مستقل؟
5. هل ينقل عن مصدر أصلي أم عن ملخّص؟ (اذهب للأصل)
6. هل يخلط بين رأي وقياس؟ (ابحث عن أفعال مثل «نعتقد» مقابل «قِسنا»)

---

## 5) ملاحظة عن الاستشهاد في هذا المشروع

كل ملف يذكر معلومة خارجية يذكر معرّف المصدر (مثل `IAEA-PRIS`) أو رابطاً مباشراً.
الأرقام في `MAP/14-frontiers-2026.md` كلها من مصادر A أو B مع تواريخها،
والمواضع التي تختلف فيها المصادر (مثل عدد المفاعلات بين PRIS وتقارير أخرى)
معلَّمة باختلافها الصريح.
