import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs = ['renderOfficerDecisionQueue', 'renderVillageSignalBoard', 'renderSampleTracker', 'renderParavetInbox', 'renderVetDesk']

for fn in funcs:
    idx = js.find(f'function {fn}')
    if idx != -1:
        print(f"\n==================== {fn} ====================")
        snippet = js[idx:idx+1200]
        print(snippet[:700])

