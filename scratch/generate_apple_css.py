# scratch/generate_apple_css.py
import sys

sys.stdout.reconfigure(encoding='utf-8')

css_content = """/* ==========================================================================
   PASHUSACHET (पशूसचेत) — APPLE DESIGN SYSTEM & FLUID USER EXPERIENCE
   Rooted in Apple's Human Interface Guidelines & "Designing Fluid Interfaces"
   Materials: Translucent Liquid Glass, Optical Typography, Critically Damped Springs, Squircle Geometry
   ========================================================================== */

@import url('tokens.css');

/* --------------------------------------------------------------------------
   1. GLOBAL RESET & FOUNDATIONAL TYPOGRAPHY (SF Optical Scale)
   -------------------------------------------------------------------------- */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  text-rendering: optimizeLegibility;
}

body {
  font-family: var(--font-sans);
  background-color: var(--apple-canvas);
  color: var(--apple-text-primary);
  line-height: 1.55;
  letter-spacing: -0.006em;
  overflow-x: hidden;
  min-height: 100vh;
}

/* Apple Display & Section Headings */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  color: var(--apple-text-primary);
  font-weight: 700;
  letter-spacing: -0.022em;
}

h1 {
  font-size: clamp(2rem, 3.8vw, 3rem);
  line-height: 1.08;
  letter-spacing: -0.032em;
}

h2 {
  font-size: clamp(1.5rem, 2.6vw, 2.1rem);
  line-height: 1.18;
  letter-spacing: -0.024em;
}

h3 {
  font-size: 1.28rem;
  line-height: 1.25;
  letter-spacing: -0.018em;
}

h4 {
  font-size: 1.05rem;
  line-height: 1.35;
  letter-spacing: -0.012em;
}

p {
  color: var(--apple-text-secondary);
  line-height: 1.6;
}

a {
  color: var(--apple-blue);
  text-decoration: none;
  transition: color 0.18s var(--spring-default);
}
a:hover {
  color: var(--apple-blue-hover);
}

/* --------------------------------------------------------------------------
   2. RESPONSE — KILL LATENCY & TACTILE SPRINGS (Active Physicality)
   -------------------------------------------------------------------------- */
button, .btn, .persona-pill, .species-card, .chip-box, .vision-chip-btn,
.vision-tool-pill, .quick-card, .whatsapp-floating-btn, .lang-btn, .role-pill {
  touch-action: manipulation;
  user-select: none;
  cursor: pointer;
}

button:active, .btn:active, .persona-pill:active, .species-card:active,
.chip-box:active, .vision-chip-btn:active, .vision-tool-pill:active,
.quick-card:active, .whatsapp-floating-btn:active {
  transform: scale(0.97) !important;
  transition: transform 100ms var(--spring-press) !important;
}

/* Container */
.container {
  width: 100%;
  max-width: 1220px;
  margin: 0 auto;
  padding: 0 24px;
}

/* --------------------------------------------------------------------------
   3. GOVERNMENT OVERSIGHT BANNER (Obsidian Glass)
   -------------------------------------------------------------------------- */
.gov-banner {
  background: var(--glass-dark);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  color: #f1f5f9;
  font-size: 0.82rem;
  padding: 8px 0;
  border-bottom: 1px solid var(--glass-dark-border);
  position: relative;
  z-index: 102;
}
.gov-banner .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
.gov-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
  letter-spacing: -0.005em;
  color: #cbd5e1;
}
.helpline-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: linear-gradient(180deg, #ef4444 0%, #dc2626 100%);
  color: #ffffff;
  padding: 3px 12px;
  border-radius: var(--radius-pill);
  font-weight: 700;
  font-size: 0.78rem;
  letter-spacing: 0.02em;
  box-shadow: 0 2px 6px rgba(220, 38, 38, 0.35);
  transition: all 0.2s var(--spring-default);
}
.helpline-badge:hover {
  background: linear-gradient(180deg, #dc2626 0%, #b91c1c 100%);
  transform: translateY(-0.5px);
  box-shadow: 0 4px 10px rgba(220, 38, 38, 0.45);
}

/* --------------------------------------------------------------------------
   4. MULTI-ROLE PERSONA SWITCHER BAR (Apple Segmented Capsule)
   -------------------------------------------------------------------------- */
.persona-switcher-bar {
  background: rgba(255, 255, 255, 0.78);
  backdrop-filter: var(--glass-blur-lg);
  -webkit-backdrop-filter: var(--glass-blur-lg);
  border-bottom: 1px solid rgba(0, 0, 0, 0.07);
  padding: 8px 0;
  position: sticky;
  top: 0;
  z-index: 101;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}
.persona-grid {
  display: flex;
  align-items: center;
  gap: 6px;
  overflow-x: auto;
  white-space: nowrap;
  padding: 2px 0;
  scrollbar-width: none;
}
.persona-grid::-webkit-scrollbar {
  display: none;
}
.persona-label {
  font-size: 0.72rem;
  color: var(--apple-text-tertiary);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-right: 6px;
}
.persona-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0, 0, 0, 0.04);
  color: var(--apple-text-secondary);
  border: 1px solid transparent;
  border-radius: var(--radius-pill);
  padding: 6px 14px;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  transition: all 0.22s var(--spring-default);
}
.persona-pill:hover {
  background: rgba(0, 0, 0, 0.07);
  color: var(--apple-text-primary);
}
.persona-pill.active {
  background: #ffffff;
  color: var(--apple-green);
  border-color: rgba(22, 163, 74, 0.22);
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.04);
  font-weight: 700;
  transform: translateY(-0.5px);
}

/* --------------------------------------------------------------------------
   5. FLOATING LIQUID GLASS HEADER & NAVIGATION
   -------------------------------------------------------------------------- */
.site-header {
  background: var(--glass-nav);
  backdrop-filter: var(--glass-blur-lg);
  -webkit-backdrop-filter: var(--glass-blur-lg);
  border-bottom: 1px solid var(--glass-nav-border);
  position: sticky;
  top: 45px;
  z-index: 100;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.02);
  transition: background-color 0.3s ease;
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 68px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--apple-text-primary);
}
.brand-logo {
  width: 42px;
  height: 42px;
  background: linear-gradient(145deg, #16a34a 0%, #15803d 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 20px;
  box-shadow: 0 3px 10px rgba(22, 163, 74, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.3);
  transition: transform 0.25s var(--spring-default);
}
.brand:hover .brand-logo {
  transform: scale(1.04);
}
.brand-text h1 {
  font-size: 1.22rem;
  font-weight: 700;
  letter-spacing: -0.025em;
  color: #14532d;
  line-height: 1.15;
}
.brand-text span {
  font-size: 0.72rem;
  color: var(--apple-text-tertiary);
  font-weight: 600;
  letter-spacing: 0.01em;
  display: block;
}

/* Nav links */
.nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
  list-style: none;
}
.nav-links a {
  text-decoration: none;
  color: var(--apple-text-secondary);
  font-weight: 500;
  font-size: 0.88rem;
  letter-spacing: -0.01em;
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  transition: all 0.2s var(--spring-default);
}
.nav-links a:hover {
  color: var(--apple-text-primary);
  background: rgba(0, 0, 0, 0.04);
}
.nav-links a.active {
  color: var(--apple-green);
  background: var(--apple-green-light);
  font-weight: 600;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

/* Role switch pills */
.role-switch {
  display: flex;
  background: rgba(0, 0, 0, 0.05);
  border-radius: var(--radius-pill);
  padding: 3px;
  border: 1px solid rgba(0, 0, 0, 0.04);
}
.role-pill {
  border: none;
  background: transparent;
  padding: 4px 12px;
  font-size: 0.8rem;
  font-weight: 600;
  border-radius: var(--radius-pill);
  color: var(--apple-text-secondary);
  transition: all 0.2s var(--spring-default);
}
.role-pill.active {
  background: #ffffff;
  color: var(--apple-green);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
}

/* Language selector */
.lang-selector {
  display: flex;
  background: rgba(0, 0, 0, 0.05);
  border-radius: var(--radius-pill);
  padding: 3px;
  border: 1px solid rgba(0, 0, 0, 0.04);
}
.lang-btn {
  border: none;
  background: transparent;
  padding: 4px 10px;
  font-size: 0.8rem;
  font-weight: 600;
  border-radius: var(--radius-pill);
  color: var(--apple-text-secondary);
  transition: all 0.2s var(--spring-default);
}
.lang-btn.active {
  background: #ffffff;
  color: var(--apple-text-primary);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
}

/* User Profile Badge */
.user-profile-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: var(--radius-pill);
  padding: 4px 12px 4px 8px;
  box-shadow: var(--shadow-xs);
}
.user-avatar {
  font-size: 1.15rem;
  display: flex;
  align-items: center;
}
.user-name-role {
  display: flex;
  flex-direction: column;
}
.user-name {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--apple-text-primary);
  line-height: 1.2;
}
.user-role-label {
  font-size: 0.68rem;
  color: var(--apple-text-secondary);
  line-height: 1.2;
}
.logout-btn {
  background: transparent;
  border: none;
  font-size: 0.74rem;
  font-weight: 600;
  color: var(--apple-red);
  cursor: pointer;
  margin-left: 4px;
  padding: 2px 6px;
  border-radius: 4px;
  transition: background-color 0.15s ease;
}
.logout-btn:hover {
  background: var(--apple-red-light);
}

/* --------------------------------------------------------------------------
   6. APPLE BUTTON SYSTEM (.btn, .btn-primary, .btn-outline, .btn-lg, .btn-sm)
   -------------------------------------------------------------------------- */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 18px;
  font-size: 0.92rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  text-decoration: none;
  transition: transform 0.25s var(--spring-default), box-shadow 0.25s var(--spring-default), background-color 0.2s ease, border-color 0.2s ease;
  white-space: nowrap;
}

.btn-primary {
  background: linear-gradient(180deg, #16a34a 0%, #15803d 100%);
  color: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05), inset 0 1px 0 rgba(255, 255, 255, 0.2);
}
.btn-primary:hover {
  background: linear-gradient(180deg, #15803d 0%, #166534 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(22, 163, 74, 0.32), inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.btn-outline {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  border-color: rgba(0, 0, 0, 0.12);
  color: var(--apple-text-primary);
  box-shadow: var(--shadow-xs);
}
.btn-outline:hover {
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.2);
  transform: translateY(-1px);
  box-shadow: var(--shadow-sm);
}

.btn-accent {
  background: linear-gradient(180deg, #f59e0b 0%, #d97706 100%);
  color: #ffffff;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05), inset 0 1px 0 rgba(255, 255, 255, 0.25);
}
.btn-accent:hover {
  background: linear-gradient(180deg, #d97706 0%, #b45309 100%);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35);
}

.btn-sm {
  padding: 6px 14px;
  font-size: 0.82rem;
  border-radius: 8px;
}

.btn-lg {
  padding: 14px 28px;
  font-size: 1.02rem;
  border-radius: var(--radius-md);
  font-weight: 700;
}

/* --------------------------------------------------------------------------
   7. HERO SECTION & LIVE TELEMETRY DISPLAY
   -------------------------------------------------------------------------- */
.hero-section {
  background: radial-gradient(ellipse 80% 50% at 50% -10%, rgba(22, 163, 74, 0.09) 0%, rgba(251, 251, 253, 0) 100%), var(--apple-canvas);
  padding: 56px 0 48px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  position: relative;
  overflow: hidden;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 48px;
  align-items: center;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--apple-green-light);
  color: var(--apple-green);
  border: 1px solid var(--apple-green-border);
  padding: 6px 16px;
  border-radius: var(--radius-pill);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.01em;
  margin-bottom: 20px;
}
.hero-title {
  font-size: clamp(2.3rem, 4vw, 3.25rem);
  line-height: 1.08;
  font-weight: 800;
  color: var(--apple-text-primary);
  margin-bottom: 18px;
  letter-spacing: -0.035em;
}
.hero-title span {
  color: var(--apple-green);
  display: inline-block;
}
.hero-subtitle {
  font-size: 1.12rem;
  color: var(--apple-text-secondary);
  line-height: 1.6;
  letter-spacing: -0.01em;
  margin-bottom: 28px;
}
.hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 28px;
}

/* Hero Live Ticker Card */
.hero-card {
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: var(--glass-blur-lg);
  -webkit-backdrop-filter: var(--glass-blur-lg);
  border: 1px solid rgba(255, 255, 255, 0.85);
  border-radius: var(--radius-xl);
  padding: 28px;
  box-shadow: var(--shadow-card);
  position: relative;
}
.hero-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  padding-bottom: 16px;
  margin-bottom: 18px;
}
.live-indicator {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.78rem;
  color: var(--apple-green);
  font-weight: 700;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}
.pulse-dot {
  width: 8px;
  height: 8px;
  background: #22c55e;
  border-radius: 50%;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
  70% { transform: scale(1.05); box-shadow: 0 0 0 6px rgba(34, 197, 94, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
}

.stat-ticker-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
  margin-bottom: 18px;
}
.stat-box {
  background: var(--apple-canvas-subtle);
  padding: 16px 14px;
  border-radius: var(--radius-md);
  border: 1px solid rgba(0, 0, 0, 0.04);
  transition: transform 0.25s var(--spring-default);
}
.stat-box:hover {
  transform: translateY(-1px);
}
.stat-val {
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--apple-green);
  line-height: 1;
  letter-spacing: -0.02em;
  margin-bottom: 6px;
}
.stat-label {
  font-size: 0.78rem;
  color: var(--apple-text-secondary);
  font-weight: 600;
  letter-spacing: -0.005em;
}

.alert-quick-box {
  background: var(--apple-red-light);
  border: 1px solid var(--apple-red-border);
  border-radius: var(--radius-md);
  padding: 14px 16px;
  font-size: 0.84rem;
  color: #991b1b;
  display: flex;
  align-items: center;
  gap: 12px;
  line-height: 1.45;
}

/* --------------------------------------------------------------------------
   8. QUICK ACTION STRIP (Ultra-Inclusive Alternate Channels)
   -------------------------------------------------------------------------- */
.quick-strip {
  background: var(--apple-canvas-subtle);
  padding: 22px 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}
.strip-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.strip-item {
  display: flex;
  align-items: center;
  gap: 14px;
  background: #ffffff;
  padding: 16px 18px;
  border-radius: var(--radius-lg);
  border: 1px solid rgba(0, 0, 0, 0.06);
  box-shadow: var(--shadow-sm);
  text-decoration: none;
  color: var(--apple-text-primary);
  transition: transform 0.25s var(--spring-default), box-shadow 0.25s var(--spring-default);
}
.strip-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-card);
}
.strip-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--apple-canvas-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  flex-shrink: 0;
}
.strip-text strong {
  display: block;
  font-size: 0.92rem;
  color: var(--apple-text-primary);
  letter-spacing: -0.01em;
  margin-bottom: 2px;
}
.strip-text span {
  font-size: 0.78rem;
  color: var(--apple-text-secondary);
}

/* --------------------------------------------------------------------------
   9. CORE MODULE SECTION & CARDS
   -------------------------------------------------------------------------- */
.module-section {
  padding: 56px 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}
.section-header {
  text-align: center;
  max-width: 760px;
  margin: 0 auto 36px;
}
.section-tag {
  display: inline-block;
  background: var(--apple-green-light);
  color: var(--apple-green);
  border: 1px solid var(--apple-green-border);
  padding: 4px 14px;
  border-radius: var(--radius-pill);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.section-title {
  font-size: clamp(1.8rem, 3vw, 2.3rem);
  letter-spacing: -0.028em;
  margin-bottom: 12px;
}
.section-subtitle {
  font-size: 1.02rem;
  color: var(--apple-text-secondary);
  line-height: 1.6;
}

/* --------------------------------------------------------------------------
   10. 90-SECOND INTAKE FORM (Species, Symptoms, AI Vision & Results)
   -------------------------------------------------------------------------- */
.screening-card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-card);
  padding: 36px 32px;
  margin-bottom: 28px;
}
.form-step-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--apple-text-primary);
  margin-bottom: 16px;
  letter-spacing: -0.015em;
}
.step-num {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--apple-green);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85rem;
  font-weight: 700;
}

/* Species Option Cards (9 Species Grid) */
.species-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(105px, 1fr));
  gap: 10px;
  margin-bottom: 24px;
}
.species-option {
  position: relative;
  cursor: pointer;
}
.species-option input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
.species-card {
  background: var(--apple-canvas-subtle);
  border: 1.5px solid transparent;
  border-radius: var(--radius-md);
  padding: 14px 10px;
  text-align: center;
  transition: transform 0.25s var(--spring-default), box-shadow 0.25s var(--spring-default), border-color 0.2s ease, background-color 0.2s ease;
}
.species-card:hover {
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.1);
  transform: translateY(-1.5px);
  box-shadow: var(--shadow-sm);
}
.species-option input[type="radio"]:checked + .species-card {
  background: #ffffff;
  border-color: var(--apple-green);
  box-shadow: 0 4px 14px rgba(22, 163, 74, 0.18), 0 0 0 2px rgba(22, 163, 74, 0.25);
  transform: translateY(-1px);
}
.species-card .emoji {
  font-size: 1.8rem;
  display: block;
  margin-bottom: 6px;
}
.species-card .title {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--apple-text-primary);
  display: block;
  line-height: 1.2;
}
.species-card .sub {
  font-size: 0.72rem;
  color: var(--apple-text-secondary);
  display: block;
  margin-top: 2px;
}

/* Symptom Chip Grid */
.symptom-chip-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 10px;
  margin-bottom: 24px;
}
.chip-item {
  position: relative;
  cursor: pointer;
}
.chip-item input[type="checkbox"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}
.chip-box {
  background: var(--apple-canvas-subtle);
  border: 1.5px solid transparent;
  border-radius: var(--radius-sm);
  padding: 12px 14px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--apple-text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.22s var(--spring-default);
}
.chip-box:hover {
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.1);
  transform: translateY(-1px);
}
.chip-item input[type="checkbox"]:checked + .chip-box {
  background: #ffffff;
  border-color: var(--apple-green);
  color: #14532d;
  box-shadow: 0 4px 14px rgba(22, 163, 74, 0.15), 0 0 0 2px rgba(22, 163, 74, 0.22);
}

/* Form Controls & Inputs */
.form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin-bottom: 16px;
}
.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.form-group label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--apple-text-primary);
  letter-spacing: -0.005em;
}
.form-control {
  font-family: var(--font-sans);
  font-size: 0.92rem;
  padding: 12px 14px;
  background: var(--apple-canvas);
  border: 1.5px solid rgba(0, 0, 0, 0.12);
  border-radius: var(--radius-sm);
  color: var(--apple-text-primary);
  transition: all 0.2s var(--spring-default);
}
.form-control:focus {
  background: #ffffff;
  border-color: var(--apple-green);
  box-shadow: 0 0 0 4px rgba(22, 163, 74, 0.15);
  outline: none;
}
textarea.form-control {
  line-height: 1.5;
  resize: vertical;
}

/* --------------------------------------------------------------------------
   11. AI CLINICAL VISION HUD & DETECTION
   -------------------------------------------------------------------------- */
.vision-preset-grid {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 14px;
}
.vision-chip-btn {
  background: #ffffff;
  color: var(--apple-text-primary);
  border: 1px solid rgba(0, 0, 0, 0.12);
  border-radius: var(--radius-pill);
  padding: 7px 14px;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: -0.005em;
  box-shadow: var(--shadow-xs);
  transition: all 0.2s var(--spring-default);
}
.vision-chip-btn:hover {
  background: var(--apple-canvas-subtle);
  border-color: rgba(0, 0, 0, 0.2);
  transform: translateY(-0.5px);
}
.vision-chip-btn.active {
  background: var(--apple-blue);
  color: #ffffff;
  border-color: var(--apple-blue);
  box-shadow: 0 3px 12px rgba(0, 113, 227, 0.35);
}

.vision-tool-pill {
  background: #ffffff;
  color: var(--apple-text-secondary);
  border: 1px solid rgba(0, 0, 0, 0.12);
  border-radius: var(--radius-pill);
  padding: 6px 14px;
  font-size: 0.8rem;
  font-weight: 600;
  box-shadow: var(--shadow-xs);
  transition: all 0.2s var(--spring-default);
}
.vision-tool-pill:hover {
  background: var(--apple-canvas-subtle);
  color: var(--apple-text-primary);
}
.vision-tool-pill.active {
  background: #7c3aed;
  color: #ffffff;
  border-color: #7c3aed;
  box-shadow: 0 3px 12px rgba(124, 58, 237, 0.35);
}
.vision-tool-pill.thermal-active {
  background: #ea580c;
  color: #ffffff;
  border-color: #ea580c;
  box-shadow: 0 3px 12px rgba(234, 88, 12, 0.35);
}

/* --------------------------------------------------------------------------
   12. ASSESSMENT RESULTS & UNCERTAINTY BANDS
   -------------------------------------------------------------------------- */
.assessment-result {
  display: none;
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: var(--radius-xl);
  padding: 28px;
  box-shadow: var(--shadow-card);
  margin-top: 24px;
  animation: slideUp 0.35s var(--spring-default);
}
@keyframes slideUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

.triage-banner {
  padding: 16px 20px;
  border-radius: var(--radius-md);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 20px;
}
.triage-critical {
  background: var(--apple-red-light);
  border: 1.5px solid var(--apple-red-border);
  color: #991b1b;
}
.triage-urgent {
  background: var(--apple-amber-light);
  border: 1.5px solid var(--apple-amber-border);
  color: #92400e;
}
.triage-moderate {
  background: var(--apple-green-light);
  border: 1.5px solid var(--apple-green-border);
  color: #14532d;
}

.prediction-card-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 24px;
}
.diag-card, .action-card {
  background: var(--apple-canvas-subtle);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: var(--radius-lg);
  padding: 20px;
}
.triage-band {
  display: inline-block;
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}
.triage-band.likely {
  background: #dcfce7;
  color: #166534;
}
.triage-band.possible {
  background: #fef3c7;
  color: #92400e;
}
.triage-band.abstention {
  background: #e0f2fe;
  color: #0369a1;
}

/* --------------------------------------------------------------------------
   13. OUTBREAK GIS RADAR, SEIR SIMULATOR & MVU TELEMATICS
   -------------------------------------------------------------------------- */
.radar-grid {
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  gap: 24px;
}
.radar-canvas-card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: var(--radius-xl);
  padding: 24px;
  box-shadow: var(--shadow-card);
}
.seir-hud-panel {
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: var(--radius-lg);
  padding: 20px;
  color: #f8fafc;
  margin-top: 18px;
}
.seir-metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
  gap: 12px;
  margin-top: 14px;
}
.seir-metric-card {
  background: #1e293b;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-md);
  padding: 12px 10px;
  text-align: center;
}
.seir-metric-val {
  font-size: 1.35rem;
  font-weight: 800;
  font-family: var(--font-mono);
  letter-spacing: -0.02em;
}
.seir-metric-lbl {
  font-size: 0.7rem;
  color: #94a3b8;
  font-weight: 700;
  text-transform: uppercase;
  margin-top: 4px;
}

/* SEIR Slider */
input[type="range"] {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 6px;
  background: #334155;
  border-radius: 3px;
  outline: none;
}
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #38bdf8;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
  cursor: pointer;
  transition: transform 0.15s ease;
}
input[type="range"]::-webkit-slider-thumb:hover {
  transform: scale(1.2);
}

/* MVU Telematics */
.mvu-telematics-panel {
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: var(--radius-lg);
  padding: 20px;
  color: #e2e8f0;
  margin-top: 18px;
}

/* --------------------------------------------------------------------------
   14. VILLAGE SIGNAL BOARD & PARA-VET INBOX QUEUES
   -------------------------------------------------------------------------- */
.signals-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 18px;
}
.signal-card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow-card);
  transition: transform 0.25s var(--spring-default), box-shadow 0.25s var(--spring-default);
}
.signal-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}
.signal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}
.status-pill {
  display: inline-block;
  padding: 3px 10px;
  border-radius: var(--radius-pill);
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}
.status-verified {
  background: #dcfce7;
  color: #166534;
}
.status-pending {
  background: #fef3c7;
  color: #92400e;
}
.status-surge {
  background: #fee2e2;
  color: #991b1b;
}

/* --------------------------------------------------------------------------
   15. CLOSED-LOOP SAMPLE TRACKER (RDDL Pune)
   -------------------------------------------------------------------------- */
.sample-pipeline-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 18px;
}
.sample-card {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: var(--radius-lg);
  padding: 22px;
  box-shadow: var(--shadow-card);
}
.stage-tracker-bar {
  display: flex;
  justify-content: space-between;
  position: relative;
  margin: 18px 0;
}
.stage-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  font-size: 0.72rem;
  color: var(--apple-text-tertiary);
  font-weight: 600;
}
.stage-step.active {
  color: var(--apple-green);
  font-weight: 700;
}
.stage-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.stage-step.active .stage-dot {
  background: var(--apple-green);
  box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.25);
}

/* --------------------------------------------------------------------------
   16. DIGITAL PASHU AADHAR & HEALTH PASSPORT (Apple Wallet Style)
   -------------------------------------------------------------------------- */
.pashu-wallet-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
  border: 1.5px solid rgba(0, 0, 0, 0.08);
  border-radius: var(--radius-xl);
  padding: 28px;
  box-shadow: var(--shadow-card);
  position: relative;
  overflow: hidden;
  max-width: 520px;
  margin: 0 auto;
}
.pashu-wallet-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: linear-gradient(90deg, #16a34a, #0284c7, #f59e0b);
}

/* Milk Withholding Countdown Box */
.withdrawal-countdown-box {
  background: #fef2f2;
  border: 1.5px solid #fecaca;
  border-radius: var(--radius-md);
  padding: 12px 16px;
  font-size: 0.88rem;
  color: #991b1b;
  font-weight: 700;
  text-align: center;
  margin-top: 14px;
  font-family: var(--font-mono);
}

/* --------------------------------------------------------------------------
   17. MODALS & SHEETS (Apple Frosted Scrim & Spring Entry)
   -------------------------------------------------------------------------- */
.modal-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.38);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  z-index: 1000;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.modal-overlay.active {
  display: flex;
}
.modal-card {
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: var(--glass-blur-lg);
  -webkit-backdrop-filter: var(--glass-blur-lg);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-modal);
  width: 100%;
  max-width: 560px;
  max-height: 90vh;
  overflow-y: auto;
  padding: 30px;
  position: relative;
  animation: modalSpring 0.32s var(--spring-default);
}
@keyframes modalSpring {
  from { opacity: 0; transform: scale(0.95) translateY(12px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  padding-bottom: 14px;
}
.modal-close {
  background: rgba(0, 0, 0, 0.05);
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: var(--apple-text-secondary);
  cursor: pointer;
  transition: all 0.18s ease;
}
.modal-close:hover {
  background: rgba(0, 0, 0, 0.1);
  color: var(--apple-text-primary);
}

/* --------------------------------------------------------------------------
   18. FLOATING WHATSAPP CHATBOT SIMULATOR
   -------------------------------------------------------------------------- */
.whatsapp-floating-btn {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: linear-gradient(145deg, #25d366 0%, #128c7e 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: var(--radius-pill);
  padding: 12px 22px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  font-size: 0.92rem;
  letter-spacing: -0.01em;
  box-shadow: 0 6px 24px rgba(37, 211, 102, 0.42);
  z-index: 999;
  transition: transform 0.25s var(--spring-default), box-shadow 0.25s var(--spring-default);
}
.whatsapp-floating-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(37, 211, 102, 0.55);
}
.whatsapp-drawer {
  position: fixed;
  bottom: 86px;
  right: 24px;
  width: 380px;
  max-width: 90vw;
  height: 520px;
  background: #efeae2;
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-modal);
  display: none;
  flex-direction: column;
  overflow: hidden;
  z-index: 1001;
  border: 1px solid rgba(0, 0, 0, 0.1);
  animation: modalSpring 0.3s var(--spring-default);
}
.whatsapp-drawer.active {
  display: flex;
}
.whatsapp-chat-header {
  background: #075e54;
  color: #ffffff;
  padding: 14px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* --------------------------------------------------------------------------
   19. ACCESSIBILITY & REDUCED MOTION (Apple Guidelines)
   -------------------------------------------------------------------------- */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
    transform: none !important;
  }
  .modal-card, .assessment-result, .whatsapp-drawer {
    animation: none !important;
    transform: none !important;
  }
}

@media (prefers-reduced-transparency: reduce) {
  .site-header, .persona-switcher-bar, .gov-banner, .modal-card, .hero-card {
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    background: #ffffff !important;
  }
  .gov-banner {
    background: #0f172a !important;
  }
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .hero-grid, .radar-grid, .prediction-card-grid {
    grid-template-columns: 1fr;
  }
  .strip-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .site-header {
    top: 40px;
  }
}
@media (max-width: 600px) {
  .strip-grid {
    grid-template-columns: 1fr;
  }
  .hero-title {
    font-size: 2.1rem;
  }
}
"""

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✓ Successfully generated Apple Design System css/style.css!")

