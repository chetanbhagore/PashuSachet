# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Executing Phase 2: Ultra-Inclusive Intake, 90-Sec Flow, USSD, Missed-Call & Proxy Reporting...")

# 1. ADD CSS STYLES FOR LOW-DIGITAL INCLUSION & USSD
ussd_css = '''
/* Phase 2: Low-Digital Inclusion & USSD Styles */
.inclusion-channel-bar {
  background: #f0fdf4;
  border: 2px dashed #16a34a;
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
.channel-buttons-group {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.channel-btn {
  background: #ffffff;
  border: 1.5px solid #16a34a;
  color: #15803d;
  font-weight: 700;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 0.85rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}
.channel-btn:hover {
  background: #15803d;
  color: #ffffff;
}

/* Feature Phone USSD Simulation Screen */
.ussd-screen {
  background: #0f172a;
  color: #22c55e;
  font-family: 'Consolas', 'Courier New', monospace;
  padding: 20px;
  border-radius: 12px;
  border: 4px solid #334155;
  box-shadow: inset 0 0 10px rgba(0,0,0,0.8);
  min-height: 220px;
}
.ussd-header {
  border-bottom: 1px dashed #334155;
  padding-bottom: 8px;
  margin-bottom: 12px;
  font-size: 0.85rem;
  color: #94a3b8;
  display: flex;
  justify-content: space-between;
}
.ussd-content {
  font-size: 0.95rem;
  line-height: 1.6;
  white-space: pre-wrap;
}
.ussd-input-row {
  display: flex;
  gap: 8px;
  margin-top: 14px;
}
.ussd-input {
  background: #1e293b;
  border: 1px solid #22c55e;
  color: #22c55e;
  font-family: monospace;
  font-size: 1.1rem;
  padding: 6px 12px;
  border-radius: 4px;
  width: 80px;
  outline: none;
}
.ussd-send-btn {
  background: #22c55e;
  color: #0f172a;
  border: none;
  font-weight: 800;
  padding: 6px 16px;
  border-radius: 4px;
  cursor: pointer;
}
'''

with open("css/style.css", "a", encoding="utf-8") as f:
    f.write("\n" + ussd_css)
print("Appended Phase 2 CSS styles.")

# 2. UPDATE INDEX.HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Low-Digital Inclusion Bar right inside #symptom-screening container
screening_header_marker = '<div class="section-header">\n        <span class="section-tag">Participatory Early Warning</span>'

inclusion_bar = '''      <!-- Low-Digital Inclusion Multi-Channel Feeder Bar -->
      <div class="inclusion-channel-bar">
        <div>
          <span style="font-size: 0.78rem; font-weight: 800; color: #166534; text-transform: uppercase; letter-spacing: 0.5px;">
            सर्वांसाठी विनामूल्य सेवा (100% Free Rural Channels)
          </span>
          <h3 style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin: 2px 0;">
            स्मार्टफोन किंवा इंटरनेट नाही? तरीही 60 सेकंदात नोंद करा
          </h3>
          <p style="font-size: 0.82rem; color: #475569;">
            साध्या ₹1000 च्या फोनवरून मिस कॉल किंवा USSD द्वारे थेट नोंदणी करा.
          </p>
        </div>
        <div class="channel-buttons-group">
          <button type="button" class="channel-btn" onclick="openMissedCallModal()">
            📞 मिस कॉल: 1800-889-1962
          </button>
          <button type="button" class="channel-btn" onclick="openUssdModal()">
            📱 USSD कोड: *992#
          </button>
          <button type="button" class="channel-btn" onclick="startVoiceSimulation()">
            🎙️ येथे बोला (Marathi Voice)
          </button>
        </div>
      </div>
'''

if screening_header_marker in html:
    html = html.replace(screening_header_marker, inclusion_bar + '\n      ' + screening_header_marker)
    print("Injected Low-Digital Inclusion Bar into #symptom-screening.")

