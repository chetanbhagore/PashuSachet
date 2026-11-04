# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read().replace('\r\n', '\n')

# 1. Update the species grid and add digital inclusion bar & symptom tags
old_species_block = """        <div class="interactive-body">
          <form id="symptomForm">
            <!-- Step 1: Species Selection -->
            <div class="form-step-title">
              <span class="step-num">1</span>
              <span data-i18n="step1">1. Select Animal Species</span>
            </div>

            <div class="species-grid">
              <label class="species-option">
                <input type="radio" name="species" value="cattle" checked>
                <div class="species-card">
                  <span class="emoji">🐄</span>
                  <span class="title">Cattle</span>
                  <span class="sub">गाय / Cow</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="buffalo">
                <div class="species-card">
                  <span class="emoji">🐃</span>
                  <span class="title">Buffalo</span>
                  <span class="sub">म्हैस</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="goat">
                <div class="species-card">
                  <span class="emoji">🐐</span>
                  <span class="title">Goat</span>
                  <span class="sub">शेळी</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="sheep">
                <div class="species-card">
                  <span class="emoji">🐑</span>
                  <span class="title">Sheep</span>
                  <span class="sub">मेंढी</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="poultry">
                <div class="species-card">
                  <span class="emoji">🐔</span>
                  <span class="title">Poultry</span>
                  <span class="sub">कुक्कुटपालन</span>
                </div>
              </label>
            </div>

            <!-- Step 2: Observed Symptoms -->
            <div class="form-step-title">
              <span class="step-num">2</span>
              <span data-i18n="step2">2. Observed Clinical Symptoms (Select all that apply)</span>
            </div>"""

new_species_block = """        <div class="interactive-body">
          <!-- Low-Digital Inclusion Quick Actions Bar -->
          <div class="digital-inclusion-bar" style="background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%); border: 1.5px solid #86efac; border-radius: 12px; padding: 14px 18px; margin-bottom: 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px;">
            <div>
              <div style="font-weight: 800; color: #166534; font-size: 0.95rem; display: flex; align-items: center; gap: 6px;">
                <span>⚡ अति-सुलभ तक्रार नोंदणी (Zero Smartphone / Low-Literacy Channels)</span>
              </div>
              <div style="font-size: 0.82rem; color: #15803d;">
                स्मार्टफोन नाही किंवा इंटरनेट कमजोर? साध्या फोनवरून ९० सेकंदात कॉल किंवा मेसेजने नोंदवा.
              </div>
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <button type="button" class="btn btn-sm" id="missedCallTriggerBtn" onclick="openMissedCallModal()" style="background: #15803d; color: #ffffff; font-weight: 700; border-radius: 8px;">
                📞 Missed Call 1800-889-1962
              </button>
              <button type="button" class="btn btn-sm" id="ussdTriggerBtn" onclick="openUssdModal()" style="background: #0f766e; color: #ffffff; font-weight: 700; border-radius: 8px;">
                📱 USSD *992#
              </button>
              <button type="button" class="btn btn-sm" id="voiceIvrBtn" onclick="openVoiceIvrModal()" style="background: #0284c7; color: #ffffff; font-weight: 700; border-radius: 8px;">
                🎙️ Marathi Voice IVR
              </button>
            </div>
          </div>

          <form id="symptomForm">
            <!-- Hidden synchronizer for current species -->
            <input type="hidden" id="animalSpecies" value="cattle">

            <!-- Step 1: Species Selection (9 Primary Species) -->
            <div class="form-step-title">
              <span class="step-num">1</span>
              <span data-i18n="step1">1. Select Animal Species (९ प्रमुख पशू प्रजाती)</span>
            </div>

            <div class="species-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(105px, 1fr)); gap: 8px;">
              <label class="species-option">
                <input type="radio" name="species" value="cattle" checked onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐄</span>
                  <span class="title">Cattle</span>
                  <span class="sub">गाय / Cow</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="buffalo" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐃</span>
                  <span class="title">Buffalo</span>
                  <span class="sub">म्हैस</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="goat" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐐</span>
                  <span class="title">Goat</span>
                  <span class="sub">शेळी</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="sheep" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐑</span>
                  <span class="title">Sheep</span>
                  <span class="sub">मेंढी</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="poultry" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐔</span>
                  <span class="title">Poultry</span>
                  <span class="sub">कुक्कुटपालन</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="pig" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐖</span>
                  <span class="title">Pig</span>
                  <span class="sub">डुक्कर</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="horse" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐴</span>
                  <span class="title">Equine</span>
                  <span class="sub">घोडा / गाढव</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="camel" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐪</span>
                  <span class="title">Camel</span>
                  <span class="sub">उंट</span>
                </div>
              </label>

              <label class="species-option">
                <input type="radio" name="species" value="dog" onchange="syncSpecies(this.value)">
                <div class="species-card">
                  <span class="emoji">🐕</span>
                  <span class="title">Canine</span>
                  <span class="sub">श्वान</span>
                </div>
              </label>
            </div>

            <!-- Step 2: Observed Symptoms -->
            <div class="form-step-title" style="margin-top: 20px;">
              <span class="step-num">2</span>
              <span data-i18n="step2">2. Observed Clinical Symptoms (Select all that apply)</span>
            </div>

            <!-- Quick symptom tag filter container -->
            <div id="symptomTagsContainer" class="symptom-tags-bar" style="margin-bottom: 12px; display: flex; gap: 6px; flex-wrap: wrap;">
              <span class="tag-chip" style="font-size: 0.75rem; background: #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 4px;">वारंवार विचारली जाणारी लक्षणे (Common Signs):</span>
              <button type="button" class="quick-tag-btn" onclick="toggleSymptomVal('fever')" style="font-size: 0.75rem; border: 1px solid #cbd5e1; background: #ffffff; border-radius: 4px; padding: 2px 8px; cursor: pointer;">ताप (Fever)</button>
              <button type="button" class="quick-tag-btn" onclick="toggleSymptomVal('mouth_lesions')" style="font-size: 0.75rem; border: 1px solid #cbd5e1; background: #ffffff; border-radius: 4px; padding: 2px 8px; cursor: pointer;">तोंडातील फोड (Mouth Ulcers)</button>
              <button type="button" class="quick-tag-btn" onclick="toggleSymptomVal('skin_nodules')" style="font-size: 0.75rem; border: 1px solid #cbd5e1; background: #ffffff; border-radius: 4px; padding: 2px 8px; cursor: pointer;">गाठी (Lumps)</button>
              <button type="button" class="quick-tag-btn" onclick="toggleSymptomVal('sudden_death')" style="font-size: 0.75rem; border: 1px solid #cbd5e1; background: #ffffff; border-radius: 4px; padding: 2px 8px; cursor: pointer;">अचानक मृत्यू (Sudden Death)</button>
            </div>"""

