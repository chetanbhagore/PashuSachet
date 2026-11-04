# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs_to_check = [
    'confirmSignal', 'dismissSignal', 'promptSignalVitals', 'requestSignalSample',
    'advanceSampleStageLocal', 'exportNadresBatch', 'lookupNdlmTag',
    'openBookModal', 'openBookModalForAnimal', 'prefillSymptomCheck',
    'appendUssdKey', 'openVoiceIvrModal', 'sendFarmerOtp',
    'resolveOfficerDecision'
]

for fn in funcs_to_check:
    found = f"function {fn}" in js
    print(f"{fn}: {'FOUND' if found else 'MISSING'}")

