import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('id="workspaceOfficer"')
end = html.find('id="workspaceRddl"')
print(html[start:end])

