# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Persona Switcher Bar right after the gov-banner (line 29)
persona_bar_html = '''
  <!-- Multi-Role Persona Switcher Bar (Field to State Level) -->
  <div class="persona-switcher-bar">
    <div class="container persona-grid">
      <span class="persona-label">Persona View:</span>
      <button class="persona-pill active" id="personaFarmer" onclick="activatePersona('farmer')">🧑‍🌾 Shetkari / Farmer</button>
      <button class="persona-pill" id="personaParavet" onclick="activatePersona('paravet')">🩺 Pashu Sakhi / Para-Vet</button>
      <button class="persona-pill" id="personaLdo" onclick="activatePersona('ldo')">👨‍⚕️ LDO Doctor (Dispensary)</button>
      <button class="persona-pill" id="personaCollector" onclick="activatePersona('collector')">🏛️ District Collector / AD</button>
      <button class="persona-pill" id="personaRddl" onclick="activatePersona('rddl')">🔬 State Epidemiologist (RDDL Pune)</button>
    </div>
  </div>
'''

if 'class="persona-switcher-bar"' not in html:
    html = html.replace('  <!-- Header -->', persona_bar_html + '\n  <!-- Header -->')
    print("✓ Added Persona Switcher Bar")

# 2. Upgrade AI Vision Sentinel Toolbar
old_vision_toolbar = '''            <!-- Interactive Action Toolbar: Presets, Upload & Voice -->
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px;">
              <button type="button" class="btn btn-sm" onclick="simulateVisionDetection('lsd')" style="font-size: 0.8rem; background: #1e293b; color: #ffffff; font-weight: 700;">
                📷 Scan Lumpy Skin Disease
              </button>
              <button type="button" class="btn btn-sm" onclick="simulateVisionDetection('fmd')" style="font-size: 0.8rem; background: #1e293b; color: #ffffff; font-weight: 700;">
                📷 Scan FMD Mouth Vesicles
              </button>
              <button type="button" class="btn btn-sm" onclick="simulateVisionDetection('mastitis')" style="font-size: 0.8rem; background: #1e293b; color: #ffffff; font-weight: 700;">
                📷 Scan Mastitis Udder
              </button>

              <input type="file" id="lesionUploadInput" accept="image/*" style="display: none;" onchange="handleLesionUpload(event)">
              <button type="button" class="btn btn-sm btn-outline" onclick="document.getElementById('lesionUploadInput').click()" style="font-size: 0.8rem; border-color: #0284c7; color: #0284c7; font-weight: 700;">
                📤 Upload Custom Photo
              </button>

              <!-- Live Marathi Voice Microphone Input Button -->
              <button type="button" class="btn btn-sm" id="marathiVoiceBtn" onclick="toggleMarathiVoiceRecognition()" style="font-size: 0.8rem; background: #e11d48; color: #ffffff; font-weight: 800; margin-left: auto;">
                🎙️ Speak Symptoms in Marathi (माईकवर बोला)
              </button>
            </div>'''

