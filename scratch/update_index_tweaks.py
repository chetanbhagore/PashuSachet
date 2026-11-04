# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make Para-Vet nav link visible
html = html.replace('<li id="paravetNavLink" style="display: none;"><a href="#paravet-inbox">Para-Vet Inbox</a></li>',
                    '<li id="paravetNavLink"><a href="#paravet-inbox">Para-Vet Inbox</a></li>')

# Pre-fill NDLM tag input
html = html.replace('id="ndlmTagInput" class="form-control" placeholder="उदा. 123456789012"',
                    'id="ndlmTagInput" class="form-control" value="240019283741" placeholder="उदा. 123456789012"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated")

