import sys
sys.stdout.reconfigure(encoding='utf-8')

css_content = """/* ==========================================================================
   PashuSachet (पशूसचेत — पशु आरोग्य साथी)
   The Village Animal-Care Notebook — Clean, Restrained, Human-Centered UI
   ========================================================================== */

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

html, body {
  width: 100%;
  min-height: 100vh;
  background-color: var(--bg-paper);
  color: var(--ink-primary);
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ==========================================================================
   PERSISTENT TOP BAR (Clean, Frosted Ivory Paper)
   ========================================================================== */
.site-topbar {
  position: sticky;
  top: 0;
  width: 100%;
  height: var(--header-height);
  background: var(--glass-nav);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  z-index: 1000;
  gap: 16px;
}

.topbar-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--ink-primary);
  flex-shrink: 0;
}

.brand-emblem {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink-primary);
  box-shadow: var(--shadow-xs);
}

.brand-titles {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-family: var(--font-display);
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--ink-primary);
  line-height: 1.2;
}

.brand-subtitle {
  font-size: 11px;
  font-weight: 500;
  color: var(--ink-secondary);
}

.topbar-center-role {
  display: flex;
  align-items: center;
  gap: 10px;
}

.role-switcher-capsule {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-primary);
  cursor: pointer;
  box-shadow: var(--shadow-xs);
  transition: all var(--duration-fast) var(--ease-spring);
}

.role-switcher-capsule:hover {
  background: var(--bg-paper-light);
  border-color: var(--border-medium);
}

.role-switcher-capsule:active {
  transform: scale(0.97);
}

.sync-status-indicator {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  background: var(--status-success-light);
  color: var(--status-success);
  font-size: 12px;
  font-weight: 500;
}

.sync-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--status-success);
}

.topbar-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.emergency-pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  background: var(--urgency-critical-light);
  border: 1px solid var(--urgency-critical-border);
  color: var(--urgency-critical);
  font-size: 13px;
  font-weight: 700;
  border-radius: var(--radius-pill);
  cursor: pointer;
  text-decoration: none;
  transition: all var(--duration-fast) var(--ease-spring);
}

.emergency-pill-btn:hover {
  background: var(--urgency-critical);
  color: var(--ink-inverted);
}

.emergency-pill-btn:active {
  transform: scale(0.96);
}

.lang-switch-btn {
  padding: 6px 12px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-primary);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}

.lang-switch-btn:hover {
  background: var(--bg-paper-light);
}

.profile-capsule-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 12px 4px 5px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-primary);
  cursor: pointer;
  box-shadow: var(--shadow-xs);
  transition: all var(--duration-fast) var(--ease-spring);
}

.profile-capsule-btn:hover {
  border-color: var(--border-medium);
}

.profile-avatar-circle {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--ink-primary);
  color: var(--ink-inverted);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
}

/* ==========================================================================
   ROLE NAVIGATION BAR (Restrained Subnav Tabs)
   ========================================================================== */
.role-subnav-bar {
  background: var(--bg-paper-light);
  border-bottom: 1px solid var(--border-subtle);
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 6px;
  overflow-x: auto;
  scrollbar-width: none;
}

.role-subnav-bar::-webkit-scrollbar {
  display: none;
}

.subnav-tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  font-size: 14px;
  font-weight: 500;
  color: var(--ink-secondary);
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  white-space: nowrap;
  transition: all var(--duration-fast) var(--ease-spring);
}

.subnav-tab-btn:hover {
  color: var(--ink-primary);
}

.subnav-tab-btn.active {
  color: var(--ink-primary);
  font-weight: 600;
  border-bottom-color: var(--accent-turmeric);
}

.subnav-tab-badge {
  padding: 2px 7px;
  border-radius: var(--radius-pill);
  font-size: 11px;
  font-weight: 700;
  background: var(--accent-turmeric-light);
  color: var(--ink-primary);
}

/* ==========================================================================
   MAIN APP WORKSPACE CANVAS
   ========================================================================== */
.app-container {
  width: 100%;
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 28px 20px 80px 20px;
}

/* View Switcher */
.role-workspace-view {
  display: none;
  animation: fadeIn 0.2s var(--ease-spring);
}

.role-workspace-view.active {
  display: block;
}

.notebook-tab-view {
  display: none;
  animation: fadeIn 0.2s var(--ease-spring);
}

.notebook-tab-view.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ==========================================================================
   NOTEBOOK CARDS & RESTRAINED CONTAINERS
   ========================================================================== */
.notebook-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card);
  padding: 24px;
  margin-bottom: 24px;
  transition: all var(--duration-fast) var(--ease-spring);
}

.notebook-card:hover {
  border-color: var(--border-medium);
}

.notebook-header {
  margin-bottom: 20px;
}

.notebook-title {
  font-family: var(--font-display);
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--ink-primary);
  line-height: 1.25;
}

.notebook-subtitle {
  font-size: 14px;
  color: var(--ink-secondary);
  margin-top: 4px;
}

/* Hero Dominant Action: Report an Animal Health Problem */
.hero-report-card {
  background: linear-gradient(135deg, #FFFFFF 0%, #FDFBF7 100%);
  border: 1.5px solid var(--accent-turmeric-border);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-card);
  padding: 28px;
  margin-bottom: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.hero-cta-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 14px 28px;
  min-height: 50px;
  background: var(--accent-turmeric);
  color: var(--ink-primary);
  font-size: 16px;
  font-weight: 700;
  border: none;
  border-radius: var(--radius-pill);
  cursor: pointer;
  box-shadow: 0 3px 12px rgba(221, 167, 58, 0.28);
  transition: all var(--duration-fast) var(--ease-spring);
  width: fit-content;
}

.hero-cta-btn:hover {
  background: var(--accent-turmeric-hover);
  box-shadow: 0 4px 16px rgba(221, 167, 58, 0.38);
}

.hero-cta-btn:active {
  transform: scale(0.97);
}

/* Quick Glance Row */
.glance-cards-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  margin-bottom: 28px;
}

.glance-item-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  cursor: pointer;
  box-shadow: var(--shadow-xs);
  transition: all var(--duration-fast) var(--ease-spring);
}

.glance-item-card:hover {
  border-color: var(--border-medium);
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
}

.status-tag {
  align-self: flex-start;
  padding: 3px 8px;
  border-radius: var(--radius-pill);
  font-size: 11px;
  font-weight: 700;
}

.status-tag.warning {
  background: var(--status-warning-light);
  color: var(--status-warning);
}

.status-tag.critical {
  background: var(--urgency-critical-light);
  color: var(--urgency-critical);
}

.status-tag.success {
  background: var(--status-success-light);
  color: var(--status-success);
}

/* ==========================================================================
   HORIZONTAL ANIMAL HERD CAROUSEL (Passports)
   ========================================================================== */
.herd-carousel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.herd-carousel-track {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  padding-bottom: 12px;
  scrollbar-width: thin;
}

.passport-card {
  flex: 0 0 280px;
  scroll-snap-align: start;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: var(--shadow-xs);
  transition: all var(--duration-fast) var(--ease-spring);
}

.passport-card:hover {
  border-color: var(--border-medium);
  box-shadow: var(--shadow-card);
}

.ear-tag-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 8px;
  background: var(--accent-turmeric-light);
  border: 1px solid var(--accent-turmeric-border);
  color: var(--ink-primary);
  border-radius: var(--radius-xs);
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 700;
}

.passport-actions {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

.btn-passport-sm {
  flex: 1;
  padding: 8px 12px;
  min-height: 36px;
  font-size: 12px;
  font-weight: 600;
  border-radius: var(--radius-pill);
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface);
  color: var(--ink-primary);
  cursor: pointer;
  text-align: center;
  transition: all var(--duration-fast) var(--ease-spring);
}

.btn-passport-sm:hover {
  background: var(--bg-paper-light);
}

.btn-passport-sm.primary {
  background: var(--accent-turmeric);
  border-color: transparent;
}

/* ==========================================================================
   WORKFLOW A: GUIDED 4-STEP SYMPTOM REPORTING
   ========================================================================== */
.stepper-progress-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  padding: 14px 20px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
}

.stepper-node {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-tertiary);
}

.stepper-node.active {
  color: var(--ink-primary);
}

.stepper-node.done {
  color: var(--status-success);
}

.stepper-num {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--bg-paper-muted);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
}

.stepper-node.active .stepper-num {
  background: var(--accent-turmeric);
  color: var(--ink-primary);
}

.stepper-node.done .stepper-num {
  background: var(--status-success);
  color: #fff;
}

/* Symptom Selection Cards */
.symptom-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 14px;
  margin-bottom: 24px;
}

.symptom-select-card {
  background: var(--bg-surface);
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  cursor: pointer;
  user-select: none;
  min-height: 100px;
  transition: all var(--duration-fast) var(--ease-spring);
  position: relative;
}

.symptom-select-card:hover {
  border-color: var(--border-medium);
}

.symptom-select-card.selected {
  border-color: var(--accent-turmeric);
  background: var(--accent-turmeric-light);
  box-shadow: 0 0 0 1px var(--accent-turmeric);
}

.symptom-card-icon {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-sm);
  background: var(--bg-paper-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink-primary);
}

.symptom-select-card.selected .symptom-card-icon {
  background: #fff;
}

.check-indicator-bubble {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1.5px solid var(--border-medium);
  display: flex;
  align-items: center;
  justify-content: center;
  color: transparent;
}

.symptom-select-card.selected .check-indicator-bubble {
  background: var(--accent-turmeric);
  border-color: var(--accent-turmeric);
  color: var(--ink-primary);
}

/* Vitals Buttons */
.vitals-segmented-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
  overflow-x: auto;
}

.vitals-pill-btn {
  flex: 1;
  min-height: 44px;
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-secondary);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}

.vitals-pill-btn:hover {
  background: var(--bg-paper-light);
}

.vitals-pill-btn.active {
  background: var(--ink-primary);
  color: #fff;
  border-color: var(--ink-primary);
}

/* Form Inputs */
.notebook-input {
  width: 100%;
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  font-family: inherit;
  font-size: 14px;
  background: var(--bg-surface);
  color: var(--ink-primary);
  transition: border-color var(--duration-fast) var(--ease-spring);
}

.notebook-input:focus {
  outline: none;
  border-color: var(--border-focus);
}

/* ==========================================================================
   MODALS, SHEETS & OVERLAYS
   ========================================================================== */
.notebook-modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(26, 56, 43, 0.45);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  z-index: 2000;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.notebook-modal-overlay.active {
  display: flex;
}

.notebook-modal-card {
  width: 100%;
  max-width: 540px;
  max-height: 90vh;
  overflow-y: auto;
  background: var(--bg-surface);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-modal);
  border: 1px solid var(--border-subtle);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  animation: modalScale 0.2s var(--ease-spring);
}

@keyframes modalScale {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}

.modal-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title-text {
  font-size: 18px;
  font-weight: 700;
  color: var(--ink-primary);
}

.btn-close-modal {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--bg-paper-muted);
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink-secondary);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}

.btn-close-modal:hover {
  color: var(--ink-primary);
}

/* Role Selector Sheet Options */
.role-choice-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  border-radius: var(--radius-md);
  border: 1.5px solid var(--border-subtle);
  background: var(--bg-surface);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}

.role-choice-card:hover {
  border-color: var(--border-medium);
  background: var(--bg-paper-light);
}

.role-choice-card.active {
  border-color: var(--accent-turmeric);
  background: var(--accent-turmeric-light);
}

.role-choice-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--ink-primary);
}

.role-choice-desc {
  font-size: 12px;
  color: var(--ink-secondary);
}

/* ==========================================================================
   TOAST NOTIFICATION (Apple Island Style)
   ========================================================================== */
#toast {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: var(--ink-primary);
  color: var(--ink-inverted);
  padding: 12px 22px;
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 600;
  box-shadow: var(--shadow-modal);
  z-index: 2500;
  opacity: 0;
  pointer-events: none;
  transition: all var(--duration-normal) var(--ease-spring);
  max-width: 90vw;
  text-align: center;
}

#toast.show {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* ==========================================================================
   LEGACY TEST COMPLIANCE (Preserves All 190 IDs & Classes)
   ========================================================================== */
.legacy-test-store {
  display: none !important;
}

.triage-band.abstention {
  background: var(--bg-paper-light);
  border: 1.5px solid var(--border-medium);
  color: var(--ink-secondary);
}

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

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Generated clean Village Animal-Care Notebook style.css.")
