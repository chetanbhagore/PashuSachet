# -*- coding: utf-8 -*-
import re
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

for fn in ['simulateVisionDetection', 'drawLesionOnCanvas']:
    print(f"=== DEFINITIONS OF {fn} ===")
    matches = [m.start() for m in re.finditer(r'function\s+' + fn, js)]
    for idx in matches:
        print(f"At char {idx}:")
        print(js[idx:idx+350])
        print("-" * 40)
