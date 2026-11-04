# -*- coding: utf-8 -*-
import re
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Find all onclick calls in html
onclicks = re.findall(r'onclick="([^"]+)"', html)
print(f'Total onclick handlers in HTML: {len(onclicks)}')
missing_functions = set()
for oc in onclicks:
    clean = oc.strip()
    if any(clean.startswith(prefix) for prefix in ['window.', 'document.', 'this.', 'event.', 'location.']) or '=' in clean:
        continue
    fn_name = clean.split('(')[0].strip()
    if fn_name and fn_name not in js:
        missing_functions.add(fn_name)

print(f'Missing onclick functions in js/app.js ({len(missing_functions)}):')
for fn in sorted(missing_functions):
    print(f'  - {fn}')

# 2. Find all getElementById in js
get_elements = re.findall(r'getElementById\([\'"]([^\'"]+)[\'"]\)', js)
print(f'\nTotal getElementById calls in JS: {len(get_elements)}')
missing_ids = set()
for gid in set(get_elements):
    if f'id="{gid}"' not in html and f"id='{gid}'" not in html:
        missing_ids.add(gid)

print(f'Missing IDs in HTML referenced by getElementById ({len(missing_ids)}):')
for gid in sorted(missing_ids):
    print(f'  - {gid}')

# 3. Check for syntax or DOMContentLoaded issues
print("\nInspecting initialization & forms...")
forms = re.findall(r'<form\b[^>]*>', html)
print(f'Total forms in HTML: {len(forms)}')
for f in forms:
    print(f'  Form tag: {f[:80]}...')

