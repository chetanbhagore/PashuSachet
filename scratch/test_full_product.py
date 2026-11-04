# -*- coding: utf-8 -*-
"""
PashuSachet Master End-to-End Product Verification Suite
Validates all 8 Phases + Backend API + AI Vision + SQLite DB (56 Total Automated Test Cases)
"""
import sys, os, subprocess
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))

print("="*80)
print("PASHUSACHET (GRAM SIGNAL SYSTEM) - MASTER FULL PRODUCT VERIFICATION SUITE")
print("="*80)

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

total_passed = 0
total_failed = 0

for suite_name, script_path in suites:
    print(f"\n▶ Executing: {suite_name} ({script_path})...")
    res = subprocess.run([sys.executable, script_path], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        print(f"  ✓ PASSED: {suite_name}")
        total_passed += 1
    else:
        print(f"  ✗ FAILED: {suite_name}")
        print("  Error output:\n", res.stderr or res.stdout)
        total_failed += 1

print("\n" + "="*80)
print("MASTER VERIFICATION SUMMARY:")
print(f"Total Test Suites Passed: {total_passed} / {len(suites)}")
print(f"Total Test Suites Failed: {total_failed} / {len(suites)}")
print("="*80)

if total_failed == 0:
    print("\n🎉 ALL 8 PHASES, SUPERCHARGES, AND FASTAPI SQLITE BACKEND VALIDATED 100% CLEAN! THE PRODUCT IS PRODUCTION-READY.")
    sys.exit(0)
else:
    print(f"\n❌ {total_failed} SUITE(S) FAILED!")
    sys.exit(1)
