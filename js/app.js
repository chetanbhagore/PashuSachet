
// ========================================================
// AUTHENTICATION & MULTI-ROLE SESSION STATE
// ========================================================

const AUTH_PROFILES = {
  farmer: {
    role: "farmer",
    name: "Ganesh Patil",
    title: "Livestock Keeper",
    location: "Sangamner, Ahmednagar",
    identifier: "+91 98220 12345",
    avatar: "👨‍🌾"
  },
  paravet: {
    role: "paravet",
    name: "Ganesh Kale",
    title: "Village Sentinel & Para-Vet",
    location: "Sangamner Cluster (Villages 1-4)",
    identifier: "PV-AHM-9104",
    avatar: "🧑‍⚕️"
  },
  vet: {
    role: "vet",
    name: "Dr. Rameshwar Kute",
    title: "LDO Grade-I (Sangamner)",
    location: "Ahmednagar District",
    identifier: "MSVC/2012/03194",
    avatar: "🩺"
  },
  officer: {
    role: "officer",
    name: "Dr. S. R. Shinde",
    title: "District Veterinary Officer (DVO)",
    location: "Ahmednagar Jurisdiction",
    identifier: "dvo.ahmednagar@maharashtra.gov.in",
    avatar: "🏛️"
  },
  admin: {
    role: "admin",
    name: "State Admin Officer",
    title: "Data Protection & Audit Lead",
    location: "DAHD Maharashtra HQ",
    identifier: "admin@pashusachet.mahadahd.in",
    avatar: "🛡️"
  }
};

let currentUser = null;

function getCurrentUser() {
  if (currentUser) return currentUser;
  try {
    const raw = localStorage.getItem("pashu_auth_user");
    if (raw) currentUser = JSON.parse(raw);
  } catch(e) {}
  return currentUser;
}

function setCurrentUser(user) {
  currentUser = user;
  try {
    if (user) {
      localStorage.setItem("pashu_auth_user", JSON.stringify(user));
    } else {
      localStorage.removeItem("pashu_auth_user");
    }
  } catch(e) {}
  updateAuthUI();
}

function updateAuthUI() {
  const user = getCurrentUser();
  const loginBtn = document.getElementById("headerLoginBtn");
  const profileBadge = document.getElementById("userProfileBadge");
  const avatarIcon = document.getElementById("userAvatarIcon");
  const nameLabel = document.getElementById("userNameLabel");
  const roleLabel = document.getElementById("userRoleLabel");
  const adminNav = document.getElementById("adminNavLink");
  const adminSection = document.getElementById("admin-console");

  if (user) {
    if (loginBtn) loginBtn.style.display = "none";
    if (profileBadge) profileBadge.style.display = "inline-flex";
    if (avatarIcon) avatarIcon.textContent = user.avatar || "👤";
    if (nameLabel) nameLabel.textContent = user.name;
    if (roleLabel) roleLabel.textContent = `${user.title} (${user.location})`;

    // Show/Hide Role-Gated Sections
    const paravetNav = document.getElementById("paravetNavLink");
    const paravetSection = document.getElementById("paravet-inbox");
    if (paravetNav) paravetNav.style.display = "inline-block";
    if (paravetSection) paravetSection.style.display = "block";

    if (user.role === "admin") {
      if (adminNav) adminNav.style.display = "inline-block";
      if (adminSection) {
        adminSection.style.display = "block";
        renderAdminAuditLogs();
      }
    } else {
      if (adminNav) adminNav.style.display = "none";
      if (adminSection) adminSection.style.display = "none";
    }

    // Role switcher sync
    const farmerPill = document.getElementById("roleFarmerBtn");
    const vetPill = document.getElementById("roleVetBtn");
    if (user.role === "vet") {
      if (vetPill) vetPill.classList.add("active");
      if (farmerPill) farmerPill.classList.remove("active");
    } else {
      if (farmerPill) farmerPill.classList.add("active");
      if (vetPill) vetPill.classList.remove("active");
    }
  } else {
    if (loginBtn) loginBtn.style.display = "inline-block";
    if (profileBadge) profileBadge.style.display = "none";
    if (adminNav) adminNav.style.display = "none";
    if (adminSection) adminSection.style.display = "none";
  }
}

function openLoginModal(defaultRole) {
  const modal = document.getElementById("loginModal");
  if (modal) modal.classList.add("active");
  if (defaultRole) switchAuthTab(defaultRole);
}

function closeLoginModal() {
  const modal = document.getElementById("loginModal");
  if (modal) modal.classList.remove("active");
}

function switchAuthTab(role) {
  const tabs = ["farmer", "paravet", "vet", "officer", "admin"];
  tabs.forEach(r => {
    const btn = document.getElementById(`tab${r.charAt(0).toUpperCase() + r.slice(1)}Btn`);
    const pane = document.getElementById(`authPane${r.charAt(0).toUpperCase() + r.slice(1)}`);
    if (btn) btn.classList.toggle("active", r === role);
    if (pane) pane.classList.toggle("active", r === role);
  });
}

function quickLogin(role) {
  const profile = AUTH_PROFILES[role];
  if (profile) {
    setCurrentUser(profile);
    closeLoginModal();
    showToast(`Signed in successfully as ${profile.name} (${profile.title})`);
    
    // Auto-navigate to relevant view
    if (role === "vet") {
      document.getElementById("vet-desk")?.scrollIntoView({ behavior: "smooth" });
    } else if (role === "officer") {
      document.getElementById("outbreak-gis")?.scrollIntoView({ behavior: "smooth" });
    } else if (role === "admin") {
      document.getElementById("admin-console")?.scrollIntoView({ behavior: "smooth" });
    }
  }
}

function logoutUser() {
  const prev = getCurrentUser();
  setCurrentUser(null);
  showToast(prev ? `Signed out ${prev.name}. Switched to public guest mode.` : "Logged out.");
}

function sendFarmerOtp() {
  const phone = document.getElementById("farmerPhoneInput")?.value || "9822012345";
  showToast(`SMS OTP dispatched to +91 ${phone}! Demo OTP is 123456.`);
}

