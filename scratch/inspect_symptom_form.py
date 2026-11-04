# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Inspect showToast
print("--- showToast ---")
for line in js.splitlines():
    if 'function showToast' in line or 'toastContainer' in line:
        print(line)

# Inspect symptomForm submission
print("\n--- symptomForm handler ---")
idx = js.find('symptomForm')
while idx != -1:
    snippet = js[max(0, idx-100):min(len(js), idx+300)]
    print(snippet)
    print("="*40)
    idx = js.find('symptomForm', idx + 1)

