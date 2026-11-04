import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('js/app.js', encoding='utf-8').read()
idx = c.find('function evaluateSymptoms')
print(c[idx:idx+1200])
