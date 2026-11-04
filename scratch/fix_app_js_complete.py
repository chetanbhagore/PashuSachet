# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update DOMContentLoaded
old_dom_load = """document.addEventListener("DOMContentLoaded", () => {
  initLanguage();
  initSymptomChecker();
  initGIS();
  renderAnimals();
  renderVets();
  renderVetDesk();
  updateAuthUI();
  initModals();
});"""

new_dom_load = """document.addEventListener("DOMContentLoaded", () => {
  initLanguage();
  initSymptomChecker();
  initGIS();
  renderAnimals();
  renderVets();
  renderVetDesk();
  renderParavetInbox();
  renderSampleTracker();
  renderVillageSignalBoard();
  renderOfficerDecisionQueue();
  updateAuthUI();
  initModals();
  // Pre-render AI Vision Sentinel on page load
  simulateVisionDetection('lsd');
});"""

if old_dom_load in js:
    js = js.replace(old_dom_load, new_dom_load)
    print("✓ Updated DOMContentLoaded with all core render functions")

# 2. Update saveOfflineReport to push into villageSignals and re-render Para-Vet Inbox
old_save_offline = """function saveOfflineReport(reportData) {
  try {
    const existing = JSON.parse(localStorage.getItem("pashu_offline_reports") || "[]");
    existing.push(reportData);
    localStorage.setItem("pashu_offline_reports", JSON.stringify(existing));
    console.log("[PashuSachet] Signal stored in offline queue:", reportData.id);
  } catch (err) {
    console.error("Failed to save report to local storage queue:", err);
  }
}"""

new_save_offline = """function saveOfflineReport(reportData) {
  try {
    const existing = JSON.parse(localStorage.getItem("pashu_offline_reports") || "[]");
    existing.unshift(reportData);
    localStorage.setItem("pashu_offline_reports", JSON.stringify(existing));

    // Also push directly into live villageSignals so it IMMEDIATELY appears in Para-Vet Beat Inbox
    villageSignals.unshift({
      id: reportData.id,
      channel: reportData.channel || "DIRECT_WEB",
      species: reportData.species || "Cattle (गाय)",
      symptoms: Array.isArray(reportData.symptoms) ? reportData.symptoms : [reportData.symptoms || "Observed signs"],
      affectedCount: reportData.affectedCount || 1,
      village: reportData.village || "Sangamner",
      farmerName: reportData.farmerName || "Ganesh Patil",
      phone: "+91 98220 18491",
      status: "UNVERIFIED_SIGNAL",
      t0_time: "Just now",
      vitals: "Awaiting Para-Vet Beat Visit"
    });
    renderParavetInbox();
    console.log("[PashuSachet] Signal stored and rendered in Para-Vet queue:", reportData.id);
  } catch (err) {
    console.error("Failed to save report to local storage queue:", err);
  }
}"""

if old_save_offline in js:
    js = js.replace(old_save_offline, new_save_offline)
    print("✓ Updated saveOfflineReport to sync live into Para-Vet queue")

# 3. Update confirmSignal to also update village signal board
old_confirm_signal = """function confirmSignal(id) {
  const sig = villageSignals.find(s => s.id === id);
  if (sig) {
    sig.status = "VERIFIED_SIGNAL";
    sig.verifiedAt = "Just now";
    sig.verifiedBy = "Ganesh Kale (PV-AHM-9104)";
    showToast(`Signal #${id} verified! Propagated to District Surveillance Board.`);
    renderParavetInbox();
  }
}"""

new_confirm_signal = """function confirmSignal(id) {
  const sig = villageSignals.find(s => s.id === id);
  if (sig) {
    sig.status = "VERIFIED_SIGNAL";
    sig.verifiedAt = "Just now";
    sig.verifiedBy = "Ganesh Kale (PV-AHM-9104)";
    showToast(`Signal #${id} verified! Propagated to District Surveillance Board.`);
    renderParavetInbox();
    renderVillageSignalBoard();
  }
}"""

