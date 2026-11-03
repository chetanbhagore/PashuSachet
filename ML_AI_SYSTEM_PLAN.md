# 🧠 PashuSachet (पशूसचेत) — AI & Clinical Decision Support Architecture

> **Document Type:** Production AI/ML & Clinical Decision Support Architecture  
> **Status:** Revised & Scoped for V1 Delivery (Post-Audit)  
> **Target Microservice:** Python FastAPI (`pashusachet-ai-service`)  
> **Interoperability:** Consumed by Spring Boot 3 Core Backend & Offline PWA  
> **Associated Specs:** [`FRONTEND_DESIGN_SPEC.md`](file:///g:/Chetan/pashuSachet/FRONTEND_DESIGN_SPEC.md) | [`BACKEND_ARCHITECTURE_PLAN.md`](file:///g:/Chetan/pashuSachet/BACKEND_ARCHITECTURE_PLAN.md) | [`plans.md`](file:///g:/Chetan/pashuSachet/plans.md)

---

## 1. V1 Scope Realism & Design Principles

To prevent over-engineering, unvalidated claims, and clinical safety risks in V1, the AI architecture enforces five strict engineering rules:

1. **Zero Unvalidated Probabilities:** A rule engine without massive clinical cohorts cannot claim "88% confidence". V1 outputs **qualitative clinical likelihood bands** (`Likely`, `Possible`, `Less Likely`) derived from expert-weighted ICAR-NIVEDI decision matrices.
2. **De-scoped Lesion Image Classifier:** Image classification of lesions is **deferred to V2**. Without a multi-thousand labeled dataset of Indian indigenous livestock in rustic shed lighting, computer vision carries high bias and hallucination risk. V1 focuses 100% on high-reliability tabular symptom triage and vital anomaly tracking.
3. **Primary Evaluation on Clinical Safety:** Rather than generic accuracy, the system is evaluated strictly on **Under-Triage Rate** (target: $< 1\%$ for urgent illnesses; **0% under-triage on red-flag life threats**).
4. **Single Source of Truth (`triage_rules_v1.json`):** Both the offline PWA client and the Python FastAPI microservice evaluate identical, versioned JSON rule matrices. Every case permanently records `rules_version`.
5. **Continuous Ground-Truth Feedback Loop:** Every case pairs the initial triage assessment with the licensed veterinarian's physical examination findings, building an authentic, audited training dataset for future supervised iterations.

---

## 2. Multi-Tier AI System Topology (V1 Scoped)

```mermaid
flowchart TD
    subgraph FarmerClient["Farmer Client & Triage Input"]
        InpSymptoms["Species, Breed, Age, Temp, Symptoms, Duration"]
        InpVitals["Daily Milk Yield & Rumination Logs"]
    end

    subgraph CircuitBreaker["1. Hardcoded Safety Circuit Breaker (Offline First)"]
        RedFlagCheck{"Fatal Red Flags Detected?\n• Severe Bloat / Tympany\n• Continuous Convulsions\n• Sudden Hemorrhage / Collapse"}
    end

    subgraph InferenceEngines["2. AI Decision-Support Services"]
        TriageEngine["MODEL A: Species-Aware Triage Engine\n(FastAPI Microservice + PWA JSON Table)\n• Evaluates: triage_rules_v1.json\n• Outputs: Likelihood Bands & Safe First Aid"]
        
        VitalAnomaly["MODEL C: Herd Vital Anomaly Detector\n(Robust Z-Score / EWMA with Confounder Dampening)\n• Cold Start: 7-14 Days Baseline\n• Detects: >30% Milk Drop / Febrile Spikes"]
        
        SurveillanceCluster["MODEL S: Space-Time Surveillance Cluster Engine\n(ST-DBSCAN + Census Denominator)\n• Window: 7 Days x 15 km Radius\n• Computes: Attack Rate %"]
    end

    subgraph Outputs["3. Actionable Outcomes"]
        EmergencyModal["EMERGENCY OVERRIDE:\nImmediate 1962 Toll-Free Helpline Direct Call"]
        TriageResultCard["Triage Result: Urgency Rating (Critical/Urgent/Mod),\nLikely Condition, Interim First-Aid & Booking CTA"]
        FarmerAlert["Farmer Care Notification:\n'Sudden 32% Milk Drop detected in Gauri'"]
        OfficerGIS["LDO Alert:\nTier 1 Syndromic Cluster Detected in Taluka"]
    end

    InpSymptoms --> RedFlagCheck
    RedFlagCheck -->|YES| EmergencyModal
    RedFlagCheck -->|NO| TriageEngine
    
    InpVitals --> VitalAnomaly
    VitalAnomaly --> FarmerAlert

    TriageEngine --> TriageResultCard
    TriageEngine -.->|Syndromic Case Signal| SurveillanceCluster
    SurveillanceCluster --> OfficerGIS
```

---

## 3. Model A: Species-Aware Triage Engine

### 3.1 Architecture & Unified JSON Rule Specification
Model A operates as an expert-weighted differential diagnosis engine. It evaluates incoming clinical vectors against **`triage_rules_v1.json`**:

```json
{
  "version": "1.0.0",
  "last_updated": "2026-11-04",
  "approved_by": "Veterinary Advisory Board (ICAR-NIVEDI Reference)",
  "species_rules": {
    "cattle": [
      {
        "condition_id": "LSD",
        "name": "Lumpy Skin Disease (Capripoxvirus)",
        "notifiable": true,
        "urgency": "URGENT",
        "cardinal_symptoms": ["nodules", "high_fever"],
        "supporting_symptoms": ["off_feed", "swollen_lymph_nodes", "milk_drop"],
        "min_fever_f": 103.0,
        "cardinal_match_required": 1,
        "supporting_match_threshold": 1,
        "first_aid_guidance": [
          "Isolate the animal immediately in a clean, shaded, fly-proof shed.",
          "Apply neem-oil based herbal fly repellent around unbroken skin.",
          "Provide cool, clean drinking water with electrolyte powder.",
          "CRITICAL: Do not administer human painkillers (paracetamol/diclofenac) without veterinary supervision."
        ]
      },
      {
        "condition_id": "FMD",
        "name": "Foot and Mouth Disease (Aphtae Epizooticae)",
        "notifiable": true,
        "urgency": "URGENT",
        "cardinal_symptoms": ["mouth_blisters", "excessive_drool", "lameness"],
        "supporting_symptoms": ["high_fever", "off_feed"],
        "min_fever_f": 103.5,
        "cardinal_match_required": 2,
        "supporting_match_threshold": 1,
        "first_aid_guidance": [
          "Isolate animal on dry soft bedding (straw/sand).",
          "Wash mouth blisters gently with mild 1% potassium permanganate or alum solution.",
          "Do not move infected animals along village paths or communal grazing grounds."
        ]
      }
    ]
  }
}
```

### 3.2 Clinical Likelihood Bands
Rather than uncalibrated probabilities (`0.88`), the engine computes evidence matching:
* **`Likely`:** All cardinal pathognomonic symptoms present + temperature above threshold.
* **`Possible`:** At least one cardinal symptom or multiple supporting symptoms without high fever.
* **`Less Likely`:** Generic malaise (off feed) without localized pathognomonic signs.

### 3.3 Safety Framing & Routing for Notifiable Diseases
* For notifiable infectious diseases (Lumpy Skin Disease, Foot & Mouth Disease, Anthrax, Black Quarter, Peste des Petits Ruminants):
  * **Zero Direct Prescription:** The UI never suggests antibiotic names, injections, or doses to farmers.
  * **Mandatory Vet Referral:** The system locks self-treatment advice and presents a direct dispatch CTA: `[Book Government Veterinary Dispensary Now]`.
  * **Surveillance Signal:** An anonymized signal event is dispatched to the taluka surveillance stream.

---

## 4. Evaluation Protocol & Safety Metrics

### 4.1 Ground-Truth Benchmark Set (Zero Circular Synthetic Data)
Instead of generating synthetic training data from our own rules and reporting artificial 95% accuracy, Model A is validated against an external, curated test set of **50 verified clinical cases** compiled from published ICAR-NIVEDI field case registries and Maharashtra veterinary college polyclinics:
* 15 Confirmed Lumpy Skin Disease cases
* 15 Confirmed Foot & Mouth Disease cases
* 10 Acute Mastitis cases
* 10 Non-infectious / Nutritional cases

### 4.2 Target Safety Metrics (Clinical Hierarchy)

| Metric | Mathematical Formula | Target Threshold | Clinical Consequence |
| :--- | :--- | :--- | :--- |
| **Red-Flag Under-Triage Rate** | $\frac{\text{Critical Cases Categorized as Routine}}{\text{Total Critical Cases}}$ | **0.0% (Zero Tolerance)** | A suffocating or bloating animal must NEVER be told to wait. |
| **Urgent Under-Triage Rate** | $\frac{\text{Urgent Cases Categorized as Moderate/Routine}}{\text{Total Urgent Cases}}$ | **$\le 1.0\%$** | Minimizes delayed veterinary intervention for progressive viral infections. |
| **Sensitivity on Notifiable Diseases** | $\frac{TP}{TP + FN}$ | **$\ge 96.0\%$** | Catches outbreaks at the index case. |
| **Over-Triage Rate** | $\frac{\text{Moderate Cases Categorized as Urgent}}{\text{Total Moderate Cases}}$ | **$\le 15.0\%$** | Tolerable conservative bias ensuring safety while avoiding total dispensary overload. |

---

## 5. Model C: Individual Herd Vital Anomaly Detection

### 5.1 Practical Heuristic vs. Over-Engineered ML
Individual dairy cattle physiology is highly sensitive to non-disease confounders. An over-parameterized neural network produces chronic false alarms. Model C implements a **Robust Rolling Baseline (EWMA)** paired with domain confounder dampening.

### 5.2 Cold-Start & Confounder Management
* **Cold-Start Rule:** An animal must have **$\ge 7$ consecutive days** of daily milk yield logs before automated anomaly detection activates. Prior to 7 days, the UI displays: *"Building baseline: 4 of 7 days logged"*.
* **Confounder Dampening Matrix:**

| Confounder | Detection Signal | Engine Response |
| :--- | :--- | :--- |
| **Lactation Curve Decay** | Natural milk drop of 5–8% per month after peak lactation. | Normalizes baseline using standard Wood's Lactation Decay Factor. |
| **Ambient Heat Stress (THI)** | High regional Temperature-Humidity Index ($>78$). | Expands tolerance threshold by $+10\%$ across all cows in the taluka. |
| **Recent Calving / Dry Period** | Lactation status marked as `dry` or `heifer`. | Suspends milk drop alarms; temperature monitoring remains active. |

### 5.3 Anomaly Trigger Rule
For cow $i$ on day $t$ with rolling median yield $\tilde{Y}_i$ and rolling median absolute deviation $MAD_i$:
1. **Severe Acute Milk Drop:**  
   $$\frac{\tilde{Y}_i - Y_{i,t}}{\tilde{Y}_i} > 0.30 \quad (\text{Drop} > 30\% \text{ for 2 consecutive milkings})$$
2. **Febrile Temperature Spike:**  
   $$\text{Rectal Temp} > 103.5^\circ\text{F} \quad (\text{Normal Cattle Temp: } 101.5^\circ\text{F} - 102.5^\circ\text{F})$$
3. **Action:** Surfaces high-priority dashboard card:  
   `⚠️ Health Alert: Gauri showed a 34% milk drop today. Check udder for swelling or initiate health check.`

---

## 6. Space-Time Surveillance Clustering (LDO Role)

### 6.1 Spatio-Temporal Clustering (ST-DBSCAN)
Surveillance clustering must account for infectious incubation periods. Space-only clustering mistakenly groups cases that occurred months apart.
* **Spatial Distance Parameter ($\epsilon_{\text{space}}$):** $15\text{ km}$ (typical radius of vector fly dispersion and communal grazing).
* **Temporal Distance Parameter ($\epsilon_{\text{time}}$):** $7\text{ days}$ (mean incubation window for Capripoxvirus and Aphthovirus).
* **Minimum Cases ($MinPts$):** $\ge 3$ matching syndromic reports within the space-time cylinder.

### 6.2 Census Denominator & Attack Rate
A cluster of 5 cases in a village of 50 cows is an emergency; 5 cases in a taluka of 50,000 is baseline. The engine joins `outbreak_clusters` with `livestock_census`:
$$\text{Attack Rate (\%)} = \left(\frac{\text{Active Incident Cases in Cluster}}{\text{Taluka Census Species Population}}\right) \times 100$$

---

## 7. The Continuous Ground-Truth Feedback Loop

To systematically prepare for V2 supervised machine learning:

```mermaid
sequenceDiagram
    participant Farmer as Farmer
    participant Triage as Model A Triage
    participant DB as PostgreSQL 16
    participant Vet as Licensed Vet
    
    Farmer->>Triage: Enters symptoms & duration
    Triage->>DB: Stores Case with triage_output & rules_version "v1.0.0"
    Vet->>DB: Conducts physical exam & enters confirmed_diagnosis
    DB->>DB: Appends Ground-Truth Pair: [observed_symptoms ➔ confirmed_diagnosis]
    Note over DB: Audited training set grows organically without synthetic circularity
```

* **Ground-Truth Validation Set Accumulation:**
  * Every completed case records: `(observed_symptoms, temperature, triage_condition, confirmed_diagnosis, vet_id)`.
  * Cases where Vet diagnosis matches Triage condition increment the agreement ratio.
  * Cases where Vet diagnosis differs are flagged for monthly clinical review by the advisory board to refine `triage_rules_v1.json`.

---

## 8. Microservice API Interface (FastAPI Specs)

The Python AI service exposes three high-throughput, stateless endpoints to the Spring Boot Core Backend:

### 8.1 Symptom Triage Endpoint
* **`POST /ai/v1/triage/evaluate`**
* **Payload:**
  ```json
  {
    "species": "cattle",
    "breed": "Gir",
    "age_months": 42,
    "rectal_temp_f": 103.8,
    "symptoms": ["nodules", "high_fever", "off_feed"],
    "duration_days": 2,
    "red_flags": {
      "severe_bloat": false,
      "convulsions": false,
      "sudden_hemorrhage": false
    }
  }
  ```
* **Response:**
  ```json
  {
    "rules_version": "v1.0.0",
    "red_flag_triggered": false,
    "urgency": "URGENT",
    "primary_condition": {
      "condition_id": "LSD",
      "name": "Lumpy Skin Disease",
      "likelihood_band": "Likely",
      "notifiable": true
    },
    "differential_conditions": [
      {
        "condition_id": "PSEUDO_POX",
        "name": "Bovine Papular Stomatitis / Pseudocowpox",
        "likelihood_band": "Possible"
      }
    ],
    "safe_first_aid": [
      "Isolate animal in shaded, well-ventilated stall.",
      "Apply herbal neem oil fly repellent around skin.",
      "Provide clean drinking water; avoid unprescribed human painkillers."
    ],
    "recommended_action": "BOOK_LOCAL_DISPENSARY"
  }
  ```

### 8.2 Vital Anomaly Detection Endpoint
* **`POST /ai/v1/vitals/analyze-stream`**
* Evaluates 14-day chronological milk yield and temperature array; returns boolean anomaly flag, type, and human-readable explanation.

### 8.3 Space-Time Cluster Aggregator
* **`POST /ai/v1/surveillance/compute-clusters`**
* Ingests active incident coordinates and timestamps; executes ST-DBSCAN joined against `livestock_census` and returns GeoJSON cluster polygons.

---

> 📌 **Engineering Status:** Committed as [`ML_AI_SYSTEM_PLAN.md`](file:///g:/Chetan/pashuSachet/ML_AI_SYSTEM_PLAN.md).
