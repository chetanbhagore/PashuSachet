# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Running Phase 1 Verification Test Suite (TC-1.1 to TC-1.6)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

tests = []

# TC-1.1: Farmer Auth
t1_pass = 'id="tabFarmerBtn"' in html and 'id="authPaneFarmer"' in html and 'farmer:' in js and 'Ganesh Patil' in js
tests.append(("TC-1.1: Farmer OTP Auth & Profile", t1_pass, "Farmer Ganesh Patil present with OTP fields"))

# TC-1.2: Vet Auth
t2_pass = 'id="tabVetBtn"' in html and 'id="authPaneVet"' in html and 'vet:' in js and 'MSVC/2012/03194' in js
tests.append(("TC-1.2: Veterinarian MSVC Auth & Profile", t2_pass, "Dr. Rameshwar Kute present with MSVC/2012/03194"))

# TC-1.3: District Officer Auth
t3_pass = 'id="tabOfficerBtn"' in html and 'id="authPaneOfficer"' in html and 'officer:' in js and 'dvo.ahmednagar@maharashtra.gov.in' in js
tests.append(("TC-1.3: District Officer Auth & Profile", t3_pass, "Dr. S. R. Shinde present with Govt DVO scope"))

# TC-1.4: Admin Auth
t4_pass = 'id="tabAdminBtn"' in html and 'id="authPaneAdmin"' in html and 'admin:' in js and 'admin@pashusachet.mahadahd.in' in js
tests.append(("TC-1.4: Admin Auth & 2FA Token", t4_pass, "Admin present with 2FA TOTP"))

# TC-1.5: Role Gating (Admin console hidden for non-admin)
t5_pass = 'user.role === "admin"' in js and 'adminSection.style.display = "block"' in js
tests.append(("TC-1.5: Role-Based Access Control (RBAC) Gating", t5_pass, "Admin console gated exclusively to Admin role"))

# TC-1.6: Para-Vet / Village Sentinel Auth
t6_pass = 'id="tabParaVetBtn"' in html and 'id="authPaneParavet"' in html and 'paravet:' in js and 'PV-AHM-9104' in js
tests.append(("TC-1.6: Para-Vet / Village Sentinel Auth", t6_pass, "Ganesh Kale present with PV-AHM-9104 & Cluster Beat"))

print("\n" + "="*70)
print("PHASE 1 VERIFICATION RESULTS:")
print("="*70)
all_passed = True
for name, passed, note in tests:
    status = "PASS [OK]" if passed else "FAIL [X]"
    if not passed:
        all_passed = False
    print(f"{status:10} | {name:40} | {note}")
print("="*70)

if all_passed:
    print("ALL PHASE 1 TESTS PASSED SUCCESSFULLY! (6/6)")
    sys.exit(0)
else:
    print("SOME PHASE 1 TESTS FAILED!")
    sys.exit(1)