if old_confirm_signal in js:
    js = js.replace(old_confirm_signal, new_confirm_signal)
    print("✓ Updated confirmSignal to update Village Signal Board")

# 4. Update requestSignalSample to add sample and render sample tracker
old_request_sample = """function requestSignalSample(id) {
  const sig = villageSignals.find(s => s.id === id);
  if (!sig) return;
  sig.status = "SAMPLE_REQUESTED";
  sig.sampleRecord = {
    sampleId: "SMP-PUN-" + Math.floor(1000 + Math.random() * 9000),
    sampleType: "Nasal/Vesicular Swab & Serum",
    status: "SAMPLE_NEEDED",
    destinationLab: "RDDL Pune (पाषाण)",
    coldChainTracking: "Active 4°C",
    initiatedBy: "Ganesh Kale (PV-AHM-9104)",
    timestamp: "Just now"
  };
  showToast(`RDDL Sample Kit dispatched for #${id}! Tracking in Closed-Loop pipeline.`);
  renderParavetInbox();
}"""

new_request_sample = """function requestSignalSample(id) {
  const sig = villageSignals.find(s => s.id === id);
  if (!sig) return;
  sig.status = "SAMPLE_REQUESTED";
  const newSampleId = "SMP-PUN-" + Math.floor(1000 + Math.random() * 9000);
  sig.sampleRecord = {
    sampleId: newSampleId,
    sampleType: "Nasal/Vesicular Swab & Serum",
    status: "SAMPLE_NEEDED",
    destinationLab: "RDDL Pune (पाषाण)",
    coldChainTracking: "Active 4°C",
    initiatedBy: "Ganesh Kale (PV-AHM-9104)",
    timestamp: "Just now"
  };

  // Add into active diagnostic samples pipeline
  diagnosticSamples.unshift({
    sampleId: newSampleId,
    animalTag: "MH-24-" + Math.floor(1000 + Math.random() * 9000),
    animalName: sig.species,
    farmerName: sig.farmerName,
    village: sig.village,
    sampleType: "Nasal/Vesicular Swab & Serum",
    diseaseSuspected: sig.symptoms[0] || "Suspected Viral Infection",
    currentStageIndex: 0,
    coldChainTracking: "Optimal (+4.1°C Active)",
    destinationLab: "RDDL Pune (पाषाण)",
    attendingVet: "Dr. Rameshwar Kute (LDO)",
    paraVet: "Ganesh Kale (PV-AHM-9104)",
    labResult: "Awaiting sample arrival at RDDL Pune",
    closureAction: "Cold-chain pickup scheduled",
    updatedAt: "Just now"
  });

  renderParavetInbox();
  renderSampleTracker();
  showToast(`RDDL Sample Kit #${newSampleId} dispatched! Tracking live in Closed-Loop pipeline.`);
}"""

if old_request_sample in js:
    js = js.replace(old_request_sample, new_request_sample)
    print("✓ Updated requestSignalSample to sync live into Closed-Loop Sample Tracker")

