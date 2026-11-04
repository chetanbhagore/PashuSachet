import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update lines 92-97 to keep paravetNav always visible
target1 = '''    const paravetNav = document.getElementById("paravetNavLink");
    const paravetSection = document.getElementById("paravet-inbox");
    if (user.role === "paravet") {
      if (paravetNav) paravetNav.style.display = "inline-block";
      if (paravetSection) paravetSection.style.display = "block";
    } else {
      if (paravetNav) paravetNav.style.display = "none";
    }'''

replacement1 = '''    const paravetNav = document.getElementById("paravetNavLink");
    const paravetSection = document.getElementById("paravet-inbox");
    if (paravetNav) paravetNav.style.display = "inline-block";
    if (paravetSection) paravetSection.style.display = "block";'''

if target1 in js:
    js = js.replace(target1, replacement1, 1)
    print("✓ Updated paravetNav/paravetSection visibility in updateAuthUI")
else:
    print("⚠️ Target 1 not found")

# 2. Add aliases and helper functions for modals and tag verification
helpers_code = '''
// Safe Helper Functions & Global Modal Wrappers
function openEmergencyModal() {
  const modal = document.getElementById("emergencyModal");
  if (modal) modal.classList.add("active");
}

function closeEmergencyModal() {
  const modal = document.getElementById("emergencyModal");
  if (modal) modal.classList.remove("active");
}

function closeVoiceIvrModal() {
  closeMissedCallModal();
}

function verifyNdlmTag() {
  return lookupNdlmTag();
}
'''

if 'function openEmergencyModal' not in js:
    js += helpers_code
    print("✓ Appended safe modal helpers (openEmergencyModal, closeEmergencyModal, closeVoiceIvrModal, verifyNdlmTag)")

# 3. Update toggleSymptomVal and toggleSymptomCheckbox to protect Event dispatch
target_toggle = '''function toggleSymptomVal(val) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb) {
    cb.checked = !cb.checked;
    cb.dispatchEvent(new Event("change"));
  }
}'''

replacement_toggle = '''function toggleSymptomVal(val) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb) {
    cb.checked = !cb.checked;
    if (typeof Event !== 'undefined') {
      try { cb.dispatchEvent(new Event("change")); } catch(e) {}
    }
  }
}'''

if target_toggle in js:
    js = js.replace(target_toggle, replacement_toggle, 1)
    print("✓ Protected toggleSymptomVal event dispatch")

target_cb = '''function toggleSymptomCheckbox(val, state) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb && cb.checked !== state) {
    cb.checked = state;
    cb.dispatchEvent(new Event("change"));
  }
}'''

replacement_cb = '''function toggleSymptomCheckbox(val, state) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb && cb.checked !== state) {
    cb.checked = state;
    if (typeof Event !== 'undefined') {
      try { cb.dispatchEvent(new Event("change")); } catch(e) {}
    }
  }
}'''

if target_cb in js:
    js = js.replace(target_cb, replacement_cb, 1)
    print("✓ Protected toggleSymptomCheckbox event dispatch")

# 4. In activatePersona, call quickLogin('admin') for 'rddl'
target_rddl = '''  } else if (role === 'rddl') {
    renderSampleTracker();
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड: RT-PCR चाचणी व नमुना ट्रॅकिंग.');'''

replacement_rddl = '''  } else if (role === 'rddl') {
    quickLogin('admin');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderSampleTracker();
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड: RT-PCR चाचणी व नमुना ट्रॅकिंग.');'''

if target_rddl in js:
    js = js.replace(target_rddl, replacement_rddl, 1)
    print("✓ Updated activatePersona for rddl role")

# 5. Protect gisSvg querySelector in updateSeirDay
target_seir = '''  const gisSvg = document.getElementById("gisSvgMap");
  if (gisSvg) {
    const nimgaonPulse = gisSvg.querySelector('circle[fill="#dc2626"]');'''

replacement_seir = '''  const gisSvg = document.getElementById("gisSvgMap");
  if (gisSvg && typeof gisSvg.querySelector === 'function') {
    const nimgaonPulse = gisSvg.querySelector('circle[fill="#dc2626"]');'''

if target_seir in js:
    js = js.replace(target_seir, replacement_seir, 1)
    print("✓ Protected gisSvg.querySelector in updateSeirDay")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✓ Finished updating js/app.js")

