import sys, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')

suites = [
    ("Phase 1: Multi-Role Auth & RBAC", "scratch/test_phase1.py"),
    ("Phase 2: Ultra-Inclusive Intake & 90s Flow", "scratch/test_phase2.py"),
    ("Phase 3: Uncertainty ML Triage & 1962 Accelerator", "scratch/test_phase3.py"),
    ("Phase 4: Para-Vet Verification Gate", "scratch/test_phase4.py"),
    ("Phase 5: Vet Exam & Milk Withdrawal Engine", "scratch/test_phase5.py"),
    ("Phase 6: Closed-Loop Diagnostic Tracker (RDDL)", "scratch/test_phase6.py"),
    ("Phase 7: Live Village Signal Board & One Health", "scratch/test_phase7.py"),
    ("Phase 8: Govt Integrations, AI Vision & Telemetry", "scratch/test_phase8.py"),
    ("Backend Direct Function Calls & Services", "scratch/test_backend_direct.py"),
    ("Backend FastAPI TestClient & SQLite Database", "scratch/test_backend_api.py"),
    ("Supercharged Detections, SEIR, MVU & WhatsApp Bot", "scratch/test_supercharge.py"),
]

passed = 0
failed = 0

for name, script in suites:
    res = subprocess.run([sys.executable, script], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        print(f"PASS: {name}")
        passed += 1
    else:
        print(f"FAIL: {name}")
        print("STDERR:\n", res.stderr)
        print("STDOUT:\n", res.stdout)
        failed += 1

print(f"\nTOTAL: {passed}/{len(suites)} PASSED, {failed} FAILED")
if failed > 0:
    sys.exit(1)
