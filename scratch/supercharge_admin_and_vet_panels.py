import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update css/style.css with rich operational styling
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

operational_css = """
/* ==========================================================================
   10. OPERATIONAL DASHBOARD CARDS & ACTIONS (Admin, Vet, Para-Vet, RDDL)
   ========================================================================== */

/* Buttons & Interactive Elements */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 18px;
  font-size: 13.5px;
  font-weight: 600;
  border-radius: var(--radius-pill);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
  text-decoration: none;
  border: 1px solid transparent;
  user-select: none;
  touch-action: manipulation;
}

.btn:active {
  transform: scale(0.97);
}

.btn-sm {
  padding: 6px 14px;
  font-size: 12.5px;
}

.btn-primary {
  background: var(--accent-turmeric);
  color: #FFFFFF;
  border-color: transparent;
  box-shadow: 0 2px 6px rgba(221, 167, 58, 0.3);
}

.btn-primary:hover {
  background: var(--accent-turmeric-hover);
  box-shadow: 0 4px 10px rgba(221, 167, 58, 0.4);
}

.btn-success {
  background: var(--status-success);
  color: #FFFFFF;
  box-shadow: 0 2px 6px rgba(51, 107, 81, 0.25);
}

.btn-success:hover {
  background: var(--status-success-hover);
}

.btn-danger {
  background: var(--urgency-critical);
  color: #FFFFFF;
  box-shadow: 0 2px 6px rgba(184, 93, 67, 0.25);
}

.btn-danger:hover {
  background: var(--urgency-critical-hover);
}

.btn-outline {
  background: var(--bg-surface);
  border-color: var(--border-medium);
  color: var(--ink-primary);
}

.btn-outline:hover {
  background: var(--bg-paper-light);
  border-color: var(--ink-primary);
}

/* Decision Queue Cards */
.decision-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-left: 4px solid var(--accent-turmeric);
  border-radius: var(--radius-md);
  padding: 18px 20px;
  margin-bottom: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  box-shadow: var(--shadow-card);
  transition: all var(--duration-fast) var(--ease-spring);
}

.decision-card:hover {
  border-color: var(--border-medium);
  box-shadow: var(--shadow-floating);
  transform: translateY(-1px);
}

/* Village Signals Grid */
#villageSignalsGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 14px;
}

.village-signal-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: var(--shadow-card);
  transition: all var(--duration-fast) var(--ease-spring);
}

.village-signal-card:hover {
  border-color: var(--border-medium);
  box-shadow: var(--shadow-floating);
  transform: translateY(-2px);
}

/* Sample Tracker Cards & Stepper */
.sample-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 22px;
  margin-bottom: 16px;
  box-shadow: var(--shadow-card);
}

.sample-step-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 18px 0;
  position: relative;
  gap: 8px;
  overflow-x: auto;
}

.sample-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  flex: 1;
  text-align: center;
  font-size: 11.5px;
  color: var(--ink-secondary);
  white-space: nowrap;
}

.step-circle {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--bg-paper-subtle);
  color: var(--ink-secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 12px;
  border: 1.5px solid var(--border-medium);
  transition: all var(--duration-fast) var(--ease-spring);
}

.sample-step.active .step-circle {
  background: var(--accent-turmeric);
  color: #FFFFFF;
  border-color: var(--accent-turmeric);
  box-shadow: 0 0 0 3px var(--accent-turmeric-light);
}

.sample-step.completed .step-circle {
  background: var(--status-success);
  color: #FFFFFF;
  border-color: var(--status-success);
}

.sample-step.completed {
  color: var(--status-success);
  font-weight: 600;
}

/* Para-Vet Signal Cards & App Cards */
.signal-card, .app-card, .appointment-card, .case-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 20px;
  margin-bottom: 14px;
  box-shadow: var(--shadow-card);
  transition: all var(--duration-fast) var(--ease-spring);
}

.signal-card:hover, .app-card:hover, .appointment-card:hover, .case-card:hover {
  border-color: var(--border-medium);
  box-shadow: var(--shadow-floating);
  transform: translateY(-2px);
}

.badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  font-size: 12px;
  font-weight: 700;
  width: fit-content;
}
"""

