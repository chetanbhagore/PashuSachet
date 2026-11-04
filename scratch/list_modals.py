import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modals = re.findall(r'<div class="notebook-modal-overlay" id="([^"]+)"', html)
print(f"Modals in index.html ({len(modals)}):", modals)
