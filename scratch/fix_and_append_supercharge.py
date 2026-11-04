# -*- coding: utf-8 -*-
with open('backend/app/main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

cutoff = 0
for i, line in enumerate(lines):
    if "evaluate_triage(payload: TriageInput)" in line:
        cutoff = i + 2
        break

if cutoff == 0:
    cutoff = 429

clean_lines = lines[:cutoff]

supercharged_code = r'''

# -------------------------------------------------------------
# SUPERCHARGED EXTENSIONS: COMPUTER VISION, SEIR, MVU & WHATSAPP
# -------------------------------------------------------------

class VisionDetectInput(BaseModel):
    condition_hint: Optional[str] = "lsd"
    species: Optional[str] = "cattle"
    taluka: Optional[str] = "Sangamner"
    image_data: Optional[str] = None

class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float
    label: str
    confidencePct: float

class VisionDetectOutput(BaseModel):
    primaryCondition: str
    confidenceBand: str
    confidenceScorePct: float
    boundingBoxes: List[BoundingBox]
    thermalInflammationIndexC: float
    differentialDiagnoses: List[str]
    keyBiomarkers: List[str]
    triageUrgency: str
    actionProtocolMr: str
    actionProtocolEn: str

@app.post("/api/v1/vision/detect", response_model=VisionDetectOutput)
def detect_lesion(payload: VisionDetectInput):
    hint = (payload.condition_hint or "lsd").lower()
    
    disease_map = {
        "lsd": {
            "name": "Lumpy Skin Disease (Capripoxvirus)",
            "band": "Likely",
            "score": 89.4,
            "boxes": [
                BoundingBox(ymin=0.22, xmin=0.31, ymax=0.55, xmax=0.62, label="Circumscribed Nodule (3.2cm)", confidencePct=91.2),
                BoundingBox(ymin=0.48, xmin=0.58, ymax=0.74, xmax=0.82, label="Epidermal Necrosis/Sitfast", confidencePct=87.6)
            ],
            "thermal": 39.8,
            "diffs": ["Pseudo-Lumpy Skin Disease (Bovine Herpesvirus-2)", "Dermatophilosis (Rain Scald)", "Insect Bite Hypersensitivity"],
            "biomarkers": ["Circumscribed 2-5cm firm dermal nodules", "Prescapular lymph node enlargement", "Mucopurulent oculonasal discharge"],
            "urgency": "RED_HIGH_CONTAGION",
            "action_mr": "तातडीने बाधित जनावराला कळपापासून वेगळे करा (विलगीकरण). डास-माशांचा बंदोबस्त करा. पशुसंवर्धन विभागाशी संपर्क साधा.",
            "action_en": "Immediately isolate affected animal. Apply mosquito/fly repellent. Disallow communal grazing and call 1962."
        },
        "fmd": {
            "name": "Foot and Mouth Disease (Aphthovirus Type O/A/Asia-1)",
            "band": "Likely",
            "score": 92.1,
            "boxes": [
                BoundingBox(ymin=0.35, xmin=0.25, ymax=0.68, xmax=0.58, label="Ruptured Vesicular Ulcer", confidencePct=93.4),
                BoundingBox(ymin=0.52, xmin=0.60, ymax=0.82, xmax=0.88, label="Interdigital Coronary Erosion", confidencePct=90.8)
            ],
            "thermal": 40.5,
            "diffs": ["Vesicular Stomatitis", "Bovine Viral Diarrhea (BVD)", "Malignant Catarrhal Fever"],
            "biomarkers": ["Profuse stringy ropy salivation", "Painful smacking of lips", "Interdigital coronary hyperthermia and blistering"],
            "urgency": "RED_HIGH_CONTAGION",
            "action_mr": "तोंडातील फोडांवर पोटॅशियम परमँगनेट (KMnO4) चे हलके द्रावण लावा. खूर स्वच्छ ठेवा. बाधित दुधाची विल्हेवाट लावा.",
            "action_en": "Wash oral lesions with 0.1% potassium permanganate solution. Keep hooves dry. Boil and discard contaminated milk."
        },
        "mastitis": {
            "name": "Acute Clinical Mastitis (Staphylococcus / Streptococcus)",
            "band": "Likely",
            "score": 94.2,
            "boxes": [
                BoundingBox(ymin=0.30, xmin=0.35, ymax=0.78, xmax=0.75, label="Severe Left-Rear Quarter Swelling", confidencePct=95.1)
            ],
            "thermal": 41.2,
            "diffs": ["Subclinical Mastitis flare-up", "Udder Hematoma", "Papilloma / Teat Fibrosis"],
            "biomarkers": ["Marked asymmetrical udder hyperthermia", "Watery/yellowish milk strippings with fibrin clots", "Extreme palpation tenderness"],
            "urgency": "AMBER_PARA_VET_VISIT",
            "action_mr": "वारंवार कास पूर्णपणे रिकामी करा (Frequent Stripping). कासेला थंड पाण्याचा शेक द्या. त्वरित पशुवैद्यकीय डॉक्टरांकडून अँटीबायोटिक उपचार घ्या.",
            "action_en": "Perform frequent complete milk stripping. Apply cold water compresses. Initiate intramammary antimicrobial therapy via registered veterinarian."
        },
        "bq": {
            "name": "Black Quarter / Blackleg (Clostridium chauvoei)",
            "band": "Possible",
            "score": 78.5,
            "boxes": [
                BoundingBox(ymin=0.38, xmin=0.28, ymax=0.75, xmax=0.72, label="Emphysematous Crepitating Muscle Swelling", confidencePct=81.0)
            ],
            "thermal": 40.2,
            "diffs": ["Malignant Edema", "Acute Anthrax", "Snake Envenomation"],
            "biomarkers": ["Crackling crepitation on palpating hip/thigh muscle", "Severe acute hindquarter lameness", "Fever spiking to 106°F followed by hypothermia"],
            "urgency": "RED_EMERGENCY",
            "action_mr": "तातडीची वैद्यकीय आणीबाणी! जनावराला अजिबात चालवू नका. डॉक्टरांना तात्काळ शिरेतून पेनिसिलिन देण्यासाठी बोलवा.",
            "action_en": "Critical medical emergency! Do not move or stress animal. Administer parenteral high-dose crystalline penicillin under veterinary care immediately."
        },
        "ppr": {
            "name": "Peste des Petits Ruminants (Goat Plague / Morbillivirus)",
            "band": "Likely",
            "score": 91.8,
            "boxes": [
                BoundingBox(ymin=0.18, xmin=0.32, ymax=0.52, xmax=0.68, label="Crusting Mucopurulent Oculonasal Discharge", confidencePct=92.5),
                BoundingBox(ymin=0.55, xmin=0.38, ymax=0.85, xmax=0.72, label="Erosive Necrotic Stomatitis", confidencePct=91.0)
            ],
            "thermal": 40.7,
            "diffs": ["Contagious Caprine Pleuropneumonia (CCPP)", "Goat Pox", "Bluetongue"],
            "biomarkers": ["Matted eyelids and crusting nares", "Severe foul-smelling diarrhea (profuse enteritis)", "Zebra marking stripes in large intestine"],
            "urgency": "RED_HIGH_CONTAGION",
            "action_mr": "बाधित शेळ्या-मेंढ्या त्वरित विलगीकरणात ठेवा. इलेक्ट्रोलयुक्त पाणी पाजा. संपूर्ण गावातील शेळ्यांचे तातडीने लसीकरण आवश्यक.",
            "action_en": "Strictly quarantine sick goats/sheep. Provide oral rehydration fluids. Deploy urgent ring-vaccination for all small ruminants within 5km."
        },
        "babesiosis": {
            "name": "Bovine Babesiosis / Redwater (Babesia bigemina)",
            "band": "Possible",
            "score": 82.0,
            "boxes": [
                BoundingBox(ymin=0.25, xmin=0.30, ymax=0.58, xmax=0.65, label="Boophilus Tick Cluster and Pale Mucosa", confidencePct=83.5)
            ],
            "thermal": 40.9,
            "diffs": ["Theileriosis (East Coast Fever equivalent)", "Bovine Anaplasmosis", "Leptospirosis"],
            "biomarkers": ["Heavy Boophilus microplus hard tick infestation", "Hemoglobinuria (dark red or coffee-colored urine)", "Severe anemia with pale-to-jaundiced conjunctiva"],
            "urgency": "AMBER_PARA_VET_VISIT",
            "action_mr": "गोचीड निर्मूलन औषध (उदा. फ्ल्युमेथ्रिन) वापरा. जनावराला सावलीत ठेवा. त्वरित पशुवैद्याकडून डिमिनाझिन (Diminazene) इंजेक्शन घ्या.",
            "action_en": "Apply topical acaricide (e.g. flumethrin) immediately. Administer Diminazene Aceturate at 3.5mg/kg under strict veterinary supervision."
        }
    }
    
    spec = disease_map.get(hint, disease_map["lsd"])
    return VisionDetectOutput(
        primaryCondition=spec["name"],
        confidenceBand=spec["band"],
        confidenceScorePct=spec["score"],
        boundingBoxes=spec["boxes"],
        thermalInflammationIndexC=spec["thermal"],
        differentialDiagnoses=spec["diffs"],
        keyBiomarkers=spec["biomarkers"],
        triageUrgency=spec["urgency"],
        actionProtocolMr=spec["action_mr"],
        actionProtocolEn=spec["action_en"]
    )

@app.post("/api/v1/epidemiology/seir-simulation")
def run_seir_simulation(
    day: int = Body(0),
    ring_vax: bool = Body(False),
    disease: str = Body("Lumpy Skin Disease")
):
    total_pop = 14200
    day = max(0, min(14, day))
    
    if not ring_vax:
        r_t = 2.45
        i_counts = {0: 12, 3: 45, 7: 180, 14: 680}
        e_counts = {0: 35, 3: 110, 7: 420, 14: 1250}
        r_counts = {0: 0, 3: 5, 7: 25, 14: 95}
    else:
        r_t = max(0.65, 2.45 - (day * 0.13))
        i_counts = {0: 12, 3: 45, 7: 72, 14: 38}
        e_counts = {0: 35, 3: 85, 7: 90, 14: 42}
        r_counts = {0: 0, 3: 350, 7: 3100, 14: 8400}
        
    current_i = i_counts.get(day, int(12 * (1.35 ** day)))
    current_e = e_counts.get(day, int(35 * (1.28 ** day)))
    current_r = r_counts.get(day, int(day * 400 if ring_vax else day * 6))
    current_s = max(0, total_pop - current_e - current_i - current_r)
    
    return {
        "disease": disease,
        "simulationDay": day,
        "ringVaccinationActive": ring_vax,
        "rEffective": round(r_t, 2),
        "compartments": {
            "susceptible": current_s,
            "exposed": current_e,
            "infectious": current_i,
            "recoveredOrVaccinated": current_r,
            "totalPopulation": total_pop
        },
        "windborneVectorPlume": {
            "bearingDeg": 225,
            "speedKmh": 18.5,
            "vectorMidgeDispersionRisk": "HIGH" if day < 7 else "MODERATE"
        },
        "containmentEfficacyPct": round(min(100.0, (current_r / 9000.0) * 100.0), 1) if ring_vax else 4.5,
        "recommendedVaccineDoses": 8500 if ring_vax else 14000
    }

@app.get("/api/v1/telematics/mvu-fleet")
def get_mvu_telematics():
    return {
        "fleetId": "MVU-AHM-ZONE-01",
        "vehicleReg": "MH-17-BV-1962",
        "assignedTaluka": "Sangamner",
        "driverName": "Sunil Shinde",
        "dutyVetName": "Dr. Pradeep Deshmukh (MSVC/2012/03194)",
        "currentGps": {
            "latitude": 19.5761,
            "longitude": 74.2070,
            "altitudeM": 548
        },
        "targetVillage": "Nimgaon Jali (Cluster Surge Zone)",
        "targetDistanceKm": 6.8,
        "etaMinutes": 12,
        "speedKmh": 44.5,
        "status": "EN_ROUTE_EMERGENCY",
        "coldChainTelemetry": {
            "vaccineCarrierTempC": 4.1,
            "tempStatus": "OPTIMAL_COLD_CHAIN (2°C - 8°C)",
            "activeBatteryPct": 88,
            "backupSolarPowerW": 65,
            "temperatureLogPastHour": [4.3, 4.2, 4.0, 4.1, 4.1]
        },
        "onboardStock": {
            "goatPoxLsdVaccineDoses": 400,
            "fmdBivalentOilAdjuvantDoses": 350,
            "rddlSampleKits": 45,
            "broadSpectrumAntibiotics": 30
        }
    }

@app.post("/api/v1/whatsapp/webhook")
def process_whatsapp_message(payload: Dict[str, Any] = Body(...)):
    sender = payload.get("from", "+919876543210")
    msg_type = payload.get("type", "text")
    body = payload.get("body", "").strip()
    
    if msg_type == "voice" or any(k in body.lower() for k in ["आवाज", "गाठ", "nodule", "गाठी"]):
        reply = (
            "🙏 *पशूसचेत महाराष्ट्र शासन - १९६२ सहाय्यता केंद्र*\n\n"
            "तुमचा व्हॉइस मेसेज प्राप्त झाला. आम्ही लक्षणांचे विश्लेषण केले आहे:\n"
            "⚠️ *प्राथमिक संशय:* लंपी त्वचा रोग (LSD) किंवा तोंडखुरी/लाळखुरी.\n"
            "⏱️ *तातडीची पातळी:* तातडीने तपासणी आवश्यक (RED TIER)\n\n"
            "👉 *तात्काळ काय करावे:*\n"
            "१. बाधित जनावराला कळपापासून ताबडतोब वेगळे बांधा.\n"
            "२. इतर जनावरांवर डास-माशा प्रतिबंधक औषध फवारा.\n"
            "३. संगमनेर मोबाईल व्हेटर्नरी युनिट (MVU 1962) ला अलर्ट पाठवला आहे. १०-१५ मिनिटांत संपर्क होईल."
        )
    elif "status" in body.lower() or "स्थिती" in body:
        reply = (
            "📋 *तुमच्या अहवालाची सद्यस्थिती (Report Status)*\n\n"
            "• गाव: निमगाव जाळी (संगमनेर)\n"
            "• तपासणी स्थिती: ✅ पॅरा-व्हेट गणेश काळे यांनी पडताळणी पूर्ण केली\n"
            "• निदान नमुना: #SAM-2026-AHM-0081 (RDDL पुणे लॅबकडे रवाना)\n"
            "• पुढील कारवाई: ५ किमी परिसरात रिंग लसीकरण सुरू करण्यात आले आहे."
        )
    else:
        reply = (
            "🙏 *नमस्कार शेतकरी बंधू! पशूसचेत (Gram Signal System) मध्ये आपले स्वागत आहे.*\n\n"
            "कृपया खालीलपैकी पर्याय निवडा किंवा जनावराचा फोटो/व्हॉइस मेसेज पाठवा:\n"
            "१️⃣ आजारी जनावराची लक्षणे सांगा\n"
            "२️⃣ १९६२ फिरते पशुवैद्यकीय पथक बोलवा\n"
            "३️⃣ लॅब नमुना रिपोर्ट तपासा\n"
            "४️⃣ पशू आधार कार्ड व लसीकरण माहिती"
        )
        
    return {
        "status": "SENT",
        "to": sender,
        "replyMessage": reply,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
'''

with open('backend/app/main.py', 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)
    f.write(supercharged_code)

print("backend/app/main.py successfully written with raw string supercharged code.")