# Add Proxy Reporting & Mortality Controls to the Screening Form
proxy_form_group = '''
            <!-- Proxy Reporting & Mortality Controls -->
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px; margin-bottom: 16px;">
              <div style="font-weight: 700; font-size: 0.85rem; color: #0f172a; margin-bottom: 8px;">
                नोंदणी प्रकार व संख्या (Reporting Options &amp; Mortality Flag)
              </div>
              <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 10px;">
                <label style="display: flex; align-items: center; gap: 6px; font-size: 0.85rem; color: #334155; cursor: pointer;">
                  <input type="checkbox" id="isProxyCheck" onchange="toggleProxyFields()">
                  मी शेजारी किंवा कुटुंबियांच्या वतीने नोंदवत आहे (Proxy Report)
                </label>
                <label style="display: flex; align-items: center; gap: 6px; font-size: 0.85rem; color: #b91c1c; font-weight: 700; cursor: pointer;">
                  <input type="checkbox" id="isMortalityCheck" onchange="toggleMortalityWarning()">
                  जनावर आधीच दगावले आहे (Post-Loss / Mortality Report)
                </label>
              </div>

              <!-- Proxy Contact Fields (Hidden by default) -->
              <div id="proxyFieldsBox" style="display: none; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px; margin-bottom: 10px;">
                <div class="form-row">
                  <div class="form-group">
                    <label for="proxyOwnerName">जनावराच्या मालकाचे नाव (Owner Name) *</label>
                    <input type="text" id="proxyOwnerName" class="form-control" placeholder="उदा. नामदेव पाटील">
                  </div>
                  <div class="form-group">
                    <label for="proxyPhone">मालकाचा संपर्क नंबर (Owner Mobile) *</label>
                    <input type="tel" id="proxyPhone" class="form-control" placeholder="98220 12345">
                  </div>
                </div>
              </div>

              <!-- Steppers for Affected and Dead Count -->
              <div class="form-row">
                <div class="form-group">
                  <label for="affectedCount">बाधित जनावरांची संख्या (Number Affected) *</label>
                  <input type="number" id="affectedCount" class="form-control" value="1" min="1" max="50">
                </div>
                <div class="form-group">
                  <label for="deadCount">मृत जनावरांची संख्या (Number Dead) *</label>
                  <input type="number" id="deadCount" class="form-control" value="0" min="0" max="20">
                </div>
              </div>
            </div>
'''

onset_marker = '            <!-- Step 3: Onset, Duration & Vitals -->'
if onset_marker in html:
    html = html.replace(onset_marker, proxy_form_group + '\n' + onset_marker)
    print("Injected Proxy Reporting & Mortality Controls into Screening Form.")

