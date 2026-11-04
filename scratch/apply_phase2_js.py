# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("js/app.js", "r", encoding="utf-8") as f:
    js_content = f.read().replace('\r\n', '\n')

# Check if Phase 2 handlers are already present
phase2_code = """
// ==========================================
// PHASE 2: ULTRA-INCLUSIVE INTAKE & USSD/IVR
// ==========================================

// USSD State Machine (*992#)
let ussdState = {
  step: 0,
  species: "Cattle",
  symptom: "",
  count: 1,
  village: "Sangamner"
};

function openUssdModal() {
  const modal = document.getElementById("ussdModal");
  if (modal) {
    modal.classList.add("active");
    resetUssdState();
  }
}

function closeUssdModal() {
  const modal = document.getElementById("ussdModal");
  if (modal) modal.classList.remove("active");
}

function appendUssdKey(key) {
  const input = document.getElementById("ussdInput");
  if (input) {
    input.value += key;
    input.focus();
  }
}

function resetUssdState() {
  ussdState = { step: 0, species: "Cattle", symptom: "", count: 1, village: "Sangamner" };
  const screen = document.getElementById("ussdScreen");
  const input = document.getElementById("ussdInput");
  if (screen) {
    screen.innerText = "PashuSachet Gram Signal (*992#)\\n1. Cattle (गाय)\\n2. Buffalo (म्हैस)\\n3. Goat / Sheep (शेळी/मेंढी)\\n4. Poultry (कुक्कुट)\\n0. Exit";
  }
  if (input) input.value = "";
}

function submitUssdStep() {
  const input = document.getElementById("ussdInput");
  const screen = document.getElementById("ussdScreen");
  if (!input || !screen) return;
  const val = input.value.trim();
  input.value = "";

  if (ussdState.step === 0) {
    if (val === "0") {
      closeUssdModal();
      return;
    }
    const speciesMap = { "1": "Cattle (गाय)", "2": "Buffalo (म्हैस)", "3": "Goat/Sheep (शेळी/मेंढी)", "4": "Poultry (कुक्कुट)" };
    ussdState.species = speciesMap[val] || "Cattle";
    ussdState.step = 1;
    screen.innerText = `Selected: ${ussdState.species}\\nSelect Primary Sign:\\n1. Blisters/Saliva (तोंडातील फोड/लाळ)\\n2. Skin Lumps (त्वचेवर गाठी)\\n3. High Fever (तीव्र ताप)\\n4. Sudden Mortality (दगावले/मृत्यू)\\n0. Back`;
    return;
  }

  if (ussdState.step === 1) {
    if (val === "0") {
      resetUssdState();
      return;
    }
    const symptomMap = {
      "1": "Blisters in mouth / Salivation",
      "2": "Skin nodules / Lumps",
      "3": "High Fever & Anorexia",
      "4": "Post-Loss Sudden Mortality"
    };
    ussdState.symptom = symptomMap[val] || "Observed signs";
    ussdState.step = 2;
    screen.innerText = `Sign: ${ussdState.symptom}\\nEnter number of affected animals (संख्या टाका):\\n(e.g. 1, 2, 5)`;
    return;
  }

  if (ussdState.step === 2) {
    ussdState.count = parseInt(val) || 1;
    ussdState.step = 3;
    screen.innerText = `Affected: ${ussdState.count}\\nConfirm Village Location:\\n1. Sangamner (संगमनेर)\\n2. Rahata (राहाता)\\n3. Shirdi Rural (शिर्डी)\\n4. Akole (अकोले)`;
    return;
  }

  if (ussdState.step === 3) {
    const villageMap = { "1": "Sangamner", "2": "Rahata", "3": "Shirdi Rural", "4": "Akole" };
    ussdState.village = villageMap[val] || "Sangamner";
    ussdState.step = 4;

    const reportId = "GSS-USSD-" + Math.floor(1000 + Math.random() * 9000);
    const reportData = {
      id: reportId,
      channel: "USSD",
      species: ussdState.species,
      symptoms: [ussdState.symptom],
      affectedCount: ussdState.count,
      village: ussdState.village,
      status: "UNVERIFIED_SIGNAL",
      timestamp: new Date().toISOString()
    };

    saveOfflineReport(reportData);
    screen.innerText = `SUCCESS! [पशूसचेत]\\nReport ID: #${reportId}\\nVillage: ${ussdState.village}\\nLocal Para-Vet Ganesh Kale notified for beat inspection.\\nImmediate safe steps sent via SMS.\\nPress 0 to close session.`;
    showToast(`USSD Micro-Report #${reportId} submitted successfully via GSM code!`);
    return;
  }

  if (ussdState.step === 4) {
    closeUssdModal();
  }
}

// Missed Call & Marathi IVR Gateway Simulation
function openMissedCallModal() {
  const modal = document.getElementById("missedCallModal");
  if (modal) modal.classList.add("active");
}

function closeMissedCallModal() {
  const modal = document.getElementById("missedCallModal");
  if (modal) modal.classList.remove("active");
}

function openVoiceIvrModal() {
  openMissedCallModal();
}

function simulateMissedCallCallback() {
  const statusEl = document.getElementById("ivrCallStatus");
  if (!statusEl) return;

  statusEl.innerHTML = `<span style="color:#d97706;">⏳ शेतकरी क्रमांक +91 98220 18491 कडून 1800-889-1962 वर १ रिंग दिली गेली... कॉल कट झाला.</span>`;

  setTimeout(() => {
    statusEl.innerHTML = `<span style="color:#2563eb;">📞 पशूसचेत सर्व्हरकडून त्वरित कॉल-बॅक! कॉल कनेक्ट झाला... मराठी IVR ऑडिओ सुरू आहे.</span>`;
  }, 1000);

  setTimeout(() => {
    statusEl.innerHTML = `<span style="color:#7c3aed;">🎙️ व्हॉइस इनपुट नोंदवले: 'गाय, ३ दिवस ताप, तोंडातील फोड आणि लाळ, २ जनावरे बाधित'.</span>`;
  }, 2200);

  setTimeout(() => {
    const reportId = "GSS-IVR-" + Math.floor(1000 + Math.random() * 9000);
    const reportData = {
      id: reportId,
      channel: "VOICE_IVR",
      species: "Cattle (गाय)",
      symptoms: ["High Fever", "Mouth Blisters / Salivation"],
      affectedCount: 2,
      village: "Sangamner",
      status: "UNVERIFIED_SIGNAL",
      timestamp: new Date().toISOString()
    };
    saveOfflineReport(reportData);

    statusEl.innerHTML = `<span style="color:#166534; font-weight:700;">✅ तक्रार नोंदणी पूर्ण! तक्रार क्रमांक #${reportId}.<br>पशुमित्र गणेश काळे (संगमनेर बीट) यांना तपासणीसाठी मेसेज पाठवला आहे. शेतकरी मोबाईलवर मराठी SMS पाठवला.</span>`;
    showToast(`Voice IVR Signal #${reportId} captured and queued for Para-Vet!`);
  }, 3600);
}

// UI Toggles & Field Synchronizers
function toggleProxyFields(checked) {
  const box = document.getElementById("proxyFieldsBox");
  if (box) box.style.display = checked ? "block" : "none";
}

function toggleMortalityFields(checked) {
  const box = document.getElementById("mortalityCountBox");
  if (box) box.style.display = checked ? "block" : "none";
}

function syncSpecies(val) {
  const hiddenInput = document.getElementById("animalSpecies");
  if (hiddenInput) hiddenInput.value = val;
}

function toggleSymptomVal(val) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb) {
    cb.checked = !cb.checked;
    cb.dispatchEvent(new Event("change"));
  }
}

// Offline-First Queue Engine
function saveOfflineReport(reportData) {
  try {
    const existing = JSON.parse(localStorage.getItem("pashu_offline_reports") || "[]");
    existing.push(reportData);
    localStorage.setItem("pashu_offline_reports", JSON.stringify(existing));
    console.log("[PashuSachet] Signal stored in offline queue:", reportData.id);
  } catch (err) {
    console.error("Failed to save report to local storage queue:", err);
  }
}

function syncPendingReports() {
  try {
    const pending = JSON.parse(localStorage.getItem("pashu_offline_reports") || "[]");
    if (pending.length > 0) {
      console.log(`[PashuSachet] Auto-syncing ${pending.length} pending reports to village signal board...`);
      showToast(`Network restored! Synced ${pending.length} offline signals.`);
      // In a real cloud backend, POST /api/v1/reports/sync would happen here.
    }
  } catch (err) {
    console.error("Sync error:", err);
  }
}

window.addEventListener("online", syncPendingReports);
"""

# Append Phase 2 functions if not present
if "submitUssdStep" not in js_content:
    js_content += "\n" + phase2_code
    print("Appended Phase 2 functions to js/app.js!")
else:
    print("Phase 2 functions already in js/app.js!")

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("js/app.js updated successfully!")

