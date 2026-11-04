import sys
sys.stdout.reconfigure(encoding='utf-8')

for f in ['scratch/test_phase2.py', 'scratch/test_phase6.py', 'scratch/test_phase7.py', 'scratch/test_phase8.py']:
    print(f"==================== {f} ====================")
    print(open(f, encoding='utf-8').read())
