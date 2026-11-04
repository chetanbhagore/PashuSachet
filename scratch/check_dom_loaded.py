import sys, re
sys.stdout.reconfigure(encoding='utf-8')
f = open('js/app.js', encoding='utf-8').read()
matches = [m.start() for m in re.finditer(r'DOMContentLoaded', f)]
print('DOMContentLoaded occurrences:', len(matches))
for idx in matches:
    print('--- Occurrence ---')
    print(f[idx-20:idx+400])