if '.decision-card' not in css:
    css += "\n" + operational_css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✓ Added operational CSS to css/style.css")
else:
    print("operational CSS already in css/style.css")

# 2. Update js/app.js to make all cards interactive, rich, and real
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Enhance renderOfficerDecisionQueue
old_dec_queue = """function renderOfficerDecisionQueue() {
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
}"""

new_dec_queue = """function renderOfficerDecisionQueue() {
  const container = document.getElementById("officerDecisionQueue");
  if (!container) return;

  container.innerHTML = officerDecisions.map(dec => `
    <div class="decision-card" style="border-left-color: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical)' : 'var(--accent-turmeric)'};">
      <div style="flex: 1;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
          <strong style="color: var(--ink-primary); font-size: 15px;">${dec.title}</strong>
          <span class="badge-pill" style="background: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical-light)' : 'var(--accent-turmeric-light)'}; color: ${dec.priority === 'CRITICAL_ZOONOTIC' ? 'var(--urgency-critical)' : '#92400e'};">
            ${dec.priority}
          </span>
        </div>
        <p style="font-size: 13px; color: var(--ink-secondary); margin: 0; line-height: 1.5;">
          ${dec.details}
        </p>
      </div>

      <div style="flex-shrink: 0;">
        ${dec.status === 'PENDING' ? `
          <button type="button" class="btn btn-sm btn-primary" onclick="resolveOfficerDecision('${dec.id}')" style="white-space: nowrap;">
            ✓ ${dec.actionLabel}
          </button>
        ` : `
          <span class="badge-pill" style="background: var(--status-success-light); color: var(--status-success);">
            ✓ मंजूर (Action Authorized)
          </span>
        `}
      </div>
    </div>
  `).join("");
}"""

if old_dec_queue in js:
    js = js.replace(old_dec_queue, new_dec_queue)
    print("✓ Enhanced renderOfficerDecisionQueue")
else:
    print("Warning: old_dec_queue not matched")

# Enhance inspectMapPin to provide real interactive operations
old_inspect_pin = """function inspectMapPin(village, count, disease, clusterStatus) {
  const inspector = document.getElementById("mapPinInspector");
  const details = document.getElementById("mapPinDetails");
  if (!inspector || !details) return;

  inspector.style.display = "block";
  let statusBadge = clusterStatus === "SURGE_CLUSTER" ?
    '<span style="background:#dc2626; color:#ffffff; padding:2px 6px; border-radius:4px; font-weight:800;">SURGE CLUSTER</span>' :
    (clusterStatus === "K_ANONYMIZED" ?
      '<span style="background:#0f766e; color:#ffffff; padding:2px 6px; border-radius:4px; font-weight:800;">K-ANONYMIZED TALUKA BLOCK</span>' :
      '<span style="background:#d97706; color:#ffffff; padding:2px 6px; border-radius:4px; font-weight:800;">WATCH CLUSTER</span>');

  details.innerHTML = `
    <strong>Cluster Inspected:</strong> ${village} • <strong>Cases:</strong> ${count} • <strong>Disease:</strong> ${disease} • ${statusBadge}
    <div style="font-size: 0.82rem; color: #475569; margin-top: 4px;">
      Live Action Trigger: 5km Ring-Vaccination dispatched. MVU Emergency Unit 14 pre-alerted. Local Gram Panchayat quarantine advisory active.
    </div>
  `;
}"""

