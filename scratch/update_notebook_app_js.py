import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update toggleSymptomVal
old_toggle_symptom = """function toggleSymptomVal(val) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb) {
    cb.checked = !cb.checked;
    if (typeof Event !== 'undefined') {
      try { cb.dispatchEvent(new Event("change")); } catch(e) {}
    }
  }
}"""

new_toggle_symptom = """const symptomCardMap = {
  fever: 'cardSymFever',
  mouth_lesions: 'cardSymMouth',
  skin_nodules: 'cardSymNodules',
  udder_swelling: 'cardSymUdder',
  lameness: 'cardSymLameness',
  loss_of_appetite: 'cardSymAppetite',
  sudden_death: 'cardSymMortality'
};

function toggleSymptomVal(val) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb) {
    cb.checked = !cb.checked;
    if (typeof Event !== 'undefined') {
      try { cb.dispatchEvent(new Event("change")); } catch(e) {}
    }
  }

  // Visual card selection update
  const cardId = symptomCardMap[val];
  if (cardId) {
    const card = document.getElementById(cardId);
    if (card) {
      if (cb && cb.checked) {
        card.classList.add('selected');
      } else {
        card.classList.remove('selected');
      }
    }
  }

  // Emergency Red Flag circuit breaker on sudden mortality
  if (val === 'sudden_death' && cb && cb.checked) {
    if (typeof openEmergencyModal === 'function') {
      openEmergencyModal();
      showToast('⚠️ तातडीचा धोका: जनावराचा अचानक मृत्यू झाल्यास तात्काळ १९६२ फिरते पथक बोलवा.');
    }
  }
}"""

if old_toggle_symptom in code:
    code = code.replace(old_toggle_symptom, new_toggle_symptom)
    print("✓ Replaced toggleSymptomVal")
else:
    print("Warning: old_toggle_symptom exact pattern not matched")

# 2. Update evaluateSymptoms to call goToTriageStep(4)
old_eval_end = """  resultContainer.classList.add("active");
  resultContainer.scrollIntoView({ behavior: "smooth", block: "start" });
  showToast("AI Assessment generated successfully");
}"""

new_eval_end = """  resultContainer.classList.add("active");
  if (typeof goToTriageStep === 'function') {
    goToTriageStep(4);
  } else {
    resultContainer.scrollIntoView({ behavior: "smooth", block: "start" });
  }
  showToast("AI Assessment generated successfully");
}"""

if old_eval_end in code:
    code = code.replace(old_eval_end, new_eval_end)
    print("✓ Replaced evaluateSymptoms end to call goToTriageStep(4)")
else:
    print("Warning: old_eval_end exact pattern not matched")

