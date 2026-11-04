import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for path in ['scratch/test_phase2.py', 'scratch/test_phase3.py', 'scratch/test_phase6.py', 'scratch/test_phase7.py', 'scratch/test_phase8.py']:
    print(f"=== {path} ===")
    content = open(path, encoding='utf-8').read()
    for line in content.split('\n'):
        if 'def test_' in line or 'assert' in line or 'TC-' in line:
            print("  ", line.strip())
