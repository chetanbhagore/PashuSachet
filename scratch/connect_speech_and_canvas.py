# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read().replace('\r\n', '\n')

# 1. Update simulateMissedCallCallback to call speakMarathiVoice
old_ivr_target = """  setTimeout(() => {
    statusEl.innerHTML = `<span style="color:#2563eb;">📞 पशूसचेत सर्व्हरकडून त्वरित कॉल-बॅक! कॉल कनेक्ट झाला... मराठी IVR ऑडिओ सुरू आहे.</span>`;
  }, 1000);"""

new_ivr_target = """  setTimeout(() => {
    statusEl.innerHTML = `<span style="color:#2563eb;">📞 पशूसचेत सर्व्हरकडून त्वरित कॉल-बॅक! कॉल कनेक्ट झाला... मराठी IVR ऑडिओ सुरू आहे.</span>`;
    speakMarathiVoice("नमस्कार शेतकरी बंधू, पशूसचेत कॉल सहाय्यता केंद्रात आपले स्वागत आहे. तुमच्या जनावराची लक्षणे सांगा.");
  }, 1000);"""

if old_ivr_target in js:
    js = js.replace(old_ivr_target, new_ivr_target)
    print("Added Marathi speech synthesis to missed call callback!")

# 2. Update simulateVisionDetection to call drawLesionOnCanvas
old_vision_target = """  setTimeout(() => {
    if (conditionKey === 'lsd') {"""

new_vision_target = """  setTimeout(() => {
    drawLesionOnCanvas(conditionKey);
    if (conditionKey === 'lsd') {"""

if old_vision_target in js:
    js = js.replace(old_vision_target, new_vision_target)
    print("Added drawLesionOnCanvas call to simulateVisionDetection!")

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Updated js/app.js successfully!")

