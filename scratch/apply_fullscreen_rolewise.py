# -*- coding: utf-8 -*-
"""
Apply Full-Screen Edge-to-Edge and Role-Wise Workstation Switching to the Rock-Solid Base:
1. css/style.css: .container uses 100% width edge-to-edge
2. index.html: add "All Modules" option to segmented control
3. js/app.js: activatePersona(role) filters sections cleanly to role-specific workstations
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .container max-width 1220px with edge-to-edge full width
old_container = '''.container {
  width: 100%;
  max-width: 1220px;
  margin: 0 auto;
  padding: 0 24px;
}'''

new_container = '''.container {
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 0 clamp(16px, 3.5vw, 44px);
}

.role-section-hidden {
  display: none !important;
}

/* Full-width responsive section grids */
.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 36px;
  width: 100%;
}

.symptom-layout-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 28px;
  width: 100%;
}

.gis-grid {
  display: grid;
  grid-template-columns: 1.35fr 0.65fr;
  gap: 28px;
  width: 100%;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  width: 100%;
}

@media (max-width: 992px) {
  .hero-grid, .symptom-layout-grid, .gis-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}'''

if old_container in css:
    css = css.replace(old_container, new_container)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✓ Updated css/style.css with 100% edge-to-edge full-screen containers")
else:
    print("Container already edge-to-edge in css/style.css")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add personaAll button to persona-segmented-control if not present
old_pills = '''<button class="persona-pill" id="personaRddl" onclick="activatePersona('rddl')" title="RDDL Diagnostic Lab">🔬 RDDL Lab</button>
        </div>'''

new_pills = '''<button class="persona-pill" id="personaRddl" onclick="activatePersona('rddl')" title="RDDL Diagnostic Lab">🔬 RDDL Lab</button>
          <button class="persona-pill" id="personaAll" onclick="activatePersona('all')" title="Show All Modules">🌐 All (सर्व)</button>
        </div>'''

if old_pills in html:
    html = html.replace(old_pills, new_pills)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Added 'All (सर्व)' pill to segmented control in index.html")
else:
    print("Segmented control already has All pill")

# 3. Update activatePersona in js/app.js
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_activate_persona = '''function activatePersona(role) {
  currentPersona = role;
  
  const pills = ['personaFarmer', 'personaParavet', 'personaLdo', 'personaCollector', 'personaRddl'];
  pills.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });
  
  const activePill = document.getElementById(
    role === 'farmer' ? 'personaFarmer' :
    role === 'paravet' ? 'personaParavet' :
    role === 'ldo' ? 'personaLdo' :
    role === 'collector' ? 'personaCollector' : 'personaRddl'
  );
  if (activePill) activePill.classList.add('active');

  const paravetNav = document.getElementById('paravetNavLink');
  const adminNav = document.getElementById('adminNavLink');

  if (role === 'farmer') {
    quickLogin('farmer');
    renderAnimals();
    showToast('🧑‍🌾 शेतकरी मोड सक्रिय: जलद ९०-सेकंद तपासणी व पशू आधार उपलब्ध.');
    const el = document.getElementById('symptom-screening');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'paravet') {
    quickLogin('paravet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderParavetInbox();
    showToast('🩺 पशु सखी / पॅरा-व्हेट मोड: <30 सेकंद पडताळणी रांग सक्रिय.');
    const el = document.getElementById('paravet-inbox');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'ldo') {
    quickLogin('vet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderVetDesk();
    showToast('👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO) मोड: क्लिनिकल तपासणी व औषधोपचार कक्ष.');
    const el = document.getElementById('vet-desk');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'collector') {
    quickLogin('officer');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderVillageSignalBoard();
    renderOfficerDecisionQueue();
    showToast('🏛️ जिल्हा नियंत्रण कक्ष मोड: ५ किमी प्रतिबंधात्मक झोन व प्रादुर्भाव नियंत्रण नकाशा.');
    if (!ringVaxActive) toggleRingVaxRadius();
    const el = document.getElementById('outbreak-gis');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'rddl') {
    quickLogin('admin');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderSampleTracker();
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड: RT-PCR चाचणी व नमुना ट्रॅकिंग.');
    const el = document.getElementById('sample-tracker');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }
}'''

new_activate_persona = '''function applyRoleSectionFilter(role) {
  const roleSectionMap = {
    farmer: ['hero', 'symptom-screening', 'health-passport', 'vet-directory'],
    paravet: ['paravet-inbox', 'village-signal-board', 'outbreak-gis'],
    ldo: ['vet-desk', 'outbreak-gis'],
    collector: ['village-signal-board', 'outbreak-gis', 'admin-console'],
    rddl: ['sample-tracker', 'pilot-telemetry', 'admin-console'],
    all: ['hero', 'symptom-screening', 'outbreak-gis', 'village-signal-board', 'health-passport', 'vet-directory', 'vet-desk', 'paravet-inbox', 'sample-tracker', 'pilot-telemetry', 'admin-console']
  };

  const allSections = roleSectionMap.all;
  const activeSections = roleSectionMap[role] || roleSectionMap.all;

  allSections.forEach(sId => {
    const el = document.getElementById(sId);
    if (el) {
      if (role === 'all' || activeSections.includes(sId)) {
        el.classList.remove('role-section-hidden');
      } else {
        el.classList.add('role-section-hidden');
      }
    }
  });
}

function activatePersona(role) {
  currentPersona = role;
  
  const pills = ['personaFarmer', 'personaParavet', 'personaLdo', 'personaCollector', 'personaRddl', 'personaAll'];
  pills.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });
  
  const activePill = document.getElementById(
    role === 'farmer' ? 'personaFarmer' :
    role === 'paravet' ? 'personaParavet' :
    role === 'ldo' ? 'personaLdo' :
    role === 'collector' ? 'personaCollector' :
    role === 'rddl' ? 'personaRddl' : 'personaAll'
  );
  if (activePill) activePill.classList.add('active');

  const paravetNav = document.getElementById('paravetNavLink');
  const adminNav = document.getElementById('adminNavLink');

  // Filter sections to show role-specific workstation
  applyRoleSectionFilter(role);

  if (role === 'farmer') {
    quickLogin('farmer');
    renderAnimals();
    showToast('🧑‍🌾 शेतकरी मोड सक्रिय: जलद ९०-सेकंद तपासणी व पशू आधार.');
    const el = document.getElementById('symptom-screening');
    if (el && typeof el.scrollIntoView === 'function') el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'paravet') {
    quickLogin('paravet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderParavetInbox();
    showToast('🩺 पशु सखी / पॅरा-व्हेट डेस्क: <30 सेकंद पडताळणी रांग सक्रिय.');
    const el = document.getElementById('paravet-inbox');
    if (el && typeof el.scrollIntoView === 'function') el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'ldo') {
    quickLogin('vet');
    if (paravetNav) paravetNav.style.display = 'inline-block';
    renderVetDesk();
    showToast('👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO) कक्ष: क्लिनिकल तपासणी व प्रिस्क्रिप्शन.');
    const el = document.getElementById('vet-desk');
    if (el && typeof el.scrollIntoView === 'function') el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'collector') {
    quickLogin('officer');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderVillageSignalBoard();
    renderOfficerDecisionQueue();
    showToast('🏛️ जिल्हा नियंत्रण कक्ष: ५ किमी रिंग लसीकरण व प्रादुर्भाव नियंत्रण नकाशा.');
    if (!ringVaxActive) toggleRingVaxRadius();
    const el = document.getElementById('outbreak-gis');
    if (el && typeof el.scrollIntoView === 'function') el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'rddl') {
    quickLogin('admin');
    if (adminNav) adminNav.style.display = 'inline-block';
    renderSampleTracker();
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune): RT-PCR चाचणी व नमुना ट्रॅकिंग.');
    const el = document.getElementById('sample-tracker');
    if (el && typeof el.scrollIntoView === 'function') el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'all') {
    showToast('🌐 संपूर्ण प्रणाली दृश्य (All Modules View Active).');
    const el = document.getElementById('hero');
    if (el && typeof el.scrollIntoView === 'function') el.scrollIntoView({ behavior: 'smooth' });
  }
}'''

if old_activate_persona in js:
    js = js.replace(old_activate_persona, new_activate_persona)
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Updated js/app.js with role workstation filtering")
else:
    print("activatePersona already updated in js/app.js")
