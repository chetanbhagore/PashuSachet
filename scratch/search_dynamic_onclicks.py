import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

dynamic_onclicks = set(re.findall(r'onclick=[\'"]([^\'"]+)[\'"]', js))
print(f"Total dynamic onclick attributes in js/app.js: {len(dynamic_onclicks)}")
for oc in sorted(dynamic_onclicks):
    print(" •", oc)

