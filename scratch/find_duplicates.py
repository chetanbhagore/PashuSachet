# -*- coding: utf-8 -*-
import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', js)
seen = {}
duplicates = []
for f in funcs:
    if f in seen:
        duplicates.append(f)
    seen[f] = seen.get(f, 0) + 1

print(f"Total functions: {len(funcs)}")
print(f"Duplicate functions ({len(duplicates)}):")
for d in duplicates:
    print(f"  - {d} (defined {seen[d]} times)")

