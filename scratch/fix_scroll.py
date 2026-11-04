import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "window.scrollTo({ top: 0, behavior: 'smooth' });",
    "if (typeof window !== 'undefined' && typeof window.scrollTo === 'function') { window.scrollTo({ top: 0, behavior: 'smooth' }); }"
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(text)
print("Guarded window.scrollTo")
