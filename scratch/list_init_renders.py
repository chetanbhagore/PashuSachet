# -*- coding: utf-8 -*-
import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

funcs = re.findall(r'function ([a-zA-Z0-9_]+)\(', js)
init_render_funcs = [fn for fn in funcs if any(fn.startswith(prefix) for prefix in ['init', 'render', 'load', 'update', 'setup'])]

for fn in sorted(set(init_render_funcs)):
    calls = len(re.findall(r'\b' + fn + r'\(', js))
    print(f"{fn}: defined, called {calls-1} times in code")

