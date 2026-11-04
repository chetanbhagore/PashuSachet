# -*- coding: utf-8 -*-
import re
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    matches = re.findall(r'onclick="([^"]+)"', line)
    for m in matches:
        print(f"Line {i+1}: onclick=\"{m}\" | {line.strip()[:60]}")

