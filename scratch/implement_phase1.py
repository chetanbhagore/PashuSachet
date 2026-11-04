# -*- coding: utf-8 -*-
import sys

print("Executing Phase 1: Multi-Role Authentication, 5 Roles, and RBAC...")

# 1. UPDATE INDEX.HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Para-Vet tab button
old_auth_tabs = '''        <div class="auth-tabs">
          <button class="auth-tab-btn active" id="tabFarmerBtn" onclick="switchAuthTab('farmer')">
            Farmer / Keeper
          </button>
          <button class="auth-tab-btn" id="tabVetBtn" onclick="switchAuthTab('vet')">
            Veterinarian
          </button>
          <button class="auth-tab-btn" id="tabOfficerBtn" onclick="switchAuthTab('officer')">
            District Officer
          </button>
          <button class="auth-tab-btn" id="tabAdminBtn" onclick="switchAuthTab('admin')">
            Administrator
          </button>
        </div>'''

new_auth_tabs = '''        <div class="auth-tabs">
          <button class="auth-tab-btn active" id="tabFarmerBtn" onclick="switchAuthTab('farmer')">
            👨‍🌾 Farmer
          </button>
          <button class="auth-tab-btn" id="tabParaVetBtn" onclick="switchAuthTab('paravet')">
            🧑‍⚕️ Para-Vet
          </button>
          <button class="auth-tab-btn" id="tabVetBtn" onclick="switchAuthTab('vet')">
            🩺 Veterinarian
          </button>
          <button class="auth-tab-btn" id="tabOfficerBtn" onclick="switchAuthTab('officer')">
            🏛️ District Officer
          </button>
          <button class="auth-tab-btn" id="tabAdminBtn" onclick="switchAuthTab('admin')">
            🛡️ Admin
          </button>
        </div>'''

if old_auth_tabs in html:
    html = html.replace(old_auth_tabs, new_auth_tabs)
    print("Updated auth tabs to 5 roles.")

# Add Para-Vet Login Pane
paravet_pane = '''
        <!-- 1B. PARA-VET / VILLAGE SENTINEL LOGIN PANE -->
        <div class="auth-pane" id="authPaneParavet">
          <p style="font-size: 0.85rem; color: #475569; margin-bottom: 14px;">
            Frontline verification access for registered Para-Vets, Pashu Sakhi, and Village Dairy Sentinels.
          </p>
          <form id="paravetLoginForm">
            <div class="form-group" style="margin-bottom: 12px;">
              <label for="paravetIdInput">Para-Vet Registration ID / Mobile *</label>
              <input type="text" id="paravetIdInput" class="form-control" value="PV-AHM-9104" required>
            </div>
            <div class="form-group" style="margin-bottom: 14px;">
              <label for="paravetVillageSelect">Assigned Village Cluster *</label>
              <select id="paravetVillageSelect" class="form-control">
                <option value="sangamner_rural">Sangamner Cluster (Villages 1-4)</option>
                <option value="rahuri_cluster">Rahuri North Beat</option>
                <option value="baramati_east">Baramati Rural East</option>
              </select>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%; background: #0284c7;">
              Open Field Verification Inbox
            </button>
          </form>

          <div class="demo-account-box" style="border-color: #0284c7; background: #f0f9ff;">
            <div>
              <strong style="font-size: 0.82rem; color: #0369a1;">Verified Village Sentinel</strong>
              <div style="font-size: 0.78rem; color: #475569;">Ganesh Kale • Para-Vet &amp; Pashu Sakhi (Sangamner Beat)</div>
            </div>
            <button class="demo-account-btn" style="background: #0284c7;" onclick="quickLogin('paravet')">
              One-Click Login
            </button>
          </div>
        </div>
'''

farmer_pane_marker = '        <!-- 1. FARMER LOGIN PANE -->'
if farmer_pane_marker in html:
    # insert after the farmer pane closing div
    pane_end_marker = '        </div>\n\n        <!-- 2. VETERINARIAN LOGIN PANE -->'
    if pane_end_marker in html:
        html = html.replace(pane_end_marker, '        </div>\n' + paravet_pane + '\n        <!-- 2. VETERINARIAN LOGIN PANE -->')
        print("Injected Para-Vet login pane.")

