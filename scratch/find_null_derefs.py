import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

lines = js.splitlines()

# Find patterns like document.getElementById("xyz").something without optional chaining or null check
danger_lines = []
for idx, line in enumerate(lines):
    # Match document.getElementById("foo")....
    matches = re.finditer(r'document\.getElementById\([\'"]([^\'"]+)[\'"]\)\.([a-zA-Z0-9_$]+)', line)
    for m in matches:
        elem_id = m.group(1)
        prop = m.group(2)
        # Check if elem_id is in html
        if not re.search(rf'id=[\'"]{elem_id}[\'"]', html):
            danger_lines.append((idx + 1, elem_id, prop, line.strip()))

print(f"Total potential null dereferences: {len(danger_lines)}")
for line_num, eid, prop, text in danger_lines:
    print(f"Line {line_num}: ID '{eid}' missing from HTML, accessing .{prop} -> {text}")