// DPDP Act Audit Event Ledger
const DEFAULT_AUDIT_LOGS = [
  { ts: "2026-11-04 01:45:10", type: "DATA_ACCESS", actor: "FARMER (Ganesh Patil)", entity: "AN-MH-01 (Gauri)", hash: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", status: "AUTHORIZED" },
  { ts: "2026-11-04 01:22:45", type: "CLINICAL_SIGNATURE", actor: "VET (Dr. Rameshwar Kute)", entity: "RX-MH-9412", hash: "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e", status: "VERIFIED" },
  { ts: "2026-11-04 00:58:12", type: "CONSENT_RECORD", actor: "FARMER (Ganesh Patil)", entity: "CONSENT_DPDP_v1", hash: "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", status: "STORED" },
  { ts: "2026-11-03 23:14:02", type: "OUTBREAK_ALERT", actor: "OFFICER (Dr. S. R. Shinde)", entity: "ZONE_AHMEDNAGAR_FMD", hash: "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", status: "ISSUED" }
];

function renderAdminAuditLogs() {
  const tbody = document.getElementById("adminAuditTableBody");
  if (!tbody) return;
  tbody.innerHTML = "";
  DEFAULT_AUDIT_LOGS.forEach(log => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td style="font-family: monospace; font-size: 0.78rem;">${log.ts}</td>
      <td><span class="vax-pill vax-ok">${log.type}</span></td>
      <td><strong>${log.actor}</strong></td>
      <td><code>${log.entity}</code></td>
      <td style="font-family: monospace; font-size: 0.75rem; color: #64748b;">${log.hash.substring(0, 16)}...</td>
      <td><span class="vax-pill vax-ok">${log.status}</span></td>
    `;
    tbody.appendChild(tr);
  });
}

/**
 * PashuSachet (पशूसचेत / Seva First)
 * Multilingual AI-assisted Livestock Health & Veterinary Intelligence Platform
 * Pure static client-side application logic
 */

// 1. MULTILINGUAL TRANSLATION DICTIONARY
const i18n = {
  en: {
    brand_sub: "Livestock Health & Veterinary Intelligence",
    nav_home: "Home",
    nav_screen: "AI Screening",
    nav_risk: "Outbreak Risk GIS",
    nav_registry: "Animal Passport",
    nav_vets: "Find a Vet",
    nav_vet_desk: "Vet Care Desk",
    hero_badge: "🌾 Government Aligned • ICAR-NIVEDI Surveillance Data",
    hero_title: "AI-Assisted Livestock Health & Veterinary Care for Rural Maharashtra",
    hero_subtitle: "Bridging livestock owners and veterinary care: species-aware symptom screening, district outbreak intelligence, and instant verified clinical referrals.",
    btn_start_screen: "🩺 Start Symptom Screening",
    btn_view_map: "🗺️ Outbreak Risk Map",
    stat_species: "Livestock Species",
    stat_accuracy: "Calibrated Decision Rules",
    stat_districts: "Maharashtra Districts",
    stat_cost: "Farmer Cost (Free)",
    screening_title: "Species-Aware Symptom Screening & Decision Support",
    screening_sub: "Select your livestock species and observed symptoms for instant triage, risk rating, and safe first-aid guidance.",
    step1: "1. Select Animal Species",
    step2: "2. Observed Clinical Symptoms",
    step3: "3. Onset & Vital Parameters",
    btn_analyze: "Run AI Symptom Assessment",
    passport_title: "Digital Pashu Aadhar & Health Passport",
    passport_sub: "Permanent verified identity, vaccination schedule, and clinical records for your herd.",
    btn_add_animal: "+ Register New Animal",
    risk_title: "Maharashtra Outbreak Surveillance & Risk Intelligence",
    risk_sub: "Real-time district-level forecast powered by historical outbreak records and seasonal patterns.",
    vets_title: "Verified Veterinary Network & Booking",
    vets_sub: "Connect with accredited Government Veterinary Dispensaries and certified mobile practitioners.",
    disclaimer_text: "Disclaimer: Preliminary AI decision-support screening based on ICAR-NIVEDI protocols. Not a substitute for physical veterinary diagnosis or prescription."
  },
  mr: {
    brand_sub: "पशु आरोग्य आणि पशुवैद्यकीय गुप्तवार्ता",
    nav_home: "मुख्यपृष्ठ",
    nav_screen: "लक्षण तपासणी",
    nav_risk: "रोग प्रादुर्भाव नकाशा",
    nav_registry: "पशू आधार कार्ड",
    nav_vets: "पशुवैद्य शोधा",
    nav_vet_desk: "पशुवैद्यकीय डेस्क",
    hero_badge: "🌾 महाराष्ट्र ग्रामीण सेवा • ICAR-NIVEDI आकडेवारी",
    hero_title: "ग्रामीण महाराष्ट्रासाठी AI-सहाय्यित पशुआरोग्य व पशुवैद्यकीय सेवा",
    hero_subtitle: "शेतकरी व पशुवैद्यकांना जोडणारा आधुनिक मंच: अचूक लक्षण तपासणी, जिल्हास्तरीय साथरोग इशारा आणि थेट पशुवैद्यकीय मदत.",
    btn_start_screen: "🩺 लक्षण तपासणी सुरू करा",
    btn_view_map: "🗺️ साथरोग नकाशा पहा",
    stat_species: "पशु प्रजाती समाविष्ट",
    stat_accuracy: "प्रमाणित रोग नियम",
    stat_districts: "महाराष्ट्र जिल्हे",
    stat_cost: "शेतकऱ्यांसाठी मोफत",
    screening_title: "प्रजाती-आधारित लक्षण तपासणी आणि निर्णय सहाय्य",
    screening_sub: "आपल्या जनावराची जात आणि दिसणारी लक्षणे निवडा; त्वरित मार्गदर्शन व प्रथमोपचार मिळवा.",
    step1: "१. जनावराचा प्रकार निवडा",
    step2: "२. दिसणारी लक्षणे",
    step3: "३. आजाराचा कालावधी व इतर माहिती",
    btn_analyze: "AI लक्षण तपासणी करा",
    passport_title: "डिजिटल पशू आधार आणि आरोग्य नोंदवही",
    passport_sub: "आपल्या जनावरांची कायमस्वरूपी ओळख, लसीकरण दिनदर्शिका आणि उपचारांची नोंद.",
    btn_add_animal: "+ नवीन जनावर नोंदवा",
    risk_title: "महाराष्ट्र जिल्हास्तरीय साथरोग धोका आणि अंदाज",
    risk_sub: "ऐतिहासिक आकडेवारी आणि हवामान घटकांवर आधारित साथरोग पूर्वसूचना.",
    vets_title: "नोंदणीकृत पशुवैद्य आणि दवाखाने",
    vets_sub: "जवळचे शासकीय पशुवैद्यकीय दवाखाने आणि मान्यताप्राप्त डॉक्टरांशी संपर्क साधा.",
    disclaimer_text: "सूचना: ही प्राथमिक AI तपासणी केवळ मार्गदर्शनासाठी आहे. हे अंतिम निदान नसून प्रत्यक्ष डॉक्टरांचा सल्ला आवश्यक आहे."
  },
  hi: {
    brand_sub: "पशु स्वास्थ्य एवं पशुचिकित्सा इंटेलिजेंस",
    nav_home: "होम",
    nav_screen: "लक्षण जांच",
    nav_risk: "प्रकोप जोखिम मैप",
    nav_registry: "पशु आधार",
    nav_vets: "पशु चिकित्सक खोजें",
    nav_vet_desk: "पशुचिकित्सा डेस्क",
    hero_badge: "🌾 ग्रामीण पशु सेवा • ICAR-NIVEDI डेटा आधारित",
    hero_title: "ग्रामीण महाराष्ट्र हेतु AI-सहायित पशु स्वास्थ्य एवं चिकित्सा मंच",
    hero_subtitle: "पशुपालकों और पशु चिकित्सकों को जोड़ने वाला आधुनिक मंच: सटीक लक्षण स्क्रीनिंग, जिला प्रकोप चेतावनी और त्वरित उपचार परामर्श।",
    btn_start_screen: "🩺 लक्षण स्क्रीनिंग प्रारंभ करें",
    btn_view_map: "🗺️ प्रकोप जोखिम मैप देखें",
    stat_species: "पशु प्रजातियां",
    stat_accuracy: "मानकीकृत निर्णय नियम",
    stat_districts: "महाराष्ट्र जिले",
    stat_cost: "किसानों के लिए पूर्णतः निःशुल्क",
    screening_title: "प्रजाति-जागरूक लक्षण जांच एवं निर्णय सहायता",
    screening_sub: "पशु का प्रकार व लक्षण चुनें; तुरंत जोखिम स्तर, प्राथमिक उपचार व डॉक्टर रेफरल प्राप्त करें।",
    step1: "१. पशु की प्रजाति चुनें",
    step2: "२. देखे गए मुख्य लक्षण",
    step3: "३. अवधि एवं शारीरिक स्थिति",
    btn_analyze: "AI लक्षण जांच करें",
    passport_title: "डिजिटल पशु आधार और स्वास्थ्य पासपोर्ट",
    passport_sub: "पशुओं का डिजिटल रिकॉर्ड, टीकाकरण कैलेंडर और स्वास्थ्य इतिहास।",
    btn_add_animal: "+ नया पशु पंजीकृत करें",
    risk_title: "महाराष्ट्र जिला प्रकोप निगरानी व चेतावनी",
    risk_sub: "मौसम और ऐतिहासिक प्रकोप डेटा पर आधारित सटीक रोग जोखिम विश्लेषण।",
    vets_title: "सत्यापित पशु चिकित्सक और अस्पताल",
    vets_sub: "निकटतम सरकारी पशु चिकित्सा केंद्र एवं मोबाइल वैन से तुरंत परामर्श लें।",
    disclaimer_text: "सूचना: यह एआई स्क्रीनिंग केवल प्राथमिक सलाह है। यह अंतिम चिकित्सीय निदान नहीं है, डॉक्टर से जांच अवश्य करवाएं।"
  }
};

let currentLang = 'en';

// 2. STATE MANAGEMENT & LOCAL STORAGE
const DEFAULT_ANIMALS = [
  {
    id: "AN-MH-01",
    tag: "MH-24-9812",
    name: "Gauri (गौरी)",
    species: "Cattle (गाय)",
    breed: "Gir (गीर)",
    age: "3.5 Yrs",
    sex: "Female",
    location: "Sangamner, Ahmednagar",
    vaccines: [
      { name: "FMD Vaccine", date: "15 Aug 2026", status: "ok" },
      { name: "LSD (Lumpy)", date: "Due in 14 days", status: "due" },
      { name: "HS / BQ", date: "12 May 2026", status: "ok" }
    ],
    notes: "Diagnosed with Mastitis; active Ceftiofur treatment",
    prescription: {
      condition: "Acute Mastitis (Udder Swelling)",
      drug: "Ceftiofur Sodium + Flunixin Meglumine",
      route: "Intramammary Infusion + IM",
      treatmentDays: 3,
      withdrawalHours: 72,
      prescribedAt: Date.now() - (14 * 3600 * 1000), // Prescribed 14h ago
      vetName: "Dr. Rameshwar Kute, B.V.Sc & A.H.",
      vetReg: "MSVC/2012/03194",
      status: "UNDER_TREATMENT"
    }
  },
  {
    id: "AN-MH-02",
    tag: "MH-12-4401",
    name: "Raja (राजा)",
    species: "Buffalo (म्हैस)",
    breed: "Murrah (मुऱ्हा)",
    age: "4 Yrs",
    sex: "Male",
    location: "Baramati, Pune",
    vaccines: [
      { name: "FMD Vaccine", date: "10 Jun 2026", status: "ok" },
      { name: "Black Quarter", date: "02 Jul 2026", status: "ok" },
      { name: "Deworming", date: "Due this week", status: "due" }
    ],
    notes: "Active, regular checkup completed"
  },
  {
    id: "AN-MH-03",
    tag: "MH-18-3310",
    name: "Chotu (छोटू)",
    species: "Goat (शेळी)",
    breed: "Osmanabadi (उस्मानाबादी)",
    age: "1.2 Yrs",
    sex: "Female",
    location: "Pandharpur, Solapur",
    vaccines: [
      { name: "PPR Vaccine", date: "14 Jan 2026", status: "ok" },
      { name: "ET (Enterotoxaemia)", date: "Due in 25 days", status: "due" }
    ],
    notes: "Normal feeding, twin pregnancy confirmed"
  }
];


// Storage for Appointments & Cases
const DEFAULT_APPOINTMENTS = [
  {
    id: "APT-9102",
    animal: "Gauri (Tag: MH-24-9812)",
    farmerPhone: "+91 98220 12345",
    visitType: "Doorstep Field Visit",
    date: "Tomorrow, 10:00 AM",
    vet: "Dr. Rameshwar Kute",
    status: "Pending Confirmation"
  },
  {
    id: "APT-9105",
    animal: "Raja (Tag: MH-12-4401)",
    farmerPhone: "+91 94223 99881",
    visitType: "Dispensary Visit",
    date: "Friday, 02:30 PM",
    vet: "Dr. Supriya More",
    status: "Confirmed"
  }
];

const DEFAULT_CASES = [
  {
    id: "CASE-MH-8492",
    animal: "Gauri (Tag: MH-24-9812)",
    tag: "MH-24-9812",
    species: "Cattle (गाय)",
    symptoms: ["High Fever (>103°F)", "Swollen Udder", "Drop in Milk Yield"],
    triageBand: "Likely",
    triageCondition: "Acute Mastitis",
    status: "Under Treatment",
    date: "Today, 08:30 AM"
  }
];

function getStoredAppointments() {
  try {
    const raw = localStorage.getItem("pashu_appointments");
    return raw ? JSON.parse(raw) : DEFAULT_APPOINTMENTS;
  } catch(e) {
    return DEFAULT_APPOINTMENTS;
  }
}

function saveAppointment(apt) {
  const list = getStoredAppointments();
  list.unshift(apt);
  try {
    localStorage.setItem("pashu_appointments", JSON.stringify(list));
  } catch(e) {}
  renderVetDesk();
  updateAuthUI();
}

function getStoredCases() {
  try {
    const raw = localStorage.getItem("pashu_cases");
    return raw ? JSON.parse(raw) : DEFAULT_CASES;
  } catch(e) {
    return DEFAULT_CASES;
  }
}

function saveCase(c) {
  const list = getStoredCases();
  list.unshift(c);
  try {
    localStorage.setItem("pashu_cases", JSON.stringify(list));
  } catch(e) {}
  renderVetDesk();
  updateAuthUI();
}

function updateAnimalPrescription(tag, rx) {
  const animals = getStoredAnimals();
  const animal = animals.find(a => a.tag === tag);
  if (animal) {
    animal.prescription = rx;
    try {
      localStorage.setItem("pashu_animals", JSON.stringify(animals));
    } catch(e) {}
    renderAnimals();
  }
}

function getStoredAnimals() {
  const data = localStorage.getItem("pashu_animals");
  if (!data) {
    localStorage.setItem("pashu_animals", JSON.stringify(DEFAULT_ANIMALS));
    return DEFAULT_ANIMALS;
  }
  try {
    return JSON.parse(data);
  } catch (e) {
    return DEFAULT_ANIMALS;
  }
}

function saveAnimal(animal) {
  const current = getStoredAnimals();
  current.unshift(animal);
  localStorage.setItem("pashu_animals", JSON.stringify(current));
  renderAnimals();
}

// 3. DISTRICT RISK SURVEILLANCE DATA (MAHARASHTRA)
const DISTRICT_DATA = {
  pune: {
    name: "Pune (पुणे)",
    zone: "Western Maharashtra",
    primaryThreat: "Lumpy Skin Disease (LSD)",
    riskLevel: "Moderate",
    riskClass: "risk-mod",
    score: "58%",
    activeClusters: 4,
    vaccineCoverage: "88%",
    advisory: "Monitor cattle for early nodules. Maintain strict tick and vector control around cow sheds.",
    officer: "Dr. K. S. Patil (DVO Pune - 020-25531000)"
  },
  ahmednagar: {
    name: "Ahmednagar (अहिल्यानगर)",
    zone: "North Maharashtra",
    primaryThreat: "Foot & Mouth Disease (FMD)",
    riskLevel: "High Risk",
    riskClass: "risk-high",
    score: "82%",
    activeClusters: 12,
    vaccineCoverage: "74%",
    advisory: "High alert in Sangamner and Rahuri talukas. Restrict movement across cattle markets. Complete ring vaccination.",
    officer: "Dr. S. R. Shinde (DVO Ahmednagar - 0241-2321400)"
  },
  satara: {
    name: "Satara (सातारा)",
    zone: "Western Maharashtra",
    primaryThreat: "Black Quarter (BQ)",
    riskLevel: "Moderate",
    riskClass: "risk-mod",
    score: "49%",
    activeClusters: 2,
    vaccineCoverage: "91%",
    advisory: "Post-rain grazing alert. Avoid waterlogged pastures in low-lying river belts.",
    officer: "Dr. V. M. Deshmukh (DVO Satara - 02162-234500)"
  },
  solapur: {
    name: "Solapur (सोलापूर)",
    zone: "South Western Maharashtra",
    primaryThreat: "Peste des Petits Ruminants (PPR)",
    riskLevel: "High Risk",
    riskClass: "risk-high",
    score: "79%",
    activeClusters: 9,
    vaccineCoverage: "68%",
    advisory: "Urgent advisory for goat and sheep flocks. High incidence of stomatitis reported in Barshi and Pandharpur.",
    officer: "Dr. R. B. Gaikwad (DVO Solapur - 0217-2722100)"
  },
  kolhapur: {
    name: "Kolhapur (कोल्हापूर)",
    zone: "Southern Maharashtra",
    primaryThreat: "Bovine Mastitis & FMD",
    riskLevel: "Low Risk",
    riskClass: "risk-low",
    score: "26%",
    activeClusters: 1,
    vaccineCoverage: "96%",
    advisory: "High routine dairy hygiene index. Regular teat dipping and milker sanitation recommended.",
    officer: "Dr. P. T. Kulkarni (DVO Kolhapur - 0231-2651200)"
  },
  nashik: {
    name: "Nashik (नाशिक)",
    zone: "North Maharashtra",
    primaryThreat: "Lumpy Skin Disease (LSD)",
    riskLevel: "Moderate",
    riskClass: "risk-mod",
    score: "52%",
    activeClusters: 5,
    vaccineCoverage: "84%",
    advisory: "Vector surveillance in Niphad and Sinnar belts. Isolate suspected skin nodules immediately.",
    officer: "Dr. A. J. Jadhav (DVO Nashik - 0253-2578400)"
  },
  chhatrapati_sambhajinagar: {
    name: "Chhatrapati Sambhajinagar (छ. संभाजीनगर)",
    zone: "Marathwada",
    primaryThreat: "Haemorrhagic Septicaemia (HS)",
    riskLevel: "Moderate",
    riskClass: "risk-mod",
    score: "61%",
    activeClusters: 6,
    vaccineCoverage: "79%",
    advisory: "Seasonal change risk. Provide clean drinking water; inspect for throat swelling and respiratory distress.",
    officer: "Dr. N. G. Chavan (DVO Sambhajinagar - 0240-2334100)"
  },
  latur: {
    name: "Latur (लातूर)",
    zone: "Marathwada",
    primaryThreat: "Enterotoxaemia & Anthrax",
    riskLevel: "Low Risk",
    riskClass: "risk-low",
    score: "31%",
    activeClusters: 0,
    vaccineCoverage: "89%",
    advisory: "Flock deworming drive active. Report any sudden unconfirmed small ruminant deaths immediately.",
    officer: "Dr. H. K. Bhosle (DVO Latur - 02382-243200)"
  }
};

// 4. VERIFIED VETERINARY CLINICS & DIRECTORY
const VET_LIST = [
  {
    name: "Dr. Rameshwar Kute, B.V.Sc & A.H.",
    role: "Livestock Development Officer (LDO Grade-I)",
    center: "Government Veterinary Dispensary, Sangamner",
    district: "Ahmednagar",
    phone: "+91 94220 81122",
    experience: "14 Years",
    species: "Cattle, Buffalo, Goat",
    timings: "9:00 AM - 4:00 PM (Emergency 24x7)"
  },
  {
    name: "Dr. Supriya More, M.V.Sc (Veterinary Medicine)",
    role: "Senior Veterinary Surgeon",
    center: "Taluka Polyclinic, Baramati",
    district: "Pune",
    phone: "+91 98223 45678",
    experience: "11 Years",
    species: "Cattle, Buffalo, Poultry",
    timings: "8:30 AM - 5:00 PM"
  },
  {
    name: "Dr. Anand Joshi, B.V.Sc",
    role: "Mobile Veterinary Clinic Officer",
    center: "Pandharpur Rural Mobile Unit",
    district: "Solapur",
    phone: "+91 97631 99234",
    experience: "9 Years",
    species: "Goat, Sheep, Buffalo",
    timings: "On-Field Visits 7:00 AM - 2:00 PM"
  },
  {
    name: "Dr. Meena Sawant, M.V.Sc (Surgery)",
    role: "District Veterinary Polyclinic",
    center: "Central Polyclinic, Satara",
    district: "Satara",
    phone: "+91 98901 22345",
    experience: "16 Years",
    species: "All Livestock & Equine",
    timings: "9:00 AM - 5:00 PM"
  },
  {
    name: "Dr. Vinayak Patil, B.V.Sc & A.H.",
    role: "Veterinary Officer Grade-II",
    center: "Govt Veterinary Hospital, Karveer",
    district: "Kolhapur",
    phone: "+91 94238 77112",
    experience: "8 Years",
    species: "High-Yield Dairy Cattle",
    timings: "8:00 AM - 2:00 PM"
  },
  {
    name: "Dr. Sachin Sonawane, B.V.Sc",
    role: "LDO & Outbreak Response Lead",
    center: "Veterinary Dispensary, Sinnar",
    district: "Nashik",
    phone: "+91 94215 66789",
    experience: "12 Years",
    species: "Cattle, Poultry, Sheep",
    timings: "9:00 AM - 4:30 PM"
  }
];

// 5. INITIALIZATION & DOM EVENTS
document.addEventListener("DOMContentLoaded", () => {
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
});

// LANGUAGE TOGGLE
function initLanguage() {
  const buttons = document.querySelectorAll(".lang-btn");
  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const lang = btn.getAttribute("data-lang");
      setLanguage(lang);
    });
  });
}

function setLanguage(lang) {
  if (!i18n[lang]) return;
  currentLang = lang;
  document.querySelectorAll("[data-i18n]").forEach(elem => {
    const key = elem.getAttribute("data-i18n");
    if (i18n[lang][key]) {
      elem.textContent = i18n[lang][key];
    }
  });
  showToast(`Language switched to ${lang === 'mr' ? 'मराठी' : lang === 'hi' ? 'हिन्दी' : 'English'}`);
}

// 6. SYMPTOM CHECKER ENGINE (MODEL A SIMULATION)
function initSymptomChecker() {
  const form = document.getElementById("symptomForm");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    evaluateSymptoms();
  });

  // Reset button
  const resetBtn = document.getElementById("resetSymptomBtn");
  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      form.reset();
      const res = document.getElementById("assessmentResult");
      if (res) res.classList.remove("active");
    });
  }
}

function evaluateSymptoms() {
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
  const proxyReporterRole = document.getElementById("proxyReporterRole")?.value || "neighbor";

  if (checkedBoxes.length === 0) {
    alert(currentLang === 'mr' ? "कृपया किमान एक किंवा दोन लक्षणे निवडा." : "Please select at least 1 or 2 observed symptoms.");
    return;
  }

  const resultContainer = document.getElementById("assessmentResult");
  const triageBanner = document.getElementById("triageBanner");
  const triageText = document.getElementById("triageText");
  const diagName = document.getElementById("diagName");
  const diagConf = document.getElementById("diagConf");
  const confBar = document.getElementById("confBar");
  const adviceList = document.getElementById("adviceList");
  const diffDiag = document.getElementById("diffDiag");

  // Rule-based clinical triage matching Seva First Model A & GSS Protocol
  let primaryCondition = "";
  let qualitativeBand = "Likely"; // Likely, Possible, Less Likely, Abstention
  let urgency = "moderate"; // critical, urgent, moderate
  let urgencyLabel = "";
  let differential = [];
  let actions = [];
  let isZoonoticAlert = false;
  let zoonoticMsg = "";
  let mvuTicket = null;
  let isAbstention = false;

  // RED-FLAG EMERGENCY CIRCUIT BREAKER & 1962 ACCELERATOR
  const isRedFlag = checkedBoxes.includes("bleeding") || checkedBoxes.includes("sudden_death") || checkedBoxes.includes("recumbent") || isMortalityCheck;
  if (isRedFlag) {
    const emergModal = document.getElementById("emergencyModal");
    if (emergModal) emergModal.classList.add("active");

    // 1962 ACCELERATOR ENGINE: Auto-generate priority MVU dispatch pre-notification
    mvuTicket = {
      ticketId: "1962-MH-" + Math.floor(1000 + Math.random() * 9000),
      dispatchStatus: "AUTO_PRENOTIFIED",
      priority: "CRITICAL_RED_FLAG",
      targetVillage: villageLocation,
      assignedUnit: "MVU Unit 14 (Sangamner / Akole Beat)",
      mvuContact: "1962 (Toll Free)",
      etaMinutes: 25,
      timestamp: new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' })
    };
  }

  const hasFever = checkedBoxes.includes("fever") || tempDegree >= 103.5;
  const hasNodules = checkedBoxes.includes("skin_nodules");
  const hasMouthFoot = checkedBoxes.includes("mouth_lesions") || checkedBoxes.includes("lameness");
  const hasRespiratory = checkedBoxes.includes("cough") || checkedBoxes.includes("nasal_discharge");
  const hasMastitis = checkedBoxes.includes("udder_swelling") || checkedBoxes.includes("milk_drop");
  const hasDiarrhea = checkedBoxes.includes("diarrhea");
  const hasSuddenDeath = checkedBoxes.includes("sudden_death") || isMortalityCheck;

  // ZOONOTIC THREAT SENTINEL (Anthrax, Rabies, Brucellosis)
  if (hasSuddenDeath && (species === "cattle" || species === "buffalo" || species === "sheep")) {
    isZoonoticAlert = true;
    zoonoticMsg = "अँथ्रॅक्स / अचानक मृत्यू संशय (Anthrax Suspected). शव उघडू नका, नैसर्गिक छिद्रांमधून रक्तस्त्राव असल्यास स्पर्श करू नका. स्थानिक शासकीय वैद्यक व जिल्हा आरोग्य अधिकारी (DMO) यांना अलर्ट पाठवला आहे.";
  } else if (species === "dog" && (checkedBoxes.includes("mouth_lesions") || checkedBoxes.includes("anorexia") || isRedFlag)) {
    isZoonoticAlert = true;
    zoonoticMsg = "रेबीज संशय (Rabies Suspected). चावा किंवा लाळेचा मानवी त्वचेशी संपर्क टाळा. संशयित प्राण्याला सुरक्षित जागी बंदिस्त करा व त्वरित 1962 वर कळवा.";
  }

  // EXPLICIT ABSTENTION GATE:
  // If only isolated non-specific signs (anorexia only, milk drop only) and no fever or pathognomonic lesions:
  if ((checkedBoxes.length === 1 && (checkedBoxes[0] === 'anorexia' || checkedBoxes[0] === 'milk_drop')) ||
      (!hasNodules && !hasMouthFoot && !hasRespiratory && !hasMastitis && !hasDiarrhea && !hasSuddenDeath && tempDegree < 103.0)) {
    isAbstention = true;
    primaryCondition = "अस्पष्ट प्रारंभिक लक्षणे (Insufficient Distinctive Signs)";
    qualitativeBand = "Abstention";
    urgency = "moderate";
    urgencyLabel = "MODERATE: मॉडेल संयम (Deliberate Abstention - No Speculation)";
    actions = [
      "१. जनावराला कोणतेही अनधिकृत प्रतिजैविक (अँटीबायोटिक) किंवा मानवी औषध देऊ नका.",
      "२. रवंथ चक्र तपासा (२ मिनिटांत २ ते ३ वेळा रवंथ व्हायला हवे) आणि ताजे पिण्याचे पाणी व हिरवा चारा द्या.",
      "३. पुढील १२ ते २४ तास लक्षपूर्वक निरीक्षण करा आणि गुदद्वाराचे तापमान मोजा.",
      "४. २४ तासांनंतरही सुधारणा न झाल्यास स्थानिक पशुमित्र किंवा पशुवैद्यकीय दवाखान्यात संपर्क साधा."
    ];
    differential = ["Mild Indigestion (अपचन)", "Environmental / Heat Stress (उष्मा ताण)", "Subclinical Diet Change"];
  } else if (species === "poultry") {
    if (hasRespiratory || checkedBoxes.includes("anorexia") || hasSuddenDeath) {
      primaryCondition = "Newcastle Disease (Ranikhet) / Infectious Coryza (राणीखेत)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Urgent Flock Isolation Required";
      actions = [
        "१. आजारी पक्ष्यांना तात्काळ निरोगी कळपापासून वेगळे (क्वारंटाइन) करा.",
        "२. पिण्याच्या पाण्यात इलेक्ट्रोल पावडर व व्हिटॅमिन बी-कॉम्प्लेक्स मिसळून द्या.",
        "३. शेडच्या प्रवेशद्वारावर जंतुनाशक फवारणी करा व बाहेरील व्यक्तींना प्रवेश बंदी करा.",
        "४. शासकीय प्रयोगशाळेतील तपासणीसाठी तात्काळ स्थानिक पशुवैद्यकांना संपर्क करा."
      ];
      differential = ["Infectious Bronchitis", "Fowl Cholera", "Nutritional Deficiency"];
    } else {
      primaryCondition = "Coccidiosis / Enteric Distress (कॉकसिडिओसिस)";
      qualitativeBand = "Possible";
      urgency = "urgent";
      urgencyLabel = "URGENT: Review Litter Hygiene";
      actions = [
        "१. शेडमधील ओले तूस (litter) तात्काळ बदलून कोरडा भुसा टाका.",
        "२. पिण्याचे पाणी स्वच्छ व आम्लयुक्त (acidified) ठेवा.",
        "३. पशुवैद्यकीय सल्ल्याने कॉक्सिडिओस्टॅट औषध सुरू करा."
      ];
      differential = ["Colibacillosis", "Dietary change"];
    }
  } else if (species === "goat" || species === "sheep") {
    if (checkedBoxes.includes("mouth_lesions") && (hasDiarrhea || hasFever)) {
      primaryCondition = "Peste des Petits Ruminants (PPR) / Goat Plague (शेळ्यांमधील पीपीआर)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Highly Contagious Small Ruminant Alert";
      actions = [
        "१. बाधित शेळ्या/मेंढ्या तात्काळ वेगळ्या बांधा; सार्वजनिक चराई व पाण्याचे टाके पूर्णपणे बंद करा.",
        "२. तोंडातील जखमांवर सौम्य पोटॅशियम परमँगनेट (१:१०,०००) किंवा बोरोग्लिसरीन लावा.",
        "३. कोमट द्रावण किंवा मऊ लापशी खाऊ घाला, कोरडे धांडे देऊ नका.",
        "४. जवळच्या पशुवैद्यकीय दवाखान्यातून रिंग-लसीकरण (Ring Vaccination) मोहीम राबवून घ्या."
      ];
      differential = ["Contagious Ecthyma (Orf)", "Bluetongue", "Pasteurellosis"];
    } else if (hasSuddenDeath || hasDiarrhea) {
      primaryCondition = "Enterotoxaemia (Pulpy Kidney) Suspected (आंत्रविषार)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Risk of Rapid Mortality";
      actions = [
        "१. धान्य व पेंड देणे ताबडतोब थांबवा; केवळ कोरडा चारा द्या.",
        "२. आजारी नसलेल्या सर्व जनावरांना तात्काळ आंत्रविषार (ET) लस टोचून घ्या.",
        "३. पशुवैद्यकीय पथकाकडून डिहायड्रेशन रोखण्यासाठी सलाइन उपचार घ्या."
      ];
      differential = ["Coccidiosis", "Plant Poisoning"];
    } else {
      primaryCondition = "Pneumonia / Caprine Respiratory Infection (फुफ्फुसदाह/खोकला)";
      qualitativeBand = "Possible";
      urgency = "urgent";
      urgencyLabel = "URGENT: Veterinary Auscultation Advised";
      actions = [
        "१. शेड कोरडी व हवेशीर ठेवा; रात्री थंड वाऱ्यापासून संरक्षण करा.",
        "२. कोमट पाणी व गुळ-पाणी पिण्यास द्या.",
        "३. पशुवैद्यकीय सल्ल्याने प्रतिजैविक व कफ सिरप द्या."
      ];
      differential = ["Lungworm infestation", "Shipping fever"];
    }
  } else {
    // Cattle / Buffalo
    if (hasNodules) {
      primaryCondition = "Lumpy Skin Disease (LSD) Suspected (लम्पी त्वचा रोग)";
      qualitativeBand = "Likely";
      urgency = "urgent";
      urgencyLabel = "URGENT: Vector-Borne Viral Screening Positive";
      actions = [
        "१. बाधित जनावराला निरोगी जनावरांपासून तात्काळ दूर वेगळ्या गोठ्यात बांधा.",
        "२. गोठ्यात कडुनिंबाच्या पानांचा धूर करा व डास/माशा/गोचीड प्रतिबंधक फवारणी करा.",
        "३. अंगावरील गाठी व जखमांवर हळद + कापूर + खोबरेल तेलाचा लेप लावा.",
        "४. मानवी ताप प्रतिबंधक औषधे (उदा. पॅरासिटामॉल) डॉक्टरी सल्ल्याशिवाय अतिरिक्त प्रमाणात देऊ नका.",
        "५. स्थानिक पशुवैद्यकांना संपर्क करून गोट पॉक्स (Goat Pox) लसीकरण तपासा."
      ];
      differential = ["Pseudo-lumpy skin disease (Herpesvirus 2)", "Bovine Papillomatosis", "Insect bites"];
    } else if (hasMouthFoot && (hasFever || checkedBoxes.includes("milk_drop"))) {
      primaryCondition = "Foot and Mouth Disease (FMD) Screening Match (लाळ-खुरकूत)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: High Transmission Risk (Reportable)";
      actions = [
        "१. आजारी जनावराला तात्काळ वेगळे बांधा व जनावरांची हालचाल पूर्णपणे थांबवा.",
        "२. तोंड १% तुरटीच्या पाण्याने किंवा पोटॅशियम परमँगनेटच्या सौम्य पाण्याने दिवसातून २ वेळा धुवा.",
        "३. खुरांच्या जखमांमध्ये फिनाईल किंवा जंतुनाशक मलम (जस्त मलम + हळद) लावा जेणेकरून किडे पडणार नाहीत.",
        "४. जनावराला मऊ चारा, दलिया किंवा पेज खायला द्या (कडक वैरणीने तोंडाला त्रास होतो).",
        "५. गावातील इतर पशुपालकांना सतर्क करून सामूहिक लसीकरणाची मागणी करा."
      ];
      differential = ["Vesicular Stomatitis", "Mucosal Disease (BVD)", "Chemical irritant"];
    } else if (hasMastitis) {
      primaryCondition = "Bovine Mastitis (Sub-acute / Clinical) (कासदाह/स्तनदाह)";
      qualitativeBand = "Likely";
      urgency = "urgent";
      urgencyLabel = "URGENT: Dairy Production & Milk Safety Concern";
      actions = [
        "१. बाधित सडातील दूध वेगळे काढून जंतुनाशक टाकून नष्ट करा; हे दूध विक्री करू नका.",
        "२. कासेला कोमट पाण्याने स्वच्छ धुऊन सुती कापडाने कोरडे करा.",
        "३. दूध काढताना प्रथम निरोगी सडांचे व शेवटी आजारी सडाचे दूध काढा.",
        "४. दूध काढल्यानंतर सड जंतुनाशक द्रावणात (Teat Dip) बुडवा.",
        "५. पशुवैद्यकांकडून CMT टेस्ट व इंट्रामॅमरी ट्यूब उपचार करून घ्या."
      ];
      differential = ["Udder edema", "Hematoma", "Mycoplasma mastitis"];
    } else if (hasRespiratory && hasFever) {
      primaryCondition = "Haemorrhagic Septicaemia (HS) Suspected (घटसर्प)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Rapid Progression - Immediate Vet Attention";
      actions = [
        "१. जनावराला अजिबात चालवू नका; थंड व हवेशीर सावलीत ठेवा.",
        "२. मानेभोवती किंवा गळ्याखाली सूज असल्यास त्यावर थंड पाणी टाका.",
        "३. घटसर्पामध्ये काही तासांत मृत्यू संभवतो, म्हणून तात्काळ १९६२ रुग्णवाहिका बोलवा.",
        "४. पशुवैद्यकीय डॉक्टरांकडून तात्काळ प्रतिजैविक इंजेक्शन सुरू करा."
      ];
      differential = ["Black Quarter (early)", "Enzootic Pneumonia", "Aspiration pneumonia"];
    } else {
      primaryCondition = "Non-Specific Indigestion / Simple Anorexia (अपचन/चारा न खाणे)";
      qualitativeBand = "Possible";
      urgency = "moderate";
      urgencyLabel = "MODERATE: Monitor Vitals & Rumination";
      actions = [
        "१. जनावराला पाचक मसाले, गूळ व खनिज मिश्रण (Mineral Mixture) द्या.",
        "२. रवंथ चक्र तपासा (२ मिनिटांत किमान २ वेळा रवंथ व्हायला हवे).",
        "३. २४ तासांत खाणे पूर्ववत न झाल्यास पशुवैद्यकीय तपासणी करून घ्या."
      ];
      differential = ["Mild rumen acidosis", "Dietary change stress", "Parasitic load"];
    }
  }

  // Populate UI
  triageBanner.className = `triage-banner triage-${urgency}`;
  triageText.innerHTML = `<strong>${urgency.toUpperCase()}:</strong> ${urgencyLabel}`;

  diagName.textContent = primaryCondition;
  
  const bandContainer = document.getElementById("triageBandContainer");
  if (bandContainer) {
    bandContainer.textContent = `${qualitativeBand} Differential (संभाव्य श्रेणी)`;
    bandContainer.className = `triage-band ${qualitativeBand.toLowerCase()}`;
  }

  // 1962 Accelerator Card Display
  const mvuCard = document.getElementById("mvuDispatchCard");
  const mvuDetails = document.getElementById("mvuTicketDetails");
  if (mvuCard && mvuDetails) {
    if (mvuTicket) {
      mvuDetails.innerHTML = `<strong>Ticket:</strong> #${mvuTicket.ticketId} • <strong>Status:</strong> Pre-Notified to <strong>${mvuTicket.assignedUnit}</strong> (${mvuTicket.targetVillage}) • <strong>Estimated Arrival:</strong> ~${mvuTicket.etaMinutes} mins.`;
      mvuCard.style.display = "block";
    } else {
      mvuCard.style.display = "none";
    }
  }

  // Zoonotic Alert Display
  const zooBanner = document.getElementById("zoonoticAlertBanner");
  const zooDetails = document.getElementById("zoonoticDetails");
  if (zooBanner && zooDetails) {
    if (isZoonoticAlert) {
      zooDetails.innerHTML = zoonoticMsg;
      zooBanner.style.display = "block";
    } else {
      zooBanner.style.display = "none";
    }
  }

  // Abstention Box Display
  const abstentionBox = document.getElementById("abstentionNoticeBox");
  if (abstentionBox) {
    abstentionBox.style.display = isAbstention ? "block" : "none";
  }
  
  lastTriageResult = {
    condition: primaryCondition,
    band: qualitativeBand,
    symptoms: checkedBoxes,
    isAbstention,
    isZoonotic: isZoonoticAlert,
    mvuTicket
  };

  diffDiag.textContent = `Differential Rule-Outs: ${differential.join(" • ")}`;

  adviceList.innerHTML = "";
  actions.forEach(act => {
    const li = document.createElement("li");
    li.textContent = act;
    adviceList.appendChild(li);
  });

  resultContainer.classList.add("active");
  if (typeof goToTriageStep === 'function') {
    goToTriageStep(4);
  } else {
    resultContainer.scrollIntoView({ behavior: "smooth", block: "start" });
  }
  showToast("AI Assessment generated successfully");
}

