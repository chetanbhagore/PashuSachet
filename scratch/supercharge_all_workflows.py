# -*- coding: utf-8 -*-
"""
Supercharge all operational workflows in js/app.js:
Admin Decision Queue, Village Signals, 1962 MVU, GIS Map Inspector,
Para-Vet Vitals Modal, Vet Tab Switcher, RDDL RT-PCR Thermocycler.
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Check and add modal helpers & navigation functions
modal_and_nav_code = '''
// ==========================================================================
// OPERATIONAL MODAL CONTROLLERS & REAL INTERACTIVE WORKFLOWS
// ==========================================================================

function closeAboutBlueprintModal() {
  const modal = document.getElementById("aboutBlueprintModal");
  if (modal) modal.classList.remove("active");
}

function openAboutBlueprintModal() {
  const modal = document.getElementById("aboutBlueprintModal");
  if (modal) modal.classList.add("active");
}

function closeAddAnimalModal() {
  const modal = document.getElementById("addAnimalModal");
  if (modal) modal.classList.remove("active");
}

function openAddAnimalModal() {
  const modal = document.getElementById("addAnimalModal");
  if (modal) modal.classList.add("active");
}

function startGuidedTriage() {
  if (typeof switchNotebookTab === 'function') {
    switchNotebookTab('viewFarmerTriage');
  }
  if (typeof goToTriageStep === 'function') {
    goToTriageStep(1);
  }
  const el = document.getElementById('viewFarmerTriage');
  if (el && typeof el.scrollIntoView === 'function') {
    el.scrollIntoView({ behavior: 'smooth' });
  }
}

function switchVetTab(tab) {
  const apts = document.getElementById("vetAppointmentsContainer");
  const cases = document.getElementById("vetCasesContainer");
  const tabApts = document.getElementById("tabAptsBtn");
  const tabReferrals = document.getElementById("tabReferralsBtn");
  if (!apts || !cases) return;
  if (tab === "cases") {
    apts.style.display = "none";
    cases.style.display = "block";
    if (tabApts) tabApts.classList.remove("primary");
    if (tabReferrals) tabReferrals.classList.add("primary");
  } else {
    cases.style.display = "none";
    apts.style.display = "block";
    if (tabApts) tabApts.classList.add("primary");
    if (tabReferrals) tabReferrals.classList.remove("primary");
  }
}

// SMS Broadcast Modal Controls
let currentBroadcastVillage = "निमगाव जाळी";
let currentBroadcastCount = 480;

function openVillageSmsBroadcastModal(village, disease, count) {
  currentBroadcastVillage = village || "निमगाव जाळी";
  currentBroadcastCount = count || 480;
  const modal = document.getElementById("villageSmsModal");
  const targetEl = document.getElementById("smsTargetVillage");
  const countEl = document.getElementById("smsTargetCount");
  const contentEl = document.getElementById("smsMessageContent");
  const pBar = document.getElementById("smsProgressBarContainer");
  
  if (targetEl) targetEl.textContent = currentBroadcastVillage;
  if (countEl) countEl.textContent = `${currentBroadcastCount} शेतकरी`;
  if (contentEl) {
    contentEl.value = `अत्यंत महत्त्वाचे: पशूसचेत व पशुसंवर्धन विभाग अलर्ट. ${currentBroadcastVillage} येथे ${disease || 'लाळ्या खुरकूत (FMD)'} चे संशयित रुग्ण आढळले आहेत. कृपया सर्व जनावरे गोठ्यात बांधून ठेवावीत, चारा-पाणी वेगळे करावे. १९६२ फिरते पथक गावात दाखल होत आहे. - जिल्हाधिकारी कार्यालय.`;
  }
  if (pBar) pBar.style.display = "none";
  if (modal) modal.classList.add("active");
}

function closeVillageSmsModal() {
  const modal = document.getElementById("villageSmsModal");
  if (modal) modal.classList.remove("active");
}

function executeSmsBroadcast() {
  const pBarCont = document.getElementById("smsProgressBarContainer");
  const pBar = document.getElementById("smsProgressBar");
  const pPct = document.getElementById("smsProgressPercent");
  const btn = document.getElementById("btnSendSmsBlast");
  
  if (pBarCont) pBarCont.style.display = "block";
  if (btn) btn.disabled = true;

  let progress = 0;
  const interval = setInterval(() => {
    progress += 20;
    if (pBar) pBar.style.width = `${progress}%`;
    if (pPct) pPct.textContent = `${progress}%`;
    if (progress >= 100) {
      clearInterval(interval);
      setTimeout(() => {
        showToast(`✓ ${currentBroadcastCount} SMS यशस्वीरित्या पाठवले! (CDAC Gateway)`);
        closeVillageSmsModal();
        if (btn) btn.disabled = false;
        if (pBar) pBar.style.width = "0%";
      }, 500);
    }
  }, 120);
}

// Government Official Order (GR) Modal Controls
function viewOfficialOrder(decId) {
  const modal = document.getElementById("officialOrderModal");
  const content = document.getElementById("officialOrderContent");
  if (!modal || !content) return;

  const orders = {
    "DEC-001": {
      title: "५ किमी रिंग लसीकरण व जैवसुरक्षा आदेश",
      grNo: "AH-SURV-2026-DHU-0914",
      date: "०४ नोव्हेंबर २०२६",
      authority: "मा. जिल्हाधिकारी व अध्यक्ष, जिल्हा साथरोग नियंत्रण समिती, धुळे",
      subject: "निमगाव जाळी व लगतच्या ५ किमी परिक्षेत्रात खुरकूत (FMD) प्रादुर्भाव रोखण्यासाठी रिंग लसीकरण मोहीम राबविण्याबाबत.",
      provisions: [
        "पशूसचेत प्रणालीद्वारे निमगाव जाळी येथे सलग ४ खुरकूत संशयित केसेस नोंदवण्यात आल्या आहेत.",
        "साथरोग प्रतिबंधक कायदा २००९ च्या कलम ६ नुसार प्रभावित क्षेत्राभोवती ५ किमी त्रिज्या 'नियंत्रित क्षेत्र' घोषित करण्यात येत आहे.",
        "१९६२ फिरत्या पथकास (MVU 04) त्वरित २,४०० डोस वितरणासह घटनास्थळी रवाना करण्याचे आदेश देण्यात येत आहेत.",
        "पुढील ७ दिवस सर्व जनावरांचे आठवडे बाजार तात्पुरते स्थगित राहतील."
      ]
    },
    "DEC-002": {
      title: "आठवडे बाजार निलंबन व पोलीस चेकपोस्ट आदेश",
      grNo: "AH-MKT-2026-AHM-0412",
      date: "०४ नोव्हेंबर २०२६",
      authority: "जिल्हा पशुसंवर्धन उपआयुक्त (DVO), अहिल्यानगर",
      subject: "राहाता तालुक्यातील जनावरांच्या आंतरजिल्हा वाहतुकीवर तात्पुरती बंदी व चेकपोस्ट उभारणीबाबत.",
      provisions: [
        "संशयित लंपी व खुरकूत विषाणूचा इतर तालुक्यांत प्रसार रोखण्यासाठी राहाता गुरे बाजार बंद ठेवण्यात येत आहे.",
        "वाहतूक करणाऱ्या सर्व वाहनांचे हायपोक्लोराइट फवारणीद्वारे निर्जंतुकीकरण बंधनकारक राहील.",
        "स्थानिक पोलीस ठाण्याने तपासणी नाक्यांवर महसूल व पशुसंवर्धन कर्मचाऱ्यांना २४x७ सुरक्षा पुरवावी."
      ]
    },
    "DEC-003": {
      title: "झुनोटिक ब्रूसेलोसिस दूध संकलन विथड्रॉवल व DHO सूचना",
      grNo: "AH-ONEHEALTH-2026-NIV-018",
      date: "०४ नोव्हेंबर २०२६",
      authority: "जिल्हा आरोग्य अधिकारी (DHO) व जिल्हा पशुसंवर्धन अधिकारी",
      subject: "संशयित ब्रूसेलोसिस बाधित गोठ्यातील कच्च्या दुधाच्या संकलनावर तात्काळ निर्बंध घालण्याबाबत.",
      provisions: [
        "मानवी आरोग्यास संभाव्य धोका (Undulant Fever) लक्षात घेऊन One Health Sentinel सक्रिय करण्यात आले आहे.",
        "संबंधित बाधित गोठ्यातील दूध बल्क मिल्क कुलर (BMCU) मध्ये मिसळण्यास बंदी घालण्यात आली आहे.",
        "पशु सखी व आशा सेविका यांनी बाधित शेतकरी कुटुंबातील सर्व व्यक्तींची आरोग्य तपासणी करावी."
      ]
    }
  };

  const ord = orders[decId] || orders["DEC-001"];

  content.innerHTML = `
    <div style="text-align:center; border-bottom:2px solid #0f172a; padding-bottom:12px; margin-bottom:14px;">
      <div style="font-size:12px; font-weight:800; letter-spacing:1px; color:#475569;">महाराष्ट्र शासन • पशुसंवर्धन विभाग</div>
      <h3 style="margin:4px 0; font-size:17px; color:#0f172a; font-weight:800;">${ord.title}</h3>
      <div style="font-size:11.5px; color:#64748b;">आदेश क्रमांक: <strong>${ord.grNo}</strong> • दिनांक: ${ord.date}</div>
    </div>
    <div style="margin-bottom:10px;"><strong>सक्षम प्राधिकारी:</strong> ${ord.authority}</div>
    <div style="margin-bottom:12px; background:#f8fafc; padding:8px 12px; border-left:3px solid var(--accent-turmeric); border-radius:2px;">
      <strong>विषय:</strong> ${ord.subject}
    </div>
    <div style="margin-bottom:14px;">
      <strong>आदेशातील प्रमुख तरतुदी:</strong>
      <ol style="margin:6px 0 0 18px; padding:0; display:flex; flex-direction:column; gap:6px;">
        ${ord.provisions.map(p => `<li>${p}</li>`).join("")}
      </ol>
    </div>
    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #cbd5e1; padding-top:12px; margin-top:14px; font-size:11.5px; color:#64748b;">
      <div>✓ डिजिटल स्वाक्षरी: मा. जिल्हाधिकारी कार्यालय</div>
      <div>प्रणाली: PashuSachet Surveillance Sentinel (NIC)</div>
    </div>
  `;

  modal.classList.add("active");
  if (typeof renderIcons === 'function') renderIcons();
}

function closeOfficialOrderModal() {
  const modal = document.getElementById("officialOrderModal");
  if (modal) modal.classList.remove("active");
}

// Para-Vet Vitals Modal Controls
function promptSignalVitals(id) {
  const modal = document.getElementById("paravetVitalsModal");
  const idInput = document.getElementById("vitalsSignalId");
  if (idInput) idInput.value = id;
  if (modal) modal.classList.add("active");
}

function closeParavetVitalsModal() {
  const modal = document.getElementById("paravetVitalsModal");
  if (modal) modal.classList.remove("active");
}

function submitParavetVitals() {
  const id = document.getElementById("vitalsSignalId").value;
  const temp = document.getElementById("vitalsTemp").value;
  const notes = document.getElementById("vitalsNotes").value;
  
  const sig = villageSignals.find(s => s.id === id);
  if (sig) {
    sig.status = "VERIFIED_ON_FARM";
    sig.verifiedBy = "सुनिता पाटील (Pashu Sakhi)";
    sig.verifiedTemp = `${temp}°F`;
    sig.verifiedAt = "आत्ताच";
  }

  showToast(`सिग्नल #${id} प्रत्यक्ष पडताळणी पूर्ण! तापमान: ${temp}°F.`);
  closeParavetVitalsModal();
  renderParavetInbox();
  renderVillageSignalBoard();
}

// RDDL Real-time RT-PCR Simulation Controls
function openRddlPcrModal(sampleId) {
  const modal = document.getElementById("rddlPcrModal");
  const idEl = document.getElementById("pcrSampleId");
  const runState = document.getElementById("pcrRunningState");
  const resState = document.getElementById("pcrResultState");
  const countEl = document.getElementById("pcrCycleCount");
  const pBar = document.getElementById("pcrProgress");
  const btn = document.getElementById("btnRunPcr");

  if (idEl) idEl.textContent = sampleId || "SMP-2026-041";
  if (runState) runState.style.display = "block";
  if (resState) resState.style.display = "none";
  if (countEl) countEl.textContent = "Cycle: 0 / 40";
  if (pBar) pBar.style.width = "0%";
  if (btn) btn.disabled = false;
  if (modal) modal.classList.add("active");
}

function closeRddlPcrModal() {
  const modal = document.getElementById("rddlPcrModal");
  if (modal) modal.classList.remove("active");
}

function startRtPcrThermocycler() {
  const countEl = document.getElementById("pcrCycleCount");
  const pBar = document.getElementById("pcrProgress");
  const btn = document.getElementById("btnRunPcr");
  const resState = document.getElementById("pcrResultState");

  if (btn) btn.disabled = true;
  let cycle = 0;
  const interval = setInterval(() => {
    cycle += 4;
    if (countEl) countEl.textContent = `Cycle: ${cycle} / 40 (Denaturation 95°C / Annealing 60°C)`;
    if (pBar) pBar.style.width = `${(cycle / 40) * 100}%`;

    if (cycle >= 40) {
      clearInterval(interval);
      if (resState) resState.style.display = "block";
      showToast("✓ RT-PCR चाचणी पूर्ण: FMDV Serotype O पॉझिटिव्ह (Ct 18.42)!");
      advanceSampleStage("SMP-2026-041");
    }
  }, 100);
}
'''

# 2. Real Interactive Actions for Village Signals & GIS Map
operations_code = '''
// ==========================================================================
// REAL TACTILE ACTIONS FOR VILLAGE SIGNALS & GIS OPERATIONS
// ==========================================================================

function focusVillageOnMap(village, x, y, disease, count) {
  const gisSection = document.getElementById("outbreak-gis") || document.getElementById("workspaceOfficer");
  const svgMap = document.getElementById("gisSvgMap");
  const inspector = document.getElementById("mapPinInspector");
  const details = document.getElementById("mapPinDetails");

  if (svgMap) {
    // Add glowing targeting circle if not exists
    let reticle = document.getElementById("mapTargetReticle");
    if (!reticle) {
      reticle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      reticle.setAttribute("id", "mapTargetReticle");
      reticle.setAttribute("r", "28");
      reticle.setAttribute("fill", "rgba(221, 167, 58, 0.35)");
      reticle.setAttribute("stroke", "#DDA73A");
      reticle.setAttribute("stroke-width", "3");
      reticle.setAttribute("stroke-dasharray", "4");
      svgMap.appendChild(reticle);
    }
    reticle.setAttribute("cx", x || 340);
    reticle.setAttribute("cy", y || 180);
    reticle.style.display = "block";
  }

  if (inspector && details) {
    inspector.style.display = "block";
    details.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="brand-emblem" style="color:var(--urgency-critical);"><span data-icon="map-pin" data-size="16"></span></div>
          <strong style="font-size:15px; color:var(--ink-primary);">${village}</strong>
        </div>
        <span class="badge-pill" style="background:var(--urgency-critical-light); color:var(--urgency-critical);">
          ${count || 4} Signals Verified
        </span>
      </div>
      <div style="font-size:13px; color:var(--ink-secondary); margin:8px 0;">
        संशयित आजार: <strong style="color:var(--urgency-critical);">${disease || 'FMD (लाळ्या खुरकूत)'}</strong> | अधिकारक्षेत्र: <strong>CVD साक्री व संगमनेर</strong>
      </div>
      <div style="display:flex; gap:8px; margin-top:10px; flex-wrap:wrap;">
        <button type="button" class="btn btn-sm btn-primary" onclick="dispatchMvuToVillage('${village}', '${disease}')">
          <span data-icon="truck" data-size="14"></span>
          <span>१९६२ पथक रवाना करा</span>
        </button>
        <button type="button" class="btn btn-sm btn-outline" onclick="openVillageSmsBroadcastModal('${village}', '${disease}', 480)">
          <span data-icon="send" data-size="14"></span>
          <span>GP SMS सूचना पाठवा</span>
        </button>
        <button type="button" class="btn btn-sm btn-danger" onclick="enforceRingQuarantine('${village}', '${disease}')">
          <span data-icon="shield-alert" data-size="14"></span>
          <span>५ किमी रिंग विलगीकरण</span>
        </button>
        <button type="button" class="btn btn-sm btn-outline" onclick="exportNadresBatch()">
          <span data-icon="download" data-size="14"></span>
          <span>NADRES V2 निर्यात</span>
        </button>
      </div>
    `;
    if (typeof renderIcons === 'function') renderIcons();
  }

  showToast(`नकाशावर लक्ष्यित केले: ${village}.`);
}

let mvuCountdownTimer = null;

function dispatchMvuToVillage(village, disease) {
  const card = document.getElementById("mvuDispatchCard");
  const ticket = document.getElementById("mvuTicketDetails");
  const gps = document.getElementById("mvuGpsDist");

  if (ticket) {
    ticket.innerHTML = `<strong>सद्यस्थिती:</strong> ${village} कडे तातडीने रवाना • अंतर: ३.४ किमी • चालक: मोहन शिंदे (MH-17-AG-1962)`;
  }
  if (gps) {
    gps.innerHTML = `<span style="color:var(--urgency-critical); font-weight:700;">🚨 LIVE GPS DISPATCH: ३२ किमी/तास गती • सायरन चालू • अंदाजे पोहोच: <span id="mvuLiveEta">०८:४५ मिनिटे</span></span>`;
  }

  if (mvuCountdownTimer) clearInterval(mvuCountdownTimer);
  let seconds = 525; // 8 mins 45s
  mvuCountdownTimer = setInterval(() => {
    seconds--;
    if (seconds <= 0) {
      clearInterval(mvuCountdownTimer);
      if (gps) gps.innerHTML = `<span style="color:var(--status-success); font-weight:700;">✓ घटनास्थळी दाखल (ON-SCENE AT ${village}) • तपासणी व लसीकरण सुरू!</span>`;
      showToast(`१९६२ फिरते पथक ${village} येथे दाखल झाले!`);
    } else {
      const mins = Math.floor(seconds / 60);
      const remSecs = seconds % 60;
      const etaEl = document.getElementById("mvuLiveEta");
      if (etaEl) etaEl.textContent = `${String(mins).padStart(2, '0')}:${String(remSecs).padStart(2, '0')} मिनिटे`;
    }
  }, 1000);

  if (typeof playMvuSirenTone === 'function') {
    try { playMvuSirenTone(); } catch(e) {}
  }

  showToast(`१९६२ फिरते पथक (MVU Unit 04) ${village} साठी रवाना!`);
}

function enforceRingQuarantine(village, disease) {
  if (typeof ringVaxActive !== 'undefined' && !ringVaxActive) {
    toggleRingVaxRadius();
  }
  showToast(`५ किमी रिंग विलगीकरण आदेश जारी (Sec 144 / Animal Contagious Disease Act) around ${village}!`);
}
'''

# 3. Supercharged renderVillageSignalBoard
new_village_signal_board = '''function renderVillageSignalBoard() {
  const grid = document.getElementById("villageSignalsGrid");
  if (!grid) return;

  const clusters = [
    {
      id: "SIG-NIM-01",
      village: "निमगाव जाळी (Nimgaon Jali)",
      taluka: "संगमनेर (Sangamner)",
      count: 4,
      disease: "Foot and Mouth Disease (FMD / लाळ्या खुरकूत)",
      symptoms: "लाळ गळणे, खुरांमध्ये फोड, १०४.२°F ताप",
      species: "गाय (३), बैल (१)",
      atRisk: 840,
      isSurge: true,
      status: "SURGE_CLUSTER",
      lat: 340, lng: 180
    },
    {
      id: "SIG-ASH-02",
      village: "आश्वी खुर्द (Ashwi Khurd)",
      taluka: "संगमनेर (Sangamner)",
      count: 3,
      disease: "Lumpy Skin Disease (LSD / लंपी)",
      symptoms: "त्वचेवर गाठी, डोळ्यांतून पाणी, भूक मंदावणे",
      species: "गाय (२), वासरू (१)",
      atRisk: 620,
      isSurge: true,
      status: "SURGE_CLUSTER",
      lat: 420, lng: 160
    },
    {
      id: "SIG-SAK-03",
      village: "साक्री (Sakri Taluka HQ)",
      taluka: "साक्री (Sakri)",
      count: 2,
      disease: "Black Quarter (BQ / फऱ्या)",
      symptoms: "मांडीला सूज, लंगडणे, स्नायूंतून आवाज",
      species: "म्हैस (२)",
      atRisk: 410,
      isSurge: false,
      status: "WATCH_CLUSTER",
      lat: 480, lng: 220
    },
    {
      id: "SIG-RAH-04",
      village: "राहाता (Rahata)",
      taluka: "राहाता (Rahata)",
      count: 1,
      disease: "Brucellosis (ब्रूसेलोसिस)",
      symptoms: "गर्भपात (शेवटच्या टप्प्यात), वार अडकणे",
      species: "दूध देणारी गाय (१)",
      atRisk: 950,
      isSurge: false,
      status: "ZOONOTIC_MONITOR",
      lat: 280, lng: 250
    }
  ];

  grid.innerHTML = clusters.map(c => `
    <div class="village-signal-card" id="card-${c.id}" style="border-top: 4px solid ${c.isSurge ? 'var(--urgency-critical)' : 'var(--accent-turmeric)'};">
      <div style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <h4 style="margin:0; font-size:16px; font-weight:700; color:var(--ink-primary);">${c.village}</h4>
          <div style="font-size:12px; color:var(--ink-secondary); margin-top:2px;">तालुका: ${c.taluka}</div>
        </div>
        <span class="badge-pill" style="background:${c.isSurge ? 'var(--urgency-critical-light)' : 'var(--accent-turmeric-light)'}; color:${c.isSurge ? 'var(--urgency-critical)' : '#92400e'};">
          ${c.count} Signals Verified
        </span>
      </div>

      <div style="font-size:13px; color:var(--ink-primary); margin:8px 0; background:var(--bg-paper-subtle); padding:10px; border-radius:var(--radius-sm);">
        <div><strong>बाधित जनावरे:</strong> ${c.species}</div>
        <div style="margin-top:3px;"><strong>संशयित आजार:</strong> <span style="color:${c.isSurge ? 'var(--urgency-critical)' : 'var(--accent-turmeric)'}; font-weight:700;">${c.disease}</span></div>
        <div style="margin-top:3px; font-size:12px; color:var(--ink-secondary);"><strong>लक्षणे:</strong> ${c.symptoms}</div>
        <div style="margin-top:3px; font-size:12px; color:var(--status-info);"><strong>धोका असलेले पशूधन:</strong> ${c.atRisk} जनावरे</div>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:auto;">
        <button type="button" class="btn btn-sm btn-outline" onclick="focusVillageOnMap('${c.village}', ${c.lat}, ${c.lng}, '${c.disease}', ${c.count})">
          <span data-icon="map-pin" data-size="14"></span>
          <span>नकाशावर पाहा</span>
        </button>
        <button type="button" class="btn btn-sm btn-primary" onclick="dispatchMvuToVillage('${c.village}', '${c.disease}')">
          <span data-icon="truck" data-size="14"></span>
          <span>१९६२ पथक रवाना</span>
        </button>
        <button type="button" class="btn btn-sm btn-outline" onclick="openVillageSmsBroadcastModal('${c.village}', '${c.disease}', ${c.atRisk})">
          <span data-icon="send" data-size="14"></span>
          <span>GP SMS सूचना</span>
        </button>
        <button type="button" class="btn btn-sm btn-danger" onclick="enforceRingQuarantine('${c.village}', '${c.disease}')">
          <span data-icon="shield-alert" data-size="14"></span>
          <span>५ किमी विलगीकरण</span>
        </button>
      </div>
    </div>
  `).join("");

  if (typeof renderIcons === 'function') renderIcons();
}'''

# 4. Supercharged renderOfficerDecisionQueue
new_officer_decision_queue = '''function renderOfficerDecisionQueue() {
  const container = document.getElementById("officerDecisionQueue");
  if (!container) return;

  container.innerHTML = officerDecisions.map(dec => `
    <div class="decision-card" style="border-left-color: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical)' : 'var(--accent-turmeric)'};">
      <div style="flex: 1;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px; flex-wrap: wrap;">
          <strong style="color: var(--ink-primary); font-size: 15px;">${dec.title}</strong>
          <span class="badge-pill" style="background: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical-light)' : 'var(--accent-turmeric-light)'}; color: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical)' : '#92400e'};">
            ${dec.priority}
          </span>
          <span style="font-size: 11.5px; color: var(--ink-secondary);">कायदेशीर तरतूद: साथरोग प्रतिबंधक कायदा २००९ कलम ६</span>
        </div>
        <p style="font-size: 13px; color: var(--ink-secondary); margin: 0; line-height: 1.5;">
          ${dec.details}
        </p>
      </div>

      <div style="flex-shrink: 0; display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
        <button type="button" class="btn btn-sm btn-outline" onclick="viewOfficialOrder('${dec.id}')">
          <span data-icon="file-text" data-size="14"></span>
          <span>आदेश पहा (GR)</span>
        </button>
        ${dec.status === 'PENDING' ? `
          <button type="button" class="btn btn-sm btn-primary" onclick="resolveOfficerDecision('${dec.id}')" style="white-space: nowrap;">
            <span data-icon="check-circle" data-size="14"></span>
            <span>${dec.actionLabel}</span>
          </button>
        ` : `
          <span class="badge-pill" style="background: var(--status-success-light); color: var(--status-success);">
            <span data-icon="check" data-size="13"></span>
            <span>आदेश जारी (Authorized)</span>
          </span>
        `}
      </div>
    </div>
  `).join("");

  if (typeof renderIcons === 'function') renderIcons();
}'''

# 5. Supercharged inspectMapPin
new_inspect_map_pin = '''function inspectMapPin(village, count, disease, clusterStatus) {
  const inspector = document.getElementById("mapPinInspector");
  const details = document.getElementById("mapPinDetails");
  if (!inspector || !details) return;

  inspector.style.display = "block";
  let statusBadge = clusterStatus === "SURGE_CLUSTER" ?
    '<span class="badge-pill" style="background:var(--urgency-critical-light); color:var(--urgency-critical);">SURGE CLUSTER (>3 केसेस)</span>' :
    (clusterStatus === "K_ANONYMIZED" ?
      '<span class="badge-pill" style="background:#ccfbf1; color:#0f766e;">k<3 ANONYMIZED CENTROID</span>' :
      '<span class="badge-pill" style="background:var(--accent-turmeric-light); color:#92400e;">BIOSECURITY CORDON</span>');

  details.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <div class="brand-emblem" style="color:var(--urgency-critical);"><span data-icon="map-pin" data-size="16"></span></div>
        <strong style="font-size:16px; color:var(--ink-primary);">${village}</strong>
      </div>
      ${statusBadge}
    </div>
    <div style="color:var(--ink-secondary); margin-top:6px; font-size:13px;">
      पडताळलेले रुग्ण: <strong style="color:var(--ink-primary);">${count}</strong> | संशयित आजार: <strong style="color:var(--urgency-critical);">${disease}</strong> | तालुका दवाखाना: <strong>साक्री / संगमनेर (Dr. R. Kute)</strong>
    </div>
    <div style="display:flex; gap:8px; margin-top:12px; flex-wrap:wrap;">
      <button type="button" class="btn btn-sm btn-primary" onclick="dispatchMvuToVillage('${village}', '${disease}')">
        <span data-icon="truck" data-size="14"></span>
        <span>१९६२ पथक रवाना</span>
      </button>
      <button type="button" class="btn btn-sm btn-outline" onclick="openVillageSmsBroadcastModal('${village}', '${disease}', 480)">
        <span data-icon="send" data-size="14"></span>
        <span>GP SMS सूचना</span>
      </button>
      <button type="button" class="btn btn-sm btn-danger" onclick="enforceRingQuarantine('${village}', '${disease}')">
        <span data-icon="shield-alert" data-size="14"></span>
        <span>५ किमी विलगीकरण</span>
      </button>
      <button type="button" class="btn btn-sm btn-outline" onclick="exportNadresBatch()">
        <span data-icon="download" data-size="14"></span>
        <span>NADRES V2 निर्यात</span>
      </button>
    </div>
  `;

  if (typeof renderIcons === 'function') renderIcons();
}'''

# Replace renderVillageSignalBoard
js = re.sub(r'function renderVillageSignalBoard\(\)\s*\{[\s\S]*?\n\}\n(?=function renderOfficerDecisionQueue)', new_village_signal_board + '\n\n', js)

# Replace renderOfficerDecisionQueue
js = re.sub(r'function renderOfficerDecisionQueue\(\)\s*\{[\s\S]*?\n\}\n(?=function resolveOfficerDecision)', new_officer_decision_queue + '\n\n', js)

# Replace inspectMapPin
js = re.sub(r'function inspectMapPin\([^\)]*\)\s*\{[\s\S]*?\n\}\n(?=// 6\. Digital Pashu Aadhar)', new_inspect_map_pin + '\n\n', js)

# Append modal_and_nav_code and operations_code if not present
if 'function closeAboutBlueprintModal' not in js:
    js += '\n\n' + modal_and_nav_code + '\n\n' + operations_code
    print("✓ Appended operational modals and navigation handlers to js/app.js")
else:
    print("Operational handlers already in js/app.js")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Saved updated js/app.js")

