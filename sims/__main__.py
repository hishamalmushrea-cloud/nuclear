# -*- coding: utf-8 -*-
"""قائمة المختبرات الافتراضية — شغّلها هكذا:  python3 -m sims"""
from __future__ import annotations

import importlib

LABS = [
    ("01", "01_decay_lab", "مختبر الاضمحلال: قِس عمر النصف بنفسك"),
    ("02", "02_geiger_counter", "عدّاد غايغر: كفاءة + خلفية + زمن ميت"),
    ("03", "03_shielding_lab", "مختبر التدريع والجرعة"),
    ("04", "04_reactor_kinetics", "حركية المفاعل: العب بقضيب التحكم"),
]


def main():
    while True:
        print("\n" + "=" * 66)
        print("  🔬 المختبرات الافتراضية — العلوم والتكنولوجيا النووية")
        print("=" * 66)
        for code, _, title in LABS:
            print(f"   {code}) {title}")
        print("    0) خروج")
        try:
            c = input("\n؟ اختر رقم المختبر: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if c in ("0", "", "q", "exit"):
            return
        mod = None
        for code, name, _ in LABS:
            if c == code or c == name or c == name.split("_", 1)[0]:
                mod = name
        if not mod:
            print("  اختيار غير معروف.")
            continue
        try:
            importlib.import_module("." + mod, package=__package__).run()
        except (KeyboardInterrupt, EOFError):
            print("\n  (خروج من المختبر)")


if __name__ == "__main__":
    main()
