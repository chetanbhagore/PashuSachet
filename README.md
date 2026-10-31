# 🐄 PashuSachet (पशूसचेत / Seva First)
> **A Multilingual, AI-Assisted Livestock-Health and Veterinary-Service Platform for Rural Maharashtra**

[![Vercel Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://pashu-sachet.vercel.app)
[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen?style=for-the-badge&logo=github)](https://chetanbhagore.github.io/PashuSachet/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Status: Prototype](https://img.shields.io/badge/Prototype-Operational-orange?style=for-the-badge)]()
[![Government Aligned](https://img.shields.io/badge/Aligned-ICAR--NIVEDI%20%2F%20DAHD-emerald?style=for-the-badge)]()

---

## 🌟 Overview & Product Promise
**PashuSachet** (developed under the *Seva First* initiative) bridges rural livestock owners, veterinarians, and district livestock development officers across Maharashtra.

It provides:
- **Species-aware preliminary symptom screening** with triage uncertainty metrics and instant veterinary referrals.
- **District-level disease outbreak risk intelligence** based on ICAR-NIVEDI / NADRES historical patterns and seasonal climate data.
- **Digital Pashu Aadhar & Health Passports** providing persistent vaccination records, deworming calendars, and clinical timelines.
- **Multilingual rural accessibility** in **Marathi (मराठी)**, **Hindi (हिन्दी)**, and **English**.

---

## 🏛️ The Six Strategic Pillars

| Pillar | Delivery Mechanism | Primary Beneficiary |
| :--- | :--- | :--- |
| **🔍 Detect** | Species-aware symptom screening with calibrated decision trees and referral | Farmer / Vet |
| **📡 Predict** | Disease-specific geographic outbreak risk from historical & environmental data | Farmer / Livestock Officer |
| **📊 Monitor** | Animal-specific anomaly detection from vital sign observations and milk yield | Farmer / Vet |
| **🤝 Connect** | Digital animal records, verified vet directory, and doorstep appointment booking | All Stakeholders |
| **🗣️ Inform** | Multilingual guidance and plain-language vernacular explanations | Rural Livestock Keepers |
| **🛡️ Govern** | Farmer data sovereignty, One Health alignment, and strict clinical boundaries | All Users |

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

