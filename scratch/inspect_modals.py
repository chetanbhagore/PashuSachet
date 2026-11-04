import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modals = re.findall(r'id=["\']([a-zA-Z0-9_]*Modal)[\'"]', html)
print('Modals found:', modals)

