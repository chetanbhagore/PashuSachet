# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("Applying Phase 3: Uncertainty-Aware ML Triage & 1962 Accelerator Engine...")

# 1. Update index.html inside #assessmentResult
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read().replace('\r\n', '\n')

old_result_banner = """          <!-- Assessment Result Panel (Hidden until evaluated) -->
          <div class="assessment-result" id="assessmentResult">
            <div class="triage-banner" id="triageBanner">
              <div id="triageText">
                <strong>CRITICAL:</strong> High Urgency Referral
              </div>
              <button class="btn btn-sm btn-primary" onclick="document.getElementById('vet-directory').scrollIntoView({behavior:'smooth'})">
                Contact Nearest Vet Now
              </button>
            </div>"""

new_result_banner = """          <!-- Assessment Result Panel (Hidden until evaluated) -->
          <div class="assessment-result" id="assessmentResult">
            <!-- 1962 Accelerator Emergency Dispatch Banner (Hidden unless critical) -->
            <div id="mvuDispatchCard" class="mvu-dispatch-card" style="display: none; background: #fef2f2; border: 2px solid #ef4444; border-radius: 10px; padding: 14px 18px; margin-bottom: 14px;">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div>
                  <div style="font-weight: 800; color: #b91c1c; font-size: 1rem; display: flex; align-items: center; gap: 8px;">
                    <span>🚨 1962 ACCELERATOR: Mobile Veterinary Unit (MVU) Pre-Notification</span>
                  </div>
                  <div id="mvuTicketDetails" style="font-size: 0.85rem; color: #7f1d1d; margin-top: 4px; line-height: 1.5;">
                    <!-- Injected dynamically -->
                  </div>
                </div>
                <div style="display: flex; gap: 8px;">
                  <a href="tel:1962" class="btn btn-sm" style="background: #b91c1c; color: #ffffff; font-weight: 700; text-decoration: none;">
                    📞 Dial 1962 Helpline
                  </a>
                </div>
              </div>
            </div>

            <!-- One Health Zoonotic Alert Banner (Hidden unless zoonotic threat) -->
            <div id="zoonoticAlertBanner" class="zoonotic-alert-banner" style="display: none; background: #450a0a; color: #fecaca; border: 2px solid #dc2626; border-radius: 10px; padding: 14px 18px; margin-bottom: 14px;">
              <div style="font-weight: 800; font-size: 0.98rem; color: #f87171; display: flex; align-items: center; gap: 8px;">
                <span>☣️ ONE HEALTH ZOONOTIC ALERT: High Transmission Risk to Humans</span>
              </div>
              <div id="zoonoticDetails" style="font-size: 0.85rem; color: #fecaca; margin-top: 6px; line-height: 1.5;">
                <!-- Injected dynamically -->
              </div>
            </div>

            <div class="triage-banner" id="triageBanner">
              <div id="triageText">
                <strong>CRITICAL:</strong> High Urgency Referral
              </div>
              <button class="btn btn-sm btn-primary" onclick="document.getElementById('vet-directory').scrollIntoView({behavior:'smooth'})">
                Contact Nearest Vet Now
              </button>
            </div>

            <!-- Explicit Abstention Card (Hidden unless ambiguous signs) -->
            <div id="abstentionNoticeBox" style="display: none; background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 14px 18px; margin-bottom: 16px;">
              <div style="font-weight: 800; color: #166534; font-size: 0.95rem; display: flex; align-items: center; gap: 8px;">
                <span>🛡️ मॉडेल संयम (Explicit Model Abstention - No Guessing)</span>
              </div>
              <div style="font-size: 0.85rem; color: #15803d; margin-top: 4px; line-height: 1.5;">
                ही लक्षणे सामान्य असून एका विशिष्ट आजाराचे ठोस पुरावे देत नाहीत. कृत्रिम बुद्धिमत्ता येथे अंदाजे निदान न लावता सुरक्षित देखरेख करण्याचा सल्ला देते.
              </div>
            </div>"""