new_vision_toolbar = '''            <!-- Interactive Action Toolbar: 6 Disease Presets, Camera, Thermal & Voice -->
            <div class="vision-preset-grid">
              <button type="button" class="vision-chip-btn active" id="chipLsd" onclick="simulateVisionDetection('lsd')">
                📷 LSD Nodules (लंपी)
              </button>
              <button type="button" class="vision-chip-btn" id="chipFmd" onclick="simulateVisionDetection('fmd')">
                📷 FMD Vesicles (लाळखुरी)
              </button>
              <button type="button" class="vision-chip-btn" id="chipMastitis" onclick="simulateVisionDetection('mastitis')">
                📷 Mastitis Udder (कासदाह)
              </button>
              <button type="button" class="vision-chip-btn" id="chipBq" onclick="simulateVisionDetection('bq')">
                📷 Black Quarter (एकटांग्या)
              </button>
              <button type="button" class="vision-chip-btn" id="chipPpr" onclick="simulateVisionDetection('ppr')">
                📷 PPR Goats (शेळी प्लेग)
              </button>
              <button type="button" class="vision-chip-btn" id="chipBabesiosis" onclick="simulateVisionDetection('babesiosis')">
                📷 Babesiosis Ticks (गोचीड)
              </button>
            </div>

            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px; align-items: center;">
              <!-- Live Video Camera Toggle -->
              <video id="visionVideoFeed" playsinline autoplay muted style="display: none;"></video>
              <button type="button" class="vision-tool-pill" id="liveCameraBtn" onclick="toggleLiveCameraFeed()">
                📹 Open Live Camera
              </button>

              <!-- Thermal FLIR Overlay Toggle -->
              <button type="button" class="vision-tool-pill" id="thermalToggleBtn" onclick="toggleThermalMode()">
                🌡️ FLIR Thermal Heatmap
              </button>

              <!-- Grad-CAM Deep Attention Map Toggle -->
              <button type="button" class="vision-tool-pill" id="gradCamToggleBtn" onclick="toggleGradCamMode()">
                🧠 Grad-CAM Attention
              </button>

              <input type="file" id="lesionUploadInput" accept="image/*" style="display: none;" onchange="handleLesionUpload(event)">
              <button type="button" class="vision-tool-pill" onclick="document.getElementById('lesionUploadInput').click()" style="color: #0284c7; border-color: #0284c7;">
                📤 Upload Custom Photo
              </button>

              <!-- Live Marathi Voice Microphone Input Button -->
              <button type="button" class="btn btn-sm" id="marathiVoiceBtn" onclick="toggleMarathiVoiceRecognition()" style="font-size: 0.8rem; background: #e11d48; color: #ffffff; font-weight: 800; margin-left: auto;">
                🎙️ Speak in Marathi (माईकवर बोला)
              </button>
            </div>'''

if old_vision_toolbar in html:
    html = html.replace(old_vision_toolbar, new_vision_toolbar)
    print("✓ Upgraded AI Vision Sentinel Toolbar with 6 presets and camera/thermal controls")

# 3. Add Transfer to Triage Intake Button inside Vision Output Box
old_vision_output = '''            <!-- Vision Output Feedback Box -->
            <div id="visionOutputBox" style="display: none; background: #ffffff; border: 1.5px solid #86efac; border-radius: 8px; padding: 14px 18px;">
              <div id="visionResultContent" style="font-size: 0.88rem; color: #166534; line-height: 1.5;"></div>
            </div>'''

new_vision_output = '''            <!-- Vision Output Feedback Box -->
            <div id="visionOutputBox" style="display: none; background: #ffffff; border: 1.5px solid #86efac; border-radius: 8px; padding: 14px 18px;">
              <div id="visionResultContent" style="font-size: 0.88rem; color: #166534; line-height: 1.5;"></div>
              <div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #bbf7d0; display: flex; justify-content: flex-end; gap: 8px;">
                <button type="button" class="btn btn-sm btn-primary" onclick="transferVisionToTriage()" style="background: #15803d; font-size: 0.82rem; font-weight: 800;">
                  🚀 Transfer Findings to 90s Triage Intake
                </button>
              </div>
            </div>'''

if old_vision_output in html:
    html = html.replace(old_vision_output, new_vision_output)
    print("✓ Added 'Transfer Findings to 90s Triage Intake' button")

