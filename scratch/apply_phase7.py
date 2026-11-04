# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Applying Phase 7: Live Village & Block Signal Board & One Health Sentinel...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read().replace('\r\n', '\n')

village_board_section = """
  <!-- Live Village & Block Signal Board (Phase 7 Participatory Layer) -->
  <section class="module-section" id="village-signal-board" style="background: #f8fafc; border-top: 2px solid #e2e8f0; border-bottom: 2px solid #e2e8f0;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" style="background: #0f766e; color: #ffffff;">Bottom-Up Participatory Telemetry</span>
        <h2 class="section-title">📍 Live Village &amp; Block Signal Board (स्थानिक गाव-पातळी निरीक्षण मंडळ)</h2>
        <p class="section-subtitle">
          Real-time ground truth signals collected from farmers and verified by local para-vets. This observation board complements macro-level NADRES forecasts with actionable village-level early warnings.
        </p>
      </div>

      <!-- One Health Inter-Agency Surveillance Stream -->
      <div id="oneHealthStreamBanner" style="background: #450a0a; border: 1.5px solid #dc2626; border-radius: 10px; padding: 12px 18px; margin-bottom: 20px; color: #fecaca; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 1.3rem;">☣️</span>
          <div>
            <strong style="color: #f87171; font-size: 0.9rem;">ONE HEALTH INTER-AGENCY LIVE SENTINEL:</strong>
            <span style="font-size: 0.85rem; margin-left: 6px;" id="oneHealthStreamText">
              Active zoonotic monitoring in Ahmednagar district. Auto-sync linked with District Health Officer (DHO) and Public Health Department.
            </span>
          </div>
        </div>
        <span style="background: #7f1d1d; color: #fca5a5; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">
          DPDP ACT COMPLIANT
        </span>
      </div>

      <!-- Live Signals Grid with k-Anonymity Privacy -->
      <div style="margin-bottom: 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <h3 style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin: 0;">
            Active Verified Village Signals &amp; Cluster Surveillance
          </h3>
          <span style="font-size: 0.8rem; color: #0f766e; font-weight: 700; background: #ccfbf1; padding: 3px 10px; border-radius: 6px;">
            🔒 k-Anonymity (<3 Signals) Active
          </span>
        </div>
        <div id="villageSignalsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px;">
          <!-- Injected via JavaScript -->
        </div>
      </div>

      <!-- District Officer Morning Decision Queue ("Cases Requiring Action Today") -->
      <div style="background: #ffffff; border: 2px solid #cbd5e1; border-radius: 12px; padding: 20px; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 10px;">
          <div>
            <span style="font-size: 0.75rem; font-weight: 800; background: #e0e7ff; color: #3730a3; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">
              District Officer Console
            </span>
            <h3 style="font-size: 1.2rem; font-weight: 800; color: #0f172a; margin: 4px 0 0;">
              🌅 Morning Decision Queue: Cases Requiring Action Today
            </h3>
          </div>
          <div style="font-size: 0.82rem; color: #475569;">
            Officer: <strong>Dr. S. R. Shinde (DVO Ahmednagar)</strong>
          </div>
        </div>

        <div id="officerDecisionQueue" style="display: flex; flex-direction: column; gap: 12px;">
          <!-- Injected via JavaScript -->
        </div>
      </div>
    </div>
  </section>
"""

# Add to navigation
nav_target = '<li><a href="#outbreak-gis" data-i18n="nav_risk">Outbreak Risk GIS</a></li>'
nav_replacement = '<li><a href="#outbreak-gis" data-i18n="nav_risk">Outbreak Risk GIS</a></li>\n        <li><a href="#village-signal-board">Village Signals</a></li>'

if nav_target in html and '#village-signal-board' not in html:
    html = html.replace(nav_target, nav_replacement)

# Inject after outbreak-gis
target_gis_end = '    </div>\n  </section>\n\n  <!-- Digital Pashu Aadhar & Health Passport -->'
if target_gis_end in html:
    html = html.replace(target_gis_end, '    </div>\n  </section>\n' + village_board_section + '\n  <!-- Digital Pashu Aadhar & Health Passport -->')
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Injected #village-signal-board into index.html!")
else:
    print("Could not find target anchor for #village-signal-board in index.html!")
    sys.exit(1)

# 2. Add styles to css/style.css
with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read().replace('\r\n', '\n')

phase7_css = """
/* Phase 7: Village Signal Board & Decision Queue */
.village-signal-card {
  background: #ffffff;
  border: 1.5px solid #cbd5e1;
  border-radius: 10px;
  padding: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.surge-alert-pill {
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #fca5a5;
  font-size: 0.74rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 4px;
  display: inline-block;
  animation: pulse-border 1.5s infinite;
}
.decision-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #0f766e;
  border-radius: 8px;
  padding: 14px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
"""

if ".village-signal-card" not in css:
    css += "\n" + phase7_css
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Added Phase 7 styles to css/style.css!")

# 3. Add Phase 7 logic into js/app.js
with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read().replace('\r\n', '\n')

phase7_js = """
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
    <div class="decision-card">
      <div style="max-width: 650px;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
          <strong style="color: #0f172a; font-size: 0.95rem;">${dec.title}</strong>
          <span style="font-size: 0.72rem; font-weight: 800; background: ${dec.priority === 'CRITICAL_ZOONOTIC' ? '#fecaca' : '#fef3c7'}; color: ${dec.priority === 'CRITICAL_ZOONOTIC' ? '#991b1b' : '#92400e'}; padding: 2px 6px; border-radius: 4px;">
            ${dec.priority}
          </span>
        </div>
        <p style="font-size: 0.82rem; color: #475569; margin: 0; line-height: 1.4;">
          ${dec.details}
        </p>
      </div>

      <div>
        ${dec.status === 'PENDING' ? `
          <button type="button" class="btn btn-sm btn-primary" onclick="resolveOfficerDecision('${dec.id}')" style="background: #0f766e; white-space: nowrap;">
            ✓ ${dec.actionLabel}
          </button>
        ` : `
          <span style="color: #15803d; font-weight: 700; font-size: 0.85rem;">
            ✓ Action Authorized
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
"""

js += "\n" + phase7_js

if "renderVillageSignalBoard();" not in js:
    js = js.replace("window.addEventListener('DOMContentLoaded', () => {", "window.addEventListener('DOMContentLoaded', () => {\n  renderVillageSignalBoard();\n  renderOfficerDecisionQueue();")

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Appended Phase 7 logic and initialized village signals & officer queue in js/app.js!")

