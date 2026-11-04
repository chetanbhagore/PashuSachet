# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['assessmentResult', 'symptomForm', 'triageBanner', 'diagName']):
        print(f"{i+1}: {line.strip()[:100]}")