# Add Missed Call Modal & USSD Modal before Footer
feeder_modals = '''
  <!-- Missed Call Simulation Modal -->
  <div class="modal-overlay" id="missedCallModal">
    <div class="modal-card" style="max-width: 520px;">
      <div class="modal-header">
        <h3 style="color: #15803d;">📞 24×7 Missed Call Reporting (1800-889-1962)</h3>
        <button class="modal-close" onclick="closeMissedCallModal()">&times;</button>
      </div>
      <div class="modal-body" style="text-align: center;">
        <div style="font-size: 3rem; margin: 10px 0;">📲</div>
        <h4 style="font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 6px;">
          मिस कॉल नोंदणी प्रात्यक्षिक (Live Simulation)
        </h4>
        <p style="font-size: 0.85rem; color: #475569; margin-bottom: 16px;">
          शेतकऱ्याने <strong>1800-889-1962</strong> वर कॉल करताच दोन रिंगनंतर कॉल आपोआप कट होतो आणि प्रणालीकडून 60 सेकंदात मोफत कॉल येतो.
        </p>

        <div id="missedCallStatusBox" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 14px; text-align: left; margin-bottom: 16px;">
          <div style="font-size: 0.82rem; color: #64748b; font-weight: 600;">दूरध्वनी स्थिती (Call Telemetry):</div>
          <div id="missedCallLog" style="font-size: 0.9rem; font-weight: 700; color: #15803d; margin-top: 4px;">
            [1/3] मिस कॉल आला: +91 98220 12345 (संगमनेर)...
          </div>
        </div>

        <div style="display: flex; gap: 10px; justify-content: center;">
          <button type="button" class="btn btn-outline" onclick="closeMissedCallModal()">बंद करा (Close)</button>
          <button type="button" class="btn btn-primary" onclick="simulateMissedCallCallback()" style="background: #15803d;">
            कॉल सुरू करा (Simulate Inbound Call)
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- USSD Feature Phone (*992#) Simulation Modal -->
  <div class="modal-overlay" id="ussdModal">
    <div class="modal-card" style="max-width: 480px; background: #0b1120;">
      <div class="modal-header" style="border-color: #334155;">
        <h3 style="color: #22c55e; font-family: monospace;">📱 USSD (*992#) Feature Phone Terminal</h3>
        <button class="modal-close" onclick="closeUssdModal()" style="color: #94a3b8;">&times;</button>
      </div>
      <div class="modal-body">
        <div class="ussd-screen">
          <div class="ussd-header">
            <span>GSM SERVICE 2G</span>
            <span>CELL: AHM-91</span>
          </div>
          <div class="ussd-content" id="ussdText">
PashuSachet Gram Signal (Maharashtra)
1. गाय / म्हैस (Cattle/Buffalo)
2. शेळी / मेंढी (Goat/Sheep)
3. कुक्कुटपालन (Poultry)
4. तक्रार स्थिती पहा (Check Status)
          </div>
        </div>
        <div class="ussd-input-row">
          <input type="text" id="ussdUserInput" class="ussd-input" placeholder="1-4" maxlength="1" autofocus>
          <button type="button" class="ussd-send-btn" onclick="submitUssdStep()">SEND</button>
          <button type="button" class="btn btn-outline btn-sm" onclick="resetUssd()" style="color: #94a3b8; border-color: #475569;">RESET</button>
        </div>
      </div>
    </div>
  </div>
'''

if '  <!-- Footer -->' in html:
    html = html.replace('  <!-- Footer -->', feeder_modals + '\n  <!-- Footer -->')
    print("Injected Missed-Call & USSD Simulation Modals.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved updated index.html for Phase 2!")

# 3. UPDATE JS/APP.JS WITH PHASE 2 LOGIC
with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

