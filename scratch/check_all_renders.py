# -*- coding: utf-8 -*-
import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

render_funcs = re.findall(r'function (render\w+)\(', js)
print("All render functions defined in js/app.js:")
for fn in render_funcs:
    count = js.count(f"{fn}(")
    in_dom = fn in js[js.find('DOMContentLoaded'):js.find('DOMContentLoaded')+300]
    print(f"  {fn}: called {count} times (in DOMContentLoaded: {in_dom})")

