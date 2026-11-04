import sys
sys.stdout.reconfigure(encoding='utf-8')

def print_exact(path, tc):
    print(f"=== {tc} in {path} ===")
    content = open(path, encoding='utf-8').read()
    idx = content.find(tc)
    if idx != -1:
        print(content[idx:idx+600])

print_exact('scratch/test_phase3.py', 'TC-3.5')
print_exact('scratch/test_phase6.py', 'TC-6.3')
print_exact('scratch/test_phase8.py', 'TC-8.1')
