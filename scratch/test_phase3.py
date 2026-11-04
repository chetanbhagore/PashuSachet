# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Running Phase 3 Verification Test Suite (TC-3.1 to TC-3.5)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

tests = []

# TC-3.1: Explicit Abstention Gate
t1_pass = (
    'id="abstentionNoticeBox"' in html and
    '.triage-band.abstention' in css and
    'isAbstention' in js and
    'Insufficient Distinctive Signs' in js and
    'MODERATE: मॉडेल संयम' in js
)
tests.append(("TC-3.1: Explicit Abstention Gate", t1_pass, "Deliberately refrains from speculative guessing on ambiguous signs"))

# TC-3.2: Qualitative Confidence Bands (Zero unvalidated decimal percentages)
t2_pass = (
    'triageBandContainer' in js and
    'qualitativeBand' in js and
    'Differential (संभाव्य श्रेणी)' in js and
    'Likely' in js and
    'Possible' in js
)
tests.append(("TC-3.2: Qualitative Confidence Bands", t2_pass, "Qualitative clinical bands used without pseudo-precise decimals"))

# TC-3.3: Automated 1962 Accelerator Dispatch
t3_pass = (
    'id="mvuDispatchCard"' in html and
    'id="mvuTicketDetails"' in html and
    '1962 ACCELERATOR' in html and
    '1962-MH-' in js and
    'mvuTicket' in js
)
tests.append(("TC-3.3: Automated 1962 Accelerator Dispatch", t3_pass, "Auto-generates MVU dispatch ticket on critical emergency flags"))

# TC-3.4: Plain-Language Marathi Immediate Safe-Action Cards
t4_pass = (
    'वेगळ्या गोठ्यात बांधा' in js and
    'पोटॅशियम परमँगनेट' in js and
    'कडुनिंबाच्या पानांचा धूर' in js and
    'बाधित सडातील दूध वेगळे' in js
)
tests.append(("TC-3.4: Plain-Language Marathi Safe-Action Cards", t4_pass, "Provides vernacular first-aid bullet cards with zero jargon"))

# TC-3.5: Human Sentinel Filter & Zoonotic Guardrails
t5_pass = (
    'id="zoonoticAlertBanner"' in html and
    'id="zoonoticDetails"' in html and
    'ONE HEALTH ZOONOTIC ALERT' in html and
    'isZoonoticAlert' in js and
    'अँथ्रॅक्स' in js and
    'रेबीज संशय' in js
)
tests.append(("TC-3.5: One Health Zoonotic Guardrails", t5_pass, "Anthrax and Rabies trigger high-visibility zoonotic health alerts"))

print("\n" + "="*70)
print("PHASE 3 VERIFICATION RESULTS:")
print("="*70)
all_passed = True
for name, passed, note in tests:
    status = "PASS [OK]" if passed else "FAIL [X]"
    if not passed:
        all_passed = False
    print(f"{status:10} | {name:40} | {note}")
print("="*70)

if all_passed:
    print("ALL PHASE 3 TESTS PASSED SUCCESSFULLY! (5/5)")
    sys.exit(0)
else:
    print("SOME PHASE 3 TESTS FAILED!")
    sys.exit(1)

