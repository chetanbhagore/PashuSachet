# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Applying Phase 4: Para-Vet Verification Gate & Last-Mile Triage Queue...")

# 1. Inject #paravet-inbox section into index.html right after #vet-desk
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read().replace('\r\n', '\n')

paravet_section = """
  <!-- Para-Vet Verification Desk & Beat Queue (Phase 4 Gate) -->
  <section class="module-section" id="paravet-inbox" style="background: #f1f5f9; border-top: 2px solid #cbd5e1; border-bottom: 2px solid #cbd5e1;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" style="background: #0284c7; color: #ffffff;">Last-Mile Verification Gate</span>
        <h2 class="section-title">🧑‍⚕️ Para-Vet Beat Verification Desk (पशुमित्र / एलएसएस तपासणी कक्ष)</h2>
        <p class="section-subtitle">
          Review raw farmer micro-reports and USSD signals within your cluster beat. Verify clinical signs in under 30 seconds before signals reach the District Surveillance Board.
        </p>
      </div>

      <!-- Para-Vet Profile & Queue Metrics -->
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 16px 20px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <div style="font-size: 2.2rem; background: #e0f2fe; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
            🧑‍⚕️
          </div>
          <div>
            <div style="font-weight: 800; color: #0f172a; font-size: 1.05rem;">
              Ganesh Kale (पशुमित्र / Village Sentinel)
            </div>
            <div style="font-size: 0.82rem; color: #0369a1; font-weight: 600;">
              Reg ID: PV-AHM-9104 • Beat: Sangamner Cluster (5 Villages)
            </div>
          </div>
        </div>

        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
          <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 8px 14px; text-align: center;">
            <div id="pendingSignalCount" style="font-size: 1.25rem; font-weight: 800; color: #b91c1c;">2 Active</div>
            <div style="font-size: 0.72rem; color: #991b1b; font-weight: 600; text-transform: uppercase;">Pending Verification</div>
          </div>
          <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 8px 14px; text-align: center;">
            <div id="verifiedSignalCount" style="font-size: 1.25rem; font-weight: 800; color: #166534;">7 Confirmed</div>
            <div style="font-size: 0.72rem; color: #15803d; font-weight: 600; text-transform: uppercase;">Verified Today</div>
          </div>
          <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 8px 14px; text-align: center;">
            <div id="sampleSignalCount" style="font-size: 1.25rem; font-weight: 800; color: #1d4ed8;">2 Kits</div>
            <div style="font-size: 0.72rem; color: #1e40af; font-weight: 600; text-transform: uppercase;">Lab Samples Active</div>
          </div>
        </div>
      </div>

      <!-- Signals Queue Container -->
      <div id="paravetSignalsContainer" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 18px;">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </section>
"""

target_after_desk = '  </section>\n\n  <!-- Modal: Register New Animal -->'
if target_after_desk in html:
    html = html.replace(target_after_desk, '  </section>\n' + paravet_section + '\n  <!-- Modal: Register New Animal -->')
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Injected #paravet-inbox into index.html!")
else:
    print("Could not find insertion anchor for #paravet-inbox in index.html!")
    sys.exit(1)

# 2. Add Phase 4 Para-Vet Logic into js/app.js
with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read().replace('\r\n', '\n')

phase4_js = """
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
      <div style="grid-column: 1 / -1; background: #ffffff; border: 2px dashed #cbd5e1; border-radius: 12px; padding: 40px; text-align: center; color: #64748b;">
        <div style="font-size: 2.5rem; margin-bottom: 8px;">✅</div>
        <h4 style="color: #0f172a; margin: 0 0 4px;">All Signals Verified in Your Beat</h4>
        <p style="font-size: 0.85rem; margin: 0;">No pending farmer micro-reports requiring field confirmation right now.</p>
      </div>
    `;
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
"""

js += "\n" + phase4_js

# Ensure renderParavetInbox is called on init
if "renderParavetInbox();" not in js:
    js = js.replace("window.addEventListener('DOMContentLoaded', () => {", "window.addEventListener('DOMContentLoaded', () => {\n  renderParavetInbox();")

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Appended Phase 4 logic and initialized renderParavetInbox in js/app.js!")

