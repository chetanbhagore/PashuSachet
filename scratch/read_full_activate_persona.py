import sys, re
sys.stdout.reconfigure(encoding='utf-8')
f = open('js/app.js', encoding='utf-8').read()
m = re.search(r'function activatePersona[\s\S]*?(?=\nfunction [a-zA-Z]|\Z)', f)
if m:
    print(m.group(0))
