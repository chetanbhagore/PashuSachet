# -*- coding: utf-8 -*-
"""
Script to apply deep, production-grade supercharges across index.html, css/style.css, and js/app.js.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Applying Deep UX & Technical Supercharges to PashuSachet...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read().replace('\r\n', '\n')

# 1. Update #aiVisionSentinel in index.html to include Canvas, File Upload, and Voice Input
old_vision_widget = """          <!-- AI Clinical Vision Sentinel (Photo Lesion Detection) -->
          <div id="aiVisionSentinel" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 16px 20px; margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 1.3rem;">📸</span>
                <div>
                  <h4 style="margin: 0; font-size: 1rem; color: #0f172a; font-weight: 800;">
                    AI Clinical Vision Detection (पशू लक्षण फोटो तपासणी)
                  </h4>
                  <span style="font-size: 0.78rem; color: #64748b;">
                    Upload photo of skin nodules, mouth blisters, or udder swelling for automated pattern detection.
                  </span>
                </div>
              </div>
              <span style="font-size: 0.75rem; background: #ede9fe; color: #6d28d9; font-weight: 700; padding: 3px 8px; border-radius: 4px;">
                Edge Vision Model v2.4
              </span>
            </div>

            <!-- Preset Demo Test Images for Instant Evaluation -->
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px;">
              <button type="button" class="btn btn-sm btn-outline" onclick="simulateVisionDetection('lsd')" style="font-size: 0.78rem; border-color: #cbd5e1;">
                📷 Test Lumpy Skin Disease (गाठी फोटो)
              </button>
              <button type="button" class="btn btn-sm btn-outline" onclick="simulateVisionDetection('fmd')" style="font-size: 0.78rem; border-color: #cbd5e1;">
                📷 Test FMD Mouth Blisters (लाळ-खुरकूत)
              </button>
              <button type="button" class="btn btn-sm btn-outline" onclick="simulateVisionDetection('mastitis')" style="font-size: 0.78rem; border-color: #cbd5e1;">
                📷 Test Mastitis Udder (कासदाह फोटो)
              </button>
            </div>

            <!-- Vision Output Feedback Box -->
            <div id="visionOutputBox" style="display: none; background: #ffffff; border: 1.5px solid #86efac; border-radius: 8px; padding: 12px 16px;">
              <div id="visionResultContent" style="font-size: 0.85rem; color: #166534; line-height: 1.5;"></div>
            </div>
          </div>"""

new_vision_widget = """          <!-- AI Clinical Vision Sentinel (Photo Lesion Detection) -->
          <div id="aiVisionSentinel" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 18px 22px; margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 1.4rem;">📸</span>
                <div>
                  <h4 style="margin: 0; font-size: 1.05rem; color: #0f172a; font-weight: 800;">
                    AI Clinical Vision Detection (पशू लक्षण फोटो तपासणी)
                  </h4>
                  <span style="font-size: 0.8rem; color: #64748b;">
                    Computer vision lesion inspection for LSD nodules, FMD vesicles, and Mastitis inflammation.
                  </span>
                </div>
              </div>
              <div style="display: flex; gap: 6px;">
                <span style="font-size: 0.74rem; background: #ede9fe; color: #6d28d9; font-weight: 800; padding: 3px 8px; border-radius: 4px;">
                  Edge MobileNet-V3
                </span>
                <span style="font-size: 0.74rem; background: #dcfce7; color: #166534; font-weight: 800; padding: 3px 8px; border-radius: 4px;">
                  Local In-Browser Inference
                </span>
              </div>
            </div>

            <!-- Interactive Action Toolbar: Presets, Upload & Voice -->
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
            </div>

            <!-- Voice Transcript Feedback Banner -->
            <div id="voiceTranscriptBox" style="display: none; background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 10px 14px; margin-bottom: 12px; font-size: 0.85rem; color: #9f1239;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="pulse-dot" style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #e11d48;"></span>
                <strong id="voiceStatusLabel">ऐकत आहे (Listening)... मराठी किंवा इंग्रजीत लक्षणे सांगा:</strong>
              </div>
              <div id="voiceTranscriptText" style="margin-top: 4px; font-style: italic; color: #881337;"></div>
            </div>

            <!-- HTML5 Vision Canvas for Lesion Inspection & Bounding Box HUD -->
            <div id="visionCanvasContainer" style="display: none; position: relative; margin-bottom: 14px; border-radius: 8px; overflow: hidden; border: 2px solid #0f172a; background: #020617;">
              <canvas id="visionCanvas" width="640" height="320" style="width: 100%; height: auto; display: block;"></canvas>
              <div id="visionHudOverlay" style="position: absolute; bottom: 10px; left: 12px; right: 12px; background: rgba(15,23,42,0.88); backdrop-filter: blur(4px); border: 1px solid #38bdf8; border-radius: 6px; padding: 8px 12px; display: flex; justify-content: space-between; align-items: center; color: #f8fafc; font-family: monospace; font-size: 0.78rem;">
                <span id="hudStatus">READY</span>
                <span id="hudLesionMetrics">HUD: ACTIVE</span>
              </div>
            </div>

            <!-- Vision Output Feedback Box -->
            <div id="visionOutputBox" style="display: none; background: #ffffff; border: 1.5px solid #86efac; border-radius: 8px; padding: 14px 18px;">
              <div id="visionResultContent" style="font-size: 0.88rem; color: #166534; line-height: 1.5;"></div>
            </div>
          </div>"""

if old_vision_widget in html:
    html = html.replace(old_vision_widget, new_vision_widget)
    print("Enhanced #aiVisionSentinel with Canvas, Upload, and Voice Assistant!")
else:
    print("Could not find old vision widget!")
    sys.exit(1)

# 2. Add Interactive Geographic Outbreak Map & Containment Zone Visualizer in #outbreak-gis
old_gis_canvas_head = """        <!-- GIS Canvas / District Telemetry -->
        <div class="gis-map-canvas">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid var(--border); padding-bottom: 16px; margin-bottom: 20px;">"""

