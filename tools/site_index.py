#!/usr/bin/env python3
"""site_index — يبني فهرس ملفات المستودع لعارض الوثائق في المتصفح.

الاستخدام:
    python3 tools/site_index.py

ينتج: site/docs_index.json  (تقرأه site/docs.html)
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "docs_index.json")

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}

GROUPS = [
    ("MAP", "الخريطة الكبرى", "🧭"),
    ("lessons", "الدروس", "📚"),
    ("sims", "المختبرات المحاكاة", "🧪"),
    ("BUILD", "اصنعها بنفسك", "🛠️"),
    ("progress", "ملف المتعلّم", "📈"),
    ("tools", "الأدوات", "⚙️"),
    ("", "الجذر", "🏠"),
]

H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)


def title_of(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            head = fh.read(4000)
    except OSError:
        return os.path.basename(path)
    m = H1.search(head)
    if m:
        return m.group(1).strip().lstrip("#").strip()
    for line in head.splitlines():
        line = line.strip()
        if line and not line.startswith(("---", "```", "|", "<")):
            return line[:80]
    return os.path.basename(path)


def main() -> int:
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
            top = rel.split("/", 1)[0] if "/" in rel else ""
            files.append(
                {
                    "path": rel,
                    "title": title_of(full),
                    "group": top,
                    "size": os.path.getsize(full),
                }
            )
    files.sort(key=lambda f: (f["group"], f["path"]))

    groups = []
    for key, label, icon in GROUPS:
        items = [f for f in files if f["group"] == key]
        if items:
            groups.append({"key": key or ".", "label": label, "icon": icon, "items": items})

    data = {"generated": True, "count": len(files), "groups": groups}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    print(f"✓ site/docs_index.json — {len(files)} ملف، {len(groups)} مجموعة")
    return 0


if __name__ == "__main__":
    sys.exit(main())