phase2_js = '''
// ========================================================
// PHASE 2: ULTRA-INCLUSIVE INTAKE & SIMULATIONS
// ========================================================

function openMissedCallModal() {
  const modal = document.getElementById("missedCallModal");
  if (modal) modal.classList.add("active");
  const log = document.getElementById("missedCallLog");
  if (log) log.innerHTML = "[1/3] मिस कॉल नोंदवला गेला: +91 98220 12345 (संगमनेर)...";
}

function closeMissedCallModal() {
  document.getElementById("missedCallModal")?.classList.remove("active");
}

function simulateMissedCallCallback() {
  const log = document.getElementById("missedCallLog");
  if (!log) return;
  log.innerHTML = "<span style='color:#0284c7;'>[2/3] कॉलबॅक जोडला गेला... मराठी व्हॉईस मेनू वाजत आहे: 'नमस्कार शेतकरी बांधवांनो, जनावराचा प्रकार निवडा...'</span>";
  setTimeout(() => {
    log.innerHTML = "<span style='color:#15803d;'>[3/3] ✓ तक्रार यशस्वीरित्या नोंदवली गेली! पावती क्रमांक #MC-MH-9142. स्थानिक पशुसखी गणेश काळे यांना SMS अलर्ट पाठवला.</span>";
    showToast("मिस कॉलद्वारे अहवाल यशस्वीरित्या नोंदवला गेला! (Missed call report logged)");
  }, 1600);
}

// USSD Terminal State Machine (*992#)
let ussdStep = 1;
function openUssdModal() {
  document.getElementById("ussdModal")?.classList.add("active");
  resetUssd();
}

function closeUssdModal() {
  document.getElementById("ussdModal")?.classList.remove("active");
}

function resetUssd() {
  ussdStep = 1;
  const ussdText = document.getElementById("ussdText");
  if (ussdText) {
    ussdText.textContent = "PashuSachet Gram Signal (Maharashtra)\\n1. गाय / म्हैस (Cattle/Buffalo)\\n2. शेळी / मेंढी (Goat/Sheep)\\n3. कुक्कुटपालन (Poultry)\\n4. तक्रार स्थिती पहा (Check Status)";
  }
  const input = document.getElementById("ussdUserInput");
  if (input) { input.value = ""; input.focus(); }
}

function submitUssdStep() {
  const input = document.getElementById("ussdUserInput");
  const ussdText = document.getElementById("ussdText");
  if (!input || !ussdText) return;
  const val = input.value.trim();
  input.value = "";

  if (ussdStep === 1) {
    if (val === "4") {
      ussdText.textContent = "तक्रार #MH-24-9812:\\nस्थिती: औषधोपचार सुरू\\nदूध बंदी: 72 तास बाकी\\nडॉक्टर: डॉ. रमेश कुटे (LDO)";
      ussdStep = 99;
    } else {
      ussdText.textContent = "दिसणारे मुख्य लक्षण निवडा:\\n1. ताप व अंगावर गाठी (Fever/Nodules)\\n2. लाळ व तोंडात फोड (Mouth/Foot Blisters)\\n3. कास सुजणे व दूध घट (Udder Swelling)\\n4. अचानक मृत्यू (Sudden Mortality)";
      ussdStep = 2;
    }
  } else if (ussdStep === 2) {
    ussdText.textContent = "बाधित जनावरांची संख्या टाका (1-9):";
    ussdStep = 3;
  } else if (ussdStep === 3) {
    const ticketId = "USSD-MH-" + Math.floor(1000 + Math.random()*9000);
    ussdText.textContent = `धन्यवाद!\\nपावती क्रमांक: ${ticketId}\\nपॅरा-व्हेट गणेश काळे 4 तासात तपासणी करतील.\\nतातडीसाठी 1962 डायल करा.`;
    ussdStep = 99;
    showToast(`USSD अहवाल नोंदवला: ${ticketId}`);
  } else {
    resetUssd();
  }
}

function startVoiceSimulation() {
  showToast("🎙️ मराठी व्हॉईस रेकॉर्डिंग सुरू... 15 सेकंद बोला (Recording audio)...");
  setTimeout(() => {
    showToast("✓ व्हॉईस नोटचे रूपांतर झाले: 'गाय आजारी आहे, ताप आणि कास सुजली आहे'");
    const udderCb = document.querySelector('input[name="symptom"][value="udder_swelling"]');
    const feverCb = document.querySelector('input[name="symptom"][value="fever"]');
    if (udderCb) udderCb.checked = true;
    if (feverCb) feverCb.checked = true;
    evaluateSymptoms();
  }, 1800);
}

function toggleProxyFields() {
  const cb = document.getElementById("isProxyCheck");
  const box = document.getElementById("proxyFieldsBox");
  if (box && cb) {
    box.style.display = cb.checked ? "block" : "none";
  }
}

function toggleMortalityWarning() {
  const cb = document.getElementById("isMortalityCheck");
  const deadInput = document.getElementById("deadCount");
  if (cb && cb.checked) {
    if (deadInput) deadInput.value = "1";
    showToast("⚠️ मृत जनावराची नोंद: जैविक सुरक्षा नियम लागू (Mortality protocol active)");
    document.getElementById("emergencyModal")?.classList.add("active");
  }
}
'''

js = phase2_js + '\n' + js
with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Saved updated js/app.js for Phase 2!")