new_gis_canvas_head = """        <!-- GIS Canvas / District Telemetry -->
        <div class="gis-map-canvas">
          <!-- Interactive Visual Maharashtra Outbreak & Containment Zone Map -->
          <div style="background: #0f172a; border-radius: 10px; padding: 14px 18px; margin-bottom: 20px; color: #e2e8f0;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 1.2rem;">🗺️</span>
                <strong style="color: #38bdf8; font-size: 0.95rem;">Geographic Transmission &amp; Containment Zone Map</strong>
              </div>
              <div style="display: flex; gap: 8px;">
                <button type="button" class="btn btn-sm btn-outline" id="toggleRingVaxBtn" onclick="toggleRingVaxRadius()" style="color: #f87171; border-color: #ef4444; font-size: 0.75rem; font-weight: 700;">
                  🎯 Toggle 5km Ring-Vaccination Buffer
                </button>
              </div>
            </div>

            <!-- SVG Outbreak Map Canvas -->
            <div style="position: relative; background: #020617; border: 1.5px solid #1e293b; border-radius: 8px; overflow: hidden; padding: 10px;">
              <svg id="gisSvgMap" viewBox="0 0 600 280" style="width: 100%; height: auto; display: block;">
                <!-- Ahmednagar Talukas Schematic Polygons -->
                <polygon points="40,60 160,30 220,90 140,140 50,110" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
                <text x="90" y="85" fill="#94a3b8" font-size="11" font-weight="700">Akole (अकोले)</text>

                <polygon points="160,30 320,20 360,90 220,90" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
                <text x="210" y="55" fill="#38bdf8" font-size="12" font-weight="800">Sangamner (संगमनेर)</text>

                <polygon points="320,20 460,30 480,110 360,90" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
                <text x="370" y="65" fill="#94a3b8" font-size="11" font-weight="700">Rahata / Shirdi</text>

                <polygon points="140,140 220,90 360,90 380,180 200,210" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
                <text x="220" y="150" fill="#94a3b8" font-size="11" font-weight="700">Parner / Rahuri</text>

                <!-- 5km Ring-Vaccination Buffer Circles (Toggled via JS) -->
                <g id="ringVaxBuffers" style="display: none;">
                  <circle cx="280" cy="70" r="45" fill="rgba(239,68,68,0.18)" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4" />
                  <circle cx="280" cy="70" r="70" fill="rgba(245,158,11,0.08)" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" />
                  <text x="280" y="125" fill="#fca5a5" font-size="10" text-anchor="middle" font-weight="700">5km Ring-Vax Zone</text>
                </g>

                <!-- Active Village Pins -->
                <!-- Nimgaon Jali (4 signals - Surge) -->
                <g style="cursor: pointer;" onclick="inspectMapPin('Nimgaon Jali', 4, 'FMD Blisters', 'SURGE_CLUSTER')">
                  <circle cx="280" cy="70" r="8" fill="#dc2626" />
                  <circle cx="280" cy="70" r="14" fill="none" stroke="#ef4444" stroke-width="2" opacity="0.6">
                    <animate attributeName="r" values="8;20;8" dur="2s" repeatCount="indefinite" />
                    <animate attributeName="opacity" values="0.8;0;0.8" dur="2s" repeatCount="indefinite" />
                  </circle>
                  <text x="295" y="74" fill="#ffffff" font-size="11" font-weight="700">Nimgaon Jali (4 Signals)</text>
                </g>

                <!-- Sangamner Khurd (3 signals - LSD) -->
                <g style="cursor: pointer;" onclick="inspectMapPin('Sangamner Khurd', 3, 'LSD Nodules', 'VERIFIED')">
                  <circle cx="240" cy="75" r="7" fill="#f59e0b" />
                  <text x="180" y="95" fill="#fde68a" font-size="10" font-weight="600">Sangamner Khurd (3)</text>
                </g>

                <!-- Ashwi (k-anonymized centroid) -->
                <g style="cursor: pointer;" onclick="inspectMapPin('Ashwi Rural Beat', 2, 'Fever/Drop in Milk', 'K_ANONYMIZED')">
                  <circle cx="205" cy="65" r="5" fill="#0f766e" />
                  <text x="140" y="62" fill="#99f6e4" font-size="9">Ashwi Centroid (k<3)</text>
                </g>

                <!-- Kotul (Mortality) -->
                <g style="cursor: pointer;" onclick="inspectMapPin('Kotul Beat (Akole)', 2, 'Sudden Caprine Mortality', 'BIOSECURITY_CORDON')">
                  <circle cx="100" cy="95" r="7" fill="#b91c1c" />
                  <text x="80" y="115" fill="#fca5a5" font-size="10" font-weight="700">Kotul (Mortality)</text>
                </g>
              </svg>
            </div>

            <!-- Map Pin Selected Inspector -->
            <div id="mapPinInspector" style="display: none; background: #1e293b; border-radius: 6px; padding: 10px 14px; margin-top: 10px; font-size: 0.82rem;">
              <span id="mapPinDetails"></span>
            </div>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid var(--border); padding-bottom: 16px; margin-bottom: 20px;">"""

