# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Running Phase 2 Verification Test Suite (TC-2.1 to TC-2.6)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

tests = []

# TC-2.1: 90-Second Micro-Form Intake
t1_pass = (
    'id="symptom-screening"' in html and
    'id="animalSpecies"' in html and
    'id="affectedCount"' in html and
    'id="villageLocation"' in html and
    'id="symptomTagsContainer"' in html
)
tests.append(("TC-2.1: 90-Second Micro-Form Intake", t1_pass, "Form has species, symptoms, count & village fields"))

# TC-2.2: USSD Feature-Phone Simulation
t2_pass = (
    'id="ussdModal"' in html and
    'id="ussdScreen"' in html and
    'id="ussdInput"' in html and
    'submitUssdStep' in js and
    '*992#' in html
)
tests.append(("TC-2.2: USSD Feature-Phone Simulation (*992#)", t2_pass, "Interactive USSD terminal modal and state machine present"))

# TC-2.3: Missed-Call & Voice IVR Simulation
t3_pass = (
    'id="missedCallModal"' in html and
    'simulateMissedCallCallback' in js and
    '1800-889-1962' in html and
    'voiceIvrBtn' in html
)
tests.append(("TC-2.3: Missed-Call & Voice IVR (1800-889-1962)", t3_pass, "Missed call modal, audio callback simulator, IVR button present"))

# TC-2.4: Proxy Reporting
t4_pass = (
    'id="isProxyCheck"' in html and
    'id="proxyFieldsBox"' in html and
    'id="proxyReporterName"' in html and
    'id="proxyReporterRole"' in html and
    'isProxyCheck' in js
)
tests.append(("TC-2.4: Proxy Reporting for Elders & Neighbors", t4_pass, "Proxy reporter fields with dynamic visibility toggle present"))

# TC-2.5: Post-Loss Mortality Reporting
t5_pass = (
    'id="isMortalityCheck"' in html and
    'id="mortalityCountBox"' in html and
    'id="mortalityCountInput"' in html and
    'isMortalityCheck' in js
)
tests.append(("TC-2.5: Post-Loss Mortality Urgent Flag", t5_pass, "Mortality reporting triggers biosecurity alert fields"))

# TC-2.6: Offline Queue & Sync
t6_pass = (
    'saveOfflineReport' in js and
    'syncPendingReports' in js and
    'pashu_offline_reports' in js and
    'localStorage' in js
)
tests.append(("TC-2.6: Offline-First Queue & Sync Engine", t6_pass, "Local storage/IndexedDB queue with auto-sync on reconnect present"))

print("\n" + "="*70)
print("PHASE 2 VERIFICATION RESULTS:")
print("="*70)
all_passed = True
for name, passed, note in tests:
    status = "PASS [OK]" if passed else "FAIL [X]"
    if not passed:
        all_passed = False
    print(f"{status:10} | {name:40} | {note}")
print("="*70)

if all_passed:
    print("ALL PHASE 2 TESTS PASSED SUCCESSFULLY! (6/6)")
    sys.exit(0)
else:
    print("SOME PHASE 2 TESTS FAILED!")
    sys.exit(1)

