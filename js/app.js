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
    nav_blueprint: "Blueprint",
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
    nav_blueprint: "प्रकल्प आराखडा",
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
    nav_blueprint: "परियोजना रूपरेखा",
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
    notes: "Healthy, milk yield 14L/day"
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
  initTabs();
  initModals();
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
  const species = document.querySelector('input[name="species"]:checked')?.value || "cattle";
  const checkedBoxes = Array.from(document.querySelectorAll('input[name="symptom"]:checked')).map(cb => cb.value);
  const onsetDays = parseInt(document.getElementById("onsetDays")?.value || "2");
  const tempDegree = parseFloat(document.getElementById("tempInput")?.value || "102.5");

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

  // Rule-based clinical triage matching Seva First Model A
  let primaryCondition = "";
  let confidence = 0;
  let urgency = "moderate"; // critical, urgent, moderate
  let urgencyLabel = "";
  let differential = [];
  let actions = [];

  const hasFever = checkedBoxes.includes("fever") || tempDegree >= 103.5;
  const hasNodules = checkedBoxes.includes("skin_nodules");
  const hasMouthFoot = checkedBoxes.includes("mouth_lesions") || checkedBoxes.includes("lameness");
  const hasRespiratory = checkedBoxes.includes("cough") || checkedBoxes.includes("nasal_discharge");
  const hasMastitis = checkedBoxes.includes("udder_swelling") || checkedBoxes.includes("milk_drop");
  const hasDiarrhea = checkedBoxes.includes("diarrhea");

  if (species === "poultry") {
    if (hasRespiratory || checkedBoxes.includes("anorexia")) {
      primaryCondition = "Newcastle Disease (Ranikhet) / Infectious Coryza";
      confidence = 84;
      urgency = "critical";
      urgencyLabel = "CRITICAL: Urgent Flock Isolation Required";
      actions = [
        "Immediately isolate sick birds in a separate quarantine shed.",
        "Add oral electrolytes and vitamin B-complex to drinking water.",
        "Disinfect farm perimeter with approved biocide; halt visitor entry.",
        "Contact local veterinary officer immediately for confirmatory swab tests."
      ];
      differential = ["Infectious Bronchitis", "Fowl Cholera", "Nutritional Deficiency"];
    } else {
      primaryCondition = "Coccidiosis / Enteric Distress";
      confidence = 72;
      urgency = "urgent";
      urgencyLabel = "URGENT: Review Litter Hygiene";
      actions = ["Check for damp litter", "Provide clean acidified drinking water", "Consult vet for anticoccidial plan"];
      differential = ["Colibacillosis", "Dietary change"];
    }
  } else if (species === "goat" || species === "sheep") {
    if (checkedBoxes.includes("mouth_lesions") && (hasDiarrhea || hasFever)) {
      primaryCondition = "Peste des Petits Ruminants (PPR) / Goat Plague";
      confidence = 91;
      urgency = "critical";
      urgencyLabel = "CRITICAL: Highly Contagious Small Ruminant Alert";
      actions = [
        "Isolate affected sheep/goats from the flock to prevent transmission.",
        "Do not allow grazing in common pastures or water troughs.",
        "Wash oral ulcers with mild potassium permanganate (1:10,000) solution.",
        "Call veterinary dispensary for supportive fluid therapy and antipyretics."
      ];
      differential = ["Contagious Ecthyma (Orf)", "Bluetongue", "Pasteurellosis"];
    } else if (checkedBoxes.includes("sudden_death") || hasDiarrhea) {
      primaryCondition = "Enterotoxaemia (Pulpy Kidney) Suspected";
      confidence = 82;
      urgency = "critical";
      urgencyLabel = "CRITICAL: Risk of Rapid Mortality";
      actions = [
        "Stop grain feeding immediately; switch to dry roughage.",
        "Administer veterinary-directed antitoxin or alkalizing fluids.",
        "Vaccinate unaffected flock members with ET vaccine."
      ];
      differential = ["Coccidiosis", "Plant Poisoning"];
    } else {
      primaryCondition = "Pneumonia / Caprine Respiratory Infection";
      confidence = 74;
      urgency = "urgent";
      urgencyLabel = "URGENT: Veterinary Auscultation Advised";
      actions = ["Keep shelter dry, warm and draft-free", "Provide warm gruel/water", "Veterinary antibiotic assessment"];
      differential = ["Lungworm infestation", "Shipping fever"];
    }
  } else {
    // Cattle / Buffalo
    if (hasNodules) {
      primaryCondition = "Lumpy Skin Disease (LSD) Suspected";
      confidence = 94;
      urgency = "urgent";
      urgencyLabel = "URGENT: Vector-Borne Viral Screening Positive";
      actions = [
        "Strictly isolate the cow/buffalo in an insect-screened or smoky shelter.",
        "Apply neem oil or herbal fly-repellent spray over body to deter mosquitoes/ticks.",
        "Provide soft green fodder, electrolytes and fresh drinking water frequently.",
        "DO NOT use unprescribed human paracetamol or antibiotic injections.",
        "Schedule official visit by Government Livestock Development Officer."
      ];
      differential = ["Pseudo-lumpy skin disease (Herpesvirus 2)", "Bovine Papillomatosis", "Hypoderma / Insect bites"];
    } else if (hasMouthFoot && (hasFever || checkedBoxes.includes("milk_drop"))) {
      primaryCondition = "Foot and Mouth Disease (FMD) Screening Match";
      confidence = 89;
      urgency = "critical";
      urgencyLabel = "CRITICAL: High Transmission Risk (Reportable)";
      actions = [
        "Quarantine animal; restrict all cattle movement from your shed.",
        "Wash oral cavity with 1% Alum or Boro-glycerine solution gently.",
        "Apply antiseptic paste (Zinc oxide + Turmeric + Castor oil) to hoof clefts.",
        "Feed soft palatable mash or porridge; animal cannot chew hard dry stalks.",
        "Request ring-vaccination for all neighboring cattle within 5 km radius."
      ];
      differential = ["Vesicular Stomatitis", "Mucosal Disease (BVD)", "Chemical burn/irritant"];
    } else if (hasMastitis) {
      primaryCondition = "Bovine Mastitis (Sub-acute / Clinical)";
      confidence = 86;
      urgency = "urgent";
      urgencyLabel = "URGENT: Dairy Production & Welfare Concern";
      actions = [
        "Strip milk completely from affected quarter into a disinfectant container (do not spill on floor).",
        "Apply cold compress if udder is hot and swollen, followed by gentle massage.",
        "Do not allow calf to nurse from the inflamed quarter.",
        "Have veterinarian perform California Mastitis Test (CMT) and intramammary therapy."
      ];
      differential = ["Udder edema", "Hematoma", "Mycoplasma mastitis"];
    } else if (hasRespiratory && hasFever) {
      primaryCondition = "Haemorrhagic Septicaemia (HS) / Bovine Respiratory Disease";
      confidence = 87;
      urgency = "critical";
      urgencyLabel = "CRITICAL: Rapid Progression - Immediate Vet Attention";
      actions = [
        "Keep animal in well-ventilated, clean dry stall.",
        "Avoid stressing or walking the animal in hot sun.",
        "Immediate veterinary administration of broad-spectrum antibiotic and NSAID is critical."
      ];
      differential = ["Black Quarter (early)", "Enzootic Pneumonia", "Aspiration pneumonia"];
    } else {
      primaryCondition = "Non-Specific Indigestion / Simple Anorexia";
      confidence = 68;
      urgency = "moderate";
      urgencyLabel = "MODERATE: Monitor Vitals & Rumination";
      actions = [
        "Offer appetizing digestive greens and fresh water with mineral mix.",
        "Check rumination cycles (should be 2-3 per 2 minutes).",
        "If condition does not improve within 24 hours, request veterinary inspection."
      ];
      differential = ["Mild rumen acidosis", "Dietary change stress", "Parasitic load"];
    }
  }

  // Populate UI
  triageBanner.className = `triage-banner triage-${urgency}`;
  triageText.innerHTML = `<strong>${urgency.toUpperCase()}:</strong> ${urgencyLabel}`;

  diagName.textContent = primaryCondition;
  diagConf.textContent = `${confidence}% Match`;
  confBar.style.width = `${confidence}%`;

  diffDiag.textContent = `Differential Rule-Outs: ${differential.join(" • ")}`;

  adviceList.innerHTML = "";
  actions.forEach(act => {
    const li = document.createElement("li");
    li.textContent = act;
    adviceList.appendChild(li);
  });

  resultContainer.classList.add("active");
  resultContainer.scrollIntoView({ behavior: "smooth", block: "start" });
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

    card.innerHTML = `
      <div class="animal-card-header">
        <div>
          <h4 style="font-size: 1.1rem; font-weight: 700; color: #14532d;">${a.name}</h4>
          <span style="font-size: 0.8rem; color: #64748b;">${a.species} • ${a.breed}</span>
        </div>
        <span class="tag-badge">🏷️ ${a.tag}</span>
      </div>
      <div class="animal-card-body">
        <p style="font-size: 0.85rem; color: #334155; margin-bottom: 6px;">
          <strong>Age/Sex:</strong> ${a.age} • ${a.sex} | <strong>Location:</strong> ${a.location}
        </p>
        <p style="font-size: 0.82rem; color: #475569; margin-bottom: 10px; font-style: italic;">
          "${a.notes}"
        </p>
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

// 10. TABS FOR BLUEPRINT EXPLORER
function initTabs() {
  const tabBtns = document.querySelectorAll(".tab-btn");
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      tabBtns.forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      const targetId = btn.getAttribute("data-tab");
      const targetPane = document.getElementById(targetId);
      if (targetPane) targetPane.classList.add("active");
    });
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
      const vet = document.getElementById("bookVetName").value;
      const farmerPhone = document.getElementById("bookPhone").value;
      const date = document.getElementById("bookDate").value;

      bookModal.classList.remove("active");
      bookForm.reset();
      showToast(`Appointment Request #${Math.floor(100000 + Math.random()*900000)} sent to ${vet}!`);
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