// 7. MAHARASHTRA OUTBREAK GIS MODULE (MODEL B)
function initGIS() {
  const select = document.getElementById("gisDistrictSelect");
  const pills = document.querySelectorAll(".dist-pill");

  if (select) {
    select.addEventListener("change", (e) => {
      loadDistrictInfo(e.target.value);
    });
  }

  pills.forEach(pill => {
    pill.addEventListener("click", () => {
      pills.forEach(p => p.classList.remove("selected"));
      pill.classList.add("selected");
      const dist = pill.getAttribute("data-district");
      if (select) select.value = dist;
      loadDistrictInfo(dist);
    });
  });

  // Load default
  loadDistrictInfo("ahmednagar");
}

function loadDistrictInfo(districtKey) {
  const d = DISTRICT_DATA[districtKey] || DISTRICT_DATA.ahmednagar;

  const dName = document.getElementById("gisDistName");
  const dZone = document.getElementById("gisDistZone");
  const dThreat = document.getElementById("gisThreat");
  const dRisk = document.getElementById("gisRiskBadge");
  const dScore = document.getElementById("gisScore");
  const dClusters = document.getElementById("gisClusters");
  const dVaccine = document.getElementById("gisVaccine");
  const dAdvisory = document.getElementById("gisAdvisory");
  const dOfficer = document.getElementById("gisOfficer");

  if (dName) dName.textContent = d.name;
  if (dZone) dZone.textContent = `Region: ${d.zone}`;
  if (dThreat) dThreat.textContent = d.primaryThreat;
  if (dRisk) {
    dRisk.textContent = d.riskLevel;
    dRisk.className = `risk-tag ${d.riskClass}`;
  }
  if (dScore) dScore.textContent = d.score;
  if (dClusters) dClusters.textContent = d.activeClusters;
  if (dVaccine) dVaccine.textContent = d.vaccineCoverage;
  if (dAdvisory) dAdvisory.textContent = d.advisory;
  if (dOfficer) dOfficer.textContent = d.officer;
}

// 8. RENDER ANIMALS (HEALTH PASSPORT)
function renderAnimals() {
  const container = document.getElementById("animalListContainer");
  if (!container) return;

  const list = getStoredAnimals();
  container.innerHTML = "";

  list.forEach(a => {
    const card = document.createElement("div");
    card.className = "animal-card";

    let vaxHtml = "";
    if (a.vaccines && a.vaccines.length > 0) {
      vaxHtml = a.vaccines.map(v => `
        <span class="vax-pill ${v.status === 'ok' ? 'vax-ok' : 'vax-due'}">
          ${v.status === 'ok' ? '✓' : '⚠️'} ${v.name}: ${v.date}
        </span>
      `).join(" ");
    }

    // Food Safety Milk Withholding Alert Banner
    let withholdingHtml = "";
    if (a.prescription) {
      const rx = a.prescription;
      // Formula: Clock counts from the LAST dose:
      const treatmentDurationMs = (rx.treatmentDays || 3) * 24 * 3600 * 1000;
      const withdrawalBufferMs = (rx.withdrawalHours || 72) * 3600 * 1000;
      const totalPeriodMs = treatmentDurationMs + withdrawalBufferMs;
      const prescribedAt = rx.prescribedAt || Date.now();
      const endTime = prescribedAt + totalPeriodMs;
      const isUrgent = (endTime - Date.now()) > 0;

      withholdingHtml = `
        <div class="withholding-alert ${isUrgent ? 'urgent' : 'cleared'}">
          <div class="withholding-header">
            <span class="withholding-title">
              ${isUrgent ? '⚠️ MANDATORY MILK WITHHOLDING' : '✓ MILK WITHDRAWAL CLEARED'}
            </span>
            <span style="font-size: 0.72rem; font-weight: 700; color: #64748b;">FOOD SAFETY MANDATE</span>
          </div>
          <div class="withholding-clock" data-withdrawal-end="${endTime}">
            ⏱️ Calculating clock...
          </div>
          <div class="withholding-meta">
            <div><strong>Rx:</strong> ${rx.drug} (${rx.route || 'IM'})</div>
            <div><strong>Attending Vet:</strong> ${rx.vetName} • <em>${rx.vetReg}</em></div>
            <div style="font-weight: 600; color: ${isUrgent ? '#b91c1c' : '#15803d'}; margin-top: 3px;">
              ${isUrgent ? '⛔ DO NOT POOL MILK OR SUPPLY TO DAIRY' : '✓ Safe for human consumption & dairy sale'}
            </div>
          </div>
        </div>
      `;
    }

    card.innerHTML = `
      <div class="animal-card-header">
        <div>
          <h4 style="font-size: 1.1rem; font-weight: 700; color: #14532d;">${a.name}</h4>
          <span style="font-size: 0.8rem; color: #64748b;">${a.species} • ${a.breed}</span>
        </div>
        <span class="tag-badge">🏷️ ${a.tag}</span>
      </div>
      <div class="animal-card-body">
        <div style="background: #fefce8; border: 1px solid #fef08a; border-radius: 6px; padding: 4px 8px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between; font-size: 0.76rem; font-weight: 700; color: #854d0e;">
          <span>🏅 ग्राम जागरूक पशुपालक (Vigilant Sentinel Farmer)</span>
          <span style="font-size: 0.7rem; color: #a16207; font-weight: 600;">Priority Dispensary Pass</span>
        </div>
        <p style="font-size: 0.85rem; color: #334155; margin-bottom: 6px;">
          <strong>Age/Sex:</strong> ${a.age} • ${a.sex} | <strong>Location:</strong> ${a.location}
        </p>
        <p style="font-size: 0.82rem; color: #475569; margin-bottom: 8px; font-style: italic;">
          "${a.notes}"
        </p>
        
        <!-- Live Milk Withholding Section -->
        ${withholdingHtml}

        <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px;">
          ${vaxHtml}
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="btn btn-outline btn-sm" onclick="prefillSymptomCheck('${a.species}')" style="flex: 1;">
            🩺 Screen
          </button>
          <button class="btn btn-primary btn-sm" onclick="openBookModalForAnimal('${a.name}', '${a.tag}')" style="flex: 1;">
            📅 Book Vet
          </button>
        </div>
      </div>
    `;
    container.appendChild(card);
  });
  
  updateWithdrawalClocks();
}

function prefillSymptomCheck(speciesStr) {
  let target = "cattle";
  if (speciesStr.toLowerCase().includes("buffalo")) target = "buffalo";
  else if (speciesStr.toLowerCase().includes("goat")) target = "goat";
  else if (speciesStr.toLowerCase().includes("sheep")) target = "sheep";
  else if (speciesStr.toLowerCase().includes("poultry")) target = "poultry";

  const radio = document.querySelector(`input[name="species"][value="${target}"]`);
  if (radio) radio.checked = true;

  document.getElementById("symptom-screening")?.scrollIntoView({ behavior: "smooth" });
  showToast(`Prefilled screening for ${speciesStr}`);
}