# 5. Update activatePersona to quickLogin and render corresponding sections
old_activate_persona = """function activatePersona(role) {
  currentPersona = role;
  
  const pills = ['personaFarmer', 'personaParavet', 'personaLdo', 'personaCollector', 'personaRddl'];
  pills.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });
  
  const activePill = document.getElementById(
    role === 'farmer' ? 'personaFarmer' :
    role === 'paravet' ? 'personaParavet' :
    role === 'ldo' ? 'personaLdo' :
    role === 'collector' ? 'personaCollector' : 'personaRddl'
  );
  if (activePill) activePill.classList.add('active');

  const paravetNav = document.getElementById('paravetNavLink');
  const adminNav = document.getElementById('adminNavLink');

  if (role === 'farmer') {
    if (paravetNav) paravetNav.style.display = 'none';
    if (adminNav) adminNav.style.display = 'none';
    showToast('🧑‍🌾 शेतकरी मोड सक्रिय: जलद ९०-सेकंद तपासणी व पशू आधार उपलब्ध.');
    const el = document.getElementById('symptom-screening');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'paravet') {
    if (paravetNav) paravetNav.style.display = 'inline-block';
    showToast('🩺 पशु सखी / पॅरा-व्हेट मोड: <30 सेकंद पडताळणी रांग सक्रिय.');
    const el = document.getElementById('paravet-inbox');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'ldo') {
    if (paravetNav) paravetNav.style.display = 'inline-block';
    showToast('👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO) मोड: क्लिनिकल तपासणी व औषधोपचार कक्ष.');
    const el = document.getElementById('vet-desk');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'collector') {
    if (adminNav) adminNav.style.display = 'inline-block';
    showToast('🏛️ जिल्हा नियंत्रण कक्ष मोड: ५ किमी प्रतिबंधात्मक झोन व प्रादुर्भाव नियंत्रण नकाशा.');
    if (!ringVaxActive) toggleRingVaxRadius();
    const el = document.getElementById('outbreak-gis');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'rddl') {
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड: RT-PCR चाचणी व नमुना ट्रॅकिंग.');
    const el = document.getElementById('sample-tracker');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }
}"""

new_activate_persona = """function activatePersona(role) {
  currentPersona = role;
  
  const pills = ['personaFarmer', 'personaParavet', 'personaLdo', 'personaCollector', 'personaRddl'];
  pills.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });
  
  const activePill = document.getElementById(
    role === 'farmer' ? 'personaFarmer' :
    role === 'paravet' ? 'personaParavet' :
    role === 'ldo' ? 'personaLdo' :
    role === 'collector' ? 'personaCollector' : 'personaRddl'
  );
  if (activePill) activePill.classList.add('active');

  const paravetNav = document.getElementById('paravetNavLink');
  const adminNav = document.getElementById('adminNavLink');

  if (role === 'farmer') {
    quickLogin('farmer');
    renderAnimals();
    showToast('🧑‍🌾 शेतकरी मोड सक्रिय: जलद ९०-सेकंद तपासणी व पशू आधार उपलब्ध.');
    const el = document.getElementById('symptom-screening');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'paravet') {
    quickLogin('paravet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderParavetInbox();
    showToast('🩺 पशु सखी / पॅरा-व्हेट मोड: <30 सेकंद पडताळणी रांग सक्रिय.');
    const el = document.getElementById('paravet-inbox');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'ldo') {
    quickLogin('vet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderVetDesk();
    showToast('👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO) मोड: क्लिनिकल तपासणी व औषधोपचार कक्ष.');
    const el = document.getElementById('vet-desk');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'collector') {
    quickLogin('officer');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderVillageSignalBoard();
    renderOfficerDecisionQueue();
    showToast('🏛️ जिल्हा नियंत्रण कक्ष मोड: ५ किमी प्रतिबंधात्मक झोन व प्रादुर्भाव नियंत्रण नकाशा.');
    if (!ringVaxActive) toggleRingVaxRadius();
    const el = document.getElementById('outbreak-gis');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'rddl') {
    renderSampleTracker();
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड: RT-PCR चाचणी व नमुना ट्रॅकिंग.');
    const el = document.getElementById('sample-tracker');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }
}"""

if old_activate_persona in js:
    js = js.replace(old_activate_persona, new_activate_persona)
    print("✓ Updated activatePersona with quickLogin and dynamic renders")

