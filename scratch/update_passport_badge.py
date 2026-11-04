# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read().replace('\r\n', '\n')

old_animal_body = """      <div class="animal-card-body">
        <p style="font-size: 0.85rem; color: #334155; margin-bottom: 6px;">
          <strong>Age/Sex:</strong> ${a.age} • ${a.sex} | <strong>Location:</strong> ${a.location}
        </p>"""

new_animal_body = """      <div class="animal-card-body">
        <div style="background: #fefce8; border: 1px solid #fef08a; border-radius: 6px; padding: 4px 8px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between; font-size: 0.76rem; font-weight: 700; color: #854d0e;">
          <span>🏅 ग्राम जागरूक पशुपालक (Vigilant Sentinel Farmer)</span>
          <span style="font-size: 0.7rem; color: #a16207; font-weight: 600;">Priority Dispensary Pass</span>
        </div>
        <p style="font-size: 0.85rem; color: #334155; margin-bottom: 6px;">
          <strong>Age/Sex:</strong> ${a.age} • ${a.sex} | <strong>Location:</strong> ${a.location}
        </p>"""

if old_animal_body in js:
    js = js.replace(old_animal_body, new_animal_body)
    with open("js/app.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Injected Sentinel Farmer appreciation badge into animal cards!")
else:
    print("Could not find old animal body!")
    sys.exit(1)

