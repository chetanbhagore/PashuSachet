# -*- coding: utf-8 -*-
"""
Apply PashuSachet v2 App Shell Transformation:
1. Add full-screen App Shell CSS to css/style.css
2. Upgrade index.html layout to include Desktop Left Sidebar and Mobile Bottom Tab Bar
3. Update js/app.js to drive dynamic role navigation for both Sidebar and Bottom Tab Bar
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. UPDATE css/style.css
# ==============================================================================
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

app_shell_css = '''
/* ==========================================================================
   V2 FULL-SCREEN APP SHELL & CHROME (APPLE NOTES + HEALTH DESKTOP/MOBILE SHELL)
   ========================================================================== */

.authenticated-app-shell {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  background: var(--bg-paper);
  z-index: 50;
}

/* Persistent Demo Banner */
.app-demo-banner {
  background: #1C3A2E;
  color: #FAF8F5;
  height: 28px;
  min-height: 28px;
  width: 100%;
  display: flex;
  align-items: center;
  padding: 0 16px;
  font-size: 11.5px;
  font-weight: 500;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  flex-shrink: 0;
  z-index: 60;
}

.demo-banner-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 12px;
}

.demo-banner-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--accent-turmeric);
  box-shadow: 0 0 6px var(--accent-turmeric);
  display: inline-block;
  margin-right: 6px;
}

.demo-banner-pill {
  background: rgba(221, 167, 58, 0.25);
  color: #FBBF24;
  border: 1px solid rgba(221, 167, 58, 0.5);
  padding: 1px 7px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.5px;
  white-space: nowrap;
}

/* TopBar full width edge-to-edge */
.site-topbar {
  height: 56px;
  min-height: 56px;
  width: 100%;
  background: #FFFFFF;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  flex-shrink: 0;
  z-index: 55;
  box-shadow: 0 1px 3px rgba(26, 56, 43, 0.03);
}

/* Persona Segmented Control */
.persona-segmented-control {
  display: inline-flex;
  align-items: center;
  background: var(--bg-paper-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  padding: 3px;
  gap: 2px;
}

.persona-tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  border: none;
  background: transparent;
  color: var(--ink-secondary);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 140ms var(--ease-spring);
  white-space: nowrap;
}

.persona-tab-btn:hover {
  color: var(--ink-primary);
  background: rgba(26, 56, 43, 0.04);
}

.persona-tab-btn.active {
  background: #FFFFFF;
  color: var(--ink-primary);
  box-shadow: 0 1px 4px rgba(26, 56, 43, 0.08), 0 1px 1px rgba(26, 56, 43, 0.04);
  border: 1px solid var(--border-medium);
}

/* App Shell Body */
.app-shell-body {
  display: flex;
  flex: 1;
  width: 100%;
  height: calc(100vh - 56px - 28px);
  overflow: hidden;
}

/* Desktop Left Sidebar */
.app-sidebar {
  width: 260px;
  min-width: 260px;
  max-width: 260px;
  height: 100%;
  background: #FFFFFF;
  border-right: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-shrink: 0;
  overflow-y: auto;
  z-index: 40;
}

.sidebar-user-card {
  padding: 16px 18px;
  border-bottom: 1px solid var(--border-subtle);
  background: #FCFBF9;
}

.sidebar-nav-menu {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 14px 12px;
  flex: 1;
  overflow-y: auto;
}

.sidebar-nav-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  color: var(--ink-secondary);
  font-size: 13.5px;
  font-weight: 500;
  text-decoration: none;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 140ms var(--ease-spring);
}

.sidebar-nav-item:hover {
  background: var(--bg-paper-subtle);
  color: var(--ink-primary);
}

.sidebar-nav-item.active {
  background: rgba(221, 167, 58, 0.12);
  color: var(--ink-primary);
  font-weight: 700;
  border-left: 3px solid var(--accent-turmeric);
}

.sidebar-nav-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-pill);
  background: var(--bg-paper-subtle);
  color: var(--ink-secondary);
}

.sidebar-nav-item.active .sidebar-nav-badge {
  background: var(--accent-turmeric);
  color: #FFFFFF;
}

.sidebar-bottom-actions {
  padding: 14px 12px;
  border-top: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sidebar-action-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  font-size: 12.5px;
  font-weight: 600;
  color: var(--ink-secondary);
  background: transparent;
  border: 1px solid var(--border-subtle);
  cursor: pointer;
  text-decoration: none;
  transition: all 140ms ease;
  width: 100%;
}

.sidebar-action-item.emergency {
  background: var(--urgency-critical-light);
  color: var(--urgency-critical);
  border-color: var(--urgency-critical-border);
}

.sidebar-action-item:hover {
  background: var(--bg-paper-subtle);
  color: var(--ink-primary);
}

/* Main Content Area - Full screen width, no centering gutters */
.app-main-content, .app-container {
  flex: 1;
  height: 100%;
  overflow-y: auto;
  padding: 24px 32px 40px 32px !important;
  width: 100% !important;
  max-width: none !important;
  margin: 0 !important;
  background: var(--bg-paper);
}

/* Mobile Bottom Tab Bar */
.app-bottom-bar {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: #FFFFFF;
  border-top: 1px solid var(--border-subtle);
  z-index: 100;
  justify-content: space-around;
  align-items: center;
  padding: 0 4px;
  box-shadow: 0 -2px 10px rgba(26, 56, 43, 0.05);
}

.bottom-tab-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  flex: 1;
  height: 100%;
  color: var(--ink-secondary);
  font-size: 11px;
  font-weight: 500;
  background: none;
  border: none;
  cursor: pointer;
  transition: all 140ms ease;
}

.bottom-tab-item.active {
  color: var(--accent-turmeric);
  font-weight: 700;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .app-sidebar {
    display: none !important;
  }
  .app-bottom-bar {
    display: flex !important;
  }
  .app-main-content, .app-container {
    padding: 16px 14px 80px 14px !important;
  }
  .persona-segmented-control {
    display: none;
  }
  .app-demo-banner {
    display: none;
  }
  .app-shell-body {
    height: calc(100vh - 56px);
  }
}
'''

if '.app-sidebar' not in css:
    css += '\n\n' + app_shell_css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✓ Added V2 full-screen App Shell CSS to css/style.css")
else:
    print("V2 App Shell CSS already in css/style.css")


# ==============================================================================
# 2. UPDATE index.html
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the beginning of authenticatedAppShell
old_app_header_pattern = r'<div id="authenticatedAppShell" class="authenticated-app-shell" style="display: none;">[\s\S]*?<main class="app-container">'

new_app_header = '''<div id="authenticatedAppShell" class="authenticated-app-shell" style="display: none;">
  <!-- PERSISTENT DEMO BANNER -->
  <div class="app-demo-banner" id="appDemoBanner">
    <div class="demo-banner-inner">
      <div style="display:flex; align-items:center;">
        <span class="demo-banner-dot"></span>
        <span class="demo-banner-text">
          <strong>पशूसचेत • प्रत्यक्ष फील्ड प्रणाली (Field Sentinel Demo)</strong> — Bharat Pashudhan (NDLM), 1962 फिरते पशुवैद्यकीय पथक व ICAR-NIVEDI NADRES V2 डेटा sync सक्रिय.
        </span>
      </div>
      <span class="demo-banner-pill">LIVE SENTINEL DEMO</span>
    </div>
  </div>

  <!-- FIXED FULL-WIDTH TOPBAR -->
  <header class="site-topbar">
    <div class="topbar-brand">
      <div class="brand-emblem">
        <span data-icon="shield" data-size="20"></span>
      </div>
      <div class="brand-titles">
        <span class="brand-name" id="brandAppTitle">PashuSachet</span>
        <span class="brand-subtitle" id="brandAppSub">पशु आरोग्य साथी</span>
      </div>
    </div>

    <!-- CENTER PERSONA SWITCHER (5 ROLES SEGMENTED CONTROL) -->
    <div class="topbar-center-role">
      <div class="persona-segmented-control" id="personaSegmentedControl">
        <button type="button" class="persona-tab-btn active" id="btnPersonaFarmer" onclick="activatePersona('farmer')">
          <span data-icon="home" data-size="14"></span>
          <span>शेतकरी</span>
        </button>
        <button type="button" class="persona-tab-btn" id="btnPersonaParavet" onclick="activatePersona('paravet')">
          <span data-icon="clipboard-check" data-size="14"></span>
          <span>पशु सखी</span>
        </button>
        <button type="button" class="persona-tab-btn" id="btnPersonaLdo" onclick="activatePersona('ldo')">
          <span data-icon="stethoscope" data-size="14"></span>
          <span>LDO डॉक्टर</span>
        </button>
        <button type="button" class="persona-tab-btn" id="btnPersonaCollector" onclick="activatePersona('collector')">
          <span data-icon="building-2" data-size="14"></span>
          <span>जिल्हाधिकारी / DVO</span>
        </button>
        <button type="button" class="persona-tab-btn" id="btnPersonaRddl" onclick="activatePersona('rddl')">
          <span data-icon="flask" data-size="14"></span>
          <span>RDDL लॅब</span>
        </button>
      </div>

      <!-- Sync Status Indicator -->
      <div class="sync-status-indicator" id="syncStatusBadge">
        <span class="sync-dot"></span>
        <span id="syncStatusLabel">ऑफलाइन सक्षम • २ मि. पूर्वी</span>
      </div>
      <div id="appRoleBadge" style="display:none;" onclick="openRoleSwitcher()"><span id="appRoleText"></span><span id="appBeatText"></span></div>
    </div>

    <!-- RIGHT TOPBAR ACTIONS -->
    <div class="topbar-actions">
      <!-- 1962 Emergency Pill -->
      <button class="emergency-pill-btn" id="emergencyPillBtn" onclick="openEmergencyModal()" title="1962 टोल-फ्री तातडीची सेवा">
        <span data-icon="phone-call" data-size="15"></span>
        <span>१९६२</span>
      </button>

      <!-- Language Switcher -->
      <button class="lang-switch-btn" id="langSwitchBtn" onclick="toggleLanguage()" title="भाषा बदला (EN / मराठी)">
        <span id="langCurrentText">EN</span>
      </button>

      <!-- Return to Landing -->
      <button class="lang-switch-btn" onclick="showLandingPage()" title="मुख्य पानावर जा (Exit to Landing)">
        <span data-icon="home" data-size="13"></span>
        <span style="margin-left: 4px;">मुख्य पान</span>
      </button>

      <!-- User Profile Dropdown Pill -->
      <button class="profile-capsule-btn" id="profileDropdownBtn" onclick="openRoleSwitcher()">
        <span class="profile-avatar-circle" id="userAvatarText">EB</span>
        <span id="userNameHeader" style="font-size: 13px;">एकनाथराव</span>
        <span data-icon="chevron-down" data-size="12"></span>
      </button>
    </div>
  </header>

  <!-- SUBNAV BAR (Hidden or Secondary Fallback) -->
  <nav class="role-subnav-bar" id="roleSubnavBar" style="display:none;">
  </nav>

  <!-- APP SHELL BODY (SIDEBAR + MAIN WORKSPACE CANVAS) -->
  <div class="app-shell-body">
    <!-- DESKTOP LEFT SIDEBAR -->
    <aside class="app-sidebar" id="appDesktopSidebar">
      <div class="sidebar-user-card">
        <div style="display:flex; align-items:center; gap:12px;">
          <div class="profile-avatar-circle" id="sidebarAvatar">EB</div>
          <div style="flex:1; overflow:hidden;">
            <div style="font-weight:700; font-size:14px; color:var(--ink-primary); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" id="sidebarUserName">एकनाथराव पाटील</div>
            <div style="font-size:11.5px; color:var(--ink-secondary);" id="sidebarRoleLabel">शेतकरी (साक्री बीट)</div>
          </div>
        </div>
      </div>

      <!-- DYNAMIC ROLE NAVIGATION LIST -->
      <nav class="sidebar-nav-menu" id="sidebarNavList">
        <!-- Rendered dynamically by renderSidebarNav(role) -->
      </nav>

      <!-- SIDEBAR PINNED BOTTOM ACTIONS -->
      <div class="sidebar-bottom-actions">
        <a href="tel:1962" class="sidebar-action-item emergency">
          <span data-icon="phone-call" data-size="16"></span>
          <span>१९६२ फिरते पथक कॉल</span>
        </a>
        <button type="button" class="sidebar-action-item" onclick="openAboutBlueprintModal()">
          <span data-icon="info" data-size="16"></span>
          <span>प्रणाली रूपरेषा (About)</span>
        </button>
      </div>
    </aside>

    <!-- MAIN SCROLLABLE WORKSPACE (FULL REMAINING SCREEN WIDTH) -->
    <main class="app-main-content app-container" id="appMainContent">'''

if 'id="appDesktopSidebar"' not in html:
    html = re.sub(old_app_header_pattern, new_app_header, html)
    
    # Close app-shell-body before modals
    old_footer_pattern = r'</main>\s*</div>\s*<!-- ======================================================================\s*MODAL 1: ROLE SWITCHER'
    new_footer = '''</main>
  </div>

  <!-- MOBILE BOTTOM TAB BAR (< 1024px) -->
  <nav class="app-bottom-bar" id="appMobileBottomBar">
    <!-- Rendered dynamically by renderBottomTabBar(role) -->
  </nav>
</div>

  <!-- ======================================================================
       MODAL 1: ROLE SWITCHER'''

    html = re.sub(old_footer_pattern, new_footer, html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Updated index.html with Desktop Sidebar, Mobile Bottom Bar, and Full-Screen Shell")
else:
    print("App shell structure already in index.html")


# ==============================================================================
# 3. UPDATE js/app.js FOR DYNAMIC SIDEBAR AND BOTTOM BAR
# ==============================================================================
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

navigation_engine_code = '''
// ==========================================================================
// V2 APP SHELL NAVIGATION ENGINE: DESKTOP SIDEBAR + MOBILE BOTTOM BAR
// ==========================================================================

const ROLE_NAV_SPECS = {
  farmer: {
    userName: "एकनाथराव पाटील",
    roleLabel: "शेतकरी (साक्री बीट)",
    avatar: "EB",
    items: [
      { id: 'viewFarmerHome', labelMr: 'आजची काळजी (Home)', labelEn: 'Today\'s Care', icon: 'home', badge: '' },
      { id: 'viewFarmerTriage', labelMr: 'लक्षणे नोंदवा (Report)', labelEn: 'Start Health Check', icon: 'stethoscope', badge: '९० से.' },
      { id: 'viewFarmerAnimals', labelMr: 'माझी जनावरे (Animals)', labelEn: 'My Animals', icon: 'tag', badge: '३' },
      { id: 'viewFarmerCases', labelMr: 'रुग्ण नोंदवही (Cases)', labelEn: 'Active Cases', icon: 'file-text', badge: '१ चालू' },
      { id: 'viewFarmerVets', labelMr: 'पशुवैद्यकीय दवाखाने', labelEn: 'Vet Care Directory', icon: 'phone-call', badge: '' }
    ]
  },
  paravet: {
    userName: "सुनिता पाटील",
    roleLabel: "पशु सखी (साक्री व ५ गावे)",
    avatar: "SP",
    items: [
      { id: 'paravetSignalsContainer', labelMr: 'पडताळणी रांग (Queue)', labelEn: 'Verification Queue', icon: 'clipboard-check', badge: '३ प्रलंबित' },
      { id: 'paravetVillageSelect', labelMr: 'गाव निवड व फिल्टर', labelEn: 'Village Filter', icon: 'filter', badge: '५ गावे' },
      { id: 'sampleSignalCount', labelMr: 'नमुना किट्स (Samples)', labelEn: 'Diagnostic Kits', icon: 'flask', badge: '२' },
      { id: 'outbreak-gis', labelMr: 'गाव नकाशा (Field Map)', labelEn: 'Village Map', icon: 'map-pin', badge: '' }
    ]
  },
  ldo: {
    userName: "डॉ. रामेश्वर कुटे",
    roleLabel: "पशुवैद्यकीय अधिकारी (साक्री)",
    avatar: "RK",
    items: [
      { id: 'vetAppointmentsContainer', labelMr: 'दवाखाना अपॉइंटमेंट्स', labelEn: 'Appointments', icon: 'calendar', badge: '३' },
      { id: 'vetCasesContainer', labelMr: 'AI-रेफर्ड तातडीच्या केसेस', labelEn: 'Referred Cases', icon: 'alert-triangle', badge: '२' },
      { id: 'prescribeForm', labelMr: 'डिजिटल प्रिस्क्रिप्शन (Rx)', labelEn: 'Prescription Engine', icon: 'pill', badge: 'दूध सुरक्षा' },
      { id: 'outbreak-gis', labelMr: 'साथरोग नियंत्रण नकाशा', labelEn: 'Epidemic Map', icon: 'map-pin', badge: '' }
    ]
  },
  vet: {
    userName: "डॉ. रामेश्वर कुटे",
    roleLabel: "पशुवैद्यकीय अधिकारी (साक्री)",
    avatar: "RK",
    items: [
      { id: 'vetAppointmentsContainer', labelMr: 'दवाखाना अपॉइंटमेंट्स', labelEn: 'Appointments', icon: 'calendar', badge: '३' },
      { id: 'vetCasesContainer', labelMr: 'AI-रेफर्ड तातडीच्या केसेस', labelEn: 'Referred Cases', icon: 'alert-triangle', badge: '२' },
      { id: 'prescribeForm', labelMr: 'डिजिटल प्रिस्क्रिप्शन (Rx)', labelEn: 'Prescription Engine', icon: 'pill', badge: 'दूध सुरक्षा' },
      { id: 'outbreak-gis', labelMr: 'साथरोग नियंत्रण नकाशा', labelEn: 'Epidemic Map', icon: 'map-pin', badge: '' }
    ]
  },
  collector: {
    userName: "जिल्हाधिकारी कार्यालय",
    roleLabel: "जिल्हा नियंत्रण कक्ष (धुळे)",
    avatar: "DC",
    items: [
      { id: 'villageSignalsGrid', labelMr: 'गाव पातळीवरील सिग्नल', labelEn: 'Village Signal Board', icon: 'activity', badge: '४ गावे' },
      { id: 'officerDecisionQueue', labelMr: 'सकाळची निर्णय रांग', labelEn: 'Decision Queue', icon: 'shield', badge: '३ प्रलंबित' },
      { id: 'gisSvgMap', labelMr: 'साथरोग अंदाज व ५ किमी रिंग', labelEn: 'SEIR GIS Map', icon: 'map-pin', badge: '५ किमी' },
      { id: 'mvuDispatchCard', labelMr: '१९६२ फिरते पथक (MVU)', labelEn: 'MVU Live Dispatch', icon: 'truck', badge: 'लाइव्ह' }
    ]
  },
  officer: {
    userName: "जिल्हाधिकारी कार्यालय",
    roleLabel: "जिल्हा नियंत्रण कक्ष (धुळे)",
    avatar: "DC",
    items: [
      { id: 'villageSignalsGrid', labelMr: 'गाव पातळीवरील सिग्नल', labelEn: 'Village Signal Board', icon: 'activity', badge: '४ गावे' },
      { id: 'officerDecisionQueue', labelMr: 'सकाळची निर्णय रांग', labelEn: 'Decision Queue', icon: 'shield', badge: '३ प्रलंबित' },
      { id: 'gisSvgMap', labelMr: 'साथरोग अंदाज व ५ किमी रिंग', labelEn: 'SEIR GIS Map', icon: 'map-pin', badge: '५ किमी' },
      { id: 'mvuDispatchCard', labelMr: '१९६२ फिरते पथक (MVU)', labelEn: 'MVU Live Dispatch', icon: 'truck', badge: 'लाइव्ह' }
    ]
  },
  rddl: {
    userName: "राज्य रोग निदान प्रयोगशाळा",
    roleLabel: "विभागीय प्रयोगशाळा (पुणे)",
    avatar: "RD",
    items: [
      { id: 'sampleCardsContainer', labelMr: 'सक्रिय नमुना ट्रॅकिंग', labelEn: 'Sample Pipeline', icon: 'flask', badge: '१ सक्रिय' },
      { id: 'rddlPcrAction', labelMr: 'RT-PCR चाचणी विश्लेषण', labelEn: 'RT-PCR Thermocycler', icon: 'cpu', badge: '४० सायकल' },
      { id: 'nadresPayloadBox', labelMr: 'ICAR-NIVEDI NADRES V2', labelEn: 'NADRES Export', icon: 'download', badge: 'DPDP' }
    ]
  },
  admin: {
    userName: "राज्य रोग निदान प्रयोगशाळा",
    roleLabel: "विभागीय प्रयोगशाळा (पुणे)",
    avatar: "RD",
    items: [
      { id: 'sampleCardsContainer', labelMr: 'सक्रिय नमुना ट्रॅकिंग', labelEn: 'Sample Pipeline', icon: 'flask', badge: '१ सक्रिय' },
      { id: 'rddlPcrAction', labelMr: 'RT-PCR चाचणी विश्लेषण', labelEn: 'RT-PCR Thermocycler', icon: 'cpu', badge: '४० सायकल' },
      { id: 'nadresPayloadBox', labelMr: 'ICAR-NIVEDI NADRES V2', labelEn: 'NADRES Export', icon: 'download', badge: 'DPDP' }
    ]
  }
};

function renderSidebarNav(role) {
  const sidebar = document.getElementById("sidebarNavList");
  const userEl = document.getElementById("sidebarUserName");
  const roleEl = document.getElementById("sidebarRoleLabel");
  const avatarEl = document.getElementById("sidebarAvatar");

  const spec = ROLE_NAV_SPECS[role] || ROLE_NAV_SPECS.farmer;
  const isMr = (typeof currentLang === 'undefined' || currentLang === 'mr');

  if (userEl) userEl.textContent = spec.userName;
  if (roleEl) roleEl.textContent = spec.roleLabel;
  if (avatarEl) avatarEl.textContent = spec.avatar;

  if (sidebar) {
    sidebar.innerHTML = spec.items.map((item, idx) => `
      <div class="sidebar-nav-item ${idx === 0 ? 'active' : ''}" data-target="${item.id}" onclick="navigateToAppSection('${item.id}', '${role}', this)">
        <div style="display:flex; align-items:center; gap:10px;">
          <span data-icon="${item.icon}" data-size="16"></span>
          <span>${isMr ? item.labelMr : item.labelEn}</span>
        </div>
        ${item.badge ? `<span class="sidebar-nav-badge">${item.badge}</span>` : ''}
      </div>
    `).join("");
  }

  // Update topbar segmented control buttons
  const segmentedMap = {
    farmer: 'btnPersonaFarmer',
    paravet: 'btnPersonaParavet',
    ldo: 'btnPersonaLdo',
    vet: 'btnPersonaLdo',
    collector: 'btnPersonaCollector',
    officer: 'btnPersonaCollector',
    rddl: 'btnPersonaRddl',
    admin: 'btnPersonaRddl'
  };
  document.querySelectorAll('.persona-tab-btn').forEach(b => b.classList.remove('active'));
  const activeBtn = document.getElementById(segmentedMap[role]);
  if (activeBtn) activeBtn.classList.add('active');

  // Also render mobile bottom tabs
  renderBottomTabBar(role);

  if (typeof renderIcons === 'function') renderIcons();
}

function renderBottomTabBar(role) {
  const bottomBar = document.getElementById("appMobileBottomBar");
  if (!bottomBar) return;

  const spec = ROLE_NAV_SPECS[role] || ROLE_NAV_SPECS.farmer;
  const isMr = (typeof currentLang === 'undefined' || currentLang === 'mr');

  bottomBar.innerHTML = spec.items.slice(0, 5).map((item, idx) => `
    <button type="button" class="bottom-tab-item ${idx === 0 ? 'active' : ''}" data-target="${item.id}" onclick="navigateToAppSection('${item.id}', '${role}', this)">
      <span data-icon="${item.icon}" data-size="18"></span>
      <span>${isMr ? item.labelMr.split(' ')[0] : item.labelEn.split(' ')[0]}</span>
    </button>
  `).join("");

  if (typeof renderIcons === 'function') renderIcons();
}

function navigateToAppSection(targetId, role, btnEl) {
  // Update active state in sidebar and bottom bar
  document.querySelectorAll(`.sidebar-nav-item, .bottom-tab-item`).forEach(el => {
    if (el.getAttribute('data-target') === targetId) {
      el.classList.add('active');
    } else {
      el.classList.remove('active');
    }
  });

  // Action dispatches
  if (targetId === 'rddlPcrAction') {
    openRddlPcrModal("SMP-2026-041");
    return;
  }

  if (targetId.startsWith('viewFarmer')) {
    switchNotebookTab(targetId);
    return;
  }

  if (targetId === 'vetAppointmentsContainer') {
    switchVetTab('apts');
    const el = document.getElementById('vetAppointmentsContainer');
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return;
  }

  if (targetId === 'vetCasesContainer') {
    switchVetTab('cases');
    const el = document.getElementById('vetCasesContainer');
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    return;
  }

  // Smooth scroll to container within main content
  const el = document.getElementById(targetId);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    el.style.transition = 'box-shadow 0.3s ease';
    el.style.boxShadow = '0 0 0 3px var(--accent-turmeric)';
    setTimeout(() => { el.style.boxShadow = ''; }, 1200);
  }
}
'''

# Update activatePersona in js/app.js to call renderSidebarNav
old_activate_persona_snippet = r'renderRoleSubnav\(role\);'
new_activate_persona_snippet = '''renderRoleSubnav(role);
  renderSidebarNav(role);'''

if 'function renderSidebarNav' not in js:
    js = js.replace('renderRoleSubnav(role);', new_activate_persona_snippet)
    js += '\n\n' + navigation_engine_code
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✓ Added renderSidebarNav and bottom bar navigation to js/app.js")
else:
    print("Sidebar navigation engine already in js/app.js")

print("All V2 App Shell enhancements applied successfully!")