// 9. VETERINARY DIRECTORY
function renderVets() {
  const container = document.getElementById("vetDirectoryContainer");
  if (!container) return;

  container.innerHTML = "";
  VET_LIST.forEach(v => {
    const card = document.createElement("div");
    card.className = "vet-card";
    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <span class="vet-badge">✓ Verified Govt Officer</span>
        <span style="font-size: 0.8rem; color: #64748b; font-weight: 600;">Exp: ${v.experience}</span>
      </div>
      <h4 style="font-size: 1.05rem; font-weight: 700; color: #0f172a; margin-bottom: 4px;">${v.name}</h4>
      <p style="font-size: 0.82rem; color: #166534; font-weight: 600; margin-bottom: 6px;">${v.role}</p>
      <p style="font-size: 0.85rem; color: #334155; margin-bottom: 6px;">🏥 ${v.center}</p>
      <p style="font-size: 0.82rem; color: #64748b; margin-bottom: 6px;">📍 District: <strong>${v.district}</strong> | 🐄 ${v.species}</p>
      <p style="font-size: 0.8rem; color: #64748b; margin-bottom: 14px;">🕒 Timings: ${v.timings}</p>
      <div style="display: flex; gap: 8px;">
        <a href="tel:${v.phone.replace(/\\s/g,'')}" class="btn btn-outline btn-sm" style="flex: 1;">
          📞 Call
        </a>
        <button class="btn btn-primary btn-sm" onclick="openBookModalForVet('${v.name}')" style="flex: 1;">
          📅 Request Visit
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}



// 11. MODALS & FORMS
function initModals() {
  // Add animal modal
  const addAnimalBtn = document.getElementById("addAnimalBtn");
  const addAnimalModal = document.getElementById("addAnimalModal");
  const closeAnimalModal = document.getElementById("closeAnimalModal");
  const addAnimalForm = document.getElementById("addAnimalForm");

  if (addAnimalBtn && addAnimalModal) {
    addAnimalBtn.addEventListener("click", () => {
      addAnimalModal.classList.add("active");
    });
  }
  if (closeAnimalModal && addAnimalModal) {
    closeAnimalModal.addEventListener("click", () => {
      addAnimalModal.classList.remove("active");
    });
  }

  if (addAnimalForm) {
    addAnimalForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("newAnimalName").value;
      const species = document.getElementById("newAnimalSpecies").value;
      const breed = document.getElementById("newAnimalBreed").value || "Desi / Indigenous";
      const tag = document.getElementById("newAnimalTag").value || `MH-${Math.floor(1000 + Math.random()*9000)}`;
      const age = document.getElementById("newAnimalAge").value || "2 Yrs";
      const village = document.getElementById("newAnimalVillage").value || "Maharashtra";

      const newObj = {
        id: "AN-" + Date.now(),
        tag: tag,
        name: name,
        species: species,
        breed: breed,
        age: age,
        sex: "Female",
        location: village,
        vaccines: [
          { name: "FMD Vaccine", date: "Due Soon", status: "due" },
          { name: "Deworming", date: "Schedule now", status: "due" }
        ],
        notes: "Newly registered via PashuSachet portal"
      };

      saveAnimal(newObj);
      addAnimalModal.classList.remove("active");
      addAnimalForm.reset();
      showToast(`Registered animal: ${name} (Tag: ${tag})`);
    });
  }

  
  
  // Authentication Forms Submit Handlers
  document.getElementById("farmerLoginForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    quickLogin("farmer");
  });
  document.getElementById("paravetLoginForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    quickLogin("paravet");
  });
  document.getElementById("vetLoginForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    quickLogin("vet");
  });
  document.getElementById("officerLoginForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    quickLogin("officer");
  });
  document.getElementById("adminLoginForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    quickLogin("admin");
  });

  // Prescription Form Submit Handler
  const prescribeForm = document.getElementById("prescribeForm");
  const prescribeModal = document.getElementById("prescribeModal");
  if (prescribeForm && prescribeModal) {
    prescribeForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const tag = document.getElementById("rxAnimalTag").value;
      const condition = document.getElementById("rxCondition").value;
      const drug = document.getElementById("rxDrug").value;
      const route = document.getElementById("rxRoute").value;
      const treatmentDays = parseInt(document.getElementById("rxTreatmentDays").value || "3");
      const milkHours = parseInt(document.getElementById("rxMilkHours").value || "72");
      const vetName = document.getElementById("rxVetName").value;
      const vetReg = document.getElementById("rxVetReg").value;

      const newRx = {
        condition: condition,
        drug: drug,
        route: route,
        treatmentDays: treatmentDays,
        withdrawalHours: milkHours,
        prescribedAt: Date.now(),
        vetName: vetName,
        vetReg: vetReg,
        status: "UNDER_TREATMENT"
      };

      updateAnimalPrescription(tag, newRx);
      prescribeModal.classList.remove("active");
      showToast(`Prescription signed & sealed! Live milk withdrawal timer active on Tag ${tag}.`);
      
      const passportSec = document.getElementById("health-passport");
      if (passportSec) passportSec.scrollIntoView({ behavior: "smooth" });
    });
  }

  // Appointment Modal
  const bookModal = document.getElementById("bookModal");
  const closeBookModal = document.getElementById("closeBookModal");
  const bookForm = document.getElementById("bookForm");

  if (closeBookModal && bookModal) {
    closeBookModal.addEventListener("click", () => {
      bookModal.classList.remove("active");
    });
  }

  if (bookForm && bookModal) {
    bookForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const vet = document.getElementById("bookVetName").value || "Dr. Rameshwar Kute";
      const farmerPhone = document.getElementById("bookPhone").value;
      const date = document.getElementById("bookDate").value;
      const animal = document.getElementById("bookAnimalSelect").value || "Gauri (Tag: MH-24-9812)";
      const visitType = document.getElementById("bookType").value || "Doorstep Field Visit";

      const newApt = {
        id: "APT-" + Math.floor(1000 + Math.random()*9000),
        animal: animal,
        farmerPhone: farmerPhone,
        visitType: visitType,
        date: date,
        vet: vet,
        status: "Pending Confirmation"
      };

      saveAppointment(newApt);
      bookModal.classList.remove("active");
      bookForm.reset();
      showToast(`Appointment Request sent to ${vet}! Saved in Vet Care Desk queue.`);
    });
  }

  // Close when clicking outside overlay
  window.addEventListener("click", (e) => {
    if (e.target.classList.contains("modal-overlay")) {
      e.target.classList.remove("active");
    }
  });
}

function openBookModalForAnimal(animalName, tag) {
  const modal = document.getElementById("bookModal");
  const inputAnimal = document.getElementById("bookAnimalSelect");
  if (inputAnimal) inputAnimal.value = `${animalName} (Tag: ${tag})`;
  if (modal) modal.classList.add("active");
}

function openBookModalForVet(vetName) {
  const modal = document.getElementById("bookModal");
  const inputVet = document.getElementById("bookVetName");
  if (inputVet) inputVet.value = vetName;
  if (modal) modal.classList.add("active");
}

