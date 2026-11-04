# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- Lines 2285-2315 ---")
for i in range(2284, min(len(lines), 2315)):
    print(f"{i+1}: {lines[i]}", end="")

print("\n--- Lines 2580-2615 ---")
for i in range(2579, min(len(lines), 2615)):
    print(f"{i+1}: {lines[i]}", end="")