if old_species_block in content:
    content = content.replace(old_species_block, new_species_block)
    print("Replaced species and added inclusion bar & symptom tags!")
else:
    print("Could not find old species block!")
    sys.exit(1)

# 2. Update Step 3 to add affectedCount, villageLocation, isMortalityCheck, isProxyCheck
old_step3_block = """            <!-- Step 3: Vitals & Duration -->
            <div class="form-step-title">
              <span class="step-num">3</span>
              <span data-i18n="step3">3. Onset &amp; Vital Parameters</span>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="onsetDays">Symptom Onset (Days ago)</label>
                <select id="onsetDays" class="form-control">
                  <option value="1">Today (&lt; 24 hrs)</option>
                  <option value="2" selected>2 - 3 Days ago</option>
                  <option value="5">4 - 7 Days ago</option>
                  <option value="10">More than a week</option>
                </select>
              </div>

              <div class="form-group">
                <label for="tempInput">Body Temperature (°F) (Approx)</label>
                <input type="number" step="0.1" id="tempInput" class="form-control" value="103.5" placeholder="e.g. 102.5">
              </div>

              <div class="form-group">
                <label for="pashuTag">Animal Pashu Tag / Aadhar (Optional)</label>
                <input type="text" id="pashuTag" class="form-control" placeholder="e.g. MH-24-9812">
              </div>
            </div>"""

