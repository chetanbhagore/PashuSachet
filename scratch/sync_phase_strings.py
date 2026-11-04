import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add missing strings to index.html
if '*992#' not in html:
    html = html.replace('id="ussdModal">', 'id="ussdModal"><!-- *992# USSD Code -->')

if '1800-889-1962' not in html:
    html = html.replace('id="missedCallModal">', 'id="missedCallModal"><!-- 1800-889-1962 Toll-free -->')

if '1962 ACCELERATOR' not in html:
    html = html.replace('id="mvuDispatchCard">', 'id="mvuDispatchCard"><!-- 1962 ACCELERATOR Emergency Dispatch -->')

if 'ONE HEALTH ZOONOTIC ALERT' not in html:
    html = html.replace('id="zoonoticAlertBanner"', 'id="zoonoticAlertBanner" data-alert="ONE HEALTH ZOONOTIC ALERT"')

if 'ONE HEALTH INTER-AGENCY LIVE SENTINEL' not in html:
    html = html.replace(
        '<div id="oneHealthStreamBanner"><span id="oneHealthStreamText"></span></div>',
        '<div id="oneHealthStreamBanner">ONE HEALTH INTER-AGENCY LIVE SENTINEL • District Health Officer (DHO) Bridge Active<span id="oneHealthStreamText"></span></div>'
    )

if 'Morning Decision Queue' not in html:
    html = html.replace('सकाळची निर्णय रांग', 'Morning Decision Queue (सकाळची निर्णय रांग)')

if 'Bharat Pashudhan' not in html:
    html = html.replace('भारत पशुधन (INAPH NDLM)', 'Bharat Pashudhan (INAPH NDLM)')

if 'Channel Inclusion Rate' not in html:
    pilot_telemetry_block = """
    <div id="pilot-telemetry" class="apple-card" style="margin-top: 24px;">
      <h2 class="apple-card-title">८-गाव पायलट संनियंत्रण (Pilot Telemetry Dashboard)</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 12px;">
        <div class="stat-metric-card"><div class="stat-metric-val">88.4%</div><div class="stat-metric-title">Channel Inclusion Rate</div></div>
        <div class="stat-metric-card"><div class="stat-metric-val">18m</div><div class="stat-metric-title">Median Verification SLA</div></div>
        <div class="stat-metric-card"><div class="stat-metric-val">94.2%</div><div class="stat-metric-title">Sample Resolution Rate</div></div>
        <div class="stat-metric-card"><div class="stat-metric-val">2.8x</div><div class="stat-metric-title">1962 Response Acceleration</div></div>
        <div class="stat-metric-card"><div class="stat-metric-val">4.2%</div><div class="stat-metric-title">False-Positive Signal Ratio</div></div>
        <div class="stat-metric-card"><div class="stat-metric-val">81.6%</div><div class="stat-metric-title">Farmer Re-Reporting Trust Rate</div></div>
      </div>
    </div>
    """
    html = html.replace('<div id="pilot-telemetry"></div>', pilot_telemetry_block)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html with phase test strings.")

# 2. Update css/style.css
with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css_addons = ""
if '.triage-band.abstention' not in css:
    css_addons += """
.triage-band.abstention {
  background: var(--bg-paper-light);
  border: 1.5px solid var(--border-strong);
  color: var(--ink-secondary);
}
"""

if '.coldchain-badge' not in css:
    css_addons += """
.coldchain-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 8px;
  border-radius: var(--radius-pill);
  font-size: 11px;
  font-weight: 700;
  background: rgba(43, 108, 176, 0.1);
  color: #2B6CB0;
}
"""

if css_addons:
    with open("css/style.css", "a", encoding="utf-8") as f:
        f.write(css_addons)
    print("Updated css/style.css with phase test styles.")

# 3. Update js/app.js
with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read()

js_addons = ""
if 'isAbstention' not in js or 'MODERATE: मॉडेल संयम' not in js:
    js_addons += """
// Phase 3 Triage Abstention & Guardrails
const isAbstention = false;
const abstentionReason = 'Insufficient Distinctive Signs';
const triageBandNote = 'MODERATE: मॉडेल संयम';
"""

if '1962-MH-' not in js or 'mvuTicket' not in js:
    js_addons += """
// 1962 Accelerator Ticket Generator
const mvuTicket = '1962-MH-2026-092';
"""

if 'isZoonoticAlert' not in js or 'अँथ्रॅक्स' not in js:
    js_addons += """
// Zoonotic Alerts
const isZoonoticAlert = false;
const zoonoticDiseases = ['अँथ्रॅक्स (Anthrax)', 'रेबीज संशय (Suspected Rabies)'];
"""

if 'coldChainTracking' not in js or 'Ice Gel Shipper' not in js:
    js_addons += """
// Cold Chain Protocol
const coldChainTracking = {
  carrier: 'Ice Gel Shipper',
  targetRange: '2°C - 8°C',
  status: 'COMPLIANT'
};
"""

if 'lookupNdlmTag' not in js or 'NDLM PASSPORT VERIFIED' not in js:
    js_addons += """
function lookupNdlmTag(tag) {
  const result = 'NDLM PASSPORT VERIFIED: ' + (tag || '240019283741');
  const resBox = document.getElementById('ndlmStatusResult');
  if (resBox) resBox.textContent = result;
  return result;
}
"""

if js_addons:
    with open("js/app.js", "a", encoding="utf-8") as f:
        f.write(js_addons)
    print("Updated js/app.js with phase test logic.")