# Add Para-Vet Navigation Link in Header
if '<li id="adminNavLink" style="display: none;"><a href="#admin-console">Admin Console</a></li>' in html:
    html = html.replace(
        '<li id="adminNavLink" style="display: none;"><a href="#admin-console">Admin Console</a></li>',
        '<li id="paravetNavLink" style="display: none;"><a href="#paravet-inbox">Para-Vet Inbox</a></li>\n        <li id="adminNavLink" style="display: none;"><a href="#admin-console">Admin Console</a></li>'
    )
    print("Added Para-Vet Nav Link.")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved updated index.html!")

# 2. UPDATE JS/APP.JS
with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Add paravet to AUTH_PROFILES
old_profiles = '''  farmer: {
    role: "farmer",
    name: "Ganesh Patil",
    title: "Livestock Keeper",
    location: "Sangamner, Ahmednagar",
    identifier: "+91 98220 12345",
    avatar: "👨‍🌾"
  },'''

new_profiles = '''  farmer: {
    role: "farmer",
    name: "Ganesh Patil",
    title: "Livestock Keeper",
    location: "Sangamner, Ahmednagar",
    identifier: "+91 98220 12345",
    avatar: "👨‍🌾"
  },
  paravet: {
    role: "paravet",
    name: "Ganesh Kale",
    title: "Village Sentinel & Para-Vet",
    location: "Sangamner Cluster (Villages 1-4)",
    identifier: "PV-AHM-9104",
    avatar: "🧑‍⚕️"
  },'''

if old_profiles in js:
    js = js.replace(old_profiles, new_profiles)
    print("Added paravet to AUTH_PROFILES in js/app.js.")

# Update switchAuthTab to include paravet
old_switch_tab = 'const tabs = ["farmer", "vet", "officer", "admin"];'
new_switch_tab = 'const tabs = ["farmer", "paravet", "vet", "officer", "admin"];'
if old_switch_tab in js:
    js = js.replace(old_switch_tab, new_switch_tab)
    print("Updated switchAuthTab with paravet.")

# Update updateAuthUI for paravet
old_auth_ui = '''    // Show/Hide Role-Gated Sections
    if (user.role === "admin") {
      if (adminNav) adminNav.style.display = "inline-block";
      if (adminSection) {
        adminSection.style.display = "block";
        renderAdminAuditLogs();
      }
    } else {
      if (adminNav) adminNav.style.display = "none";
      if (adminSection) adminSection.style.display = "none";
    }'''

new_auth_ui = '''    // Show/Hide Role-Gated Sections
    const paravetNav = document.getElementById("paravetNavLink");
    const paravetSection = document.getElementById("paravet-inbox");
    if (user.role === "paravet") {
      if (paravetNav) paravetNav.style.display = "inline-block";
      if (paravetSection) paravetSection.style.display = "block";
    } else {
      if (paravetNav) paravetNav.style.display = "none";
    }

    if (user.role === "admin") {
      if (adminNav) adminNav.style.display = "inline-block";
      if (adminSection) {
        adminSection.style.display = "block";
        renderAdminAuditLogs();
      }
    } else {
      if (adminNav) adminNav.style.display = "none";
      if (adminSection) adminSection.style.display = "none";
    }'''

if old_auth_ui in js:
    js = js.replace(old_auth_ui, new_auth_ui)
    print("Updated updateAuthUI for paravet role.")

# Add listener for paravet form
paravet_listener = '''  document.getElementById("paravetLoginForm")?.addEventListener("submit", (e) => {
    e.preventDefault();
    quickLogin("paravet");
  });'''

if 'document.getElementById("farmerLoginForm")?.addEventListener("submit"' in js:
    js = js.replace(
        'document.getElementById("farmerLoginForm")?.addEventListener("submit", (e) => {\n    e.preventDefault();\n    quickLogin("farmer");\n  });',
        'document.getElementById("farmerLoginForm")?.addEventListener("submit", (e) => {\n    e.preventDefault();\n    quickLogin("farmer");\n  });\n' + paravet_listener
    )
    print("Added paravetLoginForm event listener.")

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Saved updated js/app.js!")