# 4. Add SEIR Outbreak Simulator and MVU Fleet Telematics to #outbreak-gis
seir_and_mvu_html = '''
            <!-- SEIR Epidemic Spread Simulation & Control Strip -->
            <div class="seir-hud-panel">
              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div>
                  <strong style="color: #38bdf8; font-size: 0.95rem;">🔬 Dynamic SEIR Outbreak Spread Simulator (14-Day Projection)</strong>
                  <div style="font-size: 0.75rem; color: #94a3b8;">Mathematical compartmental model: N = 14,200 livestock in Sangamner belt</div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <button type="button" class="btn btn-sm btn-outline" id="playSeirBtn" onclick="toggleSeirPlay()" style="border-color: #38bdf8; color: #38bdf8; font-size: 0.78rem; font-weight: 800;">
                    ▶️ Run 14-Day Simulation
                  </button>
                </div>
              </div>

              <!-- Time Step Slider -->
              <div style="margin-top: 12px; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 0.75rem; color: #94a3b8; font-weight: 700;">Timeline:</span>
                <input type="range" id="seirDaySlider" min="0" max="14" value="0" step="1" oninput="updateSeirDay(this.value)" style="flex: 1; accent-color: #38bdf8;">
                <span id="seirDayLabel" style="font-family: monospace; font-size: 0.85rem; color: #38bdf8; font-weight: 800; min-width: 60px;">Day 0</span>
              </div>

              <!-- Live SEIR Compartment Metrics -->
              <div class="seir-metric-grid">
                <div class="seir-metric-card">
                  <div class="seir-metric-val" id="seirRtVal" style="color: #ef4444;">2.45</div>
                  <div class="seir-metric-lbl">Effective R_t</div>
                </div>
                <div class="seir-metric-card">
                  <div class="seir-metric-val" id="seirInfVal" style="color: #f97316;">12</div>
                  <div class="seir-metric-lbl">Active Infectious</div>
                </div>
                <div class="seir-metric-card">
                  <div class="seir-metric-val" id="seirVaxVal" style="color: #22c55e;">0</div>
                  <div class="seir-metric-lbl">Ring-Vaccinated</div>
                </div>
                <div class="seir-metric-card">
                  <div class="seir-metric-val" id="seirEfficacyVal" style="color: #a855f7;">4.5%</div>
                  <div class="seir-metric-lbl">Containment Efficacy</div>
                </div>
              </div>
            </div>

            <!-- 1962 MVU GPS Telematics & Siren Console -->
            <div class="mvu-telematics-panel">
              <div class="mvu-header">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="font-size: 1.5rem;">🚑</span>
                  <div>
                    <div style="display: flex; align-items: center; gap: 6px;">
                      <strong style="color: #ffffff; font-size: 0.95rem;">MVU Unit #1 (Sangamner Beat)</strong>
                      <span class="mvu-badge">MH-17-BV-1962</span>
                    </div>
                    <div style="font-size: 0.76rem; color: #94a3b8;">
                      Duty Vet: Dr. Pradeep Deshmukh (MSVC/2012/03194) • Driver: Sunil Shinde
                    </div>
                  </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                  <div class="coldchain-meter">
                    <span class="pulse-dot" style="background: #34d399;"></span>
                    <span>Vaccine Cold Box: <strong>+4.1°C</strong></span>
                  </div>
                  <button type="button" class="btn btn-sm" onclick="playMvuSirenTone()" style="background: #dc2626; color: #ffffff; font-weight: 800; font-size: 0.76rem;">
                    🚨 1962 Siren Tone
                  </button>
                </div>
              </div>

              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; font-size: 0.8rem;">
                <div style="background: #1e293b; padding: 8px 12px; border-radius: 6px;">
                  <span style="color: #94a3b8; display: block; font-size: 0.72rem;">DISPATCH TARGET</span>
                  <strong style="color: #f87171;">Nimgaon Jali (Surge Zone)</strong>
                </div>
                <div style="background: #1e293b; padding: 8px 12px; border-radius: 6px;">
                  <span style="color: #94a3b8; display: block; font-size: 0.72rem;">LIVE GPS DISTANCE</span>
                  <strong id="mvuGpsDist">6.8 km (ETA: 12 mins)</strong>
                </div>
                <div style="background: #1e293b; padding: 8px 12px; border-radius: 6px;">
                  <span style="color: #94a3b8; display: block; font-size: 0.72rem;">ONBOARD VACCINE STOCK</span>
                  <strong style="color: #86efac;">400 LSD • 350 FMD Doses</strong>
                </div>
                <div style="background: #1e293b; padding: 8px 12px; border-radius: 6px;">
                  <span style="color: #94a3b8; display: block; font-size: 0.72rem;">DIAGNOSTIC KITS</span>
                  <strong>45 RDDL Sample Barcodes</strong>
                </div>
              </div>
            </div>
'''

