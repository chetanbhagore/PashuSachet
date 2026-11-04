import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Check all onclick functions
onclicks = set(re.findall(r'onclick=[\'"]([^\'"]+)[\'"]', html))
print(f"Total unique onclick attributes: {len(onclicks)}")

missing_handlers = []
for call in sorted(onclicks):
    # extract function name
    fn_match = re.match(r'([a-zA-Z0-9_$]+)\s*\(', call.strip())
    if fn_match:
        fn_name = fn_match.group(1)
        # Check if function exists in JS
        pattern = rf'function\s+{fn_name}\b|window\.{fn_name}\s*='
        if not re.search(pattern, js):
            missing_handlers.append((fn_name, call))

print(f"Missing onclick functions ({len(missing_handlers)}):")
for fn, call in missing_handlers:
    print(f"  ❌ {fn} -> {call}")

# 2. Check getElementById calls in app.js
get_elem_ids = set(re.findall(r'document\.getElementById\([\'"]([^\'"]+)[\'"]\)', js))
missing_ids = []
for elem_id in sorted(get_elem_ids):
    # Check if id exists in HTML
    pattern = rf'id=[\'"]{elem_id}[\'"]'
    if not re.search(pattern, html):
        missing_ids.append(elem_id)

print(f"\nTotal getElementById queries in JS: {len(get_elem_ids)}")
print(f"Missing IDs in index.html ({len(missing_ids)}):")
for eid in missing_ids:
    print(f"  ⚠️ {eid}")

# 3. Check addEventListener targets in app.js
# Let's inspect where null element might be causing runtime exceptions!
null_listener_candidates = []
for line in js.splitlines():
    if '.addEventListener(' in line:
        null_listener_candidates.append(line.strip())

print(f"\nTotal addEventListener lines: {len(null_listener_candidates)}")
for line in null_listener_candidates:
    print(f"  • {line}")