new_step3_block = """            <!-- Step 3: Vitals, Scale & Location -->
            <div class="form-step-title">
              <span class="step-num">3</span>
              <span data-i18n="step3">3. Onset, Scale &amp; Location (कालावधी, संख्या आणि ठिकाण)</span>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="onsetDays">लक्षणे कधीपासून आहेत? (Onset) *</label>
                <select id="onsetDays" class="form-control">
                  <option value="1">आजपासून (< 24 तास)</option>
                  <option value="2" selected>२ - ३ दिवस (2 - 3 Days ago)</option>
                  <option value="5">४ - ७ दिवस (4 - 7 Days ago)</option>
                  <option value="10">एक आठवड्यापेक्षा जास्त (Week+)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="affectedCount">बाधित जनावरांची संख्या (Affected Count) *</label>
                <input type="number" id="affectedCount" class="form-control" value="1" min="1" max="500" required>
              </div>

              <div class="form-group">
                <label for="villageLocation">गाव व तालुका (Village / Beat) *</label>
                <select id="villageLocation" class="form-control" required>
                  <option value="Sangamner Khurd (संगमनेर खुर्द)" selected>Sangamner Khurd (संगमनेर खुर्द)</option>
                  <option value="Rahata (राहाता)">Rahata (राहाता)</option>
                  <option value="Shirdi Rural (शिर्डी ग्रामीण)">Shirdi Rural (शिर्डी ग्रामीण)</option>
                  <option value="Akole (अकोले)">Akole (अकोले)</option>
                  <option value="Kopargaon (कोपरगाव)">Kopargaon (कोपरगाव)</option>
                  <option value="Shrirampur (श्रीरामपूर)">Shrirampur (श्रीरामपूर)</option>
                  <option value="Newasa (नेवासा)">Newasa (नेवासा)</option>
                  <option value="Parner (पारनेर)">Parner (पारनेर)</option>
                </select>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="tempInput">तापमान (°F) (Temperature - Optional)</label>
                <input type="number" step="0.1" id="tempInput" class="form-control" value="103.5" placeholder="उदा. 102.5">
              </div>

              <div class="form-group">
                <label for="pashuTag">पशू आधार / टॅग क्रमांक (Pashu Aadhar Tag)</label>
                <input type="text" id="pashuTag" class="form-control" placeholder="उदा. MH-24-9812 किंवा 12-digit tag">
              </div>
            </div>

            <!-- Urgent Mortality Indicator (Post-Loss Biosecurity Alert) -->
            <div style="background: #fff1f2; border: 1.5px solid #fecdd3; border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
              <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; font-weight: 700; color: #9f1239; margin: 0;">
                <input type="checkbox" id="isMortalityCheck" onchange="toggleMortalityFields(this.checked)">
                <span>⚠️ जनावर आधीच दगावले आहे का? (Animal already deceased / Post-Loss Mortality)</span>
              </label>
              <div id="mortalityCountBox" style="display: none; margin-top: 10px; padding-top: 10px; border-top: 1px dashed #f43f5e;">
                <div style="display: flex; align-items: center; gap: 12px;">
                  <label for="mortalityCountInput" style="font-size: 0.82rem; color: #881337; font-weight: 600;">दगावलेल्या जनावरांची संख्या (Deceased Count):</label>
                  <input type="number" id="mortalityCountInput" class="form-control" value="1" min="1" style="max-width: 140px;">
                </div>
                <span style="font-size: 0.78rem; color: #e11d48; display: block; margin-top: 6px; font-weight: 600;">
                  🛑 तातडीची जैवसुरक्षा सूचना: शव उघडू नका (No Cut), पाण्याचे स्त्रोत दूषित होणार नाहीत याची दक्षता घ्या. पशुवैद्यकीय पथक तत्काळ रवाना केले जाईल.
                </span>
              </div>
            </div>

            <!-- Proxy Reporting Indicator -->
            <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; margin-top: 10px;">
              <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; font-weight: 700; color: #334155; margin: 0;">
                <input type="checkbox" id="isProxyCheck" onchange="toggleProxyFields(this.checked)">
                <span>👥 दुसऱ्या पशुपालकाच्या वतीने नोंदणी? (Report on behalf of elder/neighbor/community)</span>
              </label>
              <div id="proxyFieldsBox" style="display: none; margin-top: 10px; padding-top: 10px; border-top: 1px dashed #cbd5e1;">
                <div class="form-row">
                  <div class="form-group">
                    <label for="proxyReporterName">नोंदणी करणाऱ्याचे नाव (Reporter Name) *</label>
                    <input type="text" id="proxyReporterName" class="form-control" placeholder="उदा. विशाल थोरात (शेजारी)">
                  </div>
                  <div class="form-group">
                    <label for="proxyReporterRole">नातेसंबंध / पद (Relationship / Role) *</label>
                    <select id="proxyReporterRole" class="form-control">
                      <option value="neighbor" selected>शेजारी (Neighbor)</option>
                      <option value="family_youth">कुटुंबातील तरुण (Family Youth)</option>
                      <option value="paravet">स्थानिक पशुमित्र / Para-Vet</option>
                      <option value="dairy_secretary">दुग्ध संस्था सचिव (Dairy Secretary)</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>"""

if old_step3_block in content:
    content = content.replace(old_step3_block, new_step3_block)
    print("Replaced Step 3 block with scale, location, mortality, and proxy fields!")
else:
    print("Could not find old step 3 block!")
    sys.exit(1)

