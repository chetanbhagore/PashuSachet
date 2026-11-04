import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open("js/app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# 1. Add Navigation Controller & i18n & Modal helpers at top/suitable place
nav_controller_code = """
/* ==========================================================================
   APPLE APP SHELL NAVIGATION CONTROLLER & i18n
   ========================================================================== */
let currentView = 'viewFarmerHome';
let currentLang = 'mr';

const i18nDictionary = {
  mr: {
    brandAppTitle: "PashuSachet",
    brandAppSub: "महाराष्ट्र शासन पशुसंवर्धन",
    txtAboutBlueprint: "प्रणाली रूपरेषा (About Blueprint)",
    txtEmergencyHelp: "२४×७ फिरते पशुवैद्यकीय पथक",
    farmerGreetingTitle: "नमस्कार, एकनाथराव",
    farmerGreetingSub: "मौजे साक्री, जि. धुळे • शेतकरी खाते क्र. MH-DHU-8821 • ३ नोंदणीकृत जनावरे",
    txtHeroTriageTitle: "जनावराची तपासणी सुरू करा",
    txtHeroTriageDesc: "जनावराची लक्षणे सांगा आणि त्वरित ९० सेकंदात प्राथमिक सल्ला, प्रथमोपचार व शासकीय पशुवैद्यकीय साहाय्य मिळवा.",
    txtHeroTriageBtn: "लक्षणे तपासा (Start Triage)",
    titleGlanceCase: "गौरी (गाय) - लाळ्या खुरकूत संशयित",
    descGlanceCase: "पशु सखी पडताळणी प्रलंबित (अपेक्षित वेळ: २० मि.)",
    titleGlanceMilk: "लक्ष्मी (म्हैस) - अँटिबायोटिक विथड्रॉवल",
    descGlanceMilk: "ऑक्सिटेट्रासायक्लिन उपचार चालू, दूध डेअरीत घालणे निषिद्ध.",
    titleGlanceVax: "खुरकूत (FMD) बूस्टर मोहीम",
    descGlanceVax: "साक्री प्राथमिक पशुवैद्यकीय दवाखान्यातर्फे मोफत डोस.",
    titleMyHerdCarousel: "माझा गोठा (My Registered Herd)",
    linkViewAllAnimals: "सर्व जनावरे पहा →",
    titleEmergencyStrip: "तातडीची पशुवैद्यकीय मदत हवी आहे का?",
    descEmergencyStrip: "जनावराचा अचानक मृत्यू, तीव्र रक्तस्त्राव किंवा गंभीर आजार असल्यास २४×७ फिरते पशुवैद्यकीय पथक (MVU) विनामूल्य उपलब्ध आहे.",
    btnCall1962Strip: "1962 त्वरित डायल करा",
    triageFlowTitle: "लक्षण तपासणी (Health Check)",
    triageFlowSub: "९० सेकंदात अचूक प्राथमिक तपासणी, आजार शक्यता व योग्य शासकीय कृती.",
    txtStep1Title: "पायरी १: आजारी जनावर निवडा (Choose Animal)",
    txtStep2Title: "पायरी २: जनावरात दिसणारी लक्षणे (Select Symptoms)",
    txtStep2Desc: "जनावरात दिसणाऱ्या सर्व लक्षणांवर स्पर्श करा (एकापेक्षा जास्त निवडू शकता):",
    txtStep3Title: "पायरी ३: आजाराचा कालावधी व तापमान (Vitals & Details)",
    btnEvaluateText: "निकाल तपासा (Evaluate Now)",
    txtMyAnimalsTitle: "माझी जनावरे (Pashu Aadhar Herd)",
    txtMyAnimalsSub: "नोंदणीकृत जनावरांचे डिजिटल आरोग्य पासपोर्ट, लसीकरण व दूध सुरक्षा तपशील.",
    txtFarmerCasesTitle: "माझ्या केसेस व पाठपुरावा (Cases & Alerts)",
    txtFarmerCasesSub: "नोंदवलेल्या सर्व तक्रारींची सद्यस्थिती व पशु सखी/डॉक्टरांचा अभिप्राय.",
    txtParavetDeskTitle: "पशु सखी पडताळणी डेस्क (Verification Desk)",
    txtParavetDeskSub: "गावपातळीवरील शेतकऱ्यांच्या तक्रारींची ३० सेकंदांत पडताळणी व तातडीची कारवाई."
  },
  en: {
    brandAppTitle: "PashuSachet",
    brandAppSub: "Govt of Maharashtra Animal Husbandry",
    txtAboutBlueprint: "System Blueprint & Manifesto",
    txtEmergencyHelp: "24x7 Mobile Veterinary Unit (1962)",
    farmerGreetingTitle: "Namaskar, Eknathrao",
    farmerGreetingSub: "Sakri Village, Dhule Dist • Farmer ID MH-DHU-8821 • 3 Registered Animals",
    txtHeroTriageTitle: "Start Livestock Health Check",
    txtHeroTriageDesc: "Report observed symptoms in under 90 seconds for instant AI triage, first-aid, and doorstep veterinary assistance.",
    txtHeroTriageBtn: "Start Triage (लक्षणे तपासा)",
    titleGlanceCase: "Gauri (Cow) - FMD Suspected",
    descGlanceCase: "Pashu Sakhi verification pending (ETA: 20 mins)",
    titleGlanceMilk: "Lakshmi (Buffalo) - Antibiotic Withdrawal",
    descGlanceMilk: "Oxytetracycline active. Milk supply withholding mandatory.",
    titleGlanceVax: "Foot & Mouth (FMD) Booster Due",
    descGlanceVax: "Free doorstep ring vaccination drive starting 28-Oct.",
    titleMyHerdCarousel: "My Herd (माझा गोठा)",
    linkViewAllAnimals: "View All Herd →",
    titleEmergencyStrip: "Need Urgent Veterinary Assistance?",
    descEmergencyStrip: "In case of sudden mortality, hemorrhage, or acute distress, 24x7 Mobile Veterinary Units (MVU) arrive within 18 minutes.",
    btnCall1962Strip: "Call 1962 Now (तातडीने डायल करा)",
    triageFlowTitle: "Symptom Health Check (लक्षण तपासणी)",
    triageFlowSub: "Accurate clinical triage, probable pathogen assessment, and doorstep escalation.",
    txtStep1Title: "Step 1: Choose Animal (जनावर निवडा)",
    txtStep2Title: "Step 2: Observed Symptoms (मुख्य लक्षणे)",
    txtStep2Desc: "Tap all symptoms observed on the animal (multi-select):",
    txtStep3Title: "Step 3: Vitals & Duration (तपशील व तापमान)",
    btnEvaluateText: "Evaluate Now (निकाल तपासा)",
    txtMyAnimalsTitle: "My Herd (Pashu Aadhar Herd)",
    txtMyAnimalsSub: "Digital health passports, immunization records, and food safety timers.",
    txtFarmerCasesTitle: "My Cases & Alerts (केसेस व ट्रॅकर)",
    txtFarmerCasesSub: "Live status updates from field verification to laboratory results.",
    txtParavetDeskTitle: "Para-Vet Verification Desk (पडताळणी डेस्क)",
    txtParavetDeskSub: "Rapid 30-second field verification for village micro-reports."
  }
};

function switchAppView(viewId) {
  currentView = viewId;
  if (typeof document === 'undefined') return;
  document.querySelectorAll('.app-view').forEach(v => v.classList.remove('active'));
  const target = document.getElementById(viewId);
  if (target) {
    target.classList.add('active');
  }
  const viewport = document.getElementById('appViewport');
  if (viewport) viewport.scrollTop = 0;

  document.querySelectorAll('.app-nav-item').forEach(el => {
    if (el.getAttribute('data-view') === viewId) el.classList.add('active');
    else el.classList.remove('active');
  });

  document.querySelectorAll('.bottom-tab-item').forEach(el => {
    if (el.getAttribute('data-view') === viewId) el.classList.add('active');
    else el.classList.remove('active');
  });
}

function renderAppNavigation() {
  if (typeof document === 'undefined') return;
  const sidebarNavGroup = document.getElementById('sidebarNavGroup');
  const bottomNav = document.getElementById('appBottomNav');
  if (!sidebarNavGroup || !bottomNav) return;

  let items = [];
  if (currentPersona === 'farmer') {
    items = [
      { id: 'viewFarmerHome', icon: 'home', labelMr: 'आजची काळजी', labelEn: "Today's Care", badge: '' },
      { id: 'viewSymptomTriage', icon: 'stethoscope', labelMr: 'लक्षण तपासणी', labelEn: 'Health Check', badge: '' },
      { id: 'viewMyAnimals', icon: 'tag', labelMr: 'माझी जनावरे', labelEn: 'My Herd', badge: '3' },
      { id: 'viewFarmerCases', icon: 'clipboard-list', labelMr: 'केसेस व ट्रॅकर', labelEn: 'Cases & Alerts', badge: '1' }
    ];
  } else if (currentPersona === 'paravet') {
    items = [
      { id: 'viewParavetDesk', icon: 'clipboard-check', labelMr: 'पडताळणी रांग', labelEn: 'Verification', badge: '3' },
      { id: 'viewParavetMap', icon: 'map', labelMr: 'माझे गाव नकाशा', labelEn: 'Beat Map', badge: '' },
      { id: 'viewRddlTracker', icon: 'flask', labelMr: 'नमुने व किट', labelEn: 'Sample Kits', badge: '2' },
      { id: 'viewFarmerHome', icon: 'user', labelMr: 'शेतकरी नोंदणी', labelEn: 'Farmer View', badge: '' }
    ];
  } else if (currentPersona === 'ldo') {
    items = [
      { id: 'viewLdoDesk', icon: 'activity', labelMr: 'रुग्ण डेस्क', labelEn: 'Care Desk', badge: '5' },
      { id: 'viewLdoRx', icon: 'pill', labelMr: 'प्रिस्क्रिप्शन', labelEn: 'Rx & Milk Safety', badge: '' },
      { id: 'viewRddlTracker', icon: 'flask', labelMr: 'लॅब अहवाल', labelEn: 'Lab Reports', badge: '' }
    ];
  } else if (currentPersona === 'collector') {
    items = [
      { id: 'viewCollectorBoard', icon: 'building-2', labelMr: 'गाव सिग्नल बोर्ड', labelEn: 'Signal Board', badge: '3' },
      { id: 'viewCollectorSeir', icon: 'activity', labelMr: 'साथरोग अंदाज', labelEn: 'Outbreak GIS', badge: '' },
      { id: 'viewParavetDesk', icon: 'clipboard-check', labelMr: 'पडताळणी निरीक्षण', labelEn: 'Field Audit', badge: '' }
    ];
  } else if (currentPersona === 'rddl') {
    items = [
      { id: 'viewRddlTracker', icon: 'flask', labelMr: 'नमुना पाइपलाइन', labelEn: 'Sample Tracker', badge: '4' },
      { id: 'viewRddlNadres', icon: 'download', labelMr: 'NADRES V2 डेटा', labelEn: 'NADRES Export', badge: '' }
    ];
  }

  // Sidebar HTML
  let sidebarHtml = `<div class="sidebar-nav-heading">मुख्य पर्याय (Navigation)</div>`;
  items.forEach((item, idx) => {
    const isAct = (currentView === item.id || (!currentView && idx === 0)) ? 'active' : '';
    const label = currentLang === 'en' ? item.labelEn : item.labelMr;
    sidebarHtml += `
      <button type="button" class="app-nav-item ${isAct}" data-view="${item.id}" onclick="switchAppView('${item.id}')">
        <span class="nav-icon-wrap" data-icon="${item.icon}"></span>
        <span>${label}</span>
        ${item.badge ? `<span class="nav-badge-pill">${item.badge}</span>` : ''}
      </button>
    `;
  });
  sidebarNavGroup.innerHTML = sidebarHtml;

  // Mobile Bottom Nav HTML
  let bottomHtml = '';
  items.forEach((item, idx) => {
    const isAct = (currentView === item.id || (!currentView && idx === 0)) ? 'active' : '';
    const label = currentLang === 'en' ? item.labelEn : item.labelMr;
    bottomHtml += `
      <button type="button" class="bottom-tab-item ${isAct}" data-view="${item.id}" onclick="switchAppView('${item.id}')">
        <span data-icon="${item.icon}" data-size="20"></span>
        <span class="bottom-tab-label">${label}</span>
        <span class="tab-dot-indicator"></span>
      </button>
    `;
  });
  bottomNav.innerHTML = bottomHtml;

  if (typeof renderIcons === 'function') renderIcons();
}

function startGuidedTriage() {
  switchAppView('viewSymptomTriage');
  if (typeof document !== 'undefined') {
    const box = document.getElementById('triageStep1Box');
    if (box && typeof box.scrollIntoView === 'function') box.scrollIntoView({ behavior: 'smooth' });
  }
}

function prefillTriageForAnimal(tag, sp) {
  if (typeof document !== 'undefined') {
    const tagInput = document.getElementById('pashuTag');
    if (tagInput) tagInput.value = tag;
  }
  syncSpecies(sp);
  startGuidedTriage();
}

function setQuickTemp(temp, btn) {
  if (typeof document !== 'undefined') {
    const tempInput = document.getElementById('tempInput');
    if (tempInput) tempInput.value = temp;
    document.querySelectorAll('.vitals-choice-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
  }
}

function openRoleSwitcher() {
  if (typeof document === 'undefined') return;
  const modal = document.getElementById('roleSwitcherModal');
  if (modal) modal.classList.add('active');
}

function closeRoleSwitcher() {
  if (typeof document === 'undefined') return;
  const modal = document.getElementById('roleSwitcherModal');
  if (modal) modal.classList.remove('active');
}

function selectPersona(role) {
  closeRoleSwitcher();
  activatePersona(role);
}

function openAboutBlueprintModal() {
  if (typeof document === 'undefined') return;
  const modal = document.getElementById('aboutBlueprintModal');
  if (modal) modal.classList.add('active');
}

function closeAboutBlueprintModal() {
  if (typeof document === 'undefined') return;
  const modal = document.getElementById('aboutBlueprintModal');
  if (modal) modal.classList.remove('active');
}

function openAddAnimalModal() {
  if (typeof document === 'undefined') return;
  const modal = document.getElementById('addAnimalModal');
  if (modal) modal.classList.add('active');
}

function closeAddAnimalModal() {
  if (typeof document === 'undefined') return;
  const modal = document.getElementById('addAnimalModal');
  if (modal) modal.classList.remove('active');
}

function openNdlmLookupDialog() {
  switchAppView('viewMyAnimals');
  if (typeof document !== 'undefined') {
    const input = document.getElementById('ndlmTagInput');
    if (input && typeof input.focus === 'function') input.focus();
  }
}

function switchVetTab(tab) {
  if (typeof document === 'undefined') return;
  const tabApts = document.getElementById('tabAptsBtn');
  const tabRefs = document.getElementById('tabReferralsBtn');
  const aptsCont = document.getElementById('vetAppointmentsContainer');
  const casesCont = document.getElementById('vetCasesContainer');
  if (tab === 'apts') {
    if (tabApts) tabApts.classList.add('active');
    if (tabRefs) tabRefs.classList.remove('active');
    if (aptsCont) aptsCont.style.display = 'block';
    if (casesCont) casesCont.style.display = 'none';
  } else {
    if (tabApts) tabApts.classList.remove('active');
    if (tabRefs) tabRefs.classList.add('active');
    if (aptsCont) aptsCont.style.display = 'none';
    if (casesCont) casesCont.style.display = 'block';
  }
}

function toggleLanguage() {
  currentLang = currentLang === 'mr' ? 'en' : 'mr';
  if (typeof document !== 'undefined') {
    const langCurrentText = document.getElementById('langCurrentText');
    if (langCurrentText) {
      langCurrentText.textContent = currentLang === 'mr' ? 'EN' : 'मराठी';
    }

    const dict = i18nDictionary[currentLang];
    if (dict) {
      Object.keys(dict).forEach(key => {
        const el = document.getElementById(key);
        if (el) el.textContent = dict[key];
      });
    }
  }

  renderAppNavigation();
  showToast(currentLang === 'mr' ? 'मराठी भाषा सक्रिय केली.' : 'Switched language to English.');
}
"""

# Replace activatePersona with comprehensive Apple App Shell role orchestrator
new_activate_persona = """
function activatePersona(role) {
  currentPersona = role;
  
  if (typeof document !== 'undefined') {
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

    const roleTextEl = document.getElementById('appRoleText');
    const beatTextEl = document.getElementById('appBeatText');
    const avatarInitialsEl = document.getElementById('userAvatarText');
    const nameHeaderEl = document.getElementById('userNameHeader');

    if (role === 'farmer') {
      if (roleTextEl) roleTextEl.textContent = 'शेतकरी (Farmer)';
      if (beatTextEl) beatTextEl.textContent = 'साक्री, धुळे';
      if (avatarInitialsEl) avatarInitialsEl.textContent = 'EB';
      if (nameHeaderEl) nameHeaderEl.textContent = 'एकनाथराव';
      quickLogin('farmer');
      renderAnimals();
      switchAppView('viewFarmerHome');
      showToast('🧑‍🌾 शेतकरी मोड सक्रिय: आजची काळजी व पशू आधार उपलब्ध.');
    } else if (role === 'paravet') {
      if (roleTextEl) roleTextEl.textContent = 'पशु सखी (Para-Vet)';
      if (beatTextEl) beatTextEl.textContent = 'साक्री बीट (५ गावे)';
      if (avatarInitialsEl) avatarInitialsEl.textContent = 'SP';
      if (nameHeaderEl) nameHeaderEl.textContent = 'सुनिता पाटील';
      quickLogin('paravet');
      if (paravetNav) paravetNav.style.display = 'inline-block';
      renderParavetInbox();
      switchAppView('viewParavetDesk');
      showToast('🩺 पशु सखी / पॅरा-व्हेट मोड: <30 सेकंद पडताळणी रांग सक्रिय.');
    } else if (role === 'ldo') {
      if (roleTextEl) roleTextEl.textContent = 'पशुवैद्यकीय अधिकारी (LDO Doctor)';
      if (beatTextEl) beatTextEl.textContent = 'साक्री दवाखाना';
      if (avatarInitialsEl) avatarInitialsEl.textContent = 'RK';
      if (nameHeaderEl) nameHeaderEl.textContent = 'डॉ. रामेश्वर कुटे';
      quickLogin('vet');
      if (paravetNav) paravetNav.style.display = 'inline-block';
      renderVetDesk();
      switchAppView('viewLdoDesk');
      showToast('👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO) मोड: क्लिनिकल तपासणी व प्रिस्क्रिप्शन.');
    } else if (role === 'collector') {
      if (roleTextEl) roleTextEl.textContent = 'जिल्हाधिकारी (Collector)';
      if (beatTextEl) beatTextEl.textContent = 'धुळे जिल्हा';
      if (avatarInitialsEl) avatarInitialsEl.textContent = 'AG';
      if (nameHeaderEl) nameHeaderEl.textContent = 'अभिनव गोयल, IAS';
      quickLogin('officer');
      if (adminNav) adminNav.style.display = 'inline-block';
      renderVillageSignalBoard();
      renderOfficerDecisionQueue();
      switchAppView('viewCollectorBoard');
      showToast('🏛️ जिल्हा नियंत्रण कक्ष: गाव सिग्नल बोर्ड व सकाळची निर्णय रांग.');
      if (typeof ringVaxActive !== 'undefined' && !ringVaxActive && typeof toggleRingVaxRadius === 'function') toggleRingVaxRadius();
    } else if (role === 'rddl') {
      if (roleTextEl) roleTextEl.textContent = 'विभागीय प्रयोगशाळा (RDDL Lab)';
      if (beatTextEl) beatTextEl.textContent = 'पुणे विभाग';
      if (avatarInitialsEl) avatarInitialsEl.textContent = 'VD';
      if (nameHeaderEl) nameHeaderEl.textContent = 'डॉ. व्ही. देशपांडे';
      quickLogin('admin');
      if (adminNav) adminNav.style.display = 'inline-block';
      renderSampleTracker();
      switchAppView('viewRddlTracker');
      showToast('🔬 राज्य रोग निदान प्रयोगशाळा: नमुना पाइपलाइन व NADRES V2 डेटा.');
    }

    renderAppNavigation();
  }
}
"""

# Replace activatePersona in app_js
app_js = re.sub(r'function activatePersona\(role\)[\s\S]*?(?=\n\/\/ 2\. Multi-Disease Computer Vision)', new_activate_persona + '\n', app_js)

# Add nav_controller_code before activatePersona if not present
if "function renderAppNavigation()" not in app_js:
    app_js = nav_controller_code + "\n" + app_js

# Update toggleSymptomVal to sync cards and emergency interrupts
new_toggle_symptom = """
function toggleSymptomVal(sym) {
  if (typeof document !== 'undefined') {
    const cardMap = {
      'fever': 'cardSymFever',
      'mouth_lesions': 'cardSymMouth',
      'skin_nodules': 'cardSymNodules',
      'udder_swelling': 'cardSymUdder',
      'lameness': 'cardSymLameness',
      'loss_of_appetite': 'cardSymAppetite',
      'sudden_death': 'cardSymMortality'
    };

    const cardId = cardMap[sym];
    if (cardId) {
      const cardEl = document.getElementById(cardId);
      if (cardEl) cardEl.classList.toggle('selected');
    }

    const container = document.getElementById('symptomTagsContainer');
    if (container) {
      let cb = container.querySelector(`input[value="${sym}"]`);
      if (!cb) {
        cb = document.createElement('input');
        cb.type = 'checkbox';
        cb.value = sym;
        cb.id = `cb_${sym}`;
        container.appendChild(cb);
      }
      cb.checked = !cb.checked;
    }

    if (sym === 'sudden_death') {
      const cardEl = document.getElementById('cardSymMortality');
      if (cardEl && cardEl.classList.contains('selected')) {
        toggleMortalityFields(true);
        openEmergencyModal();
        showToast('⚠️ आणीबाणी: अचानक मृत्यू नोंदवल्यामुळे १९६२ पथकाला थेट कॉल अलर्ट.');
      }
    }
  }

  evaluateSymptoms();
}
"""

app_js = re.sub(r'function toggleSymptomVal\(sym\)[\s\S]*?(?=\nfunction |\Z)', new_toggle_symptom + '\n', app_js, count=1)

# Ensure DOMContentLoaded initializes renderAppNavigation and renderIcons
if "renderAppNavigation();" not in app_js:
    app_js = app_js.replace(
        "renderAnimals();",
        "renderAppNavigation();\n  renderIcons();\n  renderAnimals();"
    )

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(app_js)

print("Updated js/app.js with Apple App Shell navigation, i18n, and reactive controllers.")
