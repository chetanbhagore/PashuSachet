# -*- coding: utf-8 -*-
import sys
import re

print("Starting PashuSachet frontend enhancement script...")

# 1. READ ORIGINAL FILES
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# 2. UPDATE INDEX.HTML

# A. Add Nav link and Role switcher in Header
nav_marker = '<ul class="nav-links">'
nav_addition = '''<ul class="nav-links">
        <li><a href="#hero" class="active" data-i18n="nav_home">Home</a></li>
        <li><a href="#symptom-screening" data-i18n="nav_screen">AI Screening</a></li>
        <li><a href="#outbreak-gis" data-i18n="nav_risk">Outbreak Risk GIS</a></li>
        <li><a href="#health-passport" data-i18n="nav_registry">Animal Passport</a></li>
        <li><a href="#vet-directory" data-i18n="nav_vets">Find a Vet</a></li>
        <li><a href="#vet-desk" data-i18n="nav_vet_desk">Vet Care Desk</a></li>
        <li><a href="#blueprint" data-i18n="nav_blueprint">Blueprint</a></li>'''

if nav_marker in html:
    html = html.replace(nav_marker + '\n        <li><a href="#hero" class="active" data-i18n="nav_home">Home</a></li>\n        <li><a href="#symptom-screening" data-i18n="nav_screen">AI Screening</a></li>\n        <li><a href="#outbreak-gis" data-i18n="nav_risk">Outbreak Risk GIS</a></li>\n        <li><a href="#health-passport" data-i18n="nav_registry">Animal Passport</a></li>\n        <li><a href="#vet-directory" data-i18n="nav_vets">Find a Vet</a></li>\n        <li><a href="#blueprint" data-i18n="nav_blueprint">Blueprint</a></li>', nav_addition)
    print("Updated navigation links with Vet Care Desk.")

header_actions_marker = '<div class="header-actions">'
header_actions_addition = '''<div class="header-actions">
        <!-- Role Mode Switcher -->
        <div class="role-switch" style="margin-right: 8px;">
          <button class="role-pill active" id="roleFarmerBtn" onclick="switchRole('farmer')">Farmer</button>
          <button class="role-pill" id="roleVetBtn" onclick="switchRole('vet')">Vet Desk</button>
        </div>'''
if header_actions_marker in html:
    html = html.replace(header_actions_marker, header_actions_addition)
    print("Added Role Mode Switcher in header.")

# B. Add Qualitative Triage Bands and Send to Vet in Assessment Result
assessment_marker = '''                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 600;">
                  <span>Confidence Level:</span>
                  <span id="diagConf" style="color: var(--primary);">92% Match</span>
                </div>
                <div class="confidence-bar">
                  <div class="confidence-fill" id="confBar" style="width: 92%;"></div>
                </div>'''

assessment_replacement = '''                <div style="margin: 8px 0;">
                  <span style="font-size: 0.85rem; font-weight: 600; color: #475569;">Clinical Triage Band:</span>
                  <div id="triageBandContainer" class="triage-band likely" style="margin-left: 6px;">Likely Differential</div>
                </div>
                <div style="margin-top: 10px;">
                  <button class="btn btn-outline btn-sm" id="sendToVetBtn" onclick="forwardCaseToVet()" style="width: 100%; border-color: #15803d; color: #15803d; font-weight: 700;">
                    Forward Case to Vet Care Desk
                  </button>
                </div>'''

if assessment_marker in html:
    html = html.replace(assessment_marker, assessment_replacement)
    print("Updated Assessment Result with Qualitative Triage Bands & Forward button.")

