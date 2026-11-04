# -*- coding: utf-8 -*-
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('paravetSignalsContainer')
while idx != -1:
    print(js[max(0, idx-100):min(len(js), idx+500)])
    print("="*50)
    idx = js.find('paravetSignalsContainer', idx + 1)

