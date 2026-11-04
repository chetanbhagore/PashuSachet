# -*- coding: utf-8 -*-
css_additions = r"""

/* ==========================================================================
   SUPERCHARGED EXTENSIONS: PERSONAS, VISION HUD, SEIR, MVU & WHATSAPP
   ========================================================================== */

/* 1. Multi-Role Persona Switcher Bar */
.persona-switcher-bar {
  background: #0f172a;
  border-bottom: 2px solid #334155;
  padding: 8px 0;
  position: sticky;
  top: 0;
  z-index: 99;
}
.persona-grid {
  display: flex;
  align-items: center;
  gap: 8px;
  overflow-x: auto;
  white-space: nowrap;
  padding: 2px 4px;
}
.persona-label {
  font-size: 0.76rem;
  color: #94a3b8;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-right: 4px;
}
.persona-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #1e293b;
  color: #cbd5e1;
  border: 1px solid #475569;
  border-radius: 20px;
  padding: 5px 12px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  user-select: none;
}
.persona-pill:hover {
  background: #334155;
  color: #ffffff;
  border-color: #64748b;
}
.persona-pill.active {
  background: #15803d;
  color: #ffffff;
  border-color: #86efac;
  box-shadow: 0 0 10px rgba(34,197,94,0.3);
}

/* 2. Computer Vision Sentinel Supercharge */
.vision-preset-grid {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 12px;
}
.vision-chip-btn {
  background: #1e293b;
  color: #f1f5f9;
  border: 1px solid #334155;
  border-radius: 6px;
  padding: 6px 10px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: all 0.15s ease;
}
.vision-chip-btn:hover {
  background: #334155;
  border-color: #38bdf8;
  color: #38bdf8;
}
.vision-chip-btn.active {
  background: #0284c7;
  color: #ffffff;
  border-color: #7dd3fc;
}
.vision-tool-pill {
  background: #f8fafc;
  color: #334155;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 5px 10px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}
.vision-tool-pill:hover {
  background: #e2e8f0;
}
.vision-tool-pill.active {
  background: #7c3aed;
  color: #ffffff;
  border-color: #c4b5fd;
}
.vision-tool-pill.thermal-active {
  background: #ea580c;
  color: #ffffff;
  border-color: #fdba74;
}

/* 3. SEIR Epidemiological Simulation HUD */
.seir-hud-panel {
  background: #090d16;
  border: 1px solid #1e293b;
  border-radius: 8px;
  padding: 14px 18px;
  margin-top: 14px;
}
.seir-metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
  margin-top: 10px;
}
.seir-metric-card {
  background: #131b2e;
  border: 1px solid #1e293b;
  border-radius: 6px;
  padding: 10px;
  text-align: center;
}
.seir-metric-val {
  font-size: 1.25rem;
  font-weight: 800;
  font-family: monospace;
}
.seir-metric-lbl {
  font-size: 0.72rem;
  color: #94a3b8;
  font-weight: 700;
  text-transform: uppercase;
  margin-top: 2px;
}

/* 4. 1962 MVU GPS Telematics Panel */
.mvu-telematics-panel {
  background: #0f172a;
  border: 1.5px solid #1e293b;
  border-radius: 10px;
  padding: 16px;
  color: #e2e8f0;
  margin-top: 16px;
}
.mvu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  border-bottom: 1px solid #1e293b;
  padding-bottom: 10px;
  margin-bottom: 12px;
}
.mvu-badge {
  background: #1e3a8a;
  color: #bfdbfe;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 800;
  font-family: monospace;
}
.coldchain-meter {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #064e3b;
  color: #6ee7b7;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 800;
}

/* 5. Floating WhatsApp Simulator Widget */
.whatsapp-floating-btn {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #25d366;
  color: #ffffff;
  border: none;
  border-radius: 50px;
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 800;
  font-size: 0.92rem;
  box-shadow: 0 4px 20px rgba(37,211,102,0.45);
  cursor: pointer;
  z-index: 1000;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.whatsapp-floating-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(37,211,102,0.6);
}
.whatsapp-drawer {
  position: fixed;
  bottom: 84px;
  right: 24px;
  width: 380px;
  max-width: 90vw;
  height: 520px;
  background: #efeae2;
  border-radius: 14px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.25);
  display: none;
  flex-direction: column;
  overflow: hidden;
  z-index: 1001;
  border: 1px solid #cbd5e1;
}
.whatsapp-drawer.active {
  display: flex;
}
.whatsapp-chat-header {
  background: #075e54;
  color: #ffffff;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.whatsapp-body {
  flex: 1;
  padding: 14px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.whatsapp-msg {
  max-width: 82%;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 0.85rem;
  line-height: 1.4;
  position: relative;
  word-break: break-word;
}
.whatsapp-msg.incoming {
  background: #ffffff;
  align-self: flex-start;
  border-top-left-radius: 0;
  color: #111827;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}
.whatsapp-msg.outgoing {
  background: #d9fdd3;
  align-self: flex-end;
  border-top-right-radius: 0;
  color: #111827;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}
.whatsapp-time {
  font-size: 0.68rem;
  color: #64748b;
  text-align: right;
  margin-top: 3px;
}
.whatsapp-footer {
  background: #f0f2f5;
  padding: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
  border-top: 1px solid #e2e8f0;
}
.whatsapp-input {
  flex: 1;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 20px;
  padding: 8px 14px;
  font-size: 0.85rem;
  outline: none;
}
.whatsapp-send-btn {
  background: #075e54;
  color: #ffffff;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1rem;
}

/* 6. Printable Digital Pashu Health Certificate */
@media print {
  body * {
    visibility: hidden;
  }
  #printableHealthCertificate, #printableHealthCertificate * {
    visibility: visible;
  }
  #printableHealthCertificate {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    margin: 0;
    padding: 20px;
    background: #ffffff !important;
    color: #000000 !important;
  }
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)

print("css/style.css successfully updated with supercharged styling.")
