import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

calls = set(re.findall(r'onclick=[\"\']\s*([a-zA-Z0-9_]+)\s*[\(;]', html))
print(f"Total unique onclick functions in index.html: {len(calls)}")

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

missing = []
for c in sorted(calls):
    if f"function {c}" not in js and f"{c} =" not in js and f"function {c}" not in html:
        missing.append(c)

print(f"Missing onclick functions ({len(missing)}):")
for m in missing:
    print(f"  - {m}")

