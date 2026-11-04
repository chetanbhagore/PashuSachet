import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function renderVillageSignalBoard')
print(js[idx:idx+1500])

