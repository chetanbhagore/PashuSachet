# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

start = js.find('function evaluateSymptoms')
if start != -1:
    end = js.find('\nfunction ', start + 25)
    print(js[start:end if end != -1 else start + 3000])
else:
    print('evaluateSymptoms not found')

