# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['id="village-signal-board"', 'id="paravet-inbox"', 'id="sample-tracker"', 'id="pilot-telemetry"']):
        print(f"Line {i+1}: {line.strip()[:100]}")

