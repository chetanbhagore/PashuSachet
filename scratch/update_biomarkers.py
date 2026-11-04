# -*- coding: utf-8 -*-
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update biomarkers to include exact terms
js = js.replace(
    "biomarkers: ['Circumscribed 2-5cm firm dermal nodules', 'Prescapular lymphadenopathy'],",
    "biomarkers: ['Circumscribed Cutaneous Nodules (2-5cm firm dermal lumps)', 'Prescapular lymphadenopathy'],"
)

js = js.replace(
    "biomarkers: ['Ruptured vesicular ulcers on tongue/gums', 'Interdigital coronary erythema'],",
    "biomarkers: ['Epithelial Vesicles & Ruptured mucosal ulcers', 'Interdigital coronary erythema'],"
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated visionDiseaseSpecs biomarkers successfully")

