import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'<section[^>]+id=[\'"]([^\'"]+)[\'"][^>]*style=[\'"]([^\'"]*display:\s*none[^\'"]*)[\'"]', html)
for m in matches:
    print('Hidden Section:', m[0], '->', m[1])

navs = re.findall(r'<a[^>]+id=[\'"]([^\'"]+)[\'"][^>]*style=[\'"]([^\'"]*display:\s*none[^\'"]*)[\'"]', html)
for n in navs:
    print('Hidden Nav Link:', n[0], '->', n[1])