# C. Add Vet Care Desk Section before Blueprint
vet_desk_section = '''
  <!-- Veterinary Care Desk & Caseload Hub -->
  <section class="module-section" id="vet-desk" style="background: #f8fafc; border-top: 2px solid #e2e8f0; border-bottom: 2px solid #e2e8f0;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Clinical Tele-Triage &amp; Caseload</span>
        <h2 class="section-title">Veterinary Care Desk &amp; Field Station</h2>
        <p class="section-subtitle">
          Authorized clinical review station for Government LDOs and Registered Veterinary Practitioners. Review farmer appointment requests, assess referred triage cases, and digitally sign prescriptions with live food-safety milk withdrawal clocks.
        </p>
      </div>

      <div class="vet-desk-grid">
        <!-- Column 1: Incoming Farm Appointments -->
        <div class="desk-column">
          <div class="desk-column-header">
            <div>
              <h3 style="font-size: 1.1rem; font-weight: 700; color: #0f172a;">Farm Appointment Requests</h3>
              <span style="font-size: 0.8rem; color: #64748b;">Direct bookings from livestock owners</span>
            </div>
            <span class="vax-pill vax-due" id="aptCountBadge">2 Active</span>
          </div>
          <div id="vetAppointmentsContainer">
            <!-- Injected by JS -->
          </div>
        </div>

        <!-- Column 2: Referred AI Triage Cases -->
        <div class="desk-column">
          <div class="desk-column-header">
            <div>
              <h3 style="font-size: 1.1rem; font-weight: 700; color: #0f172a;">Referred AI Triage Cases</h3>
              <span style="font-size: 0.8rem; color: #64748b;">Cases awaiting clinical exam &amp; prescription</span>
            </div>
            <span class="vax-pill vax-due" id="caseCountBadge">1 Active</span>
          </div>
          <div id="vetCasesContainer">
            <!-- Injected by JS -->
          </div>
        </div>
      </div>
    </div>
  </section>
'''

blueprint_marker = '  <!-- Project Blueprint & Technical Architecture Explorer -->\n  <section class="module-section" id="blueprint">'
if blueprint_marker in html:
    html = html.replace(blueprint_marker, vet_desk_section + '\n' + blueprint_marker)
    print("Injected Vet Care Desk section into index.html.")

