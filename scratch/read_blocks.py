# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- 2285 to 2355 ---")
for i in range(2284, 2355):
    print(f"{i+1}: {lines[i]}", end="")

print("\n--- 2580 to 2675 ---")
for i in range(2579, min(len(lines), 2675)):
    print(f"{i+1}: {lines[i]}", end="")
