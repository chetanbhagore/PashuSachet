import sys, re
sys.stdout.reconfigure(encoding='utf-8')
f = open('js/app.js', encoding='utf-8').read()
m = re.search(r'function activatePersona[\s\S]*?(?=\nfunction |\Z)', f)
if m:
    print('Found activatePersona:')
    print(m.group(0)[:800])
else:
    print('activatePersona not found')
