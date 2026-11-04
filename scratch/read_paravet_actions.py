# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs = ['confirmSignal', 'dismissSignal', 'promptSignalVitals', 'requestSignalSample']
for fn in funcs:
    idx = js.find(f'function {fn}')
    print(f"=== {fn} ===")
    print(js[idx:idx+450])
    print("="*50)