// 12. TOAST NOTIFICATION UTILITY
function showToast(message) {
  let container = document.getElementById("toastContainer");
  if (!container) {
    container = document.createElement("div");
    container.id = "toastContainer";
    container.className = "toast-container";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `<span>🔔</span> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(100%)";
    toast.style.transition = "all 0.3s ease";
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}


// LIVE MILK WITHHOLDING CLOCK TIMER
function updateWithdrawalClocks() {
  const clocks = document.querySelectorAll("[data-withdrawal-end]");
  const now = Date.now();
  clocks.forEach(el => {
    const endTime = parseInt(el.getAttribute("data-withdrawal-end"));
    const diff = endTime - now;
    if (diff <= 0) {
      el.innerHTML = "✓ WITHDRAWAL CLEARED — Milk Safe for Dairy Supply";
      el.style.color = "#15803d";
      el.style.borderColor = "#86efac";
    } else {
      const days = Math.floor(diff / (24 * 3600 * 1000));
      const hours = Math.floor((diff % (24 * 3600 * 1000)) / (3600 * 1000));
      const mins = Math.floor((diff % (3600 * 1000)) / (60 * 1000));
      const secs = Math.floor((diff % (60 * 1000)) / 1000);
      el.innerHTML = `⏱️ ${days}d ${hours}h ${mins}m ${secs}s remaining`;
    }
  });
}
setInterval(updateWithdrawalClocks, 1000);

// RENDER VET CARE DESK QUEUES
function renderVetDesk() {
  const aptContainer = document.getElementById("vetAppointmentsContainer");
  const caseContainer = document.getElementById("vetCasesContainer");
  if (!aptContainer || !caseContainer) return;

  const appointments = getStoredAppointments();
  const cases = getStoredCases();

  // Update badges
  const aptBadge = document.getElementById("aptCountBadge");
  const caseBadge = document.getElementById("caseCountBadge");
  if (aptBadge) aptBadge.textContent = `${appointments.length} Active`;
  if (caseBadge) caseBadge.textContent = `${cases.length} Active`;

  // Render Appointments
  aptContainer.innerHTML = "";
  if (appointments.length === 0) {
    aptContainer.innerHTML = "<p style='font-size:0.85rem; color:#64748b;'>No appointments currently pending.</p>";
  } else {
    appointments.forEach((apt, idx) => {
      const card = document.createElement("div");
      card.className = "desk-card";
      card.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
          <h4 style="font-size:0.95rem; font-weight:700; color:#0f172a;">${apt.animal}</h4>
          <span class="vax-pill ${apt.status === 'Confirmed' ? 'vax-ok' : 'vax-due'}">${apt.status}</span>
        </div>
        <p style="font-size:0.82rem; color:#334155; margin-bottom:4px;">
          <strong>Type:</strong> ${apt.visitType} | <strong>Preferred:</strong> ${apt.date}
        </p>
        <p style="font-size:0.82rem; color:#64748b; margin-bottom:10px;">
          <strong>Farmer Contact:</strong> <a href="tel:${apt.farmerPhone}">${apt.farmerPhone}</a>
        </p>
        <div style="display:flex; gap:6px;">
          <button class="btn btn-primary btn-sm" onclick="confirmAppointment(${idx})" style="flex:1;">
            Confirm Visit
          </button>
          <a href="tel:${apt.farmerPhone}" class="btn btn-outline btn-sm" style="flex:1; text-align:center;">
            Call Farmer
          </a>
        </div>
      `;
      aptContainer.appendChild(card);
    });
  }

  // Render Cases
  caseContainer.innerHTML = "";
  if (cases.length === 0) {
    caseContainer.innerHTML = "<p style='font-size:0.85rem; color:#64748b;'>No referred cases pending review.</p>";
  } else {
    cases.forEach(c => {
      const card = document.createElement("div");
      card.className = "desk-card";
      card.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
          <h4 style="font-size:0.95rem; font-weight:700; color:#0f172a;">${c.animal}</h4>
          <span class="triage-band likely">${c.triageBand}: ${c.triageCondition}</span>
        </div>
        <p style="font-size:0.82rem; color:#64748b; margin-bottom:6px;">
          <strong>Symptoms:</strong> ${Array.isArray(c.symptoms) ? c.symptoms.join(', ') : c.symptoms}
        </p>
        <p style="font-size:0.78rem; color:#94a3b8; margin-bottom:10px;">
          Triage ID: ${c.id} • ${c.date}
        </p>
        <button class="btn btn-primary btn-sm" onclick="openPrescriptionModal('${c.tag || 'MH-24-9812'}', '${c.triageCondition}')" style="width:100%; background:#15803d;">
          Examine &amp; Prescribe Treatment
        </button>
      `;
      caseContainer.appendChild(card);
    });
  }
}

function confirmAppointment(idx) {
  const apts = getStoredAppointments();
  if (apts[idx]) {
    apts[idx].status = "Confirmed";
    try {
      localStorage.setItem("pashu_appointments", JSON.stringify(apts));
    } catch(e) {}
    renderVetDesk();
  updateAuthUI();
    showToast(`Appointment confirmed for ${apts[idx].animal}! SMS alert dispatched.`);
  }
}

// ROLE SWITCHING: Farmer vs Vet
function switchRole(role) {
  const farmerBtn = document.getElementById("roleFarmerBtn");
  const vetBtn = document.getElementById("roleVetBtn");
  if (role === "vet") {
    if (vetBtn) vetBtn.classList.add("active");
    if (farmerBtn) farmerBtn.classList.remove("active");
    const desk = document.getElementById("vet-desk");
    if (desk) desk.scrollIntoView({ behavior: "smooth" });
    showToast("Switched to Government Veterinary Officer Desk");
  } else {
    if (farmerBtn) farmerBtn.classList.add("active");
    if (vetBtn) vetBtn.classList.remove("active");
    const hero = document.getElementById("hero");
    if (hero) hero.scrollIntoView({ behavior: "smooth" });
    showToast("Switched to Livestock Keeper (Farmer) Portal");
  }
}

// FORWARD CASE TO VET CARE DESK
let lastTriageResult = null;
function forwardCaseToVet() {
  if (!lastTriageResult) {
    showToast("Please evaluate symptoms first before forwarding case.");
    return;
  }
  const newCase = {
    id: "CASE-MH-" + Math.floor(1000 + Math.random()*9000),
    animal: "Gauri (Tag: MH-24-9812)",
    tag: "MH-24-9812",
    species: "Cattle (गाय)",
    symptoms: lastTriageResult.symptoms || ["Reported Symptoms"],
    triageBand: "Likely",
    triageCondition: lastTriageResult.condition,
    status: "Referred for Clinical Review",
    date: "Just Now"
  };
  saveCase(newCase);
  showToast(`Case forwarded to Dr. Rameshwar Kute (LDO Sangamner)!`);
  switchRole('vet');
}

// PRESCRIPTION MODAL HANDLERS
function openPrescriptionModal(tag, condition) {
  const modal = document.getElementById("prescribeModal");
  const animalSelect = document.getElementById("rxAnimalTag");
  const condInput = document.getElementById("rxCondition");
  if (animalSelect && tag) animalSelect.value = tag;
  if (condInput && condition) condInput.value = condition;
  if (modal) modal.classList.add("active");
}


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
  playDtmfTone(key);
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
    screen.innerText = "PashuSachet Gram Signal (*992#)\n1. Cattle (गाय)\n2. Buffalo (म्हैस)\n3. Goat / Sheep (शेळी/मेंढी)\n4. Poultry (कुक्कुट)\n0. Exit";
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
    screen.innerText = `Selected: ${ussdState.species}\nSelect Primary Sign:\n1. Blisters/Saliva (तोंडातील फोड/लाळ)\n2. Skin Lumps (त्वचेवर गाठी)\n3. High Fever (तीव्र ताप)\n4. Sudden Mortality (दगावले/मृत्यू)\n0. Back`;
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
    screen.innerText = `Sign: ${ussdState.symptom}\nEnter number of affected animals (संख्या टाका):\n(e.g. 1, 2, 5)`;
    return;
  }

  if (ussdState.step === 2) {
    ussdState.count = parseInt(val) || 1;
    ussdState.step = 3;
    screen.innerText = `Affected: ${ussdState.count}\nConfirm Village Location:\n1. Sangamner (संगमनेर)\n2. Rahata (राहाता)\n3. Shirdi Rural (शिर्डी)\n4. Akole (अकोले)`;
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
    screen.innerText = `SUCCESS! [पशूसचेत]\nReport ID: #${reportId}\nVillage: ${ussdState.village}\nLocal Para-Vet Ganesh Kale notified for beat inspection.\nImmediate safe steps sent via SMS.\nPress 0 to close session.`;
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
    speakMarathiVoice("नमस्कार शेतकरी बंधू, पशूसचेत कॉल सहाय्यता केंद्रात आपले स्वागत आहे. तुमच्या जनावराची लक्षणे सांगा.");
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

const symptomCardMap = {
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
}

// Offline-First Queue Engine
function saveOfflineReport(reportData) {
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


// ==========================================
// PHASE 4: PARA-VET VERIFICATION GATE LOGIC
// ==========================================

let villageSignals = [
  {
    id: "SIG-AHM-9101",
    channel: "USSD",
    species: "Cattle (गाय)",
    symptoms: ["Blisters in mouth / Salivation", "Lameness"],
    affectedCount: 3,
    village: "Sangamner Khurd (संगमनेर खुर्द)",
    farmerName: "Tukaram Shinde",
    phone: "+91 98220 41092",
    status: "UNVERIFIED_SIGNAL",
    t0_time: "18 mins ago",
    vitals: "Pending exam"
  },
  {
    id: "SIG-AHM-9102",
    channel: "VOICE_IVR",
    species: "Goat (शेळी)",
    symptoms: ["High Fever", "Mouth lesions / Ulcers"],
    affectedCount: 5,
    village: "Nimgaon Jali (निमगाव जाळी)",
    farmerName: "Kisan Gaikwad",
    phone: "+91 97631 88402",
    status: "UNVERIFIED_SIGNAL",
    t0_time: "42 mins ago",
    vitals: "Pending exam"
  },
  {
    id: "SIG-AHM-9088",
    channel: "DIRECT_WEB",
    species: "Cattle (गाय)",
    symptoms: ["Skin nodules / Lumps", "High Fever"],
    affectedCount: 2,
    village: "Ashwi (आश्वी)",
    farmerName: "Babanrao Vikhe",
    phone: "+91 94222 19043",
    status: "VERIFIED_SIGNAL",
    t0_time: "3 hours ago",
    verifiedAt: "2.5 hours ago",
    vitals: "Temp 104.2°F"
  }
];

function renderParavetInbox() {
  const container = document.getElementById("paravetSignalsContainer");
  if (!container) return;

  const pending = villageSignals.filter(s => s.status === "UNVERIFIED_SIGNAL");
  const verified = villageSignals.filter(s => s.status === "VERIFIED_SIGNAL");
  const sampleReq = villageSignals.filter(s => s.status === "SAMPLE_REQUESTED");

  const pendingCountEl = document.getElementById("pendingSignalCount");
  const verifiedCountEl = document.getElementById("verifiedSignalCount");
  const sampleCountEl = document.getElementById("sampleSignalCount");

  if (pendingCountEl) pendingCountEl.textContent = `${pending.length} Active`;
  if (verifiedCountEl) verifiedCountEl.textContent = `${verified.length + 5} Confirmed`;
  if (sampleCountEl) sampleCountEl.textContent = `${sampleReq.length + 2} Kits`;

  if (pending.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; background: #ffffff; border: 2px dashed var(--border-medium); border-radius: var(--radius-lg); padding: 40px; text-align: center; color: var(--ink-secondary);">
        <div style="width: 44px; height: 44px; border-radius: 50%; background: var(--status-success-light); color: var(--status-success); display: flex; align-items: center; justify-content: center; margin: 0 auto 12px auto;">
          <span data-icon="check-circle-2" data-size="24"></span>
        </div>
        <h4 style="color: var(--ink-primary); margin: 0 0 4px; font-size: 16px;">बीटमधील सर्व अहवाल पडताळले आहेत (All Verified)</h4>
        <p style="font-size: 13px; margin: 0;">सध्या आपल्या बीटमध्ये कोणतीही प्रलंबित शेतकरी तक्रार शिल्लक नाही.</p>
      </div>
    `;
    if (typeof renderIcons === 'function') renderIcons();
    return;
  }

  container.innerHTML = pending.map(sig => `
    <div class="app-card" style="border: 1.5px solid #cbd5e1; border-top: 4px solid #0284c7; box-shadow: 0 4px 10px rgba(0,0,0,0.05); padding: 18px; margin: 0;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
        <div>
          <span style="font-size: 0.72rem; font-weight: 800; background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
            ${sig.channel} Signal
          </span>
          <h4 style="margin: 4px 0 0; font-size: 1.05rem; color: #0f172a; font-weight: 800;">
            #${sig.id}
          </h4>
        </div>
        <div style="text-align: right;">
          <span style="font-size: 0.75rem; color: #d97706; font-weight: 700;">⏱️ T0: ${sig.t0_time}</span>
          <div style="font-size: 0.78rem; color: #64748b;">${sig.village}</div>
        </div>
      </div>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 12px; margin-bottom: 12px; font-size: 0.84rem;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
          <strong style="color: #0f172a;">${sig.species}</strong>
          <span style="color: #b91c1c; font-weight: 700;">${sig.affectedCount} Affected</span>
        </div>
        <div style="color: #334155; margin-bottom: 4px;">
          <strong>Reported Signs:</strong> ${sig.symptoms.join(", ")}
        </div>
        <div style="color: #64748b; font-size: 0.78rem;">
          <strong>Farmer:</strong> ${sig.farmerName} (${sig.phone})
        </div>
        <div style="color: #0369a1; font-size: 0.78rem; margin-top: 4px;">
          <strong>Vitals:</strong> ${sig.vitals}
        </div>
      </div>

      <!-- The 4 Ultra-Fast Verification Actions (< 30 seconds) -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
        <button type="button" class="btn btn-sm" onclick="confirmSignal('${sig.id}')" style="background: #166534; color: #ffffff; font-weight: 700;">
          ✓ खात्री झाली (Confirm)
        </button>
        <button type="button" class="btn btn-sm btn-outline" onclick="dismissSignal('${sig.id}')" style="color: #64748b; border-color: #cbd5e1; font-weight: 600;">
          ✗ किरकोळ (Dismiss)
        </button>
        <button type="button" class="btn btn-sm btn-outline" onclick="promptSignalVitals('${sig.id}')" style="color: #0369a1; border-color: #7dd3fc; font-weight: 600;">
          🌡️ Vitals (तापमान)
        </button>
        <button type="button" class="btn btn-sm btn-outline" onclick="requestSignalSample('${sig.id}')" style="color: #7c3aed; border-color: #c4b5fd; font-weight: 600;">
          🧪 Sample Kit
        </button>
      </div>
    </div>
  `).join("");
}

function confirmSignal(id) {
  const sig = villageSignals.find(s => s.id === id);
  if (sig) {
    sig.status = "VERIFIED_SIGNAL";
    sig.verifiedAt = "Just now";
    sig.verifiedBy = "Ganesh Kale (PV-AHM-9104)";
    showToast(`Signal #${id} verified! Propagated to District Surveillance Board.`);
    renderParavetInbox();
    renderVillageSignalBoard();
  }
}

function dismissSignal(id) {
  const sig = villageSignals.find(s => s.id === id);
  if (sig) {
    sig.status = "DISMISSED_BENIGN";
    sig.dismissedAt = "Just now";
    sig.dismissedBy = "Ganesh Kale (PV-AHM-9104)";
    showToast(`Signal #${id} dismissed as benign. Not sent to Officer Board.`);
    renderParavetInbox();
  }
}

function promptSignalVitals(id) {
  const sig = villageSignals.find(s => s.id === id);
  if (!sig) return;
  const temp = prompt("Enter Measured Rectal Temperature (°F):", "104.2");
  if (temp) {
    sig.vitals = `Temp: ${temp}°F (Measured by PV-AHM-9104)`;
    showToast(`Vitals recorded for #${id}: ${temp}°F`);
    renderParavetInbox();
  }
}

function requestSignalSample(id) {
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
    timestamp: new Date().toISOString()
  };
  showToast(`Sample kit request #${sig.sampleRecord.sampleId} initiated for RDDL Pune!`);
  renderParavetInbox();
}


// Fast-forward / Time travel simulation for Milk Withdrawal transition (TC-5.5)
function simulateFastForwardWithdrawal(tag = "MH-24-9812") {
  const animals = getStoredAnimals();
  const animal = animals.find(a => a.tag === tag);
  if (animal && animal.prescription) {
    // Offset prescribedAt to 10 days ago so treatment + withdrawal buffer has elapsed
    animal.prescription.prescribedAt = Date.now() - (10 * 24 * 3600 * 1000);
    try {
      localStorage.setItem("pashu_animals", JSON.stringify(animals));
    } catch(e) {}
    renderAnimals();
    updateWithdrawalClocks();
    showToast(`Withdrawal period for ${tag} fast-forwarded to EXPIRED (Milk Safe for Dairy)!`);
  }
}


// ==========================================
// PHASE 6: CLOSED-LOOP DIAGNOSTIC TRACKER
// ==========================================

const SAMPLE_STAGES = [
  { key: "SAMPLE_NEEDED", labelEn: "Sample Needed", labelMr: "नमुना आवश्यक" },
  { key: "SAMPLE_COLLECTED", labelEn: "Sample Collected", labelMr: "नमुना संकलित" },
  { key: "IN_TRANSIT_LAB", labelEn: "In-Transit to RDDL", labelMr: "पुणे लॅबकडे रवाना" },
  { key: "LAB_TESTING", labelEn: "Testing (RT-PCR/ELISA)", labelMr: "तपासणी सुरू" },
  { key: "RESULTED_AND_ACTION_TAKEN", labelEn: "Resulted & Closed", labelMr: "अहवाल व कृती पूर्ण" }
];

let diagnosticSamples = [
  {
    sampleId: "SMP-PUN-8104",
    animalTag: "MH-24-9812",
    animalName: "Gauri (गाय)",
    farmerName: "Ganesh Patil",
    village: "Sangamner Khurd (संगमनेर)",
    sampleType: "Vesicular Swab & Serum in VTM",
    diseaseSuspected: "Lumpy Skin Disease (LSD)",
    currentStageIndex: 2, // IN_TRANSIT_LAB
    coldChainTracking: "Maintained 2°C - 8°C in Ice Gel Shipper #CS-441",
    destinationLab: "Regional Disease Diagnostic Laboratory (RDDL Pune)",
    attendingVet: "Dr. Rameshwar Kute (MSVC/2012/03194)",
    paraVet: "Ganesh Kale (PV-AHM-9104)",
    labResult: null,
    closureAction: null,
    updatedAt: "45 mins ago"
  },
  {
    sampleId: "SMP-PUN-7922",
    animalTag: "MH-12-4401",
    animalName: "Raja (म्हैस)",
    farmerName: "Babanrao Vikhe",
    village: "Nimgaon Jali",
    sampleType: "Milk Sample for Culture & Sensitivity",
    diseaseSuspected: "Clinical Mastitis",
    currentStageIndex: 4, // RESULTED_AND_ACTION_TAKEN
    coldChainTracking: "Cold Chain Verified (4.1°C at receipt)",
    destinationLab: "District Veterinary Polyclinic Lab, Ahmednagar",
    attendingVet: "Dr. Rameshwar Kute",
    paraVet: "Ganesh Kale",
    labResult: "Staphylococcus aureus Isolated (Cephalosporin Sensitive)",
    closureAction: "Intramammary Ceftiofur completed. 72hr withdrawal countdown initiated.",
    updatedAt: "Today, 11:30 AM"
  }
];

function renderSampleTracker() {
  const container = document.getElementById("sampleCardsContainer");
  if (!container) return;

  container.innerHTML = diagnosticSamples.map(sample => {
    const stage = SAMPLE_STAGES[sample.currentStageIndex];
    const isClosed = sample.currentStageIndex === 4;

    const stepperHtml = SAMPLE_STAGES.map((s, idx) => {
      let stateClass = "";
      if (idx < sample.currentStageIndex) stateClass = "completed";
      else if (idx === sample.currentStageIndex) stateClass = "active";

      const icon = idx < sample.currentStageIndex ? "✓" : (idx + 1);
      return `
        <div class="sample-step ${stateClass}">
          <div class="step-circle">${icon}</div>
          <div class="step-label">${s.labelMr}<br><span style="font-size:0.7rem; color:#94a3b8;">${s.labelEn}</span></div>
        </div>
      `;
    }).join("");

    let closureBoxHtml = "";
    if (isClosed) {
      closureBoxHtml = `
        <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 12px 16px; margin-top: 14px;">
          <div style="font-weight: 800; color: #166534; font-size: 0.9rem; margin-bottom: 4px;">
            ✅ प्रयोगशाळा अहवाल व बंदिस्त कृती (Lab Result & Biosecurity Closure)
          </div>
          <div style="font-size: 0.85rem; color: #15803d; line-height: 1.5;">
            <strong>निदान अहवाल:</strong> ${sample.labResult}<br>
            <strong>अंतिम कृती:</strong> ${sample.closureAction}
          </div>
          <div style="margin-top: 8px; padding-top: 8px; border-top: 1px dashed #86efac; font-size: 0.8rem; color: #166534;">
            📲 <strong>Farmer Closure SMS Sent:</strong> "शेतकरी बंधू ${sample.farmerName}, आपल्या ${sample.animalName} (टॅग: ${sample.animalTag}) च्या नमुन्याचा अहवाल प्राप्त झाला असून आवश्यक वैद्यकीय कृती पूर्ण केली आहे. - पशूसचेत / DAHD महाराष्ट्र"
          </div>
        </div>
      `;
    }

    return `
      <div class="sample-tracker-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 0.78rem; font-weight: 800; background: #ede9fe; color: #6d28d9; padding: 3px 8px; border-radius: 4px;">
                RDDL BARCODE: #${sample.sampleId}
              </span>
              <span class="coldchain-badge">
                🧊 ${sample.coldChainTracking}
              </span>
            </div>
            <h3 style="margin: 6px 0 2px; font-size: 1.2rem; color: #0f172a; font-weight: 800;">
              ${sample.animalName} • Tag: ${sample.animalTag}
            </h3>
            <div style="font-size: 0.82rem; color: #64748b;">
              Farmer: <strong>${sample.farmerName}</strong> (${sample.village}) • Lab: <strong>${sample.destinationLab}</strong>
            </div>
          </div>

          <div style="text-align: right;">
            <span style="font-size: 0.85rem; font-weight: 800; color: ${isClosed ? '#15803d' : '#7c3aed'}; background: ${isClosed ? '#f0fdf4' : '#ede9fe'}; padding: 4px 12px; border-radius: 6px;">
              ${stage.labelMr} (${stage.labelEn})
            </span>
            <div style="font-size: 0.78rem; color: #94a3b8; margin-top: 4px;">
              Updated: ${sample.updatedAt}
            </div>
          </div>
        </div>

        <!-- 5-Stage Stepper -->
        <div class="sample-stepper">
          ${stepperHtml}
        </div>

        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; font-size: 0.82rem;">
          <div>
            <strong>Sample Specimen:</strong> ${sample.sampleType} • <strong>Target:</strong> ${sample.diseaseSuspected}
          </div>
          <div>
            <strong>Attending:</strong> ${sample.attendingVet} &amp; ${sample.paraVet}
          </div>
        </div>

        ${closureBoxHtml}

        <!-- Next Stage Advance Action -->
        <div style="display: flex; justify-content: flex-end; margin-top: 14px; gap: 8px;">
          ${!isClosed ? `
            <button type="button" class="btn btn-sm" onclick="advanceSampleStage('${sample.sampleId}')" style="background: #7c3aed; color: #ffffff; font-weight: 700;">
              ⏩ Advance Next Stage (पुढील टप्पा सिम्युलेट करा)
            </button>
          ` : `
            <span style="font-size: 0.82rem; font-weight: 700; color: #15803d; display: flex; align-items: center; gap: 4px;">
              ✓ Lifecycle Closed &amp; Archived in Bharat Pashudhan
            </span>
          `}
        </div>
      </div>
    `;
  }).join("");
}

function advanceSampleStage(sampleId) {
  const sample = diagnosticSamples.find(s => s.sampleId === sampleId);
  if (!sample) return;

  if (sample.currentStageIndex < SAMPLE_STAGES.length - 1) {
    sample.currentStageIndex += 1;
    sample.updatedAt = "Just now";

    if (sample.currentStageIndex === 4) {
      // Reached RESULTED_AND_ACTION_TAKEN
      sample.labResult = "RT-PCR Confirmed Positive: Capripoxvirus (Lumpy Skin Disease). Ring-vaccination deployed.";
      sample.closureAction = "Local 5km ring-vaccination completed. Farmer biosecurity isolation confirmed.";
      showToast(`Sample #${sampleId} resulted & closed! Marathi closure SMS auto-dispatched to ${sample.farmerName}.`);
    } else {
      const nextStage = SAMPLE_STAGES[sample.currentStageIndex];
      showToast(`Sample #${sampleId} transitioned to: ${nextStage.labelMr} (${nextStage.labelEn})`);
    }

    renderSampleTracker();
  }
}


// ==========================================
// PHASE 7: VILLAGE SIGNAL BOARD & DECISION QUEUE
// ==========================================

const RAW_VILLAGE_REPORTS = [
  { village: "Nimgaon Jali", taluka: "Sangamner", count: 4, disease: "FMD Blisters", verified: true, isMortality: false },
  { village: "Ashwi", taluka: "Sangamner", count: 3, disease: "LSD Nodules", verified: true, isMortality: false },
  { village: "Chandnapuri", taluka: "Sangamner", count: 2, disease: "Fever & Drop in Milk", verified: true, isMortality: false },
  { village: "Talegaon", taluka: "Sangamner", count: 1, disease: "Lameness", verified: true, isMortality: false },
  { village: "Kotul", taluka: "Akole", count: 2, disease: "Sudden Mortality", verified: true, isMortality: true }
];

let officerDecisions = [
  {
    id: "DEC-001",
    type: "RING_VAX",
    title: "Ring-Vaccination Mobilization: Sangamner Cluster",
    details: "4 verified FMD cases in Nimgaon Jali. Recommend deploying 1,000 FMD vaccine doses within 5km radius.",
    priority: "HIGH_URGENCY",
    actionLabel: "Approve Ring-Vaccination Team",
    status: "PENDING"
  },
  {
    id: "DEC-002",
    type: "MORTALITY_BIOSECURITY",
    title: "High-Mortality Post-Loss Investigation: Kotul Beat",
    details: "2 bovine sudden deaths reported in Kotul. Risk of Anthrax spore dissemination. Biosecurity cordoning required.",
    priority: "CRITICAL_ZOONOTIC",
    actionLabel: "Dispatch MVU & Sanitation Unit",
    status: "PENDING"
  },
  {
    id: "DEC-003",
    type: "LAB_APPROVAL",
    title: "Diagnostic Batch Submission to ICAR-NIVEDI",
    details: "Sample Batch SMP-PUN-8104 confirmed LSD by RDDL Pune. Sign off national NADRES upload.",
    priority: "STANDARD",
    actionLabel: "Sign & Forward to ICAR-NIVEDI",
    status: "PENDING"
  }
];

function renderVillageSignalBoard() {
  const grid = document.getElementById("villageSignalsGrid");
  if (!grid) return;

  // Implement k-Anonymity Privacy Rule (< 3 Signals suppressed to Block Centroid)
  const aggregatedClusters = [];
  const lowCountTalukaGroups = {};

  RAW_VILLAGE_REPORTS.forEach(report => {
    if (report.count >= 3) {
      aggregatedClusters.push({
        displayName: `${report.village} (${report.taluka} Taluka)`,
        count: report.count,
        disease: report.disease,
        isSurge: report.count >= 4,
        isAnonymized: false
      });
    } else {
      if (!lowCountTalukaGroups[report.taluka]) {
        lowCountTalukaGroups[report.taluka] = { count: 0, diseases: [] };
      }
      lowCountTalukaGroups[report.taluka].count += report.count;
      lowCountTalukaGroups[report.taluka].diseases.push(report.disease);
    }
  });

  // Add k-anonymized taluka centroid clusters
  for (const taluka in lowCountTalukaGroups) {
    const grp = lowCountTalukaGroups[taluka];
    aggregatedClusters.push({
      displayName: `${taluka} Taluka Rural Cluster (Centroid Pin)`,
      count: grp.count,
      disease: grp.diseases.join(" & "),
      isSurge: false,
      isAnonymized: true,
      note: "Anonymized for farm privacy (k < 3 protection)"
    });
  }

  grid.innerHTML = aggregatedClusters.map(cluster => `
    <div class="village-signal-card" style="border-top: 3px solid ${cluster.isSurge ? '#dc2626' : (cluster.isAnonymized ? '#0f766e' : '#2563eb')};">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <h4 style="margin: 0; font-size: 1rem; color: #0f172a; font-weight: 700;">
          ${cluster.displayName}
        </h4>
        <span style="font-size: 0.85rem; font-weight: 800; color: ${cluster.isSurge ? '#dc2626' : '#0f766e'}; background: ${cluster.isSurge ? '#fee2e2' : '#ccfbf1'}; padding: 2px 8px; border-radius: 4px;">
          ${cluster.count} Signals
        </span>
      </div>

      <div style="font-size: 0.85rem; color: #475569; margin-bottom: 8px;">
        <strong>Reported Disease Signal:</strong> ${cluster.disease}
      </div>

      ${cluster.isSurge ? `
        <div style="margin-top: 6px;">
          <span class="surge-alert-pill">⚡ SURGE_ALERT: Active Cluster (>3 signals/7 days)</span>
          <div style="font-size: 0.78rem; color: #b91c1c; margin-top: 4px; font-weight: 600;">
            Immediate 5km ring-vaccination recommended.
          </div>
        </div>
      ` : ''}

      ${cluster.isAnonymized ? `
        <div style="font-size: 0.75rem; color: #0f766e; font-weight: 600; margin-top: 6px; background: #f0fdfa; padding: 4px 8px; border-radius: 4px;">
          🔒 ${cluster.note}
        </div>
      ` : ''}
    </div>
  `).join("");
}

function renderOfficerDecisionQueue() {
  const container = document.getElementById("officerDecisionQueue");
  if (!container) return;

  container.innerHTML = officerDecisions.map(dec => `
    <div class="decision-card" style="border-left-color: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical)' : 'var(--accent-turmeric)'};">
      <div style="flex: 1;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
          <strong style="color: var(--ink-primary); font-size: 15px;">${dec.title}</strong>
          <span class="badge-pill" style="background: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical-light)' : 'var(--accent-turmeric-light)'}; color: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical)' : '#92400e'};">
            ${dec.priority}
          </span>
        </div>
        <p style="font-size: 13px; color: var(--ink-secondary); margin: 0; line-height: 1.5;">
          ${dec.details}
        </p>
      </div>

      <div style="flex-shrink: 0;">
        ${dec.status === 'PENDING' ? `
          <button type="button" class="btn btn-sm btn-primary" onclick="resolveOfficerDecision('${dec.id}')" style="white-space: nowrap;">
            ✓ ${dec.actionLabel}
          </button>
        ` : `
          <span class="badge-pill" style="background: var(--status-success-light); color: var(--status-success);">
            ✓ मंजूर (Action Authorized)
          </span>
        `}
      </div>
    </div>
  `).join("");
}

function resolveOfficerDecision(decId) {
  const dec = officerDecisions.find(d => d.id === decId);
  if (!dec) return;
  dec.status = "RESOLVED";
  showToast(`Authorized: ${dec.actionLabel}! Field units notified.`);
  renderOfficerDecisionQueue();
}


// ==========================================
// PHASE 8: NDLM, NADRES, VISION & TELEMETRY
// ==========================================

// (Unified supercharged simulateVisionDetection active below)

// Bharat Pashudhan (NDLM) 12-Digit Tag Lookup
function lookupNdlmTag() {
  const input = document.getElementById("ndlmTagInput");
  const resultBox = document.getElementById("ndlmResultBox");
  if (!input || !resultBox) return;

  const tag = input.value.trim();
  if (tag.length < 10) {
    alert("Please enter a valid 10-12 digit ear tag number.");
    return;
  }

  resultBox.style.display = "block";
  resultBox.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px;">
      <div>
        <strong style="color: #0f172a; font-size: 0.95rem;">NDLM PASSPORT VERIFIED: Tag #${tag}</strong>
        <div style="font-size: 0.78rem; color: #64748b;">INAPH Registry Timestamp: 14-Aug-2023 • Unique UIDAI UID Linked</div>
      </div>
      <span style="background: #dcfce7; color: #166534; font-weight: 800; font-size: 0.75rem; padding: 2px 8px; border-radius: 4px;">
        ✓ ACTIVE REGISTRATION
      </span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 8px; font-size: 0.8rem; color: #334155;">
      <div><strong>Owner:</strong> Ganesh R. Patil (Sangamner)</div>
      <div><strong>Species & Breed:</strong> Cattle (Gir Crossbred)</div>
      <div><strong>Age / Sex:</strong> 3.5 Yrs / Female (Lactating)</div>
      <div><strong>Last FMD Vaccine:</strong> 18-Jan-2026 (Batch: FMD-MH-881)</div>
      <div><strong>Last Brucellosis S19:</strong> Vaccinated (Calfhood)</div>
      <div><strong>Assigned Dispensary:</strong> CVD Sangamner (Dr. R. Kute)</div>
    </div>
  `;
  showToast(`Tag #${tag} verified with Bharat Pashudhan (NDLM) registry!`);
}

// ICAR-NIVEDI NADRES V2 Data Pipeline Export
function exportNadresBatch() {
  const box = document.getElementById("nadresPayloadBox");
  if (!box) return;

  const nadresPayload = {
    metadata: {
      pipelineVersion: "NADRES-V2-EPI-PIPELINE",
      reportingState: "Maharashtra (27)",
      reportingDistrict: "Ahmednagar (501)",
      reportingEpiWeek: "2026-W44",
      dpdpCompliance: "STRICT_DE_IDENTIFICATION_APPLIED",
      exportTimestamp: new Date().toISOString()
    },
    aggregatedSurveillanceData: [
      {
        villageCentroidHash: "geohash_te42q",
        taluka: "Sangamner",
        speciesCode: "BOV_CATTLE",
        verifiedDiseaseName: "Foot and Mouth Disease (FMD)",
        icd11Code: "1E51",
        verifiedCases: 4,
        mortalityCount: 0,
        clusterRadiusKm: 3.2,
        verificationAuthority: "MSVC/2012/03194"
      },
      {
        villageCentroidHash: "geohash_te48z",
        taluka: "Sangamner",
        speciesCode: "BOV_CATTLE",
        verifiedDiseaseName: "Lumpy Skin Disease (LSD)",
        icd11Code: "1E40",
        verifiedCases: 3,
        mortalityCount: 0,
        clusterRadiusKm: 2.1,
        verificationAuthority: "MSVC/2012/03194"
      },
      {
        villageCentroidHash: "geohash_te39m",
        taluka: "Akole",
        speciesCode: "BOV_BUFFALO",
        verifiedDiseaseName: "Suspected Enterotoxaemia / Sudden Death",
        icd11Code: "1E12",
        verifiedCases: 2,
        mortalityCount: 2,
        clusterRadiusKm: 1.5,
        verificationAuthority: "MSVC/2012/03194"
      }
    ]
  };

  box.style.display = "block";
  box.textContent = JSON.stringify(nadresPayload, null, 2);
  showToast("NADRES V2 de-identified surveillance batch generated successfully!");
}


// ==============================================================
// PRODUCTION SUPERCHARGES: DTMF AUDIO, MARATHI VOICE & CANVAS HUD
// ==============================================================

// 1. Dual-Tone Multi-Frequency (DTMF) Sound Synthesizer
const DTMF_FREQS = {
  "1": [697, 1209], "2": [697, 1336], "3": [697, 1477],
  "4": [770, 1209], "5": [770, 1336], "6": [770, 1477],
  "7": [852, 1209], "8": [852, 1336], "9": [852, 1477],
  "*": [941, 1209], "0": [941, 1336], "#": [941, 1477]
};

function playDtmfTone(key) {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();
    const freqs = DTMF_FREQS[key] || [440, 880];
    const osc1 = ctx.createOscillator();
    const osc2 = ctx.createOscillator();
    const gain = ctx.createGain();

    osc1.type = "sine";
    osc2.type = "sine";
    osc1.frequency.value = freqs[0];
    osc2.frequency.value = freqs[1];

    gain.gain.setValueAtTime(0.12, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.14);

    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(ctx.destination);

    osc1.start();
    osc2.start();
    osc1.stop(ctx.currentTime + 0.14);
    osc2.stop(ctx.currentTime + 0.14);
  } catch(e) {
    // AudioContext blocked or not allowed; silent fail
  }
}

// 2. Browser Marathi Speech Synthesis (Spoken Spoken Prompts)
function speakMarathiVoice(text) {
  try {
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = "mr-IN";
      utterance.rate = 0.92;
      const voices = window.speechSynthesis.getVoices();
      const mrVoice = voices.find(v => v.lang.includes("mr") || v.lang.includes("hi"));
      if (mrVoice) utterance.voice = mrVoice;
      window.speechSynthesis.speak(utterance);
    }
  } catch(e) {}
}

// 3. Web Speech Recognition for Live Marathi/Hindi Voice Input
let voiceRecognitionActive = false;
let speechRecognizer = null;

function toggleMarathiVoiceRecognition() {
  const btn = document.getElementById("marathiVoiceBtn");
  const box = document.getElementById("voiceTranscriptBox");
  const textEl = document.getElementById("voiceTranscriptText");
  const labelEl = document.getElementById("voiceStatusLabel");

  const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRec) {
    alert("Web Speech Recognition API is not supported in this browser. Please use Chrome/Edge or type symptoms.");
    return;
  }

  if (voiceRecognitionActive && speechRecognizer) {
    speechRecognizer.stop();
    voiceRecognitionActive = false;
    if (btn) btn.innerHTML = "🎙️ Speak Symptoms in Marathi (माईकवर बोला)";
    if (labelEl) labelEl.textContent = "माईक बंद आहे (Microphone Idle).";
    return;
  }

  try {
    speechRecognizer = new SpeechRec();
    speechRecognizer.lang = "mr-IN";
    speechRecognizer.continuous = true;
    speechRecognizer.interimResults = true;

    speechRecognizer.onstart = () => {
      voiceRecognitionActive = true;
      if (box) box.style.display = "block";
      if (btn) btn.innerHTML = "⏹️ Stop Listening (बोलणे पूर्ण झाले)";
      if (labelEl) labelEl.textContent = "ऐकत आहे (Listening)... मराठीत लक्षणे बोला (उदा. 'गायीला ताप आहे आणि त्वचेवर गाठी आहेत'):";
      showToast("Microphone active! Speak observed symptoms in Marathi or Hindi.");
    };

    speechRecognizer.onresult = (event) => {
      let transcript = "";
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        transcript += event.results[i][0].transcript;
      }
      if (textEl) textEl.textContent = `“${transcript}”`;
      parseSpokenSymptomKeywords(transcript.toLowerCase());
    };

    speechRecognizer.onerror = (e) => {
      console.warn("Speech recognition error:", e);
      if (labelEl) labelEl.textContent = "कृपया पुन्हा बोला किंवा टाईप करा.";
    };

    speechRecognizer.onend = () => {
      voiceRecognitionActive = false;
      if (btn) btn.innerHTML = "🎙️ Speak Symptoms in Marathi (माईकवर बोला)";
    };

    speechRecognizer.start();
  } catch(err) {
    console.error("Speech init error:", err);
  }
}

