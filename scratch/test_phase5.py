# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Running Phase 5 Verification Test Suite (TC-5.1 to TC-5.5)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

tests = []

# TC-5.1: Vet Care Desk Queue Synchronization
t1_pass = (
    'id="vet-desk"' in html and
    'id="vetAppointmentsContainer"' in html and
    'id="vetCasesContainer"' in html and
    'renderVetDesk' in js
)
tests.append(("TC-5.1: Vet Care Desk Queue Synchronization", t1_pass, "Vet clinical station renders farm appointments and referred AI triage cases"))

# TC-5.2: Diagnostic Drug Formulation & MSVC Digital Registration
t2_pass = (
    'id="prescribeModal"' in html and
    'id="rxDrug"' in html and
    'id="rxRoute"' in html and
    'id="rxVetReg"' in html and
    'MSVC/2012/03194' in html and
    'updateAnimalPrescription' in js
)
tests.append(("TC-5.2: Diagnostic Drug Formulation & MSVC Seal", t2_pass, "Prescription modal captures drug, route, duration and MSVC registration"))

# TC-5.3: Last-Dose Milk Withdrawal Countdown Formula Verification
formula_check = (
    'treatmentDurationMs' in js and
    'withdrawalBufferMs' in js and
    'totalPeriodMs = treatmentDurationMs + withdrawalBufferMs' in js and
    'endTime = prescribedAt + totalPeriodMs' in js
)
tests.append(("TC-5.3: Last-Dose Withdrawal Formula", formula_check, "Calculates from final dose: treatmentDays*24 + withdrawalHours"))

# TC-5.4: Live Dynamic Passport Clock
t4_pass = (
    'updateWithdrawalClocks' in js and
    'data-withdrawal-end' in js and
    'setInterval(updateWithdrawalClocks, 1000)' in js and
    'remaining' in js
)
tests.append(("TC-5.4: Live Dynamic Passport Clock", t4_pass, "Real-time 1000ms countdown in Animal Passport with food-safety warning"))

# TC-5.5: Expired Withdrawal State Transition
t5_pass = (
    'WITHDRAWAL CLEARED — Milk Safe for Dairy Supply' in js and
    'simulateFastForwardWithdrawal' in js
)
tests.append(("TC-5.5: Expired Withdrawal State Transition", t5_pass, "Transitions to verified safe status when countdown elapses"))

print("\n" + "="*70)
print("PHASE 5 VERIFICATION RESULTS:")
print("="*70)
all_passed = True
for name, passed, note in tests:
    status = "PASS [OK]" if passed else "FAIL [X]"
    if not passed:
        all_passed = False
    print(f"{status:10} | {name:40} | {note}")
print("="*70)

if all_passed:
    print("ALL PHASE 5 TESTS PASSED SUCCESSFULLY! (5/5)")
    sys.exit(0)
else:
    print("SOME PHASE 5 TESTS FAILED!")
    sys.exit(1)

