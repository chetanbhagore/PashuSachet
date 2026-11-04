# -*- coding: utf-8 -*-
import subprocess
import time
import json
import urllib.request
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
port = 9222

cmd = [
    edge_path,
    "--headless=new",
    f"--remote-debugging-port={port}",
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check",
    "http://localhost:8000"
]

print("Launching Edge headless...")
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)

try:
    # Query DevTools targets
    url = f"http://127.0.0.1:{port}/json"
    req = urllib.request.urlopen(url, timeout=5)
    targets = json.loads(req.read().decode('utf-8'))
    print(f"Found {len(targets)} targets:")
    for t in targets:
        print(f"  Target: {t.get('title')} ({t.get('url')})")
        print(f"  WS URL: {t.get('webSocketDebuggerUrl')}")
finally:
    proc.terminate()
    proc.kill()

