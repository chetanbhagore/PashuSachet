# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

terms = ['gisDistName', 'gisDistZone', 'gisThreat', 'gisRiskBadge', 'gisScore', 'gisClusters', 'gisVaccine', 'gisAdvisory', 'gisOfficer']
for term in terms:
    target = f'id="{term}"'
    print(f"{term}: {'FOUND' if target in html else 'MISSING'}")