# 3. Add the USSD & Missed-Call modals right before footer
modals_to_inject = """  <!-- USSD Feature-Phone Simulation Modal (*992#) -->
  <div class="modal-overlay" id="ussdModal">
    <div class="modal-card" style="max-width: 420px; background: #0f172a; color: #e2e8f0; border: 2px solid #334155;">
      <div class="modal-header" style="border-bottom: 1px solid #334155;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 1.2rem;">📱</span>
          <h3 style="color: #38bdf8; font-size: 1.1rem; margin: 0;">USSD Service (*992#)</h3>
        </div>
        <button class="modal-close" onclick="closeUssdModal()" style="color: #94a3b8;">&times;</button>
      </div>
      <div class="modal-body" style="padding: 16px;">
        <div style="font-size: 0.78rem; color: #94a3b8; margin-bottom: 10px;">
          Simulating real-time GSM USSD interactive session on basic feature phone.
        </div>
        <!-- Terminal Screen -->
        <div id="ussdScreen" style="background: #020617; border: 1.5px solid #22c55e; border-radius: 8px; padding: 14px; min-height: 140px; font-family: monospace; font-size: 0.88rem; color: #4ade80; line-height: 1.5; white-space: pre-wrap; margin-bottom: 14px; box-shadow: inset 0 0 10px rgba(34,197,94,0.2);">
PashuSachet Gram Signal (*992#)
1. Cattle (गाय)
2. Buffalo (म्हैस)
3. Goat / Sheep (शेळी/मेंढी)
4. Poultry (कुक्कुट)
0. Exit
        </div>
        <!-- USSD Input & Action -->
        <form id="ussdForm" onsubmit="event.preventDefault(); submitUssdStep();">
          <div style="display: flex; gap: 8px; margin-bottom: 12px;">
            <input type="text" id="ussdInput" class="form-control" placeholder="Enter option (e.g. 1)" style="background: #1e293b; color: #ffffff; border-color: #475569; font-family: monospace;" required autofocus>
            <button type="submit" class="btn btn-primary" style="background: #22c55e; color: #052e16; font-weight: 800;">
              Send
            </button>
          </div>
        </form>
        <!-- Keypad quick touch -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('1')" style="color: #cbd5e1; border-color: #334155;">1</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('2')" style="color: #cbd5e1; border-color: #334155;">2</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('3')" style="color: #cbd5e1; border-color: #334155;">3</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('4')" style="color: #cbd5e1; border-color: #334155;">4</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('5')" style="color: #cbd5e1; border-color: #334155;">5</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('6')" style="color: #cbd5e1; border-color: #334155;">6</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('7')" style="color: #cbd5e1; border-color: #334155;">7</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('8')" style="color: #cbd5e1; border-color: #334155;">8</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('9')" style="color: #cbd5e1; border-color: #334155;">9</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('*')" style="color: #cbd5e1; border-color: #334155;">*</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('0')" style="color: #cbd5e1; border-color: #334155;">0</button>
          <button type="button" class="btn btn-sm btn-outline" onclick="appendUssdKey('#')" style="color: #cbd5e1; border-color: #334155;">#</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Missed-Call & Voice IVR Simulation Modal -->
  <div class="modal-overlay" id="missedCallModal">
    <div class="modal-card" style="max-width: 460px; border-top: 5px solid #15803d;">
      <div class="modal-header">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 1.3rem;">📞</span>
          <h3 style="color: #15803d; font-size: 1.15rem; margin: 0;">पशूसचेत कॉल सहाय्यता (1800-889-1962)</h3>
        </div>
        <button class="modal-close" onclick="closeMissedCallModal()">&times;</button>
      </div>
      <div class="modal-body">
        <div style="text-align: center; padding: 10px 0 16px;">
          <div style="font-size: 2.4rem; margin-bottom: 6px;">📲</div>
          <h4 style="margin: 0; color: #0f172a;">Toll-Free Missed Call Gateway</h4>
          <p style="font-size: 0.85rem; color: #64748b; margin-top: 4px;">
            शेतकरी फक्त १ रिंग देऊन फोन ठेवू शकतात. प्रणाली ३० सेकंदात कॉल-बॅक करून मराठीत संवाद साधते.
          </p>
        </div>

        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; margin-bottom: 16px;">
          <div style="font-size: 0.8rem; font-weight: 700; color: #475569; margin-bottom: 6px;">Simulated Call Progression:</div>
          <div id="ivrCallStatus" style="font-size: 0.88rem; color: #166534; font-weight: 600; line-height: 1.5;">
            Ready to simulate missed call trigger from farmer number +91 98220 18491...
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 8px;">
          <button type="button" class="btn btn-primary" onclick="simulateMissedCallCallback()" style="background: #15803d; width: 100%;">
            🔔 Simulate Farmer Missed Call (१ रिंग द्या)
          </button>
          <button type="button" class="btn btn-outline" onclick="closeMissedCallModal()" style="width: 100%;">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
"""

content = content.replace('  <!-- Footer -->', modals_to_inject + '\n  <!-- Footer -->')
print("Injected USSD and Missed-Call modals!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated index.html for Phase 2!")

