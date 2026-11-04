# -*- coding: utf-8 -*-
with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines):
    if 'DOMContentLoaded' in line or 'window.onload' in line or line.startswith('init') or line.startswith('document.addEventListener'):
        print(f"Line {i+1}: {line.strip()}")