new_inspect_pin = """function inspectMapPin(village, count, disease, clusterStatus) {
  const inspector = document.getElementById("mapPinInspector");
  const details = document.getElementById("mapPinDetails");
  if (!inspector || !details) return;

  inspector.style.display = "block";
  let statusBadge = clusterStatus === "SURGE_CLUSTER" ?
    '<span class="badge-pill" style="background: var(--urgency-critical-light); color: var(--urgency-critical);">SURGE CLUSTER</span>' :
    (clusterStatus === "K_ANONYMIZED" ?
      '<span class="badge-pill" style="background: var(--status-success-light); color: var(--status-success);">K-ANONYMIZED BLOCK</span>' :
      '<span class="badge-pill" style="background: var(--status-warning-light); color: var(--status-warning);">WATCH CLUSTER</span>');

  details.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 14px; flex-wrap: wrap;">
      <div>
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
          <strong style="font-size: 16px; color: var(--ink-primary);">गाव / क्लस्टर: ${village}</strong>
          ${statusBadge}
        </div>
        <div style="font-size: 13px; color: var(--ink-secondary);">
          बाधित जनावरे: <strong>${count} केसेस</strong> • संशयित आजार: <strong>${disease}</strong> • पशुधन जनगणना: २,४८० गुरे
        </div>
      </div>

      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <button type="button" class="btn btn-sm btn-danger" onclick="dispatchMvuToVillage('${village}')">
          <span data-icon="phone-call" data-size="13"></span>
          <span>१९६२ पथक पाठवा</span>
        </button>
        <button type="button" class="btn btn-sm btn-primary" onclick="toggleRingVaxRadius(); showToast('५ किमी रिंग लसीकरण ${village} येथे सक्रिय!')">
          <span data-icon="shield" data-size="13"></span>
          <span>५ किमी रिंग लावा</span>
        </button>
        <button type="button" class="btn btn-sm btn-outline" onclick="showToast('${village} ग्रामपंचायतीस अलर्ट SMS पाठवला!')">
          <span data-icon="send" data-size="13"></span>
          <span>अलर्ट SMS पाठवा</span>
        </button>
      </div>
    </div>
  `;

  if (typeof renderIcons === 'function') renderIcons();
}

function dispatchMvuToVillage(village) {
  const mvuDetails = document.getElementById("mvuTicketDetails");
  const mvuGps = document.getElementById("mvuGpsDist");
  if (mvuDetails) {
    mvuDetails.innerHTML = `<strong>थेट कारवाई:</strong> फिरते पशुवैद्यकीय रुग्णालय (MVU Unit 04) तात्काळ <strong>${village}</strong> कडे रवाना केले आहे. अंदाजे पोहच वेळ: ~१६ मिनिटे.`;
  }
  if (mvuGps) {
    mvuGps.innerHTML = `GPS LIVE: ४२ किमी/तास गती • ${village} क्लस्टरकडे मार्गस्थ`;
  }
  showToast(`१९६२ रुग्णवाहिका ${village} क्लस्टरसाठी रवाना केली!`);
}"""

if old_inspect_pin in js:
    js = js.replace(old_inspect_pin, new_inspect_pin)
    print("✓ Enhanced inspectMapPin with real operational action triggers")
else:
    print("Warning: old_inspect_pin not matched")

# Enhance renderParavetInbox to remove emoji and give rich Apple buttons
old_paravet_render = """  if (pending.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; background: #ffffff; border: 2px dashed #cbd5e1; border-radius: 12px; padding: 40px; text-align: center; color: #64748b;">
        <div style="font-size: 2.5rem; margin-bottom: 8px;">✅</div>
        <h4 style="color: #0f172a; margin: 0 0 4px;">All Signals Verified in Your Beat</h4>
        <p style="font-size: 0.85rem; margin: 0;">No pending farmer micro-reports requiring field confirmation right now.</p>
      </div>
    `;
    return;
  }"""

new_paravet_render = """  if (pending.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; background: #ffffff; border: 2px dashed var(--border-medium); border-radius: var(--radius-lg); padding: 40px; text-align: center; color: var(--ink-secondary);">
        <div style="width: 44px; height: 44px; border-radius: 50%; background: var(--status-success-light); color: var(--status-success); display: flex; align-items: center; justify-content: center; margin: 0 auto 12px auto;">
          <span data-icon="check-circle-2" data-size="24"></span>
        </div>
        <h4 style="color: var(--ink-primary); margin: 0 0 4px; font-size: 16px;">बीटमधील सर्व अहवाल पडताळले आहेत (All Verified)</h4>
        <p style="font-size: 13px; margin: 0;">सध्या आपल्या बीटमध्ये कोणतीही प्रलंबित शेतकरी तक्रार शिल्लक नाही.</p>
      </div>
    `;
    if (typeof renderIcons === 'function') renderIcons();
    return;
  }"""

if old_paravet_render in js:
    js = js.replace(old_paravet_render, new_paravet_render)
    print("✓ Replaced emoji in renderParavetInbox")
else:
    print("Warning: old_paravet_render not matched")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Saved updated js/app.js with real admin operations")

