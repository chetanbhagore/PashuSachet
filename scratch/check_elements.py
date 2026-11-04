# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

elements = [
    'assessmentResult', 'triageBanner', 'triageText', 'diagName', 'diagConf',
    'confBar', 'adviceList', 'diffDiag', 'emergencyModal', 'mvuDispatchCard',
    'mvuTicketDetails', 'zoonoticAlertBanner', 'zoonoticDetails', 'abstentionNoticeBox',
    'triageBandContainer', 'symptomForm', 'toastContainer', 'triageSubmitBtn',
    'farmerVoiceNotes', 'villageLocation', 'affectedCount', 'onsetDays', 'tempInput'
]

for el_id in elements:
    found = f'id="{el_id}"' in html or f"id='{el_id}'" in html
    print(f"{el_id}: {'FOUND' if found else 'MISSING'}")

