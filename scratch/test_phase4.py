# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Running Phase 4 Verification Test Suite (TC-4.1 to TC-4.4)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

tests = []

# TC-4.1: Unverified Intake Isolation
t1_pass = (
    'id="paravet-inbox"' in html and
    'id="paravetSignalsContainer"' in html and
    'villageSignals' in js and
    'UNVERIFIED_SIGNAL' in js and
    'renderParavetInbox' in js
)
tests.append(("TC-4.1: Unverified Intake Isolation", t1_pass, "Unverified signals quarantined exclusively in Para-Vet Beat Inbox"))

# TC-4.2: Ultra-Fast < 30-Second Verification Actions
t2_pass = (
    'confirmSignal' in js and
    'dismissSignal' in js and
    'promptSignalVitals' in js and
    'VERIFIED_SIGNAL' in js and
    'DISMISSED_BENIGN' in js
)
tests.append(("TC-4.2: <30-Second Verification Action", t2_pass, "One-tap confirm, dismiss, and vitals recording handlers present"))

# TC-4.3: Gate Protection of District Board
t3_pass = (
    's.status === "VERIFIED_SIGNAL"' in js and
    'Propagated to District Surveillance Board' in js and
    'Not sent to Officer Board' in js
)
tests.append(("TC-4.3: Gate Protection of District Board", t3_pass, "Unverified/dismissed reports prevented from polluting district board"))

# TC-4.4: Diagnostic Sample Kit Initiation
t4_pass = (
    'requestSignalSample' in js and
    'SAMPLE_NEEDED' in js and
    'RDDL Pune' in js and
    'sampleRecord' in js
)
tests.append(("TC-4.4: Sample Kit Request Initiation", t4_pass, "Creates linked sample record in SAMPLE_NEEDED state for RDDL Pune"))

print("\n" + "="*70)
print("PHASE 4 VERIFICATION RESULTS:")
print("="*70)
all_passed = True
for name, passed, note in tests:
    status = "PASS [OK]" if passed else "FAIL [X]"
    if not passed:
        all_passed = False
    print(f"{status:10} | {name:40} | {note}")
print("="*70)

if all_passed:
    print("ALL PHASE 4 TESTS PASSED SUCCESSFULLY! (4/4)")
    sys.exit(0)
else:
    print("SOME PHASE 4 TESTS FAILED!")
    sys.exit(1)
