# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs = ['appendUssdKey', 'lookupNdlmTag', 'exportNadresBatch']
for fn in funcs:
    idx = js.find(f'function {fn}')
    if idx != -1:
        print(f"=== {fn} ===")
        print(js[idx:idx+500])
        print("="*50)
    else:
        print(f"=== {fn} NOT FOUND ===")

