# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Applying Phase 6: Closed-Loop Diagnostic Sample Tracker (RDDL Pune Pipeline)...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read().replace('\r\n', '\n')

sample_tracker_section = """
  <!-- Closed-Loop Diagnostic Sample Tracker (Phase 6 RDDL Pipeline) -->
  <section class="module-section" id="sample-tracker" style="background: #ffffff; border-top: 2px solid #e2e8f0; border-bottom: 2px solid #e2e8f0;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" style="background: #7c3aed; color: #ffffff;">Closed-Loop Disease Surveillance</span>
        <h2 class="section-title">🧪 Closed-Loop Diagnostic Sample Tracker (प्रयोगशाळा नमुना ट्रॅकर)</h2>
        <p class="section-subtitle">
          End-to-end biological sample lifecycle tracking from village cow-shed collection to Regional Disease Diagnostic Laboratory (RDDL Pune) results and field biosecurity closure.
        </p>
      </div>

      <!-- Live Samples Grid -->
      <div id="sampleCardsContainer" style="display: flex; flex-direction: column; gap: 20px;">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </section>
"""

# Add to navigation
nav_target = '<li><a href="#vet-desk" data-i18n="nav_vet_desk">Vet Care Desk</a></li>'
nav_replacement = '<li><a href="#vet-desk" data-i18n="nav_vet_desk">Vet Care Desk</a></li>\n        <li><a href="#sample-tracker">Sample Tracker</a></li>'

if nav_target in html and '#sample-tracker' not in html:
    html = html.replace(nav_target, nav_replacement)

# Inject after paravet-inbox
target_anchor = '    </div>\n  </section>\n\n  <!-- Modal: Register New Animal -->'
if target_anchor in html:
    html = html.replace(target_anchor, '    </div>\n  </section>\n' + sample_tracker_section + '\n  <!-- Modal: Register New Animal -->')
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Injected #sample-tracker into index.html!")
else:
    print("Could not find target anchor in index.html!")
    sys.exit(1)

# 2. Add styles to css/style.css
with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read().replace('\r\n', '\n')

phase6_css = """
/* Phase 6: Closed-Loop Sample Tracker */
.sample-tracker-card {
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}
.sample-stepper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin: 24px 0 18px;
}
.sample-stepper::before {
  content: '';
  position: absolute;
  top: 14px;
  left: 30px;
  right: 30px;
  height: 3px;
  background: #e2e8f0;
  z-index: 1;
}
.sample-step {
  position: relative;
  z-index: 2;
  text-align: center;
  flex: 1;
}
.step-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #f1f5f9;
  border: 2px solid #cbd5e1;
  color: #64748b;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 6px;
  font-size: 0.85rem;
  font-weight: 700;
}
.sample-step.completed .step-circle {
  background: #15803d;
  border-color: #15803d;
  color: #ffffff;
}
.sample-step.active .step-circle {
  background: #7c3aed;
  border-color: #6d28d9;
  color: #ffffff;
  box-shadow: 0 0 0 4px rgba(124, 58, 237, 0.2);
}
.step-label {
  font-size: 0.76rem;
  font-weight: 600;
  color: #64748b;
}
.sample-step.completed .step-label {
  color: #15803d;
}
.sample-step.active .step-label {
  color: #7c3aed;
  font-weight: 700;
}
.coldchain-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  color: #1e40af;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 6px;
}
"""

if ".sample-tracker-card" not in css:
    css += "\n" + phase6_css
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Added Phase 6 styles to css/style.css!")

# 3. Add Phase 6 logic into js/app.js
with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read().replace('\r\n', '\n')

phase6_js = """
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
"""

js += "\n" + phase6_js

if "renderSampleTracker();" not in js:
    js = js.replace("window.addEventListener('DOMContentLoaded', () => {", "window.addEventListener('DOMContentLoaded', () => {\n  renderSampleTracker();")

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Appended Phase 6 logic and initialized renderSampleTracker in js/app.js!")