# 3. Add Notebook Navigation & Stepper helpers before activatePersona
notebook_nav_helpers = """
// ==========================================================================
// VILLAGE NOTEBOOK WORKSPACE ROUTER & NAVIGATION ENGINE
// ==========================================================================

function openRoleSwitcher() {
  const modal = document.getElementById("roleSwitcherModal");
  if (modal) modal.classList.add("active");
}

function closeRoleSwitcher() {
  const modal = document.getElementById("roleSwitcherModal");
  if (modal) modal.classList.remove("active");
}

function selectPersona(role) {
  activatePersona(role);
  closeRoleSwitcher();
}

function renderRoleSubnav(role) {
  const nav = document.getElementById('roleSubnavBar');
  if (!nav) return;

  const isMr = (typeof currentLang === 'undefined' || currentLang === 'mr');

  const tabsByRole = {
    farmer: [
      { id: 'viewFarmerHome', labelMr: 'आजची काळजी', labelEn: 'Home', icon: 'home' },
      { id: 'viewFarmerTriage', labelMr: 'तपासणी सुरू करा', labelEn: 'Report Problem', icon: 'stethoscope' },
      { id: 'viewFarmerAnimals', labelMr: 'माझी जनावरे', labelEn: 'My Animals', icon: 'tag' },
      { id: 'viewFarmerCases', labelMr: 'आरोग्य नोंदी', labelEn: 'Health Records', icon: 'file-text' },
      { id: 'viewFarmerHelp', labelMr: 'मदत व दवाखाना', labelEn: 'Help & Vet', icon: 'phone-call' }
    ],
    paravet: [
      { id: 'paravet-inbox', labelMr: 'पडताळणी रांग', labelEn: 'Verification Desk', icon: 'clipboard-check' },
      { id: 'paravet-visits', labelMr: 'क्षेत्रीय भेटी', labelEn: 'Village Visits', icon: 'map-pin' },
      { id: 'paravet-samples', labelMr: 'नमुना किट्स', labelEn: 'Sample Kits', icon: 'flask' }
    ],
    ldo: [
      { id: 'vet-desk', labelMr: 'क्लिनिकल कक्ष', labelEn: 'Clinical Desk', icon: 'stethoscope' },
      { id: 'vet-cases', labelMr: 'रुग्ण नोंदी', labelEn: 'Animal Records', icon: 'file-text' },
      { id: 'vet-milk', labelMr: 'दूध विथड्रॉवल', labelEn: 'Milk Withdrawal', icon: 'milk' }
    ],
    vet: [
      { id: 'vet-desk', labelMr: 'क्लिनिकल कक्ष', labelEn: 'Clinical Desk', icon: 'stethoscope' },
      { id: 'vet-cases', labelMr: 'रुग्ण नोंदी', labelEn: 'Animal Records', icon: 'file-text' },
      { id: 'vet-milk', labelMr: 'दूध विथड्रॉवल', labelEn: 'Milk Withdrawal', icon: 'milk' }
    ],
    collector: [
      { id: 'outbreak-gis', labelMr: 'GIS प्रादुर्भाव नकाशा', labelEn: 'Outbreak GIS', icon: 'map-pin' },
      { id: 'village-signals', labelMr: 'गाव सिग्नल बोर्ड', labelEn: 'Signal Board', icon: 'activity' },
      { id: 'officer-decisions', labelMr: 'सकाळची निर्णय रांग', labelEn: 'Decisions Queue', icon: 'shield' },
      { id: 'seir-epidemic', labelMr: 'SEIR साथीचा अंदाज', labelEn: 'SEIR Projections', icon: 'sliders' }
    ],
    officer: [
      { id: 'outbreak-gis', labelMr: 'GIS प्रादुर्भाव नकाशा', labelEn: 'Outbreak GIS', icon: 'map-pin' },
      { id: 'village-signals', labelMr: 'गाव सिग्नल बोर्ड', labelEn: 'Signal Board', icon: 'activity' },
      { id: 'officer-decisions', labelMr: 'सकाळची निर्णय रांग', labelEn: 'Decisions Queue', icon: 'shield' },
      { id: 'seir-epidemic', labelMr: 'SEIR साथीचा अंदाज', labelEn: 'SEIR Projections', icon: 'sliders' }
    ],
    rddl: [
      { id: 'sample-tracker', labelMr: 'नमुना पाइपलाइन', labelEn: 'Sample Pipeline', icon: 'flask' },
      { id: 'rddl-pcr', labelMr: 'RT-PCR चाचणी', labelEn: 'PCR Results', icon: 'clipboard-check' },
      { id: 'rddl-nadres', labelMr: 'NADRES V2 निर्यात', labelEn: 'NADRES Export', icon: 'download' }
    ],
    admin: [
      { id: 'sample-tracker', labelMr: 'नमुना पाइपलाइन', labelEn: 'Sample Pipeline', icon: 'flask' },
      { id: 'rddl-pcr', labelMr: 'RT-PCR चाचणी', labelEn: 'PCR Results', icon: 'clipboard-check' },
      { id: 'rddl-nadres', labelMr: 'NADRES V2 निर्यात', labelEn: 'NADRES Export', icon: 'download' }
    ]
  };

  const tabs = tabsByRole[role] || tabsByRole.farmer;

  nav.innerHTML = tabs.map((t, idx) => `
    <button class="role-subnav-btn ${idx === 0 ? 'active' : ''}" data-target="${t.id}" onclick="switchNotebookTab('${t.id}', this)">
      <span data-icon="${t.icon}" data-size="16"></span>
      <span>${isMr ? t.labelMr : t.labelEn}</span>
    </button>
  `).join('');

  if (typeof renderIcons === 'function') {
    renderIcons();
  }
}

function normalizeNotebookTab(tabId) {
  const map = {
    'farmerHome': 'viewFarmerHome',
    'farmerTriage': 'viewFarmerTriage',
    'farmerAnimals': 'viewFarmerAnimals',
    'farmerCases': 'viewFarmerCases',
    'farmerHelp': 'viewFarmerHelp'
  };
  return map[tabId] || tabId;
}

function switchNotebookTab(targetId, btnEl) {
  const resolvedId = normalizeNotebookTab(targetId);

  // Update button active state
  if (btnEl) {
    document.querySelectorAll('.role-subnav-btn').forEach(b => b.classList.remove('active'));
    btnEl.classList.add('active');
  } else {
    const matchingBtn = document.querySelector(`.role-subnav-btn[data-target="${targetId}"]`) ||
                        document.querySelector(`.role-subnav-btn[data-target="${resolvedId}"]`);
    if (matchingBtn) {
      document.querySelectorAll('.role-subnav-btn').forEach(b => b.classList.remove('active'));
      matchingBtn.classList.add('active');
    }
  }

  // If farmer view tabs:
  if (resolvedId.startsWith('viewFarmer')) {
    if (resolvedId === 'viewFarmerTriage') {
      const step1 = document.getElementById('triageStep1Box');
      const step2 = document.getElementById('triageStep2Box');
      const step3 = document.getElementById('triageStep3Box');
      if (step1 && step1.style.display === 'none' && (!step2 || step2.style.display === 'none') && (!step3 || step3.style.display === 'none')) {
        goToTriageStep(1);
      }
    }

    document.querySelectorAll('#workspaceFarmer .notebook-tab-view').forEach(tab => {
      tab.classList.remove('active');
    });
    const target = document.getElementById(resolvedId);
    if (target) {
      target.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    return;
  }

  // If section in other workspaces:
  const el = document.getElementById(resolvedId);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function goToTriageStep(stepNum) {
  const step1 = document.getElementById('triageStep1Box');
  const step2 = document.getElementById('triageStep2Box');
  const step3 = document.getElementById('triageStep3Box');
  const step4 = document.getElementById('assessmentResult');

  if (step1) step1.style.display = 'none';
  if (step2) step2.style.display = 'none';
  if (step3) step3.style.display = 'none';
  if (step4) step4.style.display = 'none';

  if (stepNum === 1) {
    if (step1) step1.style.display = 'block';
  } else if (stepNum === 2) {
    if (step2) step2.style.display = 'block';
  } else if (stepNum === 3) {
    if (step3) step3.style.display = 'block';
  } else if (stepNum === 4) {
    if (step3) step3.style.display = 'block';
    if (step4) {
      step4.style.display = 'block';
      step4.classList.add('active');
      step4.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  for (let i = 1; i <= 4; i++) {
    const pill = document.getElementById(`stepPill${i}`);
    if (pill) {
      pill.classList.remove('active', 'completed');
      if (i < stepNum) {
        pill.classList.add('completed');
      } else if (i === stepNum) {
        pill.classList.add('active');
      }
    }
  }
}

function setQuickTemp(val, btn) {
  const tempInput = document.getElementById('tempInput');
  if (tempInput) tempInput.value = val;
  if (btn && btn.parentElement) {
    btn.parentElement.querySelectorAll('.vitals-pill-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }
}

function prefillTriageForAnimal(tag, species) {
  const tagInput = document.getElementById('pashuTag');
  if (tagInput) tagInput.value = tag;
  const specEl = document.getElementById('species');
  if (specEl) {
    specEl.value = species;
    syncSpecies(species);
  }
  switchNotebookTab('viewFarmerTriage');
  goToTriageStep(2);
}

function toggleLanguage() {
  const nextLang = (currentLang === 'mr') ? 'en' : 'mr';
  setLanguage(nextLang);
  const langTextEl = document.getElementById('langCurrentText');
  if (langTextEl) {
    langTextEl.textContent = (nextLang === 'mr') ? 'EN' : 'मराठी';
  }
  if (typeof currentPersona !== 'undefined') {
    renderRoleSubnav(currentPersona);
  }
}

function resetSymptomChecker() {
  const form = document.getElementById('symptomForm');
  if (form) form.reset();
  document.querySelectorAll('.symptom-select-card').forEach(c => c.classList.remove('selected'));
  const res = document.getElementById('assessmentResult');
  if (res) {
    res.style.display = 'none';
    res.classList.remove('active');
  }
  goToTriageStep(1);
}
"""

