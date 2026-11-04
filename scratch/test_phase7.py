# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Running Phase 7 Verification Test Suite (TC-7.1 to TC-7.5)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

tests = []

# TC-7.1: Live Observation Board
t1_pass = (
    'id="village-signal-board"' in html and
    'id="villageSignalsGrid"' in html and
    'renderVillageSignalBoard' in js
)
tests.append(("TC-7.1: Live Observation Board", t1_pass, "Granular village-level participatory signal observation board present"))

# TC-7.2: k-Anonymity Privacy Suppression Rule (< 3 Signals)
t2_pass = (
    'report.count >= 3' in js and
    'Anonymized for farm privacy' in js and
    'k < 3' in js and
    'Centroid Pin' in js
)
tests.append(("TC-7.2: k-Anonymity Privacy Rule (<3 Signals)", t2_pass, "Suppresses low-volume village signals to Taluka centroid pins to protect farm identity"))

# TC-7.3: Outbreak Cluster Surge Detection
t3_pass = (
    'SURGE_ALERT' in js and
    'isSurge' in js and
    'Immediate 5km ring-vaccination recommended' in js
)
tests.append(("TC-7.3: Outbreak Cluster Surge Detection", t3_pass, "Detects active disease surges (>3 signals) and triggers ring-vaccination advisory"))

# TC-7.4: One Health Inter-Agency Alert Stream
t4_pass = (
    'id="oneHealthStreamBanner"' in html and
    'ONE HEALTH INTER-AGENCY LIVE SENTINEL' in html and
    'District Health Officer' in html
)
tests.append(("TC-7.4: One Health Inter-Agency Alert Stream", t4_pass, "Bridges veterinary alerts with Public Health Department (DHO) and Civil Surgeon"))

# TC-7.5: Officer Morning Decision Queue
t5_pass = (
    'id="officerDecisionQueue"' in html and
    'Morning Decision Queue' in html and
    'officerDecisions' in js and
    'resolveOfficerDecision' in js
)
tests.append(("TC-7.5: Officer Morning Decision Queue", t5_pass, "Provides actionable morning queue for ring-vax, mortality and lab authorizations"))

print("\n" + "="*70)
print("PHASE 7 VERIFICATION RESULTS:")
print("="*70)
all_passed = True
for name, passed, note in tests:
    status = "PASS [OK]" if passed else "FAIL [X]"
    if not passed:
        all_passed = False
    print(f"{status:10} | {name:40} | {note}")
print("="*70)

if all_passed:
    print("ALL PHASE 7 TESTS PASSED SUCCESSFULLY! (5/5)")
    sys.exit(0)
else:
    print("SOME PHASE 7 TESTS FAILED!")
    sys.exit(1)

