import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['heroAnimalsCarousel', 'farmerAnimalsList', 'animalListContainer']):
        print(f"{i+1}: {l.strip()}")
