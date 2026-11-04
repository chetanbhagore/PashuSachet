# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs = [
    'renderParavetInbox',
    'renderSampleTracker',
    'renderVillageSignalBoard',
    'renderOfficerDecisionQueue'
]

for fn in funcs:
    idx = js.find(f'function {fn}')
    if idx != -1:
        end = js.find('\nfunction ', idx + 10)
        print(f"=== {fn} ===")
        print(js[idx:end if end != -1 else idx + 1000])
        print("="*60)