target_map_end = '<!-- Map Pin Selected Inspector -->'
if target_map_end in html and 'class="seir-hud-panel"' not in html:
    html = html.replace(target_map_end, seir_and_mvu_html + '\n            ' + target_map_end)
    print("✓ Added SEIR Simulation HUD and 1962 MVU Telematics Card")

# 5. Add Floating WhatsApp Widget & Drawer before </body>
whatsapp_widget_html = '''
  <!-- Floating WhatsApp Simulator Button -->
  <button type="button" class="whatsapp-floating-btn" onclick="toggleWhatsAppChat()">
    <span style="font-size: 1.25rem;">💬</span>
    <span>1962 WhatsApp Bot</span>
  </button>

  <!-- Floating WhatsApp Interactive Drawer -->
  <div class="whatsapp-drawer" id="whatsappDrawer">
    <div class="whatsapp-chat-header">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.4rem;">🐄</span>
        <div>
          <div style="font-weight: 800; font-size: 0.9rem;">1962 Pashu Helpline</div>
          <div style="font-size: 0.7rem; color: #a7f3d0;">✓ Official Govt of Maharashtra Bot</div>
        </div>
      </div>
      <button onclick="toggleWhatsAppChat()" style="background: none; border: none; color: #ffffff; font-size: 1.2rem; cursor: pointer;">&times;</button>
    </div>

    <div class="whatsapp-body" id="whatsappMessagesList">
      <div class="whatsapp-msg incoming">
        🙏 <strong>नमस्कार शेतकरी बंधू!</strong><br>
        मी महाराष्ट्र शासन पशुसंवर्धन विभागाचा १९६२ व्हर्च्युअल सहाय्यक आहे. आपण जनावराची लक्षणे मराठीत सांगू शकता किंवा फोटो पाठवू शकता.
        <div class="whatsapp-time">१०:३० AM</div>
      </div>
    </div>

    <!-- Quick Action Chips for WhatsApp Simulation -->
    <div style="background: #e2e8f0; padding: 6px 10px; display: flex; gap: 6px; overflow-x: auto; white-space: nowrap;">
      <button type="button" onclick="sendWhatsAppQuickMsg('voice')" style="font-size: 0.72rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 2px 8px; cursor: pointer;">
        🎙️ व्हॉइस मेसेज पाठवा
      </button>
      <button type="button" onclick="sendWhatsAppQuickMsg('photo')" style="font-size: 0.72rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 2px 8px; cursor: pointer;">
        📷 फोटो पाठवा (LSD)
      </button>
      <button type="button" onclick="sendWhatsAppQuickMsg('status')" style="font-size: 0.72rem; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 2px 8px; cursor: pointer;">
        📋 केस स्टेटस तपासा
      </button>
    </div>

    <div class="whatsapp-footer">
      <input type="text" class="whatsapp-input" id="whatsappUserInput" placeholder="मराठीत संदेश टाइप करा..." onkeydown="if(event.key==='Enter') sendWhatsAppUserText()">
      <button type="button" class="whatsapp-send-btn" onclick="sendWhatsAppUserText()">➤</button>
    </div>
  </div>
'''

if 'class="whatsapp-floating-btn"' not in html:
    html = html.replace('</body>', whatsapp_widget_html + '\n</body>')
    print("✓ Added Floating WhatsApp Simulator Widget and Drawer")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated with all supercharged features.")