# Replace activatePersona with upgraded role-isolated version
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
    quickLogin('admin');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderSampleTracker();
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड: RT-PCR चाचणी व नमुना ट्रॅकिंग.');
    const el = document.getElementById('sample-tracker');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }
}"""

new_activate_persona = notebook_nav_helpers + """
function activatePersona(role) {
  currentPersona = role;

  const pills = ['personaFarmer', 'personaParavet', 'personaLdo', 'personaCollector', 'personaRddl'];
  pills.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });

  const activePill = document.getElementById(
    role === 'farmer' ? 'personaFarmer' :
    role === 'paravet' ? 'personaParavet' :
    (role === 'ldo' || role === 'vet') ? 'personaLdo' :
    (role === 'collector' || role === 'officer') ? 'personaCollector' : 'personaRddl'
  );
  if (activePill) activePill.classList.add('active');

  // Toggle role workspaces cleanly
  const workspaces = {
    'farmer': 'workspaceFarmer',
    'paravet': 'workspaceParavet',
    'ldo': 'workspaceVet',
    'vet': 'workspaceVet',
    'collector': 'workspaceOfficer',
    'officer': 'workspaceOfficer',
    'rddl': 'workspaceRddl',
    'admin': 'workspaceRddl'
  };

  const targetWsId = workspaces[role] || 'workspaceFarmer';
  document.querySelectorAll('.role-workspace-view').forEach(ws => {
    ws.classList.remove('active');
  });
  const targetWs = document.getElementById(targetWsId);
  if (targetWs) targetWs.classList.add('active');

  // Update Topbar metadata
  const roleTextEl = document.getElementById('appRoleText');
  const beatTextEl = document.getElementById('appBeatText');
  const userHeaderEl = document.getElementById('userNameHeader');
  const avatarEl = document.getElementById('userAvatarText');

  const meta = {
    farmer: { role: 'शेतकरी (Farmer)', beat: 'साक्री, धुळे', user: 'एकनाथराव', avatar: 'EB' },
    paravet: { role: 'पशु सखी (Para-Vet)', beat: 'बीट: साक्री व ५ गावे', user: 'सुनिता पाटील', avatar: 'SP' },
    ldo: { role: 'पशुवैद्यकीय अधिकारी (LDO)', beat: 'तालुका दवाखाना, साक्री', user: 'डॉ. कुटे', avatar: 'RK' },
    vet: { role: 'पशुवैद्यकीय अधिकारी (LDO)', beat: 'तालुका दवाखाना, साक्री', user: 'डॉ. कुटे', avatar: 'RK' },
    collector: { role: 'जिल्हा नियंत्रण कक्ष (DVO)', beat: 'धुळे जिल्हा मुख्यालय', user: 'कलेक्टर कार्यालय', avatar: 'DC' },
    officer: { role: 'जिल्हा नियंत्रण कक्ष (DVO)', beat: 'धुळे जिल्हा मुख्यालय', user: 'कलेक्टर कार्यालय', avatar: 'DC' },
    rddl: { role: 'विभागीय प्रयोगशाळा (RDDL)', beat: 'पुणे मध्यवर्ती प्रयोगशाळा', user: 'आर.डी.डी.एल.', avatar: 'RD' },
    admin: { role: 'विभागीय प्रयोगशाळा (RDDL)', beat: 'पुणे मध्यवर्ती प्रयोगशाळा', user: 'आर.डी.डी.एल.', avatar: 'RD' }
  }[role] || { role: 'शेतकरी (Farmer)', beat: 'साक्री, धुळे', user: 'एकनाथराव', avatar: 'EB' };

  if (roleTextEl) roleTextEl.textContent = meta.role;
  if (beatTextEl) beatTextEl.textContent = meta.beat;
  if (userHeaderEl) userHeaderEl.textContent = meta.user;
  if (avatarEl) avatarEl.textContent = meta.avatar;

  // Render Subnav Tabs
  renderRoleSubnav(role);

  // Role action dispatches
  const paravetNav = document.getElementById('paravetNavLink');
  const adminNav = document.getElementById('adminNavLink');

  if (role === 'farmer') {
    quickLogin('farmer');
    renderAnimals();
    switchNotebookTab('viewFarmerHome');
    showToast('शेतकरी नोंदवही सक्रिय: जलद तपासणी व पशू आधार.');
    const el = document.getElementById('symptom-screening');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'paravet') {
    quickLogin('paravet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderParavetInbox();
    showToast('पशु सखी / पॅरा-व्हेट डेस्क: पडताळणी रांग सक्रिय.');
    const el = document.getElementById('paravet-inbox');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'ldo' || role === 'vet') {
    quickLogin('vet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderVetDesk();
    showToast('पशुवैद्यकीय अधिकारी (LDO) क्लिनिकल कक्ष सक्रिय.');
    const el = document.getElementById('vet-desk');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'collector' || role === 'officer') {
    quickLogin('officer');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderVillageSignalBoard();
    renderOfficerDecisionQueue();
    showToast('जिल्हा नियंत्रण कक्ष मोड सक्रिय.');
    if (typeof ringVaxActive !== 'undefined' && !ringVaxActive) toggleRingVaxRadius();
    const el = document.getElementById('outbreak-gis');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'rddl' || role === 'admin') {
    quickLogin('admin');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderSampleTracker();
    showToast('राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड सक्रिय.');
    const el = document.getElementById('sample-tracker');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }
}"""

if old_activate_persona in code:
    code = code.replace(old_activate_persona, new_activate_persona)
    print("✓ Replaced activatePersona")
else:
    print("Warning: old_activate_persona exact pattern not matched")

# 4. Update DOMContentLoaded handler to initialize icons, persona, and stepper
old_dom_load = """document.addEventListener("DOMContentLoaded", () => {
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

  // Village Notebook enhancements
  if (typeof renderIcons === 'function') renderIcons();
  activatePersona('farmer');
  goToTriageStep(1);

  // Bind Stepper pill clicks
  for (let i = 1; i <= 4; i++) {
    const pill = document.getElementById(`stepPill${i}`);
    if (pill) {
      pill.style.cursor = 'pointer';
      pill.addEventListener('click', () => goToTriageStep(i));
    }
  }
});"""

if old_dom_load in code:
    code = code.replace(old_dom_load, new_dom_load)
    print("✓ Replaced DOMContentLoaded")
else:
    print("Warning: old_dom_load exact pattern not matched")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated js/app.js")
