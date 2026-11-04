# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function simulateVisionDetection' in line or 'function drawLesionOnCanvas' in line:
        print(f"Line {i+1}: {line.strip()}")