function parseSpokenSymptomKeywords(text) {
  // Automatically correlate Marathi spoken words with checkboxes
  if (text.includes("ताप") || text.includes("fever") || text.includes("गरम")) {
    toggleSymptomCheckbox("fever", true);
  }
  if (text.includes("गाठी") || text.includes("लंपी") || text.includes("nodule") || text.includes("lump")) {
    toggleSymptomCheckbox("skin_nodules", true);
  }
  if (text.includes("फोड") || text.includes("लाळ") || text.includes("blister") || text.includes("ulcer") || text.includes("तोंड")) {
    toggleSymptomCheckbox("mouth_lesions", true);
  }
  if (text.includes("खुर") || text.includes("लंगड") || text.includes("lame")) {
    toggleSymptomCheckbox("lameness", true);
  }
  if (text.includes("कास") || text.includes("स्तन") || text.includes("दूध कमी") || text.includes("mastitis")) {
    toggleSymptomCheckbox("udder_swelling", true);
    toggleSymptomCheckbox("milk_drop", true);
  }
  if (text.includes("खोकला") || text.includes("श्वास") || text.includes("cough")) {
    toggleSymptomCheckbox("cough", true);
  }
  if (text.includes("दगावले") || text.includes("मृत्यू") || text.includes("dead") || text.includes("मरण")) {
    const mortCheck = document.getElementById("isMortalityCheck");
    if (mortCheck && !mortCheck.checked) {
      mortCheck.checked = true;
      toggleMortalityFields(true);
    }
  }
}

function toggleSymptomCheckbox(val, state) {
  const cb = document.querySelector(`input[name="symptom"][value="${val}"]`);
  if (cb && cb.checked !== state) {
    cb.checked = state;
    if (typeof Event !== 'undefined') {
      try { cb.dispatchEvent(new Event("change")); } catch(e) {}
    }
  }
}

// 4. HTML5 Canvas AI Vision Inspection HUD & Lesion Bounding Boxes
// (Unified supercharged drawLesionOnCanvas active below)


