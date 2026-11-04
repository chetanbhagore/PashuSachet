import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('scratch/test_phase3.py', encoding='utf-8').read()
idx = c.find('TC-3.5:')
print(c[idx:idx+400])
