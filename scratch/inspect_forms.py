import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

textareas = re.findall(r'<textarea[^>]+>', html)
print("Textareas:")
for t in textareas:
    print(" ", t)

forms = re.findall(r'<form[^>]+id=[\'"]([^\'"]+)[\'"]', html)
print("\nForms:")
for form in forms:
    print(" ", form)

