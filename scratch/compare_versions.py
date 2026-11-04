import subprocess
import os

# Check size and line count of index.html in 7f3a336
proc = subprocess.run(['git', 'show', '7f3a336:index.html'], capture_output=True, text=True, encoding='utf-8')
old_html = proc.stdout
print("Old index.html lines:", len(old_html.splitlines()))

with open('index.html', 'r', encoding='utf-8') as f:
    curr_html = f.read()
print("Current index.html lines:", len(curr_html.splitlines()))
