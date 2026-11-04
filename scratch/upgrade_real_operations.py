# -*- coding: utf-8 -*-
"""
PashuSachet Operational Upgrade:
Transforms all static cards & mockups into tactile, interactive government & veterinary workflows.
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Operational Modals right before the legacy test store
operational_modals = '''
  <!-- ======================================================================
       OPERATIONAL MODAL 1: GRAM PANCHAYAT EMERGENCY SMS BROADCAST
       ====================================================================== -->
  <div class="notebook-modal-overlay" id="villageSmsModal">
    <div class="notebook-modal-card" style="max-width: 520px;">
      <div class="modal-header-row">
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="brand-emblem" style="color:var(--urgency-critical);"><span data-icon="send" data-size="18"></span></div>
          <h2 class="modal-title-text">ग्रामपंचायत तातडीचा SMS अलर्ट (Emergency Blast)</h2>
        </div>
        <button class="btn-close-modal" onclick="closeVillageSmsModal()"><span data-icon="x" data-size="16"></span></button>
      </div>
      <div style="margin-top:14px;">
        <div style="background:var(--bg-paper-subtle); padding:12px; border-radius:var(--radius-sm); font-size:13px; margin-bottom:12px;">
          <div><strong>लक्ष्यित गाव:</strong> <span id="smsTargetVillage">निमगाव जाळी (Nimgaon Jali)</span></div>
          <div style="margin-top:3px;"><strong>नोंदणीकृत पशुपालक:</strong> <span id="smsTargetCount" style="color:var(--status-info); font-weight:700;">480 शेतकरी</span></div>
          <div style="margin-top:3px;"><strong>प्रसारण गेटवे:</strong> CDAC e-Gov SMS Gateway (Bulk Push)</div>
        </div>
        <label style="font-size:12px; font-weight:600; color:var(--ink-secondary);">मराठी संदेश मसुदा (SMS Template)</label>
        <textarea id="smsMessageContent" class="notebook-input" rows="4" style="margin-top:4px; font-size:13px; line-height:1.5; resize:none;">अत्यंत महत्त्वाचे: पशूसचेत व पशुसंवर्धन विभाग अलर्ट. गावात लाळ्या खुरकूत (FMD) संशयित रुग्ण आढळले आहेत. कृपया सर्व जनावरे गोठ्यात बांधून ठेवावीत, चारा-पाणी वेगळे करावे. १९६२ फिरते पथक गावात दाखल होत आहे. - जिल्हाधिकारी कार्यालय.</textarea>
        
        <div id="smsProgressBarContainer" style="display:none; margin:14px 0;">
          <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:600; margin-bottom:4px;">
            <span>SMS पाठवले जात आहेत...</span>
            <span id="smsProgressPercent">0%</span>
          </div>
          <div style="height:6px; background:var(--border-subtle); border-radius:3px; overflow:hidden;">
            <div id="smsProgressBar" style="width:0%; height:100%; background:var(--status-success); transition:width 0.3s ease;"></div>
          </div>
        </div>

        <div style="display:flex; gap:10px; margin-top:16px;">
          <button type="button" class="btn btn-outline" onclick="closeVillageSmsModal()" style="flex:1;">रद्द करा</button>
          <button type="button" class="btn btn-primary" id="btnSendSmsBlast" onclick="executeSmsBroadcast()" style="flex:2;">
            <span data-icon="send" data-size="14"></span>
            <span>तातडीने SMS पाठवा (Broadcast)</span>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ======================================================================
       OPERATIONAL MODAL 2: OFFICIAL GOVERNMENT ORDER (GR) VIEWER
       ====================================================================== -->
  <div class="notebook-modal-overlay" id="officialOrderModal">
    <div class="notebook-modal-card" style="max-width: 600px;">
      <div class="modal-header-row">
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="brand-emblem" style="color:var(--accent-turmeric);"><span data-icon="file-text" data-size="18"></span></div>
          <h2 class="modal-title-text">अधिकृत शासन निर्णय (Government Order)</h2>
        </div>
        <button class="btn-close-modal" onclick="closeOfficialOrderModal()"><span data-icon="x" data-size="16"></span></button>
      </div>
      <div id="officialOrderContent" style="margin-top:14px; background:#FFFFFF; border:1px solid var(--border-medium); padding:20px; border-radius:var(--radius-sm); font-size:13px; line-height:1.6; color:#1e293b;">
        <!-- Populated dynamically by viewOfficialOrder() -->
      </div>
      <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:16px;">
        <button type="button" class="btn btn-outline" onclick="window.print()">
          <span data-icon="printer" data-size="14"></span>
          <span>प्रत मुद्रित करा (Print)</span>
        </button>
        <button type="button" class="btn btn-primary" onclick="closeOfficialOrderModal()">
          <span>समजले (Done)</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ======================================================================
       OPERATIONAL MODAL 3: PARA-VET ON-FARM VITALS ENTRY
       ====================================================================== -->
  <div class="notebook-modal-overlay" id="paravetVitalsModal">
    <div class="notebook-modal-card" style="max-width: 480px;">
      <div class="modal-header-row">
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="brand-emblem" style="color:var(--status-success);"><span data-icon="clipboard-check" data-size="18"></span></div>
          <h2 class="modal-title-text">गोठा पातळीवर शारीरिक तपासणी (On-Farm Vitals)</h2>
        </div>
        <button class="btn-close-modal" onclick="closeParavetVitalsModal()"><span data-icon="x" data-size="16"></span></button>
      </div>
      <form id="paravetVitalsForm" onsubmit="event.preventDefault(); submitParavetVitals();" style="margin-top:14px;">
        <input type="hidden" id="vitalsSignalId">
        <div style="display:flex; flex-direction:column; gap:12px;">
          <div>
            <label style="font-size:12px; font-weight:600; color:var(--ink-secondary);">गुदाशय तापमान (Rectal Temp °F)</label>
            <input type="number" id="vitalsTemp" class="notebook-input" value="103.8" step="0.1" required>
          </div>
          <div>
            <label style="font-size:12px; font-weight:600; color:var(--ink-secondary);">रवंथ हालचाल (Rumination/min)</label>
            <select id="vitalsRumination" class="notebook-input">
              <option value="depressed">मंदावलेली (१ पेक्षा कमी / २ मिनिटे) - गंभीर</option>
              <option value="normal">सामान्य (२ ते ३ / २ मिनिटे)</option>
              <option value="absent">पूर्णपणे बंद (Absent) - तातडीची केस</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; font-weight:600; color:var(--ink-secondary);">तोंडातील / खुरांमधील फोड (Vesicular Lesions)</label>
            <select id="vitalsLesions" class="notebook-input">
              <option value="present_ruptured">फोड फुटून जखमा झालेल्या (Erosions Present)</option>
              <option value="present_intact">ताजे फोड (Intact Vesicles)</option>
              <option value="nodules">त्वचेवर कडक गाठी (LSD Nodules)</option>
              <option value="none">काहीही नाही (None)</option>
            </select>
          </div>
          <div>
            <label style="font-size:12px; font-weight:600; color:var(--ink-secondary);">पशु सखी शेरा (Field Observations)</label>
            <input type="text" id="vitalsNotes" class="notebook-input" value="लाळ गळत आहे, जनावराला चालताना त्रास होतोय. तात्काळ पशुवैद्यकीय अधिकारी तपासणीची गरज." required>
          </div>
          <div style="display:flex; gap:10px; margin-top:8px;">
            <button type="button" class="btn btn-outline" onclick="closeParavetVitalsModal()" style="flex:1;">रद्द करा</button>
            <button type="submit" class="btn btn-primary" style="flex:2;">
              <span>नोंद जतन करा व पाठवा</span>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>

  <!-- ======================================================================
       OPERATIONAL MODAL 4: RDDL REAL-TIME RT-PCR SIMULATOR
       ====================================================================== -->
  <div class="notebook-modal-overlay" id="rddlPcrModal">
    <div class="notebook-modal-card" style="max-width: 540px;">
      <div class="modal-header-row">
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="brand-emblem" style="color:var(--ink-secondary);"><span data-icon="flask" data-size="18"></span></div>
          <h2 class="modal-title-text">RDDL RT-PCR विश्‍लेषण (Thermocycler Run)</h2>
        </div>
        <button class="btn-close-modal" onclick="closeRddlPcrModal()"><span data-icon="x" data-size="16"></span></button>
      </div>
      <div style="margin-top:14px;">
        <div style="font-size:13px; color:var(--ink-secondary); margin-bottom:12px;">
          नमुना क्र.: <strong id="pcrSampleId">SMP-2026-041</strong> • लक्ष्यित विषाणू: <strong>Foot and Mouth Disease Virus (FMDV Serotype O)</strong>
        </div>
        
        <div id="pcrRunningState" style="text-align:center; padding:20px; background:var(--bg-paper-subtle); border-radius:var(--radius-sm);">
          <div style="font-size:24px; font-weight:800; font-family:var(--font-mono); color:var(--accent-turmeric);" id="pcrCycleCount">Cycle: 0 / 40</div>
          <div style="font-size:12px; color:var(--ink-secondary); margin-top:4px;">TaqMan Real-Time Fluorogenic Probe Active...</div>
          <div style="height:6px; background:var(--border-subtle); border-radius:3px; overflow:hidden; margin-top:14px;">
            <div id="pcrProgress" style="width:0%; height:100%; background:var(--accent-turmeric); transition:width 0.1s linear;"></div>
          </div>
        </div>

        <div id="pcrResultState" style="display:none; margin-top:14px; background:#f0fdf4; border:1px solid #bbf7d0; padding:16px; border-radius:var(--radius-sm);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong style="color:#166534; font-size:15px;">✓ RT-PCR निकाल: पॉझिटिव्ह (POSITIVE)</strong>
            <span class="badge-pill" style="background:#dcfce7; color:#15803d;">Ct = 18.42</span>
          </div>
          <p style="font-size:13px; color:#1e293b; margin:8px 0 0; line-height:1.5;">
            उच्च विषाणू भार (High Viral Load detected). ICAR-NIVEDI NADRES V2 राष्ट्रीय डेटाबेसमध्ये स्वयंचलित नोंदणी पूर्ण.
          </p>
        </div>

        <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:16px;">
          <button type="button" class="btn btn-outline" onclick="closeRddlPcrModal()">बंद करा</button>
          <button type="button" class="btn btn-primary" id="btnRunPcr" onclick="startRtPcrThermocycler()">
            <span>विश्लेषण सुरू करा (Start 40 Cycles)</span>
          </button>
        </div>
      </div>
    </div>
  </div>
'''

if 'id="villageSmsModal"' not in html:
    html = html.replace('<div class="legacy-test-store"', operational_modals + '\n  <div class="legacy-test-store"')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Added 4 operational modals to index.html")
else:
    print("Operational modals already exist in index.html")

print("index.html successfully updated.")