# D. Add Prescription Modal & Emergency Red-Flag Modal
new_modals = '''
  <!-- Clinical Examination & Prescription Modal -->
  <div class="modal-overlay" id="prescribeModal">
    <div class="modal-card" style="max-width: 600px;">
      <div class="modal-header">
        <h3 style="color: #15803d;">Veterinary Clinical Examination &amp; Prescription</h3>
        <button class="modal-close" onclick="document.getElementById('prescribeModal').classList.remove('active')">&times;</button>
      </div>
      <div class="modal-body">
        <form id="prescribeForm">
          <div class="form-row" style="margin-bottom: 14px;">
            <div class="form-group">
              <label for="rxAnimalTag">Animal Tag / Patient *</label>
              <select id="rxAnimalTag" class="form-control" required>
                <option value="MH-24-9812">Gauri (Tag: MH-24-9812) - Cattle</option>
                <option value="MH-12-4401">Raja (Tag: MH-12-4401) - Buffalo</option>
                <option value="MH-18-3310">Chotu (Tag: MH-18-3310) - Goat</option>
              </select>
            </div>
            <div class="form-group">
              <label for="rxCondition">Confirmed Clinical Diagnosis *</label>
              <input type="text" id="rxCondition" class="form-control" value="Acute Mastitis (Udder Swelling)" required>
            </div>
          </div>

          <div class="form-row" style="margin-bottom: 14px;">
            <div class="form-group">
              <label for="rxDrug">Prescribed Antimicrobial / Drug *</label>
              <input type="text" id="rxDrug" class="form-control" value="Ceftiofur Sodium + Flunixin Meglumine" required>
            </div>
            <div class="form-group">
              <label for="rxRoute">Route of Administration *</label>
              <select id="rxRoute" class="form-control">
                <option value="Intramammary + IM">Intramammary Infusion + IM</option>
                <option value="Intramuscular (IM)">Intramuscular (IM)</option>
                <option value="Intravenous (IV)">Intravenous (IV)</option>
                <option value="Oral Bolus">Oral Bolus</option>
              </select>
            </div>
          </div>

          <!-- HIGHEST STAKES LOGIC: WITHDRAWAL PERIOD FROM FINAL DOSE -->
          <div style="background: #fffbeb; border: 1.5px solid #f59e0b; border-radius: 8px; padding: 12px; margin-bottom: 14px;">
            <div style="font-weight: 700; color: #b45309; font-size: 0.88rem; margin-bottom: 6px;">
              Food Safety &amp; Withdrawal Calculation (Critical)
            </div>
            <p style="font-size: 0.8rem; color: #78350f; margin-bottom: 10px;">
              Withdrawal clock computes from the <strong>last dose</strong>: T_end = Exam_Date + (Treatment_Days + Milk_Withdrawal_Hours). Never clear milk while dosing is active.
            </p>
            <div class="form-row">
              <div class="form-group">
                <label for="rxTreatmentDays">Treatment Duration (Days) *</label>
                <input type="number" id="rxTreatmentDays" class="form-control" value="3" min="1" max="14" required>
              </div>
              <div class="form-group">
                <label for="rxMilkHours">Milk Withdrawal Period (Hours post-final-dose) *</label>
                <input type="number" id="rxMilkHours" class="form-control" value="72" min="0" max="360" required>
              </div>
            </div>
          </div>

          <div class="form-row" style="margin-bottom: 16px;">
            <div class="form-group">
              <label for="rxVetName">Attending Veterinary Officer *</label>
              <input type="text" id="rxVetName" class="form-control" value="Dr. Rameshwar Kute, B.V.Sc &amp; A.H." required>
            </div>
            <div class="form-group">
              <label for="rxVetReg">MSVC Registration Number *</label>
              <input type="text" id="rxVetReg" class="form-control" value="MSVC/2012/03194" required>
            </div>
          </div>

          <div style="display: flex; justify-content: flex-end; gap: 10px;">
            <button type="button" class="btn btn-outline" onclick="document.getElementById('prescribeModal').classList.remove('active')">Cancel</button>
            <button type="submit" class="btn btn-primary" style="background: #15803d;">Sign &amp; Seal Clinical Record</button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- Emergency 1962 Red-Flag Modal -->
  <div class="modal-overlay" id="emergencyModal">
    <div class="modal-card" style="max-width: 540px; border-top: 6px solid #b91c1c;">
      <div class="modal-header">
        <h3 style="color: #b91c1c; display: flex; align-items: center; gap: 8px;">
          CRITICAL BIOSECURITY &amp; HERD HEALTH ALERT
        </h3>
        <button class="modal-close" onclick="document.getElementById('emergencyModal').classList.remove('active')">&times;</button>
      </div>
      <div class="modal-body">
        <div class="emergency-banner-box">
          <div style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Government of Maharashtra Emergency Helpline</div>
          <div style="font-size: 2.2rem; font-weight: 800; margin: 6px 0;">1962 (Toll-Free)</div>
          <p style="font-size: 0.85rem; opacity: 0.95;">
            Red-flag symptom detected indicating possible notifiable pathogen (e.g. Anthrax, Acute Hemorrhagic Septicemia, or virulent outbreak).
          </p>
          <a href="tel:1962" class="emergency-call-btn">
            Dial 1962 Emergency Hotline Now
          </a>
        </div>

        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
          <h4 style="font-size: 0.9rem; font-weight: 700; color: #0f172a; margin-bottom: 8px;">Immediate Biosecurity Directives:</h4>
          <ol style="font-size: 0.82rem; color: #334155; padding-left: 20px; line-height: 1.6;">
            <li><strong>Isolate the affected animal</strong> at least 50 meters away from healthy herd members.</li>
            <li><strong>Halt milk pooling and sales</strong> immediately to protect human food safety.</li>
            <li><strong>Do not transport or slaughter</strong> any animal from the premises.</li>
            <li><strong>Disinfect cow shed perimeter</strong> with quicklime or 4% sodium carbonate.</li>
          </ol>
        </div>

        <div style="margin-top: 16px; text-align: right;">
          <button type="button" class="btn btn-outline btn-sm" onclick="document.getElementById('emergencyModal').classList.remove('active')">
            Acknowledge &amp; Return to Screening
          </button>
        </div>
      </div>
    </div>
  </div>
'''

footer_marker = '  <!-- Footer -->'
if footer_marker in html:
    html = html.replace(footer_marker, new_modals + '\n' + footer_marker)
    print("Injected Prescribe Modal & Emergency 1962 Modal into index.html.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved updated index.html successfully!")

