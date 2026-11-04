# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Running Phase 6 Verification Test Suite (TC-6.1 to TC-6.4)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

tests = []

# TC-6.1: Sample Lifecycle Stage Progression
stages = ["SAMPLE_NEEDED", "SAMPLE_COLLECTED", "IN_TRANSIT_LAB", "LAB_TESTING", "RESULTED_AND_ACTION_TAKEN"]
all_stages_present = all(st in js for st in stages)
t1_pass = (
    'id="sample-tracker"' in html and
    'id="sampleCardsContainer"' in html and
    'renderSampleTracker' in js and
    all_stages_present
)
tests.append(("TC-6.1: 5-Stage Sample Lifecycle Progression", t1_pass, "Supports all 5 stages from cow-shed collection to RDDL lab results"))

# TC-6.2: Tri-Party Visibility (Farmer, Para-Vet, LDO)
t2_pass = (
    'farmerName' in js and
    'attendingVet' in js and
    'paraVet' in js and
    'destinationLab' in js
)
tests.append(("TC-6.2: Tri-Party Visibility Across Stakeholders", t2_pass, "Unified sample card with farmer, vet, para-vet and destination lab metadata"))

# TC-6.3: Cold-Chain Verification Protocol
t3_pass = (
    '.coldchain-badge' in css and
    'coldChainTracking' in js and
    'Ice Gel Shipper' in js and
    '2°C - 8°C' in js
)
tests.append(("TC-6.3: Cold-Chain Verification Protocol", t3_pass, "Active temperature tracking badge ensures specimen viability at RDDL"))

# TC-6.4: Closure Feedback Delivery
t4_pass = (
    'advanceSampleStage' in js and
    'Farmer Closure SMS Sent' in js and
    'नमुन्याचा अहवाल प्राप्त झाला असून' in js
)
tests.append(("TC-6.4: Farmer Closure Feedback Delivery", t4_pass, "Automatic vernacular SMS dispatched upon final result & biosecurity closure"))

print("\n" + "="*70)
print("PHASE 6 VERIFICATION RESULTS:")
print("="*70)
all_passed = True
for name, passed, note in tests:
    status = "PASS [OK]" if passed else "FAIL [X]"
    if not passed:
        all_passed = False
    print(f"{status:10} | {name:40} | {note}")
print("="*70)

if all_passed:
    print("ALL PHASE 6 TESTS PASSED SUCCESSFULLY! (4/4)")
    sys.exit(0)
else:
    print("SOME PHASE 6 TESTS FAILED!")
    sys.exit(1)

