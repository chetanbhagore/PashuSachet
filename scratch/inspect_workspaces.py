import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

workspaces = ['workspaceFarmer', 'workspaceVet', 'workspaceParavet', 'workspaceOfficer', 'workspaceRddl']

for ws in workspaces:
    idx = html.find(f'id="{ws}"')
    if idx != -1:
        print(f"\n==================== {ws} (starts at {idx}) ====================")
        snippet = html[idx:idx+1200]
        print(snippet[:600])
        print("...")