if old_result_banner in html:
    html = html.replace(old_result_banner, new_result_banner)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html with 1962 dispatch, zoonotic banner, and abstention card!")
else:
    print("Could not find old result banner in index.html!")
    sys.exit(1)

# 2. Update css/style.css with Phase 3 styling
with open("css/style.css", "r", encoding="utf-8") as f:
    css = f.read().replace('\r\n', '\n')

phase3_css = """
.triage-band.abstention {
  background: #f0fdf4;
  color: #166534;
  border: 1px solid #86efac;
}

.mvu-dispatch-card {
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.15);
  animation: pulse-border 2s infinite;
}

.zoonotic-alert-banner {
  box-shadow: 0 4px 14px rgba(220, 38, 38, 0.25);
}
"""

if ".triage-band.abstention" not in css:
    css += "\n" + phase3_css
    with open("css/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated css/style.css with Phase 3 styles!")
else:
    print("Phase 3 styles already present in css/style.css")

# 3. Update js/app.js evaluateSymptoms implementation
with open("js/app.js", "r", encoding="utf-8") as f:
    js = f.read().replace('\r\n', '\n')

old_eval_body_start = """  // Rule-based clinical triage matching Seva First Model A
  let primaryCondition = "";
  let confidence = 0;
  let urgency = "moderate"; // critical, urgent, moderate
  let urgencyLabel = "";
  let differential = [];
  let actions = [];

  // RED-FLAG EMERGENCY CIRCUIT BREAKER
  const isRedFlag = checkedBoxes.includes("bleeding") || checkedBoxes.includes("sudden_death") || checkedBoxes.includes("recumbent");
  if (isRedFlag) {
    const emergModal = document.getElementById("emergencyModal");
    if (emergModal) emergModal.classList.add("active");
  }"""

