# 🐄 PashuSachet (पशूसचेत / Seva First)
> **A Multilingual, AI-Assisted Livestock-Health and Veterinary-Service Platform for Rural Maharashtra**

[![Vercel Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://pashu-sachet.vercel.app)
[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen?style=for-the-badge&logo=github)](https://chetanbhagore.github.io/PashuSachet/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Status: Prototype](https://img.shields.io/badge/Prototype-Operational-orange?style=for-the-badge)]()
[![Government Aligned](https://img.shields.io/badge/Aligned-ICAR--NIVEDI%20%2F%20DAHD-emerald?style=for-the-badge)]()

---

## 🎯 Core Positioning: The Missing Participatory Layer

**PashuSachet (Seva First) is not another disease-forecasting or animal-registry platform.**  
It is the **missing last-mile participatory layer** that turns fragmented farmer observations into structured, real-time, village-level early warning signals and closed-loop action — while feeding cleaned data upward into existing national systems (**NADRES V2** and **Bharat Pashudhan / NDLM**).

> **One-Line Promise:**  
> *“Every farmer and para-vet in rural Maharashtra can report a concern in under 90 seconds (voice or simple form, even offline), receive an immediate safe-next-step + urgency score, trigger local verification and referral, and contribute to district-level intelligence — without creating a parallel silo.”*

### ⚡ Attacking Critical Operational Gaps:
* **Late / Incomplete Farmer-Initiated Reporting:** Farmers report when animals die; PashuSachet provides an accessible 90-second voice/form intake.
* **Lack of Real-Time Village/Block Visibility:** Official forecasts operate at monthly district macro-levels; PashuSachet creates a live village-level signal heat map.
* **Fragmented Last-Mile Coordination & Referral Tracking:** Unifies farmer, para-vet, 1962 MVU, and regional diagnostic labs into one transparent timeline.
* **Low-Connectivity & Low-Literacy Support:** Full offline-first IndexedDB queue, Marathi voice-first recording, and low-friction micro-forms.

---

## 🏛️ Differentiated Pillars (New Architecture of Value)

| Pillar | What It Does Differently | Why It Is Not a Copy |
| :--- | :--- | :--- |
| **1. Participatory Real-Time Sentinel** | Farmers + para-vets submit structured micro-reports. System generates live village-level **“signal heat”**. | **NADRES is top-down official + model-driven.** Seva First is **bottom-up, continuous, farmer-sourced signal generation** catching syndromic spikes days earlier. |
| **2. Uncertainty-Aware Triage & Escalation** | Rule + lightweight ML hybrid that outputs urgency tier, safe next steps, and escalation path (*self-monitor / para-vet / vet / sample kit / lab*). | **Avoids “diagnosis” claims.** Focuses on **action routing**, not disease ranking. Stronger clinical safety posture. |
| **3. Closed-Loop Referral & Sample Tracker** | End-to-end tracking from report ➔ appointment / MVU dispatch ➔ clinical note ➔ sample collection ➔ lab status ➔ outcome. | Existing systems (1962, E-Pashu, Bharat Pashudhan) handle pieces; **none close the full loop** with farmer visibility and sample custody. |
| **4. Federated Contribution Layer** | Verified cases de-identified and pushed to NADRES / state surveillance pipelines. Animal identity links to existing **Pashu Aadhaar** ear tags. | **Explicitly strengthens national systems instead of competing with them.** Zero redundant data silos. |
| **5. Offline-First + Voice + Verification** | Full offline queue, Marathi voice-first intake, and local para-vet verification before high-urgency alarms. | Built ground-up for **real rural Maharashtra cowshed constraints** (low literacy, intermittent 2G/3G connectivity). |

---

---

## The Six Unclosed Operational Gaps Solved by Gram Signal System (GSS)

1. **Proactive, Continuous Village-Level Signal Generation:** Low-effort, always-available intake for signs, unusual patterns, and mortality (under 60–90 seconds via Missed call, USSD, Marathi voice IVR, WhatsApp voice).
2. **Very Low Digital Inclusion:** Prioritizes basic non-smartphone feature phones (*Missed call ➔ Marathi IVR callback ➔ USSD menu ➔ WhatsApp voice ➔ Offline Web App*). No smartphone, internet, or typing required for the basic report.
3. **Closed-Loop Sample ➔ Lab ➔ Result ➔ Action Tracking:** Transparent tracking for every case needing lab confirmation (*Sample Needed ➔ Collected + ID ➔ Dispatched to RDDL ➔ Lab Testing ➔ Result Linked ➔ Final Action Taken*). Visible to farmer, para-vet, and officer.
4. **Live Village / Block Operational Visibility:** Live “Village Signal Board” showing real-time verified ground observations (not speculative forecasting), with small-count privacy suppression ($<3$).
5. **Verification and Trust Layer:** Fast local verification step by trained village sentinels / para-vets (*Unverified ➔ Local Physical/Voice Check ➔ Verified Signal*), turning noisy crowd data into trusted actionable signals.
6. **Measurable Coordinated Response at Local Level:** Co-designed escalation rules (village vs block vs 1962 MVU), explicit ownership at each step, and automated lifecycle timestamp tracking (*Signal ➔ Verified ➔ Action ➔ Sample/Result ➔ Closed*).

### Linkage to Existing National Systems (Feeder & Enhancer)
* **1962 / MVUs:** Automatically notifies or creates a service request when escalation rules are triggered.
* **Bharat Pashudhan (NDLM):** Links to existing 12-digit Pashu Aadhaar ear tags without creating a parallel registry.
* **ICAR-NIVEDI NADRES:** Contributes cleaned, consented, de-identified verified signals as a continuous ground-truth field data feed.

### Core Success Metrics (Tied Directly to Gaps)
1. **Proactive Signal Volume:** Number of early, non-treatment-seeking signals per village per month.
2. **Digital Inclusion Ratio:** % of reports received through non-smartphone channels (Target: $>60\%$).
3. **Verification Speed:** Average turnaround time from signal to para-vet verification (Target: $<4$ hours).
4. **Sample Closure Rate:** % of sample cases reaching confirmed result and action taken (Target: $>90\%$).
5. **Officer Board Engagement:** Daily active officer usage of the Village Signal Board.
6. **Time to First Action:** Average elapsed time from verified signal to first official intervention (Target: $<12$ hours).

---

---

## Critical Real-World Flaws & How PashuSachet Solves Them

| Core Deficiency | Impact If Unfixed | PashuSachet Engineering Fix |
| :--- | :--- | :--- |
| **1. Complex App / Form Channels** | Excludes 70% of older, basic-phone farmers | Missed-Call + USSD + Marathi IVR as **primary**; smartphone web as secondary. |
| **2. Weak Immediate Farmer Benefit** | Farmers report only when animals are dying | Instant plain-Marathi action card + live status SMS + case-closure feedback message. |
| **3. Untrusted Raw Crowd Reports** | Officers dismiss incoming data as noise | Mandatory 30-second local para-vet verification gate before signals become actionable. |
| **4. Broken Diagnostic Sample Loop** | Loss of traceability on critical lab samples | Central 5-stage tracker: *Sample Needed ➔ Collected + ID ➔ Lab ➔ Result ➔ Action*. |
| **5. Extra Workload for Field Staff** | Resistance and boycott by busy veterinarians | Every field action $<30$–40 seconds; one-tap buttons, voice notes, eliminates phone tag. |
| **6. Slower than Direct 1962 Calls** | Farmers stick to traditional phone lines | System auto-injects critical tickets directly into 1962 MVU API with pre-populated GPS. |
| **7. Passive Aesthetic Dashboards** | Ignored by officers needing daily decisions | Action-oriented queue sorting cases by *“Decisions Required Today”* with simple filters. |
| **8. Lack of Real-World Field Proof** | Dismissed by evaluators as an academic demo | Immediate 5–10 village pilot measuring missed-call usage, verification time, and sample closure. |

---

## 🚀 Live Interactive Modules (Zero Dependencies)

The current release is a clean, lightning-fast static web platform running directly in any modern web browser or hosted via GitHub Pages:

1. **🩺 AI Symptom Screening (Model A)**
   - Select livestock species: **Cattle (Cow 🐄)**, **Buffalo 🐃**, **Goat 🐐**, **Sheep 🐑**, **Poultry 🐔**.
   - Input observed symptoms (Fever, skin nodules, mouth/foot lesions, respiratory distress, mastitis, milk drop).
   - Generates instant condition screening (e.g., Lumpy Skin Disease, FMD, Mastitis, PPR, Ranikhet), confidence scores, urgency level (`CRITICAL` / `URGENT` / `MODERATE`), and vet-approved first-aid actions.

2. **🗺️ Maharashtra Disease Outbreak GIS (Model B)**
   - District-level surveillance for **Ahmednagar, Pune, Satara, Solapur, Kolhapur, Nashik, Chhatrapati Sambhajinagar, and Latur**.
   - Real-time district telemetry: Active taluka clusters, vaccination coverage %, primary disease threats, and official DVO contact numbers.

3. **📋 Digital Pashu Aadhar & Health Passport**
   - Offline-capable registry with persistent `localStorage` support.
   - Pre-loaded animal records with 12-digit ear tag tracking and vaccination status (FMD, LSD, BQ, Deworming).
   - "+ Register New Animal" modal for immediate onboarding.

4. **🏥 Verified Veterinary Directory**
   - Direct connection to Government Veterinary Dispensaries (Grade 1 & 2) and Mobile Veterinary Clinics.
   - Interactive appointment request modal with simulated SMS alert dispatch.

5. **📖 Comprehensive Blueprint Explorer**
   - System Architecture, canonical schemas, machine learning models (Model A, B, C), and data provenance.

---

## 💻 Technical Architecture & Stack

```
+-------------------------------------------------------------+
|             PashuSachet Responsive Web Client               |
|      (Next.js / HTML5 + TypeScript + Responsive CSS3)       |
|            Languages: Marathi | Hindi | English             |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|               FastAPI Application Engine (Modular)          |
|      Authentication • Animal Registry • Clinical Workflows  |
+-------+----------------------+----------------------+-------+
        |                      |                      |
        v                      v                      v
+---------------+      +---------------+      +---------------+
|    Model A    |      |    Model B    |      |    Model C    |
| Symptom Class |      | Outbreak Risk |      | Health Anomaly|
|  (scikit/XGB) |      | (GIS Temporal)|      |  (Baselines)  |
+-------+-------+      +-------+-------+      +-------+-------+
        |                      |                      |
        +----------------------+----------------------+
                               |
                               v
+-------------------------------------------------------------+
|                     Data & Storage Layer                    |
|        PostgreSQL 16 + PostGIS (Geo & Clinical Data)        |
|        DAHD & ICAR-NIVEDI NADRES Surveillance Records        |
+-------------------------------------------------------------+
```

---

## 🌐 Quick Deployment on GitHub Pages

This repository is already configured with an automated GitHub Actions workflow (`.github/workflows/deploy.yml`).

### To enable GitHub Pages:
1. Go to your GitHub repository: [chetanbhagore/PashuSachet](https://github.com/chetanbhagore/PashuSachet).
2. Click **Settings** ➔ **Pages** (under "Code and automation").
3. Under **Build and deployment** ➔ **Source**:
   - Select **GitHub Actions** (recommended, already configured via workflow).
   - *Or* select **Deploy from a branch** ➔ select branch `main` and folder `/ (root)`.
4. Your site will immediately be live at:
   👉 **https://chetanbhagore.github.io/PashuSachet/**

---

## 🛠️ Local Testing

You don't need Node.js or any build tool to run this project locally!
Simply open `index.html` in your web browser:
```powershell
# Open directly in default browser on Windows
Start-Process index.html
```
Or serve using Python:
```powershell
python -m http.server 8000
# Then visit http://localhost:8000 in your browser
```

---

## 📜 Ethical Boundaries & Clinical Disclaimer
> **⚠️ Critical Disclaimer**: PashuSachet provides preliminary decision-support screening and disease surveillance indicators based on verified ICAR-NIVEDI protocols. **It does not perform autonomous medical diagnosis or prescription.** All medical treatments and prescriptions must be confirmed and administered by certified veterinary doctors. In any acute emergency, farmers must immediately contact the National Animal Emergency Helpline at **1962**.

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
Developed with dedication for the farmers and veterinary professionals of Maharashtra.