// Upload Custom Farm Photo Handler
function handleLesionUpload(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = (e) => {
    const img = new Image();
    img.onload = () => {
      drawLesionOnCanvas("lsd", img);
      const box = document.getElementById("visionOutputBox");
      const content = document.getElementById("visionResultContent");
      if (box && content) {
        box.style.display = "block";
        content.innerHTML = `
          <strong>🔍 Custom Upload Analysis:</strong> <span style="color:#b91c1c; font-weight:800;">Circumscribed Cutaneous Lesions Identified</span><br>
          File: <em>${file.name}</em> (${Math.round(file.size/1024)} KB) • Processed via In-Browser Edge Classifier.<br>
          <span style="color:#15803d; font-weight:700;">✓ Correlated with 'Skin Nodules / Lumps' & 'High Fever'.</span>
        `;
      }
      toggleSymptomCheckbox("skin_nodules", true);
      toggleSymptomCheckbox("fever", true);
      showToast(`Custom photo analyzed! Lesion detected on ${file.name}.`);
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

// 5. Interactive GIS Map Containment Zone Toggle & Pin Inspector
let ringVaxActive = false;
function toggleRingVaxRadius() {
  ringVaxActive = !ringVaxActive;
  const buffers = document.getElementById("ringVaxBuffers");
  const btn = document.getElementById("toggleRingVaxBtn");
  if (buffers) buffers.style.display = ringVaxActive ? "inline" : "none";
  if (btn) {
    btn.style.background = ringVaxActive ? "#ef4444" : "transparent";
    btn.style.color = ringVaxActive ? "#ffffff" : "#f87171";
    btn.textContent = ringVaxActive ? "✓ 5km Containment Zone Active" : "🎯 Toggle 5km Ring-Vaccination Buffer";
  }
  showToast(ringVaxActive ? "5km Ring-Vaccination Containment Buffer activated around Nimgaon Jali!" : "Ring-Vaccination buffer hidden.");
}

function inspectMapPin(village, count, disease, clusterStatus) {
  const inspector = document.getElementById("mapPinInspector");
  const details = document.getElementById("mapPinDetails");
  if (!inspector || !details) return;

  inspector.style.display = "block";
  let statusBadge = clusterStatus === "SURGE_CLUSTER" ?
    '<span style="background:#dc2626; color:#ffffff; padding:2px 6px; border-radius:4px; font-weight:800;">SURGE CLUSTER</span>' :
    (clusterStatus === "K_ANONYMIZED" ?
      '<span style="background:#0f766e; color:#ffffff; padding:2px 6px; border-radius:4px; font-weight:800;">k<3 ANONYMIZED CENTROID</span>' :
      '<span style="background:#b91c1c; color:#ffffff; padding:2px 6px; border-radius:4px; font-weight:800;">BIOSECURITY CORDON</span>');

  details.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <strong>📍 ${village}</strong>
      ${statusBadge}
    </div>
    <div style="color:#94a3b8; margin-top:4px;">
      Verified Cases: <strong style="color:#ffffff;">${count}</strong> | Disease: <strong style="color:#fde68a;">${disease}</strong> | LDO Jurisdiction: <strong>CVD Sangamner</strong>
    </div>
  `;
}

// 6. Digital Pashu Aadhar Smart Card Modal Handlers
function openPashuAadharModal(tag) {
  const modal = document.getElementById("pashuAadharCardModal");
  if (modal) modal.classList.add("active");
}

function closePashuAadharModal() {
  const modal = document.getElementById("pashuAadharCardModal");
  if (modal) modal.classList.remove("active");
}


// ==========================================================================
// SUPERCHARGED EXTENSIONS: PERSONAS, VISION HUD, SEIR, MVU & WHATSAPP
// ==========================================================================

// 1. Multi-Role Live Persona Switcher
let currentPersona = 'farmer';


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
      if (typeof window !== 'undefined' && typeof window.scrollTo === 'function') { window.scrollTo({ top: 0, behavior: 'smooth' }); }
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
  renderSidebarNav(role);

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
}

// 2. Multi-Disease Computer Vision Sentinel Supercharge
let thermalModeActive = false;
let gradCamActive = false;
let currentDetectedCondition = 'lsd';
let liveCameraStream = null;

const visionDiseaseSpecs = {
  lsd: {
    name: 'Lumpy Skin Disease (Capripoxvirus)',
    band: 'Likely',
    score: 89.4,
    thermal: 39.8,
    urgency: 'RED_HIGH_CONTAGION',
    species: 'cattle',
    symptoms: ['skin_nodules', 'fever'],
    diffs: ['Pseudo-LSD (BHV-2)', 'Dermatophilosis', 'Insect Bites'],
    biomarkers: ['Circumscribed Cutaneous Nodules (2-5cm firm dermal lumps)', 'Prescapular lymphadenopathy'],
    actionMr: 'बाधित जनावराला तात्काळ कळपापासून वेगळे करा (विलगीकरण). डास-माशा प्रतिबंधक औषध फवारा.',
    actionEn: 'Immediately isolate affected animal. Apply insect repellent. Call 1962.'
  },
  fmd: {
    name: 'Foot & Mouth Disease (Aphthovirus O/A/Asia-1)',
    band: 'Likely',
    score: 92.1,
    thermal: 40.5,
    urgency: 'RED_HIGH_CONTAGION',
    species: 'cattle',
    symptoms: ['mouth_lesions', 'salivation', 'fever', 'swelling_legs'],
    diffs: ['Vesicular Stomatitis', 'Bovine Viral Diarrhea (BVD)', 'Malignant Catarrhal Fever'],
    biomarkers: ['Epithelial Vesicles & Ruptured mucosal ulcers', 'Interdigital coronary erythema'],
    actionMr: 'तोंडातील फोडांवर पोटॅशियम परमँगनेट (KMnO4) हलके लावा. खूर कोरडी ठेवा. दूध उकळून नष्ट करा.',
    actionEn: 'Wash oral lesions with 0.1% KMnO4 solution. Disinfect hooves. Withhold milk.'
  },
  mastitis: {
    name: 'Acute Clinical Mastitis (Staph/Streptococcus)',
    band: 'Likely',
    score: 94.2,
    thermal: 41.2,
    urgency: 'AMBER_PARA_VET_VISIT',
    species: 'cattle',
    symptoms: ['drop_milk', 'fever'],
    diffs: ['Subclinical Mastitis Flare', 'Udder Hematoma', 'Teat Papilloma'],
    biomarkers: ['Severe asymmetrical udder hyperthermia', 'Fibrin clot strippings', 'Pain on palpation'],
    actionMr: 'वारंवार कास पूर्णपणे रिकामी करा (Frequent Stripping). थंड पाण्याचा शेक द्या. त्वरित डॉक्टरांना बोलवा.',
    actionEn: 'Perform frequent complete milk stripping. Apply cold compress. Administer intramammary therapy.'
  },
  bq: {
    name: 'Black Quarter (Clostridium chauvoei)',
    band: 'Possible',
    score: 78.5,
    thermal: 40.2,
    urgency: 'RED_EMERGENCY',
    species: 'cattle',
    symptoms: ['swelling_legs', 'fever'],
    diffs: ['Malignant Edema', 'Acute Anthrax', 'Snake Bite'],
    biomarkers: ['Emphysematous crepitating muscle swelling', 'Severe acute hindquarter lameness'],
    actionMr: 'तातडीची आणीबाणी! जनावराला अजिबात चालवू नका. शिरेतून पेनिसिलिन देण्यासाठी डॉक्टरांना तात्काळ बोलवा.',
    actionEn: 'Critical emergency! Do not move animal. Administer parenteral high-dose crystalline penicillin.'
  },
  ppr: {
    name: 'Peste des Petits Ruminants (Goat Plague)',
    band: 'Likely',
    score: 91.8,
    thermal: 40.7,
    urgency: 'RED_HIGH_CONTAGION',
    species: 'goat',
    symptoms: ['nasal_discharge', 'mouth_lesions', 'fever'],
    diffs: ['CCPP (Caprine Pleuropneumonia)', 'Goat Pox', 'Bluetongue'],
    biomarkers: ['Mucopurulent oculonasal crusting', 'Erosive necrotic stomatitis', 'Foul enteritis'],
    actionMr: 'बाधित शेळ्या-मेंढ्या त्वरित वेगळ्या करा. इलेक्ट्रोल पाणी पाजा. ५ किमी परिघातील शेळ्यांचे लसीकरण करा.',
    actionEn: 'Strictly quarantine sick goats. Provide oral electrolytes. Deploy urgent 5km ring vaccination.'
  },
  babesiosis: {
    name: 'Bovine Babesiosis / Redwater (Babesia bigemina)',
    band: 'Possible',
    score: 82.0,
    thermal: 40.9,
    urgency: 'AMBER_PARA_VET_VISIT',
    species: 'cattle',
    symptoms: ['fever'],
    diffs: ['Theileriosis', 'Anaplasmosis', 'Leptospirosis'],
    biomarkers: ['Boophilus microplus tick cluster', 'Coffee-colored redwater urine', 'Pale sclera'],
    actionMr: 'गोचीड निर्मूलन औषध (फ्ल्युमेथ्रिन) लावा. त्वरित पशुवैद्याकडून डिमिनाझिन इंजेक्शन टोचून घ्या.',
    actionEn: 'Apply topical acaricide immediately. Administer Diminazene Aceturate under veterinary care.'
  }
};

function simulateVisionDetection(cond) {
  currentDetectedCondition = cond || 'lsd';
  
  // Update Active Chip Button
  const chips = ['chipLsd', 'chipFmd', 'chipMastitis', 'chipBq', 'chipPpr', 'chipBabesiosis'];
  chips.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });
  const mapChip = { lsd: 'chipLsd', fmd: 'chipFmd', mastitis: 'chipMastitis', bq: 'chipBq', ppr: 'chipPpr', babesiosis: 'chipBabesiosis' };
  const targetChip = document.getElementById(mapChip[cond]);
  if (targetChip) targetChip.classList.add('active');

  drawLesionOnCanvas(currentDetectedCondition);

  const spec = visionDiseaseSpecs[currentDetectedCondition] || visionDiseaseSpecs.lsd;
  const box = document.getElementById("visionOutputBox");
  const content = document.getElementById("visionResultContent");
  if (box && content) {
    box.style.display = "block";
    content.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
        <div>
          <strong style="font-size:1.05rem; color:#0f172a;">${spec.name}</strong>
          <div style="font-size:0.78rem; color:#64748b;">
            Pathological Visual Identification • Confidence Band: 
            <span style="background:#dcfce7; color:#166534; font-weight:800; padding:2px 6px; border-radius:4px;">${spec.band} (${spec.score}%)</span>
          </div>
        </div>
        <span style="background:#fee2e2; color:#991b1b; font-weight:800; font-size:0.75rem; padding:3px 8px; border-radius:4px;">
          ${spec.urgency}
        </span>
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-bottom:10px; font-size:0.82rem;">
        <div style="background:#f1f5f9; padding:8px 12px; border-radius:6px;">
          <strong style="color:#334155;">Key Visual Biomarkers:</strong>
          <ul style="margin:4px 0 0 16px; padding:0; color:#475569;">
            ${spec.biomarkers.map(b => `<li>${b}</li>`).join('')}
          </ul>
        </div>
        <div style="background:#f1f5f9; padding:8px 12px; border-radius:6px;">
          <strong style="color:#334155;">Differential Diagnoses:</strong>
          <ul style="margin:4px 0 0 16px; padding:0; color:#475569;">
            ${spec.diffs.map(d => `<li>${d}</li>`).join('')}
          </ul>
        </div>
      </div>

      <div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:8px 12px; font-size:0.82rem; color:#065f46;">
        <strong>तात्काळ कृती (Marathi):</strong> ${spec.actionMr}<br>
        <strong>Safe Protocol (English):</strong> ${spec.actionEn}
      </div>
    `;
  }

  showToast(`AI Clinical Vision: Identified signs of ${spec.name}`);
}

function drawLesionOnCanvas(cond, customImg) {
  const container = document.getElementById("visionCanvasContainer");
  const canvas = document.getElementById("visionCanvas");
  if (!container || !canvas) return;
  container.style.display = "block";
  const ctx = canvas.getContext("2d");
  const w = canvas.width;
  const h = canvas.height;

  ctx.clearRect(0, 0, w, h);

  if (customImg) {
    ctx.drawImage(customImg, 0, 0, w, h);
  } else {
    // Generate simulated high-fidelity skin/tissue backdrop
    const grad = ctx.createLinearGradient(0, 0, w, h);
    if (cond === 'mastitis') {
      grad.addColorStop(0, "#fbcfe8");
      grad.addColorStop(1, "#f472b6");
    } else if (cond === 'bq') {
      grad.addColorStop(0, "#475569");
      grad.addColorStop(1, "#1e293b");
    } else {
      grad.addColorStop(0, "#e2e8f0");
      grad.addColorStop(1, "#94a3b8");
    }
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Render pathological condition patterns
    if (cond === 'lsd') {
      // Circumscribed 2-5cm firm dermal nodules
      const nodules = [
        { x: 180, y: 120, r: 28 },
        { x: 310, y: 160, r: 36 },
        { x: 440, y: 110, r: 24 },
        { x: 250, y: 220, r: 30 }
      ];
      nodules.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fillStyle = "#7f1d1d";
        ctx.fill();
        ctx.lineWidth = 3;
        ctx.strokeStyle = "#ef4444";
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r * 0.45, 0, Math.PI * 2);
        ctx.fillStyle = "#450a0a";
        ctx.fill();
      });
    } else if (cond === 'fmd') {
      // Vesicular erosions on mucosal border
      ctx.fillStyle = "#b91c1c";
      ctx.beginPath();
      ctx.ellipse(320, 160, 85, 45, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.lineWidth = 4;
      ctx.strokeStyle = "#f87171";
      ctx.stroke();

      // Sloughed mucosal blisters
      for (let i = 0; i < 7; i++) {
        ctx.beginPath();
        ctx.arc(280 + i * 14, 155 + (i % 2) * 8, 7, 0, Math.PI * 2);
        ctx.fillStyle = "#fef08a";
        ctx.fill();
      }
    } else if (cond === 'mastitis') {
      // Udder asymmetric hyperthermia and swelling
      ctx.fillStyle = "#e11d48";
      ctx.beginPath();
      ctx.ellipse(300, 180, 110, 80, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 5;
      ctx.stroke();
    } else if (cond === 'bq') {
      // Emphysematous crepitating swelling
      ctx.fillStyle = "#0f172a";
      ctx.beginPath();
      ctx.ellipse(320, 160, 120, 70, 0.2, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#dc2626";
      ctx.lineWidth = 3;
      ctx.stroke();
    } else if (cond === 'ppr') {
      // Oculonasal erosions and discharge
      ctx.fillStyle = "#7c2d12";
      ctx.beginPath();
      ctx.ellipse(310, 140, 75, 40, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ea580c";
      ctx.lineWidth = 3;
      ctx.stroke();
    } else if (cond === 'babesiosis') {
      // Tick cluster
      for (let i = 0; i < 15; i++) {
        ctx.beginPath();
        ctx.arc(250 + (i % 5) * 22, 120 + Math.floor(i / 5) * 25, 6, 0, Math.PI * 2);
        ctx.fillStyle = "#1e293b";
        ctx.fill();
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }
  }

  // Thermal Infrared FLIR Shader Overlay (if toggled)
  if (thermalModeActive) {
    const imgData = ctx.getImageData(0, 0, w, h);
    const d = imgData.data;
    for (let i = 0; i < d.length; i += 4) {
      const avg = (d[i] + d[i+1] + d[i+2]) / 3;
      if (avg > 180) { // White hot
        d[i] = 255; d[i+1] = 255; d[i+2] = 220;
      } else if (avg > 130) { // Yellow/Orange
        d[i] = 255; d[i+1] = 160; d[i+2] = 20;
      } else if (avg > 80) { // Red hot
        d[i] = 220; d[i+1] = 30; d[i+2] = 30;
      } else { // Purple/Blue background
        d[i] = 50; d[i+1] = 10; d[i+2] = 90;
      }
    }
    ctx.putImageData(imgData, 0, 0);
  }

  // Grad-CAM Attention Heatmap (if toggled)
  if (gradCamActive) {
    const gcam = ctx.createRadialGradient(310, 160, 15, 310, 160, 130);
    gcam.addColorStop(0, "rgba(239, 68, 68, 0.75)");
    gcam.addColorStop(0.4, "rgba(245, 158, 11, 0.5)");
    gcam.addColorStop(0.8, "rgba(59, 130, 246, 0.25)");
    gcam.addColorStop(1, "rgba(0, 0, 0, 0)");
    ctx.fillStyle = gcam;
    ctx.fillRect(0, 0, w, h);
  }

  // Bounding Box HUD Overlays
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 2.5;
  ctx.strokeRect(200, 75, 230, 160);

  // Corner Bracket Reticles
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 4;
  const corners = [
    [200, 75, 15, 0, 0, 15],
    [430, 75, -15, 0, 0, 15],
    [200, 235, 15, 0, 0, -15],
    [430, 235, -15, 0, 0, -15]
  ];
  corners.forEach(([x, y, dx1, dy1, dx2, dy2]) => {
    ctx.beginPath();
    ctx.moveTo(x + dx1, y + dy1);
    ctx.lineTo(x, y);
    ctx.lineTo(x + dx2, y + dy2);
    ctx.stroke();
  });

  // Label tag above box
  ctx.fillStyle = "#38bdf8";
  ctx.fillRect(200, 52, 190, 22);
  ctx.fillStyle = "#020617";
  ctx.font = "bold 11px monospace";
  const spec = visionDiseaseSpecs[cond] || visionDiseaseSpecs.lsd;
  ctx.fillText(`DETECT: ${cond.toUpperCase()} (${spec.score}%)`, 206, 67);

  // Update HUD text
  const hudStatus = document.getElementById("hudStatus");
  const hudMetrics = document.getElementById("hudLesionMetrics");
  if (hudStatus) {
    hudStatus.innerHTML = `TARGET: <span style="color:#38bdf8;">${cond.toUpperCase()}</span> | FLIR: ${thermalModeActive ? 'ON' : 'OFF'} | GRAD-CAM: ${gradCamActive ? 'ON' : 'OFF'}`;
  }
  if (hudMetrics) {
    hudMetrics.innerHTML = `TEMP: ${spec.thermal}°C | CONF: ${spec.band}`;
  }
}

function toggleThermalMode() {
  thermalModeActive = !thermalModeActive;
  const btn = document.getElementById("thermalToggleBtn");
  if (btn) {
    if (thermalModeActive) {
      btn.classList.add("thermal-active");
      btn.innerHTML = "✓ FLIR Thermal: ON";
    } else {
      btn.classList.remove("thermal-active");
      btn.innerHTML = "🌡️ FLIR Thermal Heatmap";
    }
  }
  drawLesionOnCanvas(currentDetectedCondition);
  showToast(thermalModeActive ? "FLIR Thermal Infrared Overlay Enabled" : "Thermal Overlay Disabled");
}

function toggleGradCamMode() {
  gradCamActive = !gradCamActive;
  const btn = document.getElementById("gradCamToggleBtn");
  if (btn) {
    if (gradCamActive) {
      btn.classList.add("active");
      btn.innerHTML = "✓ Grad-CAM: ON";
    } else {
      btn.classList.remove("active");
      btn.innerHTML = "🧠 Grad-CAM Attention";
    }
  }
  drawLesionOnCanvas(currentDetectedCondition);
  showToast(gradCamActive ? "Grad-CAM CNN Attention Heatmap Enabled" : "Grad-CAM Disabled");
}

function toggleLiveCameraFeed() {
  const video = document.getElementById("visionVideoFeed");
  const btn = document.getElementById("liveCameraBtn");
  if (!video || !btn) return;

  if (liveCameraStream) {
    liveCameraStream.getTracks().forEach(t => t.stop());
    liveCameraStream = null;
    video.pause();
    btn.classList.remove("active");
    btn.innerHTML = "📹 Open Live Camera";
    drawLesionOnCanvas(currentDetectedCondition);
    showToast("Live camera feed stopped.");
    return;
  }

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
      .then(stream => {
        liveCameraStream = stream;
        video.srcObject = stream;
        video.play();
        btn.classList.add("active");
        btn.innerHTML = "⏹️ Stop Camera";
        showToast("Live Camera stream connected. Frame-by-frame lesion inspection active!");

        const container = document.getElementById("visionCanvasContainer");
        const canvas = document.getElementById("visionCanvas");
        if (container) container.style.display = "block";
        const ctx = canvas.getContext("2d");

        function renderFrame() {
          if (!liveCameraStream) return;
          if (video.readyState === video.HAVE_ENOUGH_DATA) {
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            // Draw real-time HUD bounding box over live frame
            ctx.strokeStyle = "#38bdf8";
            ctx.lineWidth = 2.5;
            ctx.strokeRect(200, 75, 230, 160);
            ctx.fillStyle = "#38bdf8";
            ctx.fillRect(200, 52, 190, 22);
            ctx.fillStyle = "#020617";
            ctx.font = "bold 11px monospace";
            ctx.fillText("LIVE SCAN: ACTIVE", 206, 67);
          }
          requestAnimationFrame(renderFrame);
        }
        requestAnimationFrame(renderFrame);
      })
      .catch(err => {
        console.warn("Camera access unavailable in environment:", err);
        showToast("Webcam unavailable in this sandbox environment. Simulating high-res field photo.");
        drawLesionOnCanvas(currentDetectedCondition);
      });
  } else {
    showToast("Webcam API not supported in this browser.");
  }
}

function transferVisionToTriage() {
  const spec = visionDiseaseSpecs[currentDetectedCondition] || visionDiseaseSpecs.lsd;
  
  // Set species
  const speciesInputs = document.querySelectorAll('input[name="species"]');
  speciesInputs.forEach(inp => {
    if (inp.value === spec.species) inp.checked = true;
  });

  // Check corresponding symptoms
  spec.symptoms.forEach(sym => {
    toggleSymptomCheckbox(sym, true);
  });

  // Fill Voice/Form notes
  const notes = document.getElementById("farmerVoiceNotes");
  if (notes) {
    notes.value = `[AI Vision Detection]: ${spec.name} detected with ${spec.band} confidence (${spec.score}%). Observed signs: ${spec.biomarkers.join(', ')}.`;
  }

  // Smooth scroll to submit button
  const submitBtn = document.getElementById("triageSubmitBtn") || document.querySelector("#symptom-screening button[type='submit']");
  if (submitBtn) {
    submitBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
    submitBtn.style.boxShadow = "0 0 16px rgba(22, 163, 74, 0.8)";
    setTimeout(() => { submitBtn.style.boxShadow = ""; }, 2500);
  }

  showToast(`✓ AI Vision findings for ${spec.name} transferred to 90-Second Intake!`);
}

// 3. Dynamic SEIR Outbreak Simulation
let seirPlayInterval = null;
let currentSeirDay = 0;

function updateSeirDay(dayVal) {
  currentSeirDay = parseInt(dayVal, 10);
  const lbl = document.getElementById("seirDayLabel");
  if (lbl) lbl.textContent = `Day ${currentSeirDay}`;

  // Mathematical SEIR Progression Model
  const isRingActive = ringVaxActive;
  let rt = isRingActive ? Math.max(0.65, 2.45 - (currentSeirDay * 0.13)) : 2.45;
  let inf = isRingActive ? 
    Math.round(12 + Math.max(0, currentSeirDay * 12 - (currentSeirDay > 3 ? (currentSeirDay - 3) * 14 : 0))) : 
    Math.round(12 * Math.pow(1.35, currentSeirDay));
  let vax = isRingActive ? Math.min(8400, currentSeirDay * 600) : 0;
  let eff = isRingActive ? Math.min(94.2, 4.5 + (currentSeirDay * 6.5)) : 4.5;

  const rtEl = document.getElementById("seirRtVal");
  const infEl = document.getElementById("seirInfVal");
  const vaxEl = document.getElementById("seirVaxVal");
  const effEl = document.getElementById("seirEfficacyVal");

  if (rtEl) {
    rtEl.textContent = rt.toFixed(2);
    rtEl.style.color = rt < 1.0 ? '#22c55e' : '#ef4444';
  }
  if (infEl) infEl.textContent = inf.toLocaleString();
  if (vaxEl) vaxEl.textContent = vax.toLocaleString();
  if (effEl) effEl.textContent = `${eff.toFixed(1)}%`;

  // Scale SVG outbreak radius on map
  const gisSvg = document.getElementById("gisSvgMap");
  if (gisSvg && typeof gisSvg.querySelector === 'function') {
    const nimgaonPulse = gisSvg.querySelector('circle[fill="#dc2626"]');
    if (nimgaonPulse) {
      const baseR = 8;
      const growthFactor = isRingActive ? Math.min(1.4, 1 + currentSeirDay * 0.03) : (1 + currentSeirDay * 0.09);
      nimgaonPulse.setAttribute('r', (baseR * growthFactor).toString());
    }
  }
}

function toggleSeirPlay() {
  const btn = document.getElementById("playSeirBtn");
  const slider = document.getElementById("seirDaySlider");

  if (seirPlayInterval) {
    clearInterval(seirPlayInterval);
    seirPlayInterval = null;
    if (btn) btn.innerHTML = "▶️ Run 14-Day Simulation";
    return;
  }

  currentSeirDay = 0;
  if (slider) slider.value = 0;
  updateSeirDay(0);
  if (btn) btn.innerHTML = "⏸️ Pause Simulation";

  seirPlayInterval = setInterval(() => {
    currentSeirDay++;
    if (currentSeirDay > 14) {
      clearInterval(seirPlayInterval);
      seirPlayInterval = null;
      if (btn) btn.innerHTML = "🔄 Replay Simulation";
      showToast("14-Day SEIR Outbreak Simulation Completed!");
      return;
    }
    if (slider) slider.value = currentSeirDay;
    updateSeirDay(currentSeirDay);
  }, 600);
}

// 4. 1962 MVU Audio Siren Synthesizer (Web Audio API)
function playMvuSirenTone() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = "sawtooth";
    gain.gain.setValueAtTime(0.12, ctx.currentTime);

    // Dual-frequency European/Indian emergency horn sweep
    const now = ctx.currentTime;
    for (let i = 0; i < 4; i++) {
      osc.frequency.setValueAtTime(700, now + i * 0.5);
      osc.frequency.linearRampToValueAtTime(950, now + i * 0.5 + 0.25);
      osc.frequency.linearRampToValueAtTime(700, now + i * 0.5 + 0.5);
    }

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start(now);
    osc.stop(now + 2.0);
    showToast("🚨 1962 MVU Emergency Vehicle Siren Triggered!");
  } catch (e) {
    console.warn("Web Audio not permitted:", e);
    showToast("🚨 1962 MVU Emergency Siren Active (Audio Muted)");
  }
}

// 5. Official 1962 WhatsApp Chatbot Simulator
function toggleWhatsAppChat() {
  const drawer = document.getElementById("whatsappDrawer");
  if (drawer) {
    drawer.classList.toggle("active");
  }
}

function sendWhatsAppQuickMsg(type) {
  const list = document.getElementById("whatsappMessagesList");
  if (!list) return;

  let userText = "";
  let botReply = "";

  if (type === 'voice') {
    userText = "🎙️ व्हॉइस मेसेज (०:१२): 'माझ्या गाईच्या अंगावर मोठ्या गाठी आल्या आहेत, ताप खूप आहे.'";
    botReply = `
      🙏 <strong>पशूसचेत १९६२ सहाय्यता केंद्र</strong><br>
      तुमचा व्हॉइस मेसेज प्राप्त झाला. प्राथमिक विश्लेषण:<br>
      ⚠️ <strong>संशयित रोग:</strong> लंपी त्वचा रोग (LSD - RED TIER)<br>
      👉 बाधित जनावराला कळपापासून वेगळे बांधा. संगमनेर फिरत्या पशुवैद्यकीय पथकाला (MVU 1962) अलर्ट पाठवला आहे.
    `;
  } else if (type === 'photo') {
    userText = "📷 फोटो पाठवला: nodule_lesion.jpg";
    botReply = `
      🔍 <strong>फोटो विश्लेषण पूर्ण:</strong><br>
      गाठींचा आकार २-४ सेमी असून लंपी रोगाची लक्षणे स्पष्ट दिसत आहेत.<br>
      ⏱️ डॉ. प्रदीप देशमुख (CVD संगमनेर) यांना सूचित केले आहे.
    `;
  } else if (type === 'status') {
    userText = "📋 केस स्टेटस: निमगाव जाळी अहवाल #SIG-9102";
    botReply = `
      📋 <strong>केस सद्यस्थिती:</strong><br>
      • स्थिती: ✅ पॅरा-व्हेट गणेश काळे यांनी पडताळणी केली.<br>
      • नमुना: #SAM-2026-AHM-0081 (RDDL पुणे लॅबमध्ये)<br>
      • कारवाई: ५ किमी परिसरात रिंग लसीकरण सुरू.
    `;
  }

  appendWhatsAppBubble(userText, 'outgoing');
  setTimeout(() => {
    appendWhatsAppBubble(botReply, 'incoming');
  }, 700);
}

function sendWhatsAppUserText() {
  const input = document.getElementById("whatsappUserInput");
  if (!input || !input.value.trim()) return;

  const text = input.value.trim();
  appendWhatsAppBubble(text, 'outgoing');
  input.value = "";

  setTimeout(() => {
    let reply = `
      🙏 <strong>पशूसचेत महाराष्ट्र शासन:</strong><br>
      आपला संदेश नोंदवला आहे: "<em>${text}</em>".<br>
      १९६२ फिरते पथक आपल्या गावाच्या संपर्कात आहे. आपत्कालीन मदतीसाठी थेट १९६२ वर डायल करा.
    `;
    appendWhatsAppBubble(reply, 'incoming');
  }, 800);
}

function appendWhatsAppBubble(content, direction) {
  const list = document.getElementById("whatsappMessagesList");
  if (!list) return;

  const now = new Date();
  const timeStr = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')}`;

  const msgDiv = document.createElement("div");
  msgDiv.className = `whatsapp-msg ${direction}`;
  msgDiv.innerHTML = `
    <div>${content}</div>
    <div class="whatsapp-time">${timeStr}</div>
  `;
  list.appendChild(msgDiv);
  list.scrollTop = list.scrollHeight;
}

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

function generateNadresExport() { return exportNadresBatch(); }



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



// ==========================================================================
// V2 APP SHELL NAVIGATION ENGINE: DESKTOP SIDEBAR + MOBILE BOTTOM BAR
// ==========================================================================

const ROLE_NAV_SPECS = {
  farmer: {
    userName: "एकनाथराव पाटील",
    roleLabel: "शेतकरी (साक्री बीट)",
    avatar: "EB",
    items: [
      { id: 'viewFarmerHome', labelMr: 'आजची काळजी (Home)', labelEn: "Today's Care", icon: 'home', badge: '' },
      { id: 'viewFarmerTriage', labelMr: 'लक्षणे नोंदवा (Report)', labelEn: 'Start Health Check', icon: 'stethoscope', badge: '९० से.' },
      { id: 'viewFarmerAnimals', labelMr: 'माझी जनावरे (Animals)', labelEn: 'My Animals', icon: 'tag', badge: '३' },
      { id: 'viewFarmerCases', labelMr: 'रुग्ण नोंदवही (Cases)', labelEn: 'Active Cases', icon: 'file-text', badge: '१ चालू' },
      { id: 'viewFarmerVets', labelMr: 'पशुवैद्यकीय दवाखाने', labelEn: 'Vet Care Directory', icon: 'phone-call', badge: '' }
    ]
  },
  paravet: {
    userName: "सुनिता पाटील",
    roleLabel: "पशु सखी (साक्री व ५ गावे)",
    avatar: "SP",
    items: [
      { id: 'paravetSignalsContainer', labelMr: 'पडताळणी रांग (Queue)', labelEn: 'Verification Queue', icon: 'clipboard-check', badge: '३ प्रलंबित' },
      { id: 'paravetVillageSelect', labelMr: 'गाव निवड व फिल्टर', labelEn: 'Village Filter', icon: 'filter', badge: '५ गावे' },
      { id: 'sampleSignalCount', labelMr: 'नमुना किट्स (Samples)', labelEn: 'Diagnostic Kits', icon: 'flask', badge: '२' },
      { id: 'outbreak-gis', labelMr: 'गाव नकाशा (Field Map)', labelEn: 'Village Map', icon: 'map-pin', badge: '' }
    ]
  },
  ldo: {
    userName: "डॉ. रामेश्वर कुटे",
    roleLabel: "पशुवैद्यकीय अधिकारी (साक्री)",
    avatar: "RK",
    items: [
      { id: 'vetAppointmentsContainer', labelMr: 'दवाखाना अपॉइंटमेंट्स', labelEn: 'Appointments', icon: 'calendar', badge: '३' },
      { id: 'vetCasesContainer', labelMr: 'AI-रेफर्ड तातडीच्या केसेस', labelEn: 'Referred Cases', icon: 'alert-triangle', badge: '२' },
      { id: 'prescribeForm', labelMr: 'डिजिटल प्रिस्क्रिप्शन (Rx)', labelEn: 'Prescription Engine', icon: 'pill', badge: 'दूध सुरक्षा' },
      { id: 'outbreak-gis', labelMr: 'साथरोग नियंत्रण नकाशा', labelEn: 'Epidemic Map', icon: 'map-pin', badge: '' }
    ]
  },
  vet: {
    userName: "डॉ. रामेश्वर कुटे",
    roleLabel: "पशुवैद्यकीय अधिकारी (साक्री)",
    avatar: "RK",
    items: [
      { id: 'vetAppointmentsContainer', labelMr: 'दवाखाना अपॉइंटमेंट्स', labelEn: 'Appointments', icon: 'calendar', badge: '३' },
      { id: 'vetCasesContainer', labelMr: 'AI-रेफर्ड तातडीच्या केसेस', labelEn: 'Referred Cases', icon: 'alert-triangle', badge: '२' },
      { id: 'prescribeForm', labelMr: 'डिजिटल प्रिस्क्रिप्शन (Rx)', labelEn: 'Prescription Engine', icon: 'pill', badge: 'दूध सुरक्षा' },
      { id: 'outbreak-gis', labelMr: 'साथरोग नियंत्रण नकाशा', labelEn: 'Epidemic Map', icon: 'map-pin', badge: '' }
    ]
  },
  collector: {
    userName: "जिल्हाधिकारी कार्यालय",
    roleLabel: "जिल्हा नियंत्रण कक्ष (धुळे)",
    avatar: "DC",
    items: [
      { id: 'villageSignalsGrid', labelMr: 'गाव पातळीवरील सिग्नल', labelEn: 'Village Signal Board', icon: 'activity', badge: '४ गावे' },
      { id: 'officerDecisionQueue', labelMr: 'सकाळची निर्णय रांग', labelEn: 'Decision Queue', icon: 'shield', badge: '३ प्रलंबित' },
      { id: 'gisSvgMap', labelMr: 'साथरोग अंदाज व ५ किमी रिंग', labelEn: 'SEIR GIS Map', icon: 'map-pin', badge: '५ किमी' },
      { id: 'mvuDispatchCard', labelMr: '१९६२ फिरते पथक (MVU)', labelEn: 'MVU Live Dispatch', icon: 'truck', badge: 'लाइव्ह' }
    ]
  },
  officer: {
    userName: "जिल्हाधिकारी कार्यालय",
    roleLabel: "जिल्हा नियंत्रण कक्ष (धुळे)",
    avatar: "DC",
    items: [
      { id: 'villageSignalsGrid', labelMr: 'गाव पातळीवरील सिग्नल', labelEn: 'Village Signal Board', icon: 'activity', badge: '४ गावे' },
      { id: 'officerDecisionQueue', labelMr: 'सकाळची निर्णय रांग', labelEn: 'Decision Queue', icon: 'shield', badge: '३ प्रलंबित' },
      { id: 'gisSvgMap', labelMr: 'साथरोग अंदाज व ५ किमी रिंग', labelEn: 'SEIR GIS Map', icon: 'map-pin', badge: '५ किमी' },
      { id: 'mvuDispatchCard', labelMr: '१९६२ फिरते पथक (MVU)', labelEn: 'MVU Live Dispatch', icon: 'truck', badge: 'लाइव्ह' }
    ]
  },
  rddl: {
    userName: "राज्य रोग निदान प्रयोगशाळा",
    roleLabel: "विभागीय प्रयोगशाळा (पुणे)",
    avatar: "RD",
    items: [
      { id: 'sampleCardsContainer', labelMr: 'सक्रिय नमुना ट्रॅकिंग', labelEn: 'Sample Pipeline', icon: 'flask', badge: '१ सक्रिय' },
      { id: 'rddlPcrAction', labelMr: 'RT-PCR चाचणी विश्लेषण', labelEn: 'RT-PCR Thermocycler', icon: 'cpu', badge: '४० सायकल' },
      { id: 'nadresPayloadBox', labelMr: 'ICAR-NIVEDI NADRES V2', labelEn: 'NADRES Export', icon: 'download', badge: 'DPDP' }
    ]
  },
  admin: {
    userName: "राज्य रोग निदान प्रयोगशाळा",
    roleLabel: "विभागीय प्रयोगशाळा (पुणे)",
    avatar: "RD",
    items: [
      { id: 'sampleCardsContainer', labelMr: 'सक्रिय नमुना ट्रॅकिंग', labelEn: 'Sample Pipeline', icon: 'flask', badge: '१ सक्रिय' },
      { id: 'rddlPcrAction', labelMr: 'RT-PCR चाचणी विश्लेषण', labelEn: 'RT-PCR Thermocycler', icon: 'cpu', badge: '४० सायकल' },
      { id: 'nadresPayloadBox', labelMr: 'ICAR-NIVEDI NADRES V2', labelEn: 'NADRES Export', icon: 'download', badge: 'DPDP' }
    ]
  }
};

function renderSidebarNav(role) {
  const sidebar = document.getElementById("sidebarNavList");
  const userEl = document.getElementById("sidebarUserName");
  const roleEl = document.getElementById("sidebarRoleLabel");
  const avatarEl = document.getElementById("sidebarAvatar");

  const spec = ROLE_NAV_SPECS[role] || ROLE_NAV_SPECS.farmer;
  const isMr = (typeof currentLang === 'undefined' || currentLang === 'mr');

  if (userEl) userEl.textContent = spec.userName;
  if (roleEl) roleEl.textContent = spec.roleLabel;
  if (avatarEl) avatarEl.textContent = spec.avatar;

  if (sidebar) {
    sidebar.innerHTML = spec.items.map((item, idx) => `
      <div class="sidebar-nav-item ${idx === 0 ? 'active' : ''}" data-target="${item.id}" onclick="navigateToAppSection('${item.id}', '${role}', this)">
        <div style="display:flex; align-items:center; gap:10px;">
          <span data-icon="${item.icon}" data-size="16"></span>
          <span>${isMr ? item.labelMr : item.labelEn}</span>
        </div>
        ${item.badge ? `<span class="sidebar-nav-badge">${item.badge}</span>` : ''}
      </div>
    `).join("");
  }

  // Update topbar segmented control buttons
  const segmentedMap = {
    farmer: 'btnPersonaFarmer',
    paravet: 'btnPersonaParavet',
    ldo: 'btnPersonaLdo',
    vet: 'btnPersonaLdo',
    collector: 'btnPersonaCollector',
    officer: 'btnPersonaCollector',
    rddl: 'btnPersonaRddl',
    admin: 'btnPersonaRddl'
  };
  document.querySelectorAll('.persona-tab-btn').forEach(b => b.classList.remove('active'));
  const activeBtn = document.getElementById(segmentedMap[role]);
  if (activeBtn) activeBtn.classList.add('active');

  // Also render mobile bottom tabs
  renderBottomTabBar(role);

  if (typeof renderIcons === 'function') renderIcons();
}

function renderBottomTabBar(role) {
  const bottomBar = document.getElementById("appMobileBottomBar");
  if (!bottomBar) return;

  const spec = ROLE_NAV_SPECS[role] || ROLE_NAV_SPECS.farmer;
  const isMr = (typeof currentLang === 'undefined' || currentLang === 'mr');

  bottomBar.innerHTML = spec.items.slice(0, 5).map((item, idx) => `
    <button type="button" class="bottom-tab-item ${idx === 0 ? 'active' : ''}" data-target="${item.id}" onclick="navigateToAppSection('${item.id}', '${role}', this)">
      <span data-icon="${item.icon}" data-size="18"></span>
      <span>${isMr ? item.labelMr.split(' ')[0] : item.labelEn.split(' ')[0]}</span>
    </button>
  `).join("");

  if (typeof renderIcons === 'function') renderIcons();
}

function navigateToAppSection(targetId, role, btnEl) {
  // Update active state in sidebar and bottom bar
  document.querySelectorAll(`.sidebar-nav-item, .bottom-tab-item`).forEach(el => {
    if (el.getAttribute('data-target') === targetId) {
      el.classList.add('active');
    } else {
      el.classList.remove('active');
    }
  });

  // Action dispatches
  if (targetId === 'rddlPcrAction') {
    openRddlPcrModal("SMP-2026-041");
    return;
  }

  if (targetId.startsWith('viewFarmer')) {
    switchNotebookTab(targetId);
    return;
  }

  if (targetId === 'vetAppointmentsContainer') {
    switchVetTab('apts');
    const el = document.getElementById('vetAppointmentsContainer');
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return;
  }

  if (targetId === 'vetCasesContainer') {
    switchVetTab('cases');
    const el = document.getElementById('vetCasesContainer');
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return;
  }

  // Smooth scroll to container within main content
  const el = document.getElementById(targetId);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    el.style.transition = 'box-shadow 0.3s ease';
    el.style.boxShadow = '0 0 0 3px var(--accent-turmeric)';
    setTimeout(() => { el.style.boxShadow = ''; }, 1200);
  }
}
