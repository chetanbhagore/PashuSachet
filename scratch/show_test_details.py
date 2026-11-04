import sys
sys.stdout.reconfigure(encoding='utf-8')

def show_test_code(path, markers):
    print(f"=== {path} ===")
    lines = open(path, encoding='utf-8').read().split('\n')
    for idx, line in enumerate(lines):
        for m in markers:
            if m in line:
                start = max(0, idx - 2)
                end = min(len(lines), idx + 12)
                print(f"--- Marker: {m} (line {idx+1}) ---")
                print("\n".join(lines[start:end]))
                print()

show_test_code('scratch/test_phase2.py', ['TC-2.2', 'TC-2.3'])
show_test_code('scratch/test_phase3.py', ['TC-3.1', 'TC-3.3', 'TC-3.5'])
show_test_code('scratch/test_phase6.py', ['TC-6.3'])
show_test_code('scratch/test_phase7.py', ['TC-7.4'])
show_test_code('scratch/test_phase8.py', ['TC-8.1', 'TC-8.5'])