if old_gis_canvas_head in html:
    html = html.replace(old_gis_canvas_head, new_gis_canvas_head)
    print("Injected Interactive Geographic Outbreak Map & Containment Zone Visualizer!")

# 3. Add Digital Pashu Aadhar Smart Card Modal & Trigger Button
pashu_card_trigger = """        <div style="display: flex; gap: 8px;">
          <button class="btn btn-outline btn-sm" onclick="openPashuAadharModal('MH-24-9812')" style="border-color: #15803d; color: #15803d; font-weight: 700;">
            🪪 Digital Pashu Aadhar Card
          </button>
          <button class="btn btn-primary btn-sm" onclick="document.getElementById('addAnimalModal').classList.add('active')">
            + Register New Animal
          </button>
        </div>"""

old_passport_btn_bar = """        <button class="btn btn-primary btn-sm" onclick="document.getElementById('addAnimalModal').classList.add('active')">
          + Register New Animal
        </button>"""

if old_passport_btn_bar in html:
    html = html.replace(old_passport_btn_bar, pashu_card_trigger)
    print("Injected Digital Pashu Aadhar Card trigger button!")

# Modal for Digital Pashu Aadhar Smart Card
pashu_card_modal = """
  <!-- Digital Pashu Aadhar Smart Card Modal -->
  <div class="modal-overlay" id="pashuAadharCardModal">
    <div class="modal-card" style="max-width: 520px; padding: 0; overflow: hidden; border: 2px solid #15803d; border-radius: 14px;">
      <!-- Tricolor Header -->
      <div style="background: linear-gradient(135deg, #166534 0%, #15803d 100%); color: #ffffff; padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 4px solid #f59e0b;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 1.8rem;">🐄</span>
          <div>
            <div style="font-size: 0.72rem; letter-spacing: 1px; text-transform: uppercase; color: #86efac; font-weight: 700;">
              GOVERNMENT OF MAHARASHTRA • पशुसंवर्धन विभाग
            </div>
            <h3 style="margin: 0; font-size: 1.15rem; font-weight: 900; color: #ffffff;">
              BHARAT PASHUDHAN DIGITAL AADHAR
            </h3>
          </div>
        </div>
        <button class="modal-close" onclick="closePashuAadharModal()" style="color: #ffffff;">&times;</button>
      </div>

      <div class="modal-body" style="padding: 20px; background: #fdfcf7;">
        <!-- Card Core Details -->
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; margin-bottom: 16px;">
          <div style="flex: 1;">
            <span style="font-size: 0.72rem; color: #64748b; font-weight: 700; text-transform: uppercase;">Unique Pashu Aadhar Tag (12-Digit)</span>
            <div style="font-size: 1.4rem; font-weight: 900; color: #0f172a; font-family: monospace; letter-spacing: 2px; margin: 2px 0 8px;">
              2400 1928 3741
            </div>

            <div style="font-size: 0.84rem; color: #334155; line-height: 1.6;">
              <div><strong>Animal Name:</strong> Gauri (गाय)</div>
              <div><strong>Species &amp; Breed:</strong> Cattle • Gir Crossbred</div>
              <div><strong>Age / Sex:</strong> 3.5 Yrs • Female (Lactating)</div>
              <div><strong>Owner:</strong> Ganesh R. Patil (Sangamner Khurd)</div>
              <div><strong>Jurisdiction:</strong> CVD Sangamner (Dr. R. Kute)</div>
            </div>
          </div>

          <!-- Dynamic SVG QR Code (Live Verification) -->
          <div style="text-align: center;">
            <div style="background: #ffffff; padding: 8px; border-radius: 8px; border: 1.5px solid #cbd5e1; box-shadow: 0 2px 6px rgba(0,0,0,0.06); display: inline-block;">
              <svg width="105" height="105" viewBox="0 0 100 100" style="display: block;">
                <!-- Authentic-Looking SVG QR Pattern -->
                <rect width="100" height="100" fill="#ffffff"/>
                <!-- Top-Left Corner Finder -->
                <rect x="5" y="5" width="28" height="28" fill="#0f172a"/>
                <rect x="9" y="9" width="20" height="20" fill="#ffffff"/>
                <rect x="13" y="13" width="12" height="12" fill="#0f172a"/>
                <!-- Top-Right Corner Finder -->
                <rect x="67" y="5" width="28" height="28" fill="#0f172a"/>
                <rect x="71" y="9" width="20" height="20" fill="#ffffff"/>
                <rect x="75" y="13" width="12" height="12" fill="#0f172a"/>
                <!-- Bottom-Left Corner Finder -->
                <rect x="5" y="67" width="28" height="28" fill="#0f172a"/>
                <rect x="9" y="71" width="20" height="20" fill="#ffffff"/>
                <rect x="13" y="75" width="12" height="12" fill="#0f172a"/>
                <!-- Data Blocks -->
                <rect x="38" y="10" width="8" height="8" fill="#0f172a"/>
                <rect x="50" y="14" width="8" height="8" fill="#0f172a"/>
                <rect x="38" y="24" width="8" height="8" fill="#0f172a"/>
                <rect x="10" y="38" width="8" height="8" fill="#0f172a"/>
                <rect x="22" y="44" width="8" height="8" fill="#0f172a"/>
                <rect x="38" y="38" width="24" height="24" fill="#15803d"/>
                <rect x="42" y="42" width="16" height="16" fill="#ffffff"/>
                <text x="50" y="53" font-size="8" fill="#15803d" text-anchor="middle" font-weight="900">DAHD</text>
                <rect x="68" y="38" width="8" height="8" fill="#0f172a"/>
                <rect x="80" y="46" width="8" height="8" fill="#0f172a"/>
                <rect x="38" y="68" width="8" height="8" fill="#0f172a"/>
                <rect x="50" y="74" width="8" height="8" fill="#0f172a"/>
                <rect x="68" y="68" width="8" height="8" fill="#0f172a"/>
                <rect x="80" y="80" width="8" height="8" fill="#0f172a"/>
              </svg>
            </div>
            <div style="font-size: 0.68rem; color: #64748b; font-weight: 700; margin-top: 4px;">SCAN FOR LIVE AUDIT</div>
          </div>
        </div>

        <!-- Food Safety Milk Status on Card -->
        <div style="background: #fef2f2; border: 1.5px solid #fca5a5; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.76rem; font-weight: 800; color: #991b1b; text-transform: uppercase;">FOOD SAFETY STATUS</span>
            <span style="font-size: 0.75rem; background: #fee2e2; color: #991b1b; font-weight: 800; padding: 2px 6px; border-radius: 4px;">WITHHOLDING ACTIVE</span>
          </div>
          <div style="font-size: 0.85rem; font-weight: 700; color: #b91c1c; margin-top: 4px;">
            ⛔ DO NOT SUPPLY MILK TO COOPERATIVE (126h Remaining)
          </div>
          <div style="font-size: 0.75rem; color: #7f1d1d; margin-top: 2px;">
            Prescribed: Ceftiofur Sodium • MSVC/2012/03194 (Dr. Rameshwar Kute)
          </div>
        </div>

        <!-- Card Security Footer -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px dashed #cbd5e1; font-size: 0.72rem; color: #64748b;">
          <div>INAPH Hash: <strong>SHA256: 8f4b-39a1-77b2</strong></div>
          <button type="button" class="btn btn-sm btn-outline" onclick="window.print()" style="font-size: 0.75rem;">🖨️ Print Card</button>
        </div>
      </div>
    </div>
  </div>
"""

