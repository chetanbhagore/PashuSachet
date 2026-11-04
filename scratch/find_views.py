import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="view' in l or 'id="workspace' in l:
        print(f"{i+1}: {l.strip()}")