# 6. Remove duplicate older simulateVisionDetection (lines 2288-2329)
old_vision_dup = """// AI Clinical Vision Detection Simulation
function simulateVisionDetection(conditionKey) {
  const box = document.getElementById("visionOutputBox");
  const content = document.getElementById("visionResultContent");
  if (!box || !content) return;

  box.style.display = "block";
  content.innerHTML = `<span style="color:#d97706;">⏳ Analyzing image morphology via MobileNet-V3 livestock model...</span>`;

  setTimeout(() => {
    drawLesionOnCanvas(conditionKey);
    if (conditionKey === 'lsd') {
      content.innerHTML = `
        <strong>🔍 Vision Detection Result:</strong> <span style="color:#b91c1c; font-weight:800;">Circumscribed Cutaneous Nodules Detected (Confidence: 89%)</span><br>
        <strong>Lesion Profile:</strong> Raised dermal lumps (2-4cm diameter) on neck and flank region. Consistent with <em>Lumpy Skin Disease</em>.<br>
        <span style="font-size:0.78rem; color:#15803d; font-weight:700;">✓ Synced with clinical screening: 'Skin Nodules / Lumps' checked automatically.</span>
      `;
      // Check the skin nodules box automatically
      const cb = document.querySelector('input[name="symptom"][value="skin_nodules"]');
      if (cb) { cb.checked = true; cb.dispatchEvent(new Event("change")); }
    } else if (conditionKey === 'fmd') {
      content.innerHTML = `
        <strong>🔍 Vision Detection Result:</strong> <span style="color:#b91c1c; font-weight:800;">Epithelial Vesicles & Dental Pad Erosions (Confidence: 93%)</span><br>
        <strong>Lesion Profile:</strong> Ruptured vesicular ulcers and excessive stringy saliva. Consistent with <em>Foot and Mouth Disease (FMD)</em>.<br>
        <span style="font-size:0.78rem; color:#15803d; font-weight:700;">✓ Synced with clinical screening: 'Mouth Blisters' & 'Lameness' checked automatically.</span>
      `;
      const cb1 = document.querySelector('input[name="symptom"][value="mouth_lesions"]');
      if (cb1) { cb1.checked = true; cb1.dispatchEvent(new Event("change")); }
      const cb2 = document.querySelector('input[name="symptom"][value="lameness"]');
      if (cb2) { cb2.checked = true; cb2.dispatchEvent(new Event("change")); }
    } else if (conditionKey === 'mastitis') {
      content.innerHTML = `
        <strong>🔍 Vision Detection Result:</strong> <span style="color:#b45309; font-weight:800;">Asymmetric Quarter Erythema & Udder Swelling (Confidence: 87%)</span><br>
        <strong>Lesion Profile:</strong> Hyperemia in right hind quarter with flaked milk secretions. Consistent with <em>Clinical Bovine Mastitis</em>.<br>
        <span style="font-size:0.78rem; color:#15803d; font-weight:700;">✓ Synced with clinical screening: 'Udder Swelling' checked automatically.</span>
      `;
      const cb = document.querySelector('input[name="symptom"][value="udder_swelling"]');
      if (cb) { cb.checked = true; cb.dispatchEvent(new Event("change")); }
    }
    showToast("AI Vision analysis complete and correlated with symptom form!");
  }, 900);
}"""

if old_vision_dup in js:
    js = js.replace(old_vision_dup, "// (Unified supercharged simulateVisionDetection active below)")
    print("✓ Removed duplicate older simulateVisionDetection")

# 7. Remove duplicate older drawLesionOnCanvas
old_draw_dup_start = "function drawLesionOnCanvas(lesionType, imageSource) {"
old_draw_dup_end = "if (hudMetrics) hudMetrics.textContent = `CONF: ${box.conf} | AREA: 16.4 cm²`;\n}"

if old_draw_dup_start in js and old_draw_dup_end in js:
    s_idx = js.find(old_draw_dup_start)
    e_idx = js.find(old_draw_dup_end) + len(old_draw_dup_end)
    js = js[:s_idx] + "// (Unified supercharged drawLesionOnCanvas active below)\n" + js[e_idx:]
    print("✓ Removed duplicate older drawLesionOnCanvas")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("js/app.js successfully updated and unified!")