html = html.replace('  <!-- Footer -->', pashu_card_modal + '\n  <!-- Footer -->')
print("Injected Digital Pashu Aadhar Smart Card Modal!")

# 4. Add Visual Analytics Charts Suite in #pilot-telemetry
telemetry_charts = """
      <!-- Visual Analytics & Epidemic Curve Suite -->
      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 24px;">
        <div style="margin-bottom: 16px;">
          <span style="font-size: 0.75rem; font-weight: 800; background: #e0f2fe; color: #0369a1; padding: 3px 8px; border-radius: 4px;">
            Operational Analytics
          </span>
          <h3 style="margin: 4px 0 2px; font-size: 1.15rem; color: #0f172a; font-weight: 800;">
            Pilot Telemetry Graphics &amp; Transmission Wave Analysis
          </h3>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
          <!-- Chart 1: Channel Adoption Stacked Bar -->
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
            <div style="font-size: 0.82rem; font-weight: 700; color: #0f172a; margin-bottom: 10px;">
              📊 Channel Inclusivity Breakdown (Pilot Intake)
            </div>
            <!-- Stacked bar -->
            <div style="height: 24px; display: flex; border-radius: 6px; overflow: hidden; margin-bottom: 10px;">
              <div style="width: 40%; background: #0f766e; color: #ffffff; font-size: 0.72rem; font-weight: 800; display: flex; align-items: center; justify-content: center;" title="USSD *992#: 40%">
                USSD 40%
              </div>
              <div style="width: 38%; background: #0284c7; color: #ffffff; font-size: 0.72rem; font-weight: 800; display: flex; align-items: center; justify-content: center;" title="Voice IVR: 38%">
                Voice 38%
              </div>
              <div style="width: 22%; background: #94a3b8; color: #ffffff; font-size: 0.72rem; font-weight: 800; display: flex; align-items: center; justify-content: center;" title="Web Form: 22%">
                Web 22%
              </div>
            </div>
            <div style="font-size: 0.75rem; color: #64748b; line-height: 1.4;">
              <strong>78% Non-App Adoption:</strong> Validates hypothesis that elderly rural farmers prefer voice &amp; feature phone short-codes over smartphones.
            </div>
          </div>

          <!-- Chart 2: 7-Day Epidemic Suppression Curve (SVG) -->
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
            <div style="font-size: 0.82rem; font-weight: 700; color: #0f172a; margin-bottom: 6px;">
              📉 7-Day Cluster Transmission Curve (FMD Nimgaon Jali)
            </div>
            <svg viewBox="0 0 300 90" style="width: 100%; height: auto; display: block;">
              <!-- Background Grid -->
              <line x1="20" y1="20" x2="290" y2="20" stroke="#e2e8f0" stroke-width="1" />
              <line x1="20" y1="50" x2="290" y2="50" stroke="#e2e8f0" stroke-width="1" />
              <line x1="20" y1="80" x2="290" y2="80" stroke="#cbd5e1" stroke-width="1" />
              
              <!-- Curve: Rises then flattens after ring-vax -->
              <path d="M 30,75 Q 80,15 140,25 T 210,65 T 280,75" fill="none" stroke="#dc2626" stroke-width="2.5" />
              <!-- Ring-Vax Intervention Marker -->
              <line x1="140" y1="15" x2="140" y2="80" stroke="#0f766e" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="145" y="25" fill="#0f766e" font-size="8" font-weight="800">5km Ring-Vax</text>

              <!-- Points -->
              <circle cx="30" cy="75" r="3" fill="#dc2626" />
              <circle cx="80" cy="30" r="3" fill="#dc2626" />
              <circle cx="140" cy="25" r="4" fill="#dc2626" />
              <circle cx="210" cy="65" r="3" fill="#15803d" />
              <circle cx="280" cy="75" r="3" fill="#15803d" />
            </svg>
            <div style="font-size: 0.74rem; color: #166534; font-weight: 600; margin-top: 4px;">
              ✓ Rapid containment: Cases suppressed from 14 $\to$ 2 within 5 days of ring vaccination.
            </div>
          </div>
        </div>
      </div>
"""

old_nadres_card = """      <!-- NADRES V2 Export Pipeline Card -->"""
if old_nadres_card in html:
    html = html.replace(old_nadres_card, telemetry_charts + '\n' + old_nadres_card)
    print("Injected Visual Analytics & Epidemic Curve Suite into #pilot-telemetry!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully!")

