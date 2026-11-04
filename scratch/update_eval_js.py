# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("js/app.js", "r", encoding="utf-8") as f:
    js_content = f.read().replace('\r\n', '\n')

old_eval_head = """function evaluateSymptoms() {
  const species = document.querySelector('input[name="species"]:checked')?.value || "cattle";
  const checkedBoxes = Array.from(document.querySelectorAll('input[name="symptom"]:checked')).map(cb => cb.value);
  const onsetDays = parseInt(document.getElementById("onsetDays")?.value || "2");
  const tempDegree = parseFloat(document.getElementById("tempInput")?.value || "102.5");"""

new_eval_head = """function evaluateSymptoms() {
  const species = document.querySelector('input[name="species"]:checked')?.value || document.getElementById("animalSpecies")?.value || "cattle";
  const checkedBoxes = Array.from(document.querySelectorAll('input[name="symptom"]:checked')).map(cb => cb.value);
  const onsetDays = parseInt(document.getElementById("onsetDays")?.value || "2");
  const tempDegree = parseFloat(document.getElementById("tempInput")?.value || "102.5");
  const affectedCount = parseInt(document.getElementById("affectedCount")?.value || "1");
  const villageLocation = document.getElementById("villageLocation")?.value || "Sangamner";
  const isMortalityCheck = document.getElementById("isMortalityCheck")?.checked || false;
  const mortalityCount = parseInt(document.getElementById("mortalityCountInput")?.value || "1");
  const isProxyCheck = document.getElementById("isProxyCheck")?.checked || false;
  const proxyReporterName = document.getElementById("proxyReporterName")?.value || "";
  const proxyReporterRole = document.getElementById("proxyReporterRole")?.value || "neighbor";"""

if old_eval_head in js_content:
    js_content = js_content.replace(old_eval_head, new_eval_head)
    print("Updated evaluateSymptoms() to capture Phase 2 fields!")
else:
    print("Could not find old evaluateSymptoms header!")
    sys.exit(1)

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Saved js/app.js successfully!")

