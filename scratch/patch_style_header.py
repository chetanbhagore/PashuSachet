import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .persona-switcher-bar and .site-header blocks with unified single header styling
old_block = '''/* ==========================================================================
   4. MULTI-ROLE PERSONA SWITCHER BAR (Apple Segmented Capsule)
   ========================================================================== */
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

/* ==========================================================================
   5. FLOATING LIQUID GLASS HEADER & NAVIGATION
   ========================================================================== */
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
}'''

new_block = '''/* ==========================================================================
   4. UNIFIED SINGLE APPLE NAVIGATION HEADER (Zero Overlap, Crystal Clarity)
   ========================================================================== */
.site-header {
  background: rgba(255, 255, 255, 0.86);
  backdrop-filter: var(--glass-blur-lg);
  -webkit-backdrop-filter: var(--glass-blur-lg);
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
  position: sticky;
  top: 0;
  z-index: 1000;
  height: 64px;
  display: flex;
  align-items: center;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
  transition: background-color 0.3s ease;
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 16px;
}

.header-left {
  display: flex;
  align-items: center;
  flex-shrink: 0;
}

.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}

.brand-logo {
  width: 38px;
  height: 38px;
  background: linear-gradient(145deg, #16a34a, #15803d);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 19px;
  box-shadow: 0 2px 8px rgba(22, 163, 74, 0.28);
}

.brand-text h1 {
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.024em;
  color: #14532d;
  line-height: 1.1;
}

.brand-badge {
  font-size: 0.68rem;
  color: var(--apple-text-tertiary);
  font-weight: 600;
  letter-spacing: 0.01em;
  display: block;
}

/* Center Apple Segmented Persona Control */
.header-center {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
}

.persona-segmented-control {
  display: flex;
  align-items: center;
  background: rgba(0, 0, 0, 0.05);
  border-radius: var(--radius-pill);
  padding: 3px;
  gap: 3px;
  border: 1px solid rgba(0, 0, 0, 0.04);
}

.persona-pill {
  border: none;
  background: transparent;
  color: var(--apple-text-secondary);
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  padding: 6px 13px;
  border-radius: var(--radius-pill);
  cursor: pointer;
  transition: all 0.2s var(--spring-default);
  white-space: nowrap;
}

.persona-pill:hover {
  color: var(--apple-text-primary);
  background: rgba(255, 255, 255, 0.45);
}

.persona-pill.active {
  background: #ffffff;
  color: var(--apple-green);
  font-weight: 700;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04);
}

/* Header Right */
.header-right {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

.helpline-badge-compact {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: linear-gradient(180deg, #ef4444 0%, #dc2626 100%);
  color: #ffffff;
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.01em;
  text-decoration: none;
  box-shadow: 0 2px 6px rgba(220, 38, 38, 0.28);
  transition: transform 0.2s ease;
}

.helpline-badge-compact:hover {
  transform: translateY(-0.5px);
  box-shadow: 0 3px 8px rgba(220, 38, 38, 0.38);
}

/* Scroll Offset Anchor Fix (Never hide text under top bar) */
section, .module-section, #hero, #symptom-screening, #outbreak-gis, #village-signal-board,
#paravet-inbox, #sample-tracker, #health-passport, #vet-directory, #vet-desk, #admin-console {
  scroll-margin-top: 80px;
}'''

if old_block in css:
    css = css.replace(old_block, new_block, 1)
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✓ Successfully replaced header CSS with unified Apple header in style.css!")
else:
    print("⚠️ Old block not found; appending new block and updating .site-header")
    css = css.replace('.site-header {\n  background: var(--glass-nav);\n  backdrop-filter: var(--glass-blur-lg);\n  -webkit-backdrop-filter: var(--glass-blur-lg);\n  border-bottom: 1px solid var(--glass-nav-border);\n  position: sticky;\n  top: 45px;', '.site-header {\n  background: rgba(255, 255, 255, 0.86);\n  backdrop-filter: var(--glass-blur-lg);\n  -webkit-backdrop-filter: var(--glass-blur-lg);\n  border-bottom: 1px solid rgba(0, 0, 0, 0.08);\n  position: sticky;\n  top: 0;')
    css += "\n\n" + new_block
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✓ Updated style.css with unified single header styling!")

