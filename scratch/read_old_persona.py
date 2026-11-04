import subprocess, re, sys
sys.stdout.reconfigure(encoding='utf-8')

proc = subprocess.run(['git', 'show', '7f3a336:js/app.js'], capture_output=True, text=True, encoding='utf-8')
old_js = proc.stdout

match = re.search(r'function activatePersona\([^\)]*\)\s*\{[\s\S]*?\n\}', old_js)
if match:
    print("activatePersona in 7f3a336:\n", match.group(0))
else:
    print("activatePersona not found in 7f3a336:js/app.js")
