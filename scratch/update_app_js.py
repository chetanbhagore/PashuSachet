# -*- coding: utf-8 -*-
import sys

print("Updating js/app.js with complete food safety, vet care desk, qualitative bands, and emergency circuits...")

with open("js/app.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update i18n with nav_vet_desk
code = code.replace('nav_blueprint: "Blueprint",', 'nav_vet_desk: "Vet Care Desk",\n    nav_blueprint: "Blueprint",')
code = code.replace('nav_blueprint: "प्रकल्प आराखडा",', 'nav_vet_desk: "पशुवैद्यकीय डेस्क",\n    nav_blueprint: "प्रकल्प आराखडा",')
code = code.replace('nav_blueprint: "परियोजना रूपरेखा",', 'nav_vet_desk: "पशुचिकित्सा डेस्क",\n    nav_blueprint: "परियोजना रूपरेखा",')

# 2. Add prescription to Gauri in DEFAULT_ANIMALS
gauri_old = '''  {
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
  },'''

gauri_new = '''  {
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
  },'''

if gauri_old in code:
    code = code.replace(gauri_old, gauri_new)
    print("Added active clinical treatment and withdrawal clock to Gauri.")

# 3. Add Appointments and Cases data structures
data_helpers = '''
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
'''

code = code.replace('function getStoredAnimals() {', data_helpers + '\nfunction getStoredAnimals() {')
print("Added Appointments and Cases storage helpers.")

# 4. Enhance renderAnimals to include the Live Milk Withholding Countdown Alert
old_render_animals = '''function renderAnimals() {
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
}'''

new_render_animals = '''function renderAnimals() {
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
}'''

code = code.replace(old_render_animals, new_render_animals)
print("Updated renderAnimals with live milk withholding banner.")

# 5. Add updateWithdrawalClocks, renderVetDesk, switchRole, forwardCaseToVet, and prescribeModal handlers
vet_desk_handlers = '''
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
'''

code += '\n' + vet_desk_handlers
print("Appended vet desk handlers and withdrawal clock timers.")

# 6. Update evaluateSymptoms for Qualitative Bands and Red Flag Circuit Breaker
old_eval = '''  const hasFever = checkedBoxes.includes("fever") || tempDegree >= 103.5;
  const hasNodules = checkedBoxes.includes("skin_nodules");
  const hasMouthFoot = checkedBoxes.includes("mouth_lesions") || checkedBoxes.includes("lameness");
  const hasRespiratory = checkedBoxes.includes("cough") || checkedBoxes.includes("nasal_discharge");
  const hasMastitis = checkedBoxes.includes("udder_swelling") || checkedBoxes.includes("milk_drop");
  const hasDiarrhea = checkedBoxes.includes("diarrhea");'''

new_eval = '''  // RED-FLAG EMERGENCY CIRCUIT BREAKER
  const isRedFlag = checkedBoxes.includes("bleeding") || checkedBoxes.includes("sudden_death") || checkedBoxes.includes("recumbent");
  if (isRedFlag) {
    const emergModal = document.getElementById("emergencyModal");
    if (emergModal) emergModal.classList.add("active");
  }

  const hasFever = checkedBoxes.includes("fever") || tempDegree >= 103.5;
  const hasNodules = checkedBoxes.includes("skin_nodules");
  const hasMouthFoot = checkedBoxes.includes("mouth_lesions") || checkedBoxes.includes("lameness");
  const hasRespiratory = checkedBoxes.includes("cough") || checkedBoxes.includes("nasal_discharge");
  const hasMastitis = checkedBoxes.includes("udder_swelling") || checkedBoxes.includes("milk_drop");
  const hasDiarrhea = checkedBoxes.includes("diarrhea");'''

code = code.replace(old_eval, new_eval)

# Update the display of confidence in evaluateSymptoms to Qualitative Bands
old_conf_display = '''  diagConf.textContent = `${confidence}% Match`;
  confBar.style.width = `${confidence}%`;'''

new_conf_display = '''  let qualitativeBand = "Likely";
  if (confidence < 60) qualitativeBand = "Less Likely";
  else if (confidence < 75) qualitativeBand = "Possible";
  
  const bandContainer = document.getElementById("triageBandContainer");
  if (bandContainer) {
    bandContainer.textContent = `${qualitativeBand} Match (Band: ${urgency.toUpperCase()})`;
    bandContainer.className = `triage-band ${qualitativeBand === 'Likely' ? 'likely' : (qualitativeBand === 'Possible' ? 'possible' : 'unlikely')}`;
  }
  
  lastTriageResult = {
    condition: primaryCondition,
    band: qualitativeBand,
    symptoms: checkedBoxes
  };'''

code = code.replace(old_conf_display, new_conf_display)
print("Updated evaluateSymptoms with Qualitative Bands and Red Flag Circuit Breaker.")

# 7. Add prescribeForm submit listener in initModals
prescribe_form_listener = '''
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
'''

code = code.replace('// Appointment Modal', prescribe_form_listener + '\n  // Appointment Modal')

# Update bookForm submit handler to actually save the appointment
old_book_submit = '''    bookForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const vet = document.getElementById("bookVetName").value;
      const farmerPhone = document.getElementById("bookPhone").value;
      const date = document.getElementById("bookDate").value;

      bookModal.classList.remove("active");
      bookForm.reset();
      showToast(`Appointment Request #${Math.floor(100000 + Math.random()*900000)} sent to ${vet}!`);
    });'''

new_book_submit = '''    bookForm.addEventListener("submit", (e) => {
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
    });'''

code = code.replace(old_book_submit, new_book_submit)

# Also call renderVetDesk on initial load
code = code.replace('renderVets();', 'renderVets();\n  renderVetDesk();')

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated js/app.js successfully!")

