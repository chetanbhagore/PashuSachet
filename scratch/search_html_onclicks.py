import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

funcs = [
    'VoiceIvr', 'Emergency', '1962', 'Book', 'Ndlm', 'Tag',
    'deploy', 'reroute', 'broadcast', 'filter', 'Paravet', 'Signal'
]

for kw in funcs:
    matches = re.findall(rf'onclick=["\']([^"\']*{kw}[^"\']*)["\']', html, re.I)
    print(f"Keyword '{kw}':")
    for m in set(matches):
        print(f"   onclick='{m}'")

