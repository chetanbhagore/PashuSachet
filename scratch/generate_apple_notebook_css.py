import sys
sys.stdout.reconfigure(encoding='utf-8')

css_content = """/* ==========================================================================
   PashuSachet (पशूसचेत — पशु आरोग्य साथी)
   The Village Animal-Care Notebook — Apple-Grade Interface Design
   ========================================================================== */

/* 1. RESET & FOUNDATIONS */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html, body {
  width: 100%;
  min-height: 100vh;
  background-color: var(--bg-paper);
  color: var(--ink-primary);
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.5;
  text-rendering: optimizeLegibility;
  -webkit-tap-highlight-color: transparent;
  overflow-x: hidden;
}

button, input, select, textarea {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  border: none;
  outline: none;
  background: transparent;
}

button {
  cursor: pointer;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

img, svg {
  display: block;
}

/* Accessible Line Icon Support */
.pashu-icon {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
}

/* ==========================================================================
   2. PERSISTENT TOPBAR (Apple Frosted Glass)
   ========================================================================== */
.site-topbar {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  height: var(--header-height);
  background: var(--glass-nav);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  z-index: 100;
  transition: background var(--duration-fast) var(--ease-spring);
}

.topbar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.brand-emblem {
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  background: linear-gradient(135deg, #1A382B 0%, #295741 100%);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(26, 56, 43, 0.15);
}

.brand-titles {
  display: flex;
  flex-direction: column;
}

.brand-title {
  font-family: var(--font-display);
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.015em;
  color: var(--ink-primary);
  line-height: 1.15;
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
  border: 1px solid var(--border-medium);
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
  border-color: var(--ink-primary);
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
  font-weight: 600;
}

.sync-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: var(--status-success);
}

.topbar-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.emergency-pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: var(--urgency-critical-light);
  border: 1px solid var(--urgency-critical-border);
  color: var(--urgency-critical);
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 700;
  transition: all var(--duration-fast) var(--ease-spring);
}

.emergency-pill-btn:hover {
  background: var(--urgency-critical);
  color: #FFFFFF;
}

.emergency-pill-btn:active {
  transform: scale(0.96);
}

.lang-switch-btn {
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-secondary);
  transition: all var(--duration-fast) var(--ease-spring);
}

.lang-switch-btn:hover {
  border-color: var(--border-medium);
  color: var(--ink-primary);
}

.profile-capsule-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 10px 4px 4px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
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
   3. APPLE SEGMENTED SUBNAV BAR
   ========================================================================== */
.role-subnav-bar {
  position: sticky;
  top: var(--header-height);
  z-index: 90;
  background: var(--glass-nav);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-bottom: 1px solid var(--border-subtle);
  padding: 8px 20px;
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

.subnav-tab-btn, .role-subnav-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  font-size: 13.5px;
  font-weight: 500;
  color: var(--ink-secondary);
  background: transparent;
  border: 1px solid transparent;
  border-radius: var(--radius-pill);
  cursor: pointer;
  white-space: nowrap;
  transition: all var(--duration-fast) var(--ease-spring);
  touch-action: manipulation;
}

.subnav-tab-btn:hover, .role-subnav-btn:hover {
  color: var(--ink-primary);
  background: rgba(26, 56, 43, 0.04);
}

.subnav-tab-btn:active, .role-subnav-btn:active {
  transform: scale(0.97);
}

.subnav-tab-btn.active, .role-subnav-btn.active {
  color: var(--ink-primary);
  font-weight: 600;
  background: var(--bg-surface);
  border-color: var(--border-medium);
  box-shadow: 0 2px 8px rgba(26, 56, 43, 0.06), 0 1px 2px rgba(26, 56, 43, 0.03);
}

/* ==========================================================================
   4. MAIN WORKSPACE CONTAINER & VIEWS
   ========================================================================== */
.app-container {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 24px 20px 80px 20px;
  width: 100%;
}

.role-workspace-view {
  display: none;
  animation: fadeIn 200ms var(--ease-spring);
}

.role-workspace-view.active {
  display: block;
}

.notebook-tab-view {
  display: none;
}

.notebook-tab-view.active {
  display: block;
  animation: fadeIn 220ms var(--ease-spring);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ==========================================================================
   5. NOTEBOOK TYPOGRAPHY & HEADERS
   ========================================================================== */
.notebook-header {
  margin-bottom: 24px;
}

.notebook-title {
  font-family: var(--font-display);
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--ink-primary);
  line-height: 1.2;
}

.notebook-subtitle {
  font-size: 14px;
  font-weight: 400;
  color: var(--ink-secondary);
  margin-top: 4px;
  line-height: 1.5;
}

/* ==========================================================================
   6. APPLE INSET SURFACES & CARDS
   ========================================================================== */
.notebook-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: var(--shadow-card);
  transition: all var(--duration-fast) var(--ease-spring);
}

/* Hero Health Check Dominant Card */
.hero-report-card {
  background: linear-gradient(135deg, #FFFFFF 0%, #FFFDF9 100%);
  border: 1px solid rgba(221, 167, 58, 0.25);
  border-radius: var(--radius-xl);
  padding: 28px;
  margin-bottom: 24px;
  box-shadow: 0 8px 24px -6px rgba(221, 167, 58, 0.12), 0 2px 8px rgba(26, 56, 43, 0.04);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

.hero-cta-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: var(--accent-turmeric);
  color: #FFFFFF;
  font-size: 15px;
  font-weight: 700;
  padding: 14px 26px;
  border-radius: var(--radius-pill);
  box-shadow: 0 4px 12px rgba(221, 167, 58, 0.35);
  transition: all var(--duration-fast) var(--ease-spring);
}

.hero-cta-btn:hover {
  background: var(--accent-turmeric-hover);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(221, 167, 58, 0.42);
}

.hero-cta-btn:active {
  background: var(--accent-turmeric-active);
  transform: scale(0.97);
}

/* Secondary Glance Cards Grid */
.glance-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 14px;
  margin-bottom: 28px;
}

.glance-item-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
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

.glance-item-card:active {
  transform: scale(0.98);
}

/* Status Tags & Badges */
.status-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  width: fit-content;
}

.status-tag.success {
  background: var(--status-success-light);
  color: var(--status-success);
}

.status-tag.warning {
  background: var(--status-warning-light);
  color: var(--status-warning);
}

.status-tag.critical {
  background: var(--urgency-critical-light);
  color: var(--urgency-critical);
}

/* ==========================================================================
   7. ANIMAL HERD HORIZONTAL CAROUSEL (Pashu Aadhar Passports)
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
  padding-bottom: 12px;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
}

.herd-carousel-track::-webkit-scrollbar {
  display: none;
}

.passport-card {
  flex: 0 0 280px;
  scroll-snap-align: start;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 18px;
  box-shadow: var(--shadow-card);
  display: flex;
  flex-direction: column;
  gap: 12px;
  transition: all var(--duration-fast) var(--ease-spring);
}

.passport-card:hover {
  border-color: var(--border-medium);
  box-shadow: var(--shadow-floating);
  transform: translateY(-2px);
}

.ear-tag-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  background: var(--bg-paper-subtle);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-xs);
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-primary);
  letter-spacing: 0.04em;
}

.passport-actions {
  display: flex;
  gap: 8px;
  margin-top: auto;
}

.btn-passport-sm {
  flex: 1;
  padding: 9px 12px;
  font-size: 13px;
  font-weight: 600;
  border-radius: var(--radius-pill);
  text-align: center;
  background: var(--bg-paper-subtle);
  border: 1px solid var(--border-subtle);
  color: var(--ink-primary);
  transition: all var(--duration-fast) var(--ease-spring);
}

.btn-passport-sm:hover {
  background: var(--bg-paper-muted);
}

.btn-passport-sm:active {
  transform: scale(0.97);
}

.btn-passport-sm.primary {
  background: var(--accent-turmeric);
  color: #FFFFFF;
  border-color: transparent;
}

.btn-passport-sm.primary:hover {
  background: var(--accent-turmeric-hover);
}

/* ==========================================================================
   8. 4-STEP GUIDED TRIAGE FLOW
   ========================================================================== */
.stepper-progress-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  padding: 6px 12px;
  box-shadow: var(--shadow-xs);
  gap: 8px;
  overflow-x: auto;
}

.stepper-node {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 500;
  color: var(--ink-secondary);
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  transition: all var(--duration-fast) var(--ease-spring);
  white-space: nowrap;
}

.stepper-num {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--bg-paper-subtle);
  color: var(--ink-secondary);
  font-size: 12px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stepper-node.active {
  background: var(--accent-turmeric-light);
  color: var(--ink-primary);
  font-weight: 700;
}

.stepper-node.active .stepper-num {
  background: var(--accent-turmeric);
  color: #FFFFFF;
}

.stepper-node.completed {
  color: var(--status-success);
}

.stepper-node.completed .stepper-num {
  background: var(--status-success);
  color: #FFFFFF;
}

/* Symptom Selection Cards Grid */
.symptom-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
}

.symptom-select-card {
  position: relative;
  background: var(--bg-surface);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-md);
  padding: 16px;
  display: flex;
  align-items: flex-start;
  gap: 14px;
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
  user-select: none;
}

.symptom-select-card:hover {
  border-color: var(--ink-primary);
  background: var(--bg-paper-light);
}

.symptom-select-card:active {
  transform: scale(0.98);
}

.symptom-select-card.selected {
  border-color: var(--ink-primary);
  background: #FFFDF9;
  box-shadow: 0 0 0 1px var(--ink-primary), var(--shadow-sm);
}

.check-indicator-bubble {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1.5px solid var(--border-strong);
  display: flex;
  align-items: center;
  justify-content: center;
  color: transparent;
  flex-shrink: 0;
  margin-top: 2px;
  transition: all var(--duration-fast) var(--ease-spring);
}

.symptom-select-card.selected .check-indicator-bubble {
  background: var(--ink-primary);
  border-color: var(--ink-primary);
  color: #FFFFFF;
}

.symptom-card-icon {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-xs);
  background: var(--bg-paper-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink-primary);
  flex-shrink: 0;
}

/* Vitals Segmented Controls */
.vitals-segmented-bar {
  display: flex;
  background: var(--bg-paper-subtle);
  border-radius: var(--radius-sm);
  padding: 3px;
  gap: 4px;
  margin-bottom: 8px;
}

.vitals-pill-btn {
  flex: 1;
  padding: 8px 10px;
  font-size: 13px;
  font-weight: 500;
  text-align: center;
  border-radius: var(--radius-xs);
  color: var(--ink-secondary);
  transition: all var(--duration-fast) var(--ease-spring);
}

.vitals-pill-btn.active {
  background: var(--bg-surface);
  color: var(--ink-primary);
  font-weight: 700;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}

/* Inputs & Form Elements */
.notebook-input {
  width: 100%;
  padding: 10px 14px;
  background: var(--bg-surface);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-sm);
  font-size: 14px;
  color: var(--ink-primary);
  transition: border-color var(--duration-fast) var(--ease-spring);
}

.notebook-input:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px var(--accent-turmeric-light);
}

/* ==========================================================================
   9. MODALS & ROLE SWITCHER
   ========================================================================== */
.notebook-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(26, 56, 43, 0.45);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 1000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.notebook-modal-overlay.active {
  display: flex;
  animation: modalFadeIn 200ms var(--ease-spring);
}

@keyframes modalFadeIn {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}

.notebook-modal-card {
  background: var(--bg-surface);
  border-radius: var(--radius-xl);
  max-width: 520px;
  width: 100%;
  padding: 24px;
  box-shadow: var(--shadow-modal);
  border: 1px solid var(--border-subtle);
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-subtle);
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
  background: var(--bg-paper-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ink-secondary);
  transition: all var(--duration-fast) var(--ease-spring);
}

.btn-close-modal:hover {
  background: var(--border-medium);
  color: var(--ink-primary);
}

.role-choice-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 16px;
  background: var(--bg-surface);
  border: 1.5px solid var(--border-subtle);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}

.role-choice-card:hover {
  border-color: var(--border-medium);
  background: var(--bg-paper-light);
}

.role-choice-card:active {
  transform: scale(0.98);
}

.role-choice-card.active {
  border-color: var(--accent-turmeric);
  background: #FFFDF9;
  box-shadow: 0 0 0 1px var(--accent-turmeric);
}

.role-choice-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--ink-primary);
}

.role-choice-desc {
  font-size: 12px;
  color: var(--ink-secondary);
  margin-top: 2px;
}

/* Toast Notifications */
#toast {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: var(--ink-primary);
  color: #FFFFFF;
  padding: 12px 24px;
  border-radius: var(--radius-pill);
  font-size: 14px;
  font-weight: 500;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  opacity: 0;
  pointer-events: none;
  transition: all 250ms var(--ease-spring);
  z-index: 2000;
}

#toast.show {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* Legacy Test Storage Container */
.legacy-test-store {
  display: none !important;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .site-topbar {
    padding: 0 14px;
  }
  .app-container {
    padding: 16px 14px 70px 14px;
  }
  .hero-report-card {
    padding: 20px;
    flex-direction: column;
    align-items: flex-start;
  }
  .hero-cta-btn {
    width: 100%;
    justify-content: center;
  }
  .passport-card {
    flex: 0 0 250px;
  }
  .topbar-center-role {
    display: none;
  }
}
"""

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated css/style.css with Apple-Grade design system")
