import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

icons_used = set(re.findall(r'data-icon="([^"]+)"', html))
print(f"Icons used in index.html ({len(icons_used)}):", sorted(list(icons_used)))

with open('js/icons.js', 'r', encoding='utf-8') as f:
    js = f.read()

icons_defined = set(re.findall(r'"([a-z0-9\-]+)": `<svg', js))
print(f"Icons defined in js/icons.js ({len(icons_defined)}):", sorted(list(icons_defined)))

missing = icons_used - icons_defined
print("Missing icons:", missing)
