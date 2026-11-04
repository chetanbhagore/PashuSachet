import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

test_modals = ['missedCallModal', 'ussdModal', 'voiceIvrModal', 'pashuAadharModal', 'prescribeModal']
for tm in test_modals:
    if f'id="{tm}"' in html:
        print(f"Found {tm} in index.html")
    else:
        print(f"MISSING {tm} in index.html")