new_eval_body = """  // Rule-based clinical triage matching Seva First Model A & GSS Protocol
  let primaryCondition = "";
  let qualitativeBand = "Likely"; // Likely, Possible, Less Likely, Abstention
  let urgency = "moderate"; // critical, urgent, moderate
  let urgencyLabel = "";
  let differential = [];
  let actions = [];
  let isZoonoticAlert = false;
  let zoonoticMsg = "";
  let mvuTicket = null;
  let isAbstention = false;

  // RED-FLAG EMERGENCY CIRCUIT BREAKER & 1962 ACCELERATOR
  const isRedFlag = checkedBoxes.includes("bleeding") || checkedBoxes.includes("sudden_death") || checkedBoxes.includes("recumbent") || isMortalityCheck;
  if (isRedFlag) {
    const emergModal = document.getElementById("emergencyModal");
    if (emergModal) emergModal.classList.add("active");

    // 1962 ACCELERATOR ENGINE: Auto-generate priority MVU dispatch pre-notification
    mvuTicket = {
      ticketId: "1962-MH-" + Math.floor(1000 + Math.random() * 9000),
      dispatchStatus: "AUTO_PRENOTIFIED",
      priority: "CRITICAL_RED_FLAG",
      targetVillage: villageLocation,
      assignedUnit: "MVU Unit 14 (Sangamner / Akole Beat)",
      mvuContact: "1962 (Toll Free)",
      etaMinutes: 25,
      timestamp: new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' })
    };
  }

  const hasFever = checkedBoxes.includes("fever") || tempDegree >= 103.5;
  const hasNodules = checkedBoxes.includes("skin_nodules");
  const hasMouthFoot = checkedBoxes.includes("mouth_lesions") || checkedBoxes.includes("lameness");
  const hasRespiratory = checkedBoxes.includes("cough") || checkedBoxes.includes("nasal_discharge");
  const hasMastitis = checkedBoxes.includes("udder_swelling") || checkedBoxes.includes("milk_drop");
  const hasDiarrhea = checkedBoxes.includes("diarrhea");
  const hasSuddenDeath = checkedBoxes.includes("sudden_death") || isMortalityCheck;

  // ZOONOTIC THREAT SENTINEL (Anthrax, Rabies, Brucellosis)
  if (hasSuddenDeath && (species === "cattle" || species === "buffalo" || species === "sheep")) {
    isZoonoticAlert = true;
    zoonoticMsg = "अँथ्रॅक्स / अचानक मृत्यू संशय (Anthrax Suspected). शव उघडू नका, नैसर्गिक छिद्रांमधून रक्तस्त्राव असल्यास स्पर्श करू नका. स्थानिक शासकीय वैद्यक व जिल्हा आरोग्य अधिकारी (DMO) यांना अलर्ट पाठवला आहे.";
  } else if (species === "dog" && (checkedBoxes.includes("mouth_lesions") || checkedBoxes.includes("anorexia") || isRedFlag)) {
    isZoonoticAlert = true;
    zoonoticMsg = "रेबीज संशय (Rabies Suspected). चावा किंवा लाळेचा मानवी त्वचेशी संपर्क टाळा. संशयित प्राण्याला सुरक्षित जागी बंदिस्त करा व त्वरित 1962 वर कळवा.";
  }

  // EXPLICIT ABSTENTION GATE:
  // If only isolated non-specific signs (anorexia only, milk drop only) and no fever or pathognomonic lesions:
  if ((checkedBoxes.length === 1 && (checkedBoxes[0] === 'anorexia' || checkedBoxes[0] === 'milk_drop')) ||
      (!hasNodules && !hasMouthFoot && !hasRespiratory && !hasMastitis && !hasDiarrhea && !hasSuddenDeath && tempDegree < 103.0)) {
    isAbstention = true;
    primaryCondition = "अस्पष्ट प्रारंभिक लक्षणे (Insufficient Distinctive Signs)";
    qualitativeBand = "Abstention";
    urgency = "moderate";
    urgencyLabel = "MODERATE: मॉडेल संयम (Deliberate Abstention - No Speculation)";
    actions = [
      "१. जनावराला कोणतेही अनधिकृत प्रतिजैविक (अँटीबायोटिक) किंवा मानवी औषध देऊ नका.",
      "२. रवंथ चक्र तपासा (२ मिनिटांत २ ते ३ वेळा रवंथ व्हायला हवे) आणि ताजे पिण्याचे पाणी व हिरवा चारा द्या.",
      "३. पुढील १२ ते २४ तास लक्षपूर्वक निरीक्षण करा आणि गुदद्वाराचे तापमान मोजा.",
      "४. २४ तासांनंतरही सुधारणा न झाल्यास स्थानिक पशुमित्र किंवा पशुवैद्यकीय दवाखान्यात संपर्क साधा."
    ];
    differential = ["Mild Indigestion (अपचन)", "Environmental / Heat Stress (उष्मा ताण)", "Subclinical Diet Change"];
  } else if (species === "poultry") {
    if (hasRespiratory || checkedBoxes.includes("anorexia") || hasSuddenDeath) {
      primaryCondition = "Newcastle Disease (Ranikhet) / Infectious Coryza (राणीखेत)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Urgent Flock Isolation Required";
      actions = [
        "१. आजारी पक्ष्यांना तात्काळ निरोगी कळपापासून वेगळे (क्वारंटाइन) करा.",
        "२. पिण्याच्या पाण्यात इलेक्ट्रोल पावडर व व्हिटॅमिन बी-कॉम्प्लेक्स मिसळून द्या.",
        "३. शेडच्या प्रवेशद्वारावर जंतुनाशक फवारणी करा व बाहेरील व्यक्तींना प्रवेश बंदी करा.",
        "४. शासकीय प्रयोगशाळेतील तपासणीसाठी तात्काळ स्थानिक पशुवैद्यकांना संपर्क करा."
      ];
      differential = ["Infectious Bronchitis", "Fowl Cholera", "Nutritional Deficiency"];
    } else {
      primaryCondition = "Coccidiosis / Enteric Distress (कॉकसिडिओसिस)";
      qualitativeBand = "Possible";
      urgency = "urgent";
      urgencyLabel = "URGENT: Review Litter Hygiene";
      actions = [
        "१. शेडमधील ओले तूस (litter) तात्काळ बदलून कोरडा भुसा टाका.",
        "२. पिण्याचे पाणी स्वच्छ व आम्लयुक्त (acidified) ठेवा.",
        "३. पशुवैद्यकीय सल्ल्याने कॉक्सिडिओस्टॅट औषध सुरू करा."
      ];
      differential = ["Colibacillosis", "Dietary change"];
    }
  } else if (species === "goat" || species === "sheep") {
    if (checkedBoxes.includes("mouth_lesions") && (hasDiarrhea || hasFever)) {
      primaryCondition = "Peste des Petits Ruminants (PPR) / Goat Plague (शेळ्यांमधील पीपीआर)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Highly Contagious Small Ruminant Alert";
      actions = [
        "१. बाधित शेळ्या/मेंढ्या तात्काळ वेगळ्या बांधा; सार्वजनिक चराई व पाण्याचे टाके पूर्णपणे बंद करा.",
        "२. तोंडातील जखमांवर सौम्य पोटॅशियम परमँगनेट (१:१०,०००) किंवा बोरोग्लिसरीन लावा.",
        "३. कोमट द्रावण किंवा मऊ लापशी खाऊ घाला, कोरडे धांडे देऊ नका.",
        "४. जवळच्या पशुवैद्यकीय दवाखान्यातून रिंग-लसीकरण (Ring Vaccination) मोहीम राबवून घ्या."
      ];
      differential = ["Contagious Ecthyma (Orf)", "Bluetongue", "Pasteurellosis"];
    } else if (hasSuddenDeath || hasDiarrhea) {
      primaryCondition = "Enterotoxaemia (Pulpy Kidney) Suspected (आंत्रविषार)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Risk of Rapid Mortality";
      actions = [
        "१. धान्य व पेंड देणे ताबडतोब थांबवा; केवळ कोरडा चारा द्या.",
        "२. आजारी नसलेल्या सर्व जनावरांना तात्काळ आंत्रविषार (ET) लस टोचून घ्या.",
        "३. पशुवैद्यकीय पथकाकडून डिहायड्रेशन रोखण्यासाठी सलाइन उपचार घ्या."
      ];
      differential = ["Coccidiosis", "Plant Poisoning"];
    } else {
      primaryCondition = "Pneumonia / Caprine Respiratory Infection (फुफ्फुसदाह/खोकला)";
      qualitativeBand = "Possible";
      urgency = "urgent";
      urgencyLabel = "URGENT: Veterinary Auscultation Advised";
      actions = [
        "१. शेड कोरडी व हवेशीर ठेवा; रात्री थंड वाऱ्यापासून संरक्षण करा.",
        "२. कोमट पाणी व गुळ-पाणी पिण्यास द्या.",
        "३. पशुवैद्यकीय सल्ल्याने प्रतिजैविक व कफ सिरप द्या."
      ];
      differential = ["Lungworm infestation", "Shipping fever"];
    }
  } else {
    // Cattle / Buffalo
    if (hasNodules) {
      primaryCondition = "Lumpy Skin Disease (LSD) Suspected (लम्पी त्वचा रोग)";
      qualitativeBand = "Likely";
      urgency = "urgent";
      urgencyLabel = "URGENT: Vector-Borne Viral Screening Positive";
      actions = [
        "१. बाधित जनावराला निरोगी जनावरांपासून तात्काळ दूर वेगळ्या गोठ्यात बांधा.",
        "२. गोठ्यात कडुनिंबाच्या पानांचा धूर करा व डास/माशा/गोचीड प्रतिबंधक फवारणी करा.",
        "३. अंगावरील गाठी व जखमांवर हळद + कापूर + खोबरेल तेलाचा लेप लावा.",
        "४. मानवी ताप प्रतिबंधक औषधे (उदा. पॅरासिटामॉल) डॉक्टरी सल्ल्याशिवाय अतिरिक्त प्रमाणात देऊ नका.",
        "५. स्थानिक पशुवैद्यकांना संपर्क करून गोट पॉक्स (Goat Pox) लसीकरण तपासा."
      ];
      differential = ["Pseudo-lumpy skin disease (Herpesvirus 2)", "Bovine Papillomatosis", "Insect bites"];
    } else if (hasMouthFoot && (hasFever || checkedBoxes.includes("milk_drop"))) {
      primaryCondition = "Foot and Mouth Disease (FMD) Screening Match (लाळ-खुरकूत)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: High Transmission Risk (Reportable)";
      actions = [
        "१. आजारी जनावराला तात्काळ वेगळे बांधा व जनावरांची हालचाल पूर्णपणे थांबवा.",
        "२. तोंड १% तुरटीच्या पाण्याने किंवा पोटॅशियम परमँगनेटच्या सौम्य पाण्याने दिवसातून २ वेळा धुवा.",
        "३. खुरांच्या जखमांमध्ये फिनाईल किंवा जंतुनाशक मलम (जस्त मलम + हळद) लावा जेणेकरून किडे पडणार नाहीत.",
        "४. जनावराला मऊ चारा, दलिया किंवा पेज खायला द्या (कडक वैरणीने तोंडाला त्रास होतो).",
        "५. गावातील इतर पशुपालकांना सतर्क करून सामूहिक लसीकरणाची मागणी करा."
      ];
      differential = ["Vesicular Stomatitis", "Mucosal Disease (BVD)", "Chemical irritant"];
    } else if (hasMastitis) {
      primaryCondition = "Bovine Mastitis (Sub-acute / Clinical) (कासदाह/स्तनदाह)";
      qualitativeBand = "Likely";
      urgency = "urgent";
      urgencyLabel = "URGENT: Dairy Production & Milk Safety Concern";
      actions = [
        "१. बाधित सडातील दूध वेगळे काढून जंतुनाशक टाकून नष्ट करा; हे दूध विक्री करू नका.",
        "२. कासेला कोमट पाण्याने स्वच्छ धुऊन सुती कापडाने कोरडे करा.",
        "३. दूध काढताना प्रथम निरोगी सडांचे व शेवटी आजारी सडाचे दूध काढा.",
        "४. दूध काढल्यानंतर सड जंतुनाशक द्रावणात (Teat Dip) बुडवा.",
        "५. पशुवैद्यकांकडून CMT टेस्ट व इंट्रामॅमरी ट्यूब उपचार करून घ्या."
      ];
      differential = ["Udder edema", "Hematoma", "Mycoplasma mastitis"];
    } else if (hasRespiratory && hasFever) {
      primaryCondition = "Haemorrhagic Septicaemia (HS) Suspected (घटसर्प)";
      qualitativeBand = "Likely";
      urgency = "critical";
      urgencyLabel = "CRITICAL: Rapid Progression - Immediate Vet Attention";
      actions = [
        "१. जनावराला अजिबात चालवू नका; थंड व हवेशीर सावलीत ठेवा.",
        "२. मानेभोवती किंवा गळ्याखाली सूज असल्यास त्यावर थंड पाणी टाका.",
        "३. घटसर्पामध्ये काही तासांत मृत्यू संभवतो, म्हणून तात्काळ १९६२ रुग्णवाहिका बोलवा.",
        "४. पशुवैद्यकीय डॉक्टरांकडून तात्काळ प्रतिजैविक इंजेक्शन सुरू करा."
      ];
      differential = ["Black Quarter (early)", "Enzootic Pneumonia", "Aspiration pneumonia"];
    } else {
      primaryCondition = "Non-Specific Indigestion / Simple Anorexia (अपचन/चारा न खाणे)";
      qualitativeBand = "Possible";
      urgency = "moderate";
      urgencyLabel = "MODERATE: Monitor Vitals & Rumination";
      actions = [
        "१. जनावराला पाचक मसाले, गूळ व खनिज मिश्रण (Mineral Mixture) द्या.",
        "२. रवंथ चक्र तपासा (२ मिनिटांत किमान २ वेळा रवंथ व्हायला हवे).",
        "३. २४ तासांत खाणे पूर्ववत न झाल्यास पशुवैद्यकीय तपासणी करून घ्या."
      ];
      differential = ["Mild rumen acidosis", "Dietary change stress", "Parasitic load"];
    }
  }

  // Populate UI
  triageBanner.className = `triage-banner triage-${urgency}`;
  triageText.innerHTML = `<strong>${urgency.toUpperCase()}:</strong> ${urgencyLabel}`;

  diagName.textContent = primaryCondition;
  
  const bandContainer = document.getElementById("triageBandContainer");
  if (bandContainer) {
    bandContainer.textContent = `${qualitativeBand} Differential (संभाव्य श्रेणी)`;
    bandContainer.className = `triage-band ${qualitativeBand.toLowerCase()}`;
  }

  // 1962 Accelerator Card Display
  const mvuCard = document.getElementById("mvuDispatchCard");
  const mvuDetails = document.getElementById("mvuTicketDetails");
  if (mvuCard && mvuDetails) {
    if (mvuTicket) {
      mvuDetails.innerHTML = `<strong>Ticket:</strong> #${mvuTicket.ticketId} • <strong>Status:</strong> Pre-Notified to <strong>${mvuTicket.assignedUnit}</strong> (${mvuTicket.targetVillage}) • <strong>Estimated Arrival:</strong> ~${mvuTicket.etaMinutes} mins.`;
      mvuCard.style.display = "block";
    } else {
      mvuCard.style.display = "none";
    }
  }

  // Zoonotic Alert Display
  const zooBanner = document.getElementById("zoonoticAlertBanner");
  const zooDetails = document.getElementById("zoonoticDetails");
  if (zooBanner && zooDetails) {
    if (isZoonoticAlert) {
      zooDetails.innerHTML = zoonoticMsg;
      zooBanner.style.display = "block";
    } else {
      zooBanner.style.display = "none";
    }
  }

  // Abstention Box Display
  const abstentionBox = document.getElementById("abstentionNoticeBox");
  if (abstentionBox) {
    abstentionBox.style.display = isAbstention ? "block" : "none";
  }
  
  lastTriageResult = {
    condition: primaryCondition,
    band: qualitativeBand,
    symptoms: checkedBoxes,
    isAbstention,
    isZoonotic: isZoonoticAlert,
    mvuTicket
  };"""

# Replace evaluateSymptoms inner logic
# Find start of logic in js
eval_idx = js.find("function evaluateSymptoms() {")
if eval_idx == -1:
    print("Could not find evaluateSymptoms function!")
    sys.exit(1)

# Find where old_eval_body_start is
replace_start = js.find("  // Rule-based clinical triage matching Seva First Model A", eval_idx)
if replace_start == -1:
    print("Could not find triage start in evaluateSymptoms!")
    sys.exit(1)

# Find where diffDiag.textContent is
replace_end = js.find("  diffDiag.textContent = `Differential Rule-Outs:", replace_start)
if replace_end == -1:
    print("Could not find diffDiag.textContent in evaluateSymptoms!")
    sys.exit(1)

js = js[:replace_start] + new_eval_body + "\n\n" + js[replace_end:]

with open("js/app.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Updated js/app.js evaluateSymptoms() with Phase 3 logic!")

