comp_css = """
/* ==========================================================================
   AI VISION SENTINEL & THERMAL/GRAD-CAM STYLES
   ========================================================================== */
.vision-canvas-container {
  position: relative;
  width: 100%;
  max-width: 480px;
  height: 280px;
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: #000;
  border: 1px solid var(--border-subtle);
  margin-bottom: 16px;
}

#visionCanvas {
  width: 100%;
  height: 100%;
  display: block;
}

.vision-hud-overlay {
  position: absolute;
  top: 10px;
  left: 10px;
  right: 10px;
  display: flex;
  justify-content: space-between;
  pointer-events: none;
}

.hud-badge {
  padding: 4px 8px;
  border-radius: var(--radius-xs);
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(8px);
  color: #fff;
  font-family: var(--font-mono);
  font-size: 11px;
}

.vision-tools-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.vision-tool-btn {
  padding: 8px 14px;
  border-radius: var(--radius-pill);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-secondary);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all var(--duration-fast) var(--ease-spring);
}

.vision-tool-btn:hover {
  background: var(--bg-paper-light);
  color: var(--ink-primary);
}

.vision-tool-btn.active {
  background: var(--ink-primary);
  color: #fff;
  border-color: var(--ink-primary);
}

.vision-detection-chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.detection-chip {
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-primary);
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}

.detection-chip:hover {
  border-color: var(--border-strong);
}

.detection-chip.active {
  background: var(--accent-turmeric);
  border-color: var(--accent-turmeric);
  color: var(--ink-primary);
}

/* ==========================================================================
   PARA-VET VERIFICATION QUEUE & SIGNAL CARDS
   ========================================================================== */
.stats-glance-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 14px;
  margin-bottom: 24px;
}

.stat-metric-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
  box-shadow: var(--shadow-xs);
}

.stat-metric-val {
  font-size: 28px;
  font-weight: 800;
  font-family: var(--font-display);
  color: var(--ink-primary);
  line-height: 1.1;
  margin-bottom: 4px;
}

.stat-metric-title {
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-secondary);
}

.verification-list-container {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.verification-card {
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

.verification-card:hover {
  border-color: var(--border-strong);
}

.verification-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.verification-farmer-info {
  display: flex;
  flex-direction: column;
}

.verification-farmer-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--ink-primary);
}

.verification-village-tag {
  font-size: 12px;
  color: var(--ink-secondary);
}

.verification-card-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  padding-top: 8px;
  border-top: 1px solid var(--border-subtle);
}

.action-btn-confirm {
  padding: 9px 16px;
  border-radius: var(--radius-pill);
  background: var(--status-success);
  color: #fff;
  border: none;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all var(--duration-fast) var(--ease-spring);
}

.action-btn-confirm:hover {
  background: var(--status-success-hover);
}

.action-btn-sample {
  padding: 9px 16px;
  border-radius: var(--radius-pill);
  background: var(--accent-turmeric);
  color: var(--ink-primary);
  border: none;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all var(--duration-fast) var(--ease-spring);
}

.action-btn-sample:hover {
  background: var(--accent-turmeric-hover);
}

.action-btn-dismiss {
  padding: 9px 16px;
  border-radius: var(--radius-pill);
  background: var(--bg-paper-light);
  color: var(--ink-secondary);
  border: 1px solid var(--border-subtle);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.action-btn-dismiss:hover {
  color: var(--ink-primary);
  border-color: var(--border-strong);
}

/* ==========================================================================
   DOCTOR CARE DESK & PRESCRIPTION
   ========================================================================== */
.segmented-tab-switcher {
  display: flex;
  background: var(--bg-paper-muted);
  padding: 4px;
  border-radius: var(--radius-pill);
  gap: 4px;
  margin-bottom: 20px;
  width: fit-content;
}

.segment-btn {
  padding: 8px 18px;
  border-radius: var(--radius-pill);
  border: none;
  background: transparent;
  color: var(--ink-secondary);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-spring);
}

.segment-btn.active {
  background: var(--bg-surface);
  color: var(--ink-primary);
  box-shadow: var(--shadow-xs);
}

.rx-form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin-bottom: 16px;
}

.form-group-apple {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label-apple {
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-secondary);
}

.withdrawal-countdown-box {
  background: var(--status-warning-light);
  border: 1.5px solid var(--status-warning-border);
  border-radius: var(--radius-md);
  padding: 16px;
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.withdrawal-hours-val {
  font-size: 24px;
  font-weight: 800;
  font-family: var(--font-mono);
  color: var(--status-warning);
}

/* ==========================================================================
   COLLECTOR SIGNAL BOARD & SEIR EPIDEMIOLOGY
   ========================================================================== */
.decision-card-item {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.decision-info-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--ink-primary);
}

.decision-info-desc {
  font-size: 13px;
  color: var(--ink-secondary);
}

.mvu-siren-card {
  background: linear-gradient(135deg, #FFFFFF 0%, #FFF7F5 100%);
  border: 1.5px solid var(--urgency-critical-border);
  border-radius: var(--radius-lg);
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.seir-slider-wrap {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 20px;
  margin-bottom: 20px;
}

.seir-slider-bar {
  width: 100%;
  accent-color: var(--accent-turmeric);
  cursor: pointer;
  height: 6px;
  margin: 12px 0;
}

/* ==========================================================================
   RDDL SAMPLE PIPELINE
   ========================================================================== */
.pipeline-stepper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px;
  background: var(--bg-paper-light);
  border-radius: var(--radius-pill);
  margin-bottom: 16px;
}

.pipeline-step-node {
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-tertiary);
  display: flex;
  align-items: center;
  gap: 6px;
}

.pipeline-step-node.active {
  color: var(--accent-turmeric);
}

.pipeline-step-node.done {
  color: var(--status-success);
}
"""

with open("css/style.css", "a", encoding="utf-8") as f:
    f.write(comp_css)

print("Appended component styles to css/style.css.")
