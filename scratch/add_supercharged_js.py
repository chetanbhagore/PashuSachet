# -*- coding: utf-8 -*-
js_code_to_append = r"""

// ==========================================================================
// SUPERCHARGED EXTENSIONS: PERSONAS, VISION HUD, SEIR, MVU & WHATSAPP
// ==========================================================================

// 1. Multi-Role Live Persona Switcher
let currentPersona = 'farmer';

function activatePersona(role) {
  currentPersona = role;
  
  const pills = ['personaFarmer', 'personaParavet', 'personaLdo', 'personaCollector', 'personaRddl'];
  pills.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });
  
  const activePill = document.getElementById(
    role === 'farmer' ? 'personaFarmer' :
    role === 'paravet' ? 'personaParavet' :
    role === 'ldo' ? 'personaLdo' :
    role === 'collector' ? 'personaCollector' : 'personaRddl'
  );
  if (activePill) activePill.classList.add('active');

  const paravetNav = document.getElementById('paravetNavLink');
  const adminNav = document.getElementById('adminNavLink');

  if (role === 'farmer') {
    if (paravetNav) paravetNav.style.display = 'none';
    if (adminNav) adminNav.style.display = 'none';
    showToast('🧑‍🌾 शेतकरी मोड सक्रिय: जलद ९०-सेकंद तपासणी व पशू आधार उपलब्ध.');
    const el = document.getElementById('symptom-screening');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'paravet') {
    if (paravetNav) paravetNav.style.display = 'inline-block';
    showToast('🩺 पशु सखी / पॅरा-व्हेट मोड: <30 सेकंद पडताळणी रांग सक्रिय.');
    const el = document.getElementById('paravet-inbox');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'ldo') {
    if (paravetNav) paravetNav.style.display = 'inline-block';
    showToast('👨‍⚕️ पशुवैद्यकीय अधिकारी (LDO) मोड: क्लिनिकल तपासणी व औषधोपचार कक्ष.');
    const el = document.getElementById('vet-desk');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'collector') {
    if (adminNav) adminNav.style.display = 'inline-block';
    showToast('🏛️ जिल्हा नियंत्रण कक्ष मोड: ५ किमी प्रतिबंधात्मक झोन व प्रादुर्भाव नियंत्रण नकाशा.');
    if (!ringVaxActive) toggleRingVaxRadius();
    const el = document.getElementById('outbreak-gis');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  } else if (role === 'rddl') {
    showToast('🔬 राज्य रोग निदान प्रयोगशाळा (RDDL Pune) मोड: RT-PCR चाचणी व नमुना ट्रॅकिंग.');
    const el = document.getElementById('sample-tracker');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  }
}

// 2. Multi-Disease Computer Vision Sentinel Supercharge
let thermalModeActive = false;
let gradCamActive = false;
let currentDetectedCondition = 'lsd';
let liveCameraStream = null;

const visionDiseaseSpecs = {
  lsd: {
    name: 'Lumpy Skin Disease (Capripoxvirus)',
    band: 'Likely',
    score: 89.4,
    thermal: 39.8,
    urgency: 'RED_HIGH_CONTAGION',
    species: 'cattle',
    symptoms: ['skin_nodules', 'fever'],
    diffs: ['Pseudo-LSD (BHV-2)', 'Dermatophilosis', 'Insect Bites'],
    biomarkers: ['Circumscribed 2-5cm firm dermal nodules', 'Prescapular lymphadenopathy'],
    actionMr: 'बाधित जनावराला तात्काळ कळपापासून वेगळे करा (विलगीकरण). डास-माशा प्रतिबंधक औषध फवारा.',
    actionEn: 'Immediately isolate affected animal. Apply insect repellent. Call 1962.'
  },
  fmd: {
    name: 'Foot & Mouth Disease (Aphthovirus O/A/Asia-1)',
    band: 'Likely',
    score: 92.1,
    thermal: 40.5,
    urgency: 'RED_HIGH_CONTAGION',
    species: 'cattle',
    symptoms: ['mouth_lesions', 'salivation', 'fever', 'swelling_legs'],
    diffs: ['Vesicular Stomatitis', 'Bovine Viral Diarrhea (BVD)', 'Malignant Catarrhal Fever'],
    biomarkers: ['Ruptured vesicular ulcers on tongue/gums', 'Interdigital coronary erythema'],
    actionMr: 'तोंडातील फोडांवर पोटॅशियम परमँगनेट (KMnO4) हलके लावा. खूर कोरडी ठेवा. दूध उकळून नष्ट करा.',
    actionEn: 'Wash oral lesions with 0.1% KMnO4 solution. Disinfect hooves. Withhold milk.'
  },
  mastitis: {
    name: 'Acute Clinical Mastitis (Staph/Streptococcus)',
    band: 'Likely',
    score: 94.2,
    thermal: 41.2,
    urgency: 'AMBER_PARA_VET_VISIT',
    species: 'cattle',
    symptoms: ['drop_milk', 'fever'],
    diffs: ['Subclinical Mastitis Flare', 'Udder Hematoma', 'Teat Papilloma'],
    biomarkers: ['Severe asymmetrical udder hyperthermia', 'Fibrin clot strippings', 'Pain on palpation'],
    actionMr: 'वारंवार कास पूर्णपणे रिकामी करा (Frequent Stripping). थंड पाण्याचा शेक द्या. त्वरित डॉक्टरांना बोलवा.',
    actionEn: 'Perform frequent complete milk stripping. Apply cold compress. Administer intramammary therapy.'
  },
  bq: {
    name: 'Black Quarter (Clostridium chauvoei)',
    band: 'Possible',
    score: 78.5,
    thermal: 40.2,
    urgency: 'RED_EMERGENCY',
    species: 'cattle',
    symptoms: ['swelling_legs', 'fever'],
    diffs: ['Malignant Edema', 'Acute Anthrax', 'Snake Bite'],
    biomarkers: ['Emphysematous crepitating muscle swelling', 'Severe acute hindquarter lameness'],
    actionMr: 'तातडीची आणीबाणी! जनावराला अजिबात चालवू नका. शिरेतून पेनिसिलिन देण्यासाठी डॉक्टरांना तात्काळ बोलवा.',
    actionEn: 'Critical emergency! Do not move animal. Administer parenteral high-dose crystalline penicillin.'
  },
  ppr: {
    name: 'Peste des Petits Ruminants (Goat Plague)',
    band: 'Likely',
    score: 91.8,
    thermal: 40.7,
    urgency: 'RED_HIGH_CONTAGION',
    species: 'goat',
    symptoms: ['nasal_discharge', 'mouth_lesions', 'fever'],
    diffs: ['CCPP (Caprine Pleuropneumonia)', 'Goat Pox', 'Bluetongue'],
    biomarkers: ['Mucopurulent oculonasal crusting', 'Erosive necrotic stomatitis', 'Foul enteritis'],
    actionMr: 'बाधित शेळ्या-मेंढ्या त्वरित वेगळ्या करा. इलेक्ट्रोल पाणी पाजा. ५ किमी परिघातील शेळ्यांचे लसीकरण करा.',
    actionEn: 'Strictly quarantine sick goats. Provide oral electrolytes. Deploy urgent 5km ring vaccination.'
  },
  babesiosis: {
    name: 'Bovine Babesiosis / Redwater (Babesia bigemina)',
    band: 'Possible',
    score: 82.0,
    thermal: 40.9,
    urgency: 'AMBER_PARA_VET_VISIT',
    species: 'cattle',
    symptoms: ['fever'],
    diffs: ['Theileriosis', 'Anaplasmosis', 'Leptospirosis'],
    biomarkers: ['Boophilus microplus tick cluster', 'Coffee-colored redwater urine', 'Pale sclera'],
    actionMr: 'गोचीड निर्मूलन औषध (फ्ल्युमेथ्रिन) लावा. त्वरित पशुवैद्याकडून डिमिनाझिन इंजेक्शन टोचून घ्या.',
    actionEn: 'Apply topical acaricide immediately. Administer Diminazene Aceturate under veterinary care.'
  }
};

function simulateVisionDetection(cond) {
  currentDetectedCondition = cond || 'lsd';
  
  // Update Active Chip Button
  const chips = ['chipLsd', 'chipFmd', 'chipMastitis', 'chipBq', 'chipPpr', 'chipBabesiosis'];
  chips.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  });
  const mapChip = { lsd: 'chipLsd', fmd: 'chipFmd', mastitis: 'chipMastitis', bq: 'chipBq', ppr: 'chipPpr', babesiosis: 'chipBabesiosis' };
  const targetChip = document.getElementById(mapChip[cond]);
  if (targetChip) targetChip.classList.add('active');

  drawLesionOnCanvas(currentDetectedCondition);

  const spec = visionDiseaseSpecs[currentDetectedCondition] || visionDiseaseSpecs.lsd;
  const box = document.getElementById("visionOutputBox");
  const content = document.getElementById("visionResultContent");
  if (box && content) {
    box.style.display = "block";
    content.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
        <div>
          <strong style="font-size:1.05rem; color:#0f172a;">${spec.name}</strong>
          <div style="font-size:0.78rem; color:#64748b;">
            Pathological Visual Identification • Confidence Band: 
            <span style="background:#dcfce7; color:#166534; font-weight:800; padding:2px 6px; border-radius:4px;">${spec.band} (${spec.score}%)</span>
          </div>
        </div>
        <span style="background:#fee2e2; color:#991b1b; font-weight:800; font-size:0.75rem; padding:3px 8px; border-radius:4px;">
          ${spec.urgency}
        </span>
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-bottom:10px; font-size:0.82rem;">
        <div style="background:#f1f5f9; padding:8px 12px; border-radius:6px;">
          <strong style="color:#334155;">Key Visual Biomarkers:</strong>
          <ul style="margin:4px 0 0 16px; padding:0; color:#475569;">
            ${spec.biomarkers.map(b => `<li>${b}</li>`).join('')}
          </ul>
        </div>
        <div style="background:#f1f5f9; padding:8px 12px; border-radius:6px;">
          <strong style="color:#334155;">Differential Diagnoses:</strong>
          <ul style="margin:4px 0 0 16px; padding:0; color:#475569;">
            ${spec.diffs.map(d => `<li>${d}</li>`).join('')}
          </ul>
        </div>
      </div>

      <div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:6px; padding:8px 12px; font-size:0.82rem; color:#065f46;">
        <strong>तात्काळ कृती (Marathi):</strong> ${spec.actionMr}<br>
        <strong>Safe Protocol (English):</strong> ${spec.actionEn}
      </div>
    `;
  }

  showToast(`AI Clinical Vision: Identified signs of ${spec.name}`);
}

function drawLesionOnCanvas(cond, customImg) {
  const container = document.getElementById("visionCanvasContainer");
  const canvas = document.getElementById("visionCanvas");
  if (!container || !canvas) return;
  container.style.display = "block";
  const ctx = canvas.getContext("2d");
  const w = canvas.width;
  const h = canvas.height;

  ctx.clearRect(0, 0, w, h);

  if (customImg) {
    ctx.drawImage(customImg, 0, 0, w, h);
  } else {
    // Generate simulated high-fidelity skin/tissue backdrop
    const grad = ctx.createLinearGradient(0, 0, w, h);
    if (cond === 'mastitis') {
      grad.addColorStop(0, "#fbcfe8");
      grad.addColorStop(1, "#f472b6");
    } else if (cond === 'bq') {
      grad.addColorStop(0, "#475569");
      grad.addColorStop(1, "#1e293b");
    } else {
      grad.addColorStop(0, "#e2e8f0");
      grad.addColorStop(1, "#94a3b8");
    }
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Render pathological condition patterns
    if (cond === 'lsd') {
      // Circumscribed 2-5cm firm dermal nodules
      const nodules = [
        { x: 180, y: 120, r: 28 },
        { x: 310, y: 160, r: 36 },
        { x: 440, y: 110, r: 24 },
        { x: 250, y: 220, r: 30 }
      ];
      nodules.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fillStyle = "#7f1d1d";
        ctx.fill();
        ctx.lineWidth = 3;
        ctx.strokeStyle = "#ef4444";
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r * 0.45, 0, Math.PI * 2);
        ctx.fillStyle = "#450a0a";
        ctx.fill();
      });
    } else if (cond === 'fmd') {
      // Vesicular erosions on mucosal border
      ctx.fillStyle = "#b91c1c";
      ctx.beginPath();
      ctx.ellipse(320, 160, 85, 45, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.lineWidth = 4;
      ctx.strokeStyle = "#f87171";
      ctx.stroke();

      // Sloughed mucosal blisters
      for (let i = 0; i < 7; i++) {
        ctx.beginPath();
        ctx.arc(280 + i * 14, 155 + (i % 2) * 8, 7, 0, Math.PI * 2);
        ctx.fillStyle = "#fef08a";
        ctx.fill();
      }
    } else if (cond === 'mastitis') {
      // Udder asymmetric hyperthermia and swelling
      ctx.fillStyle = "#e11d48";
      ctx.beginPath();
      ctx.ellipse(300, 180, 110, 80, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#f43f5e";
      ctx.lineWidth = 5;
      ctx.stroke();
    } else if (cond === 'bq') {
      // Emphysematous crepitating swelling
      ctx.fillStyle = "#0f172a";
      ctx.beginPath();
      ctx.ellipse(320, 160, 120, 70, 0.2, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#dc2626";
      ctx.lineWidth = 3;
      ctx.stroke();
    } else if (cond === 'ppr') {
      // Oculonasal erosions and discharge
      ctx.fillStyle = "#7c2d12";
      ctx.beginPath();
      ctx.ellipse(310, 140, 75, 40, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ea580c";
      ctx.lineWidth = 3;
      ctx.stroke();
    } else if (cond === 'babesiosis') {
      // Tick cluster
      for (let i = 0; i < 15; i++) {
        ctx.beginPath();
        ctx.arc(250 + (i % 5) * 22, 120 + Math.floor(i / 5) * 25, 6, 0, Math.PI * 2);
        ctx.fillStyle = "#1e293b";
        ctx.fill();
        ctx.strokeStyle = "#f59e0b";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }
  }

  // Thermal Infrared FLIR Shader Overlay (if toggled)
  if (thermalModeActive) {
    const imgData = ctx.getImageData(0, 0, w, h);
    const d = imgData.data;
    for (let i = 0; i < d.length; i += 4) {
      const avg = (d[i] + d[i+1] + d[i+2]) / 3;
      if (avg > 180) { // White hot
        d[i] = 255; d[i+1] = 255; d[i+2] = 220;
      } else if (avg > 130) { // Yellow/Orange
        d[i] = 255; d[i+1] = 160; d[i+2] = 20;
      } else if (avg > 80) { // Red hot
        d[i] = 220; d[i+1] = 30; d[i+2] = 30;
      } else { // Purple/Blue background
        d[i] = 50; d[i+1] = 10; d[i+2] = 90;
      }
    }
    ctx.putImageData(imgData, 0, 0);
  }

  // Grad-CAM Attention Heatmap (if toggled)
  if (gradCamActive) {
    const gcam = ctx.createRadialGradient(310, 160, 15, 310, 160, 130);
    gcam.addColorStop(0, "rgba(239, 68, 68, 0.75)");
    gcam.addColorStop(0.4, "rgba(245, 158, 11, 0.5)");
    gcam.addColorStop(0.8, "rgba(59, 130, 246, 0.25)");
    gcam.addColorStop(1, "rgba(0, 0, 0, 0)");
    ctx.fillStyle = gcam;
    ctx.fillRect(0, 0, w, h);
  }

  // Bounding Box HUD Overlays
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 2.5;
  ctx.strokeRect(200, 75, 230, 160);

  // Corner Bracket Reticles
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 4;
  const corners = [
    [200, 75, 15, 0, 0, 15],
    [430, 75, -15, 0, 0, 15],
    [200, 235, 15, 0, 0, -15],
    [430, 235, -15, 0, 0, -15]
  ];
  corners.forEach(([x, y, dx1, dy1, dx2, dy2]) => {
    ctx.beginPath();
    ctx.moveTo(x + dx1, y + dy1);
    ctx.lineTo(x, y);
    ctx.lineTo(x + dx2, y + dy2);
    ctx.stroke();
  });

  // Label tag above box
  ctx.fillStyle = "#38bdf8";
  ctx.fillRect(200, 52, 190, 22);
  ctx.fillStyle = "#020617";
  ctx.font = "bold 11px monospace";
  const spec = visionDiseaseSpecs[cond] || visionDiseaseSpecs.lsd;
  ctx.fillText(`DETECT: ${cond.toUpperCase()} (${spec.score}%)`, 206, 67);

  // Update HUD text
  const hudStatus = document.getElementById("hudStatus");
  const hudMetrics = document.getElementById("hudLesionMetrics");
  if (hudStatus) {
    hudStatus.innerHTML = `TARGET: <span style="color:#38bdf8;">${cond.toUpperCase()}</span> | FLIR: ${thermalModeActive ? 'ON' : 'OFF'} | GRAD-CAM: ${gradCamActive ? 'ON' : 'OFF'}`;
  }
  if (hudMetrics) {
    hudMetrics.innerHTML = `TEMP: ${spec.thermal}°C | CONF: ${spec.band}`;
  }
}

function toggleThermalMode() {
  thermalModeActive = !thermalModeActive;
  const btn = document.getElementById("thermalToggleBtn");
  if (btn) {
    if (thermalModeActive) {
      btn.classList.add("thermal-active");
      btn.innerHTML = "✓ FLIR Thermal: ON";
    } else {
      btn.classList.remove("thermal-active");
      btn.innerHTML = "🌡️ FLIR Thermal Heatmap";
    }
  }
  drawLesionOnCanvas(currentDetectedCondition);
  showToast(thermalModeActive ? "FLIR Thermal Infrared Overlay Enabled" : "Thermal Overlay Disabled");
}

function toggleGradCamMode() {
  gradCamActive = !gradCamActive;
  const btn = document.getElementById("gradCamToggleBtn");
  if (btn) {
    if (gradCamActive) {
      btn.classList.add("active");
      btn.innerHTML = "✓ Grad-CAM: ON";
    } else {
      btn.classList.remove("active");
      btn.innerHTML = "🧠 Grad-CAM Attention";
    }
  }
  drawLesionOnCanvas(currentDetectedCondition);
  showToast(gradCamActive ? "Grad-CAM CNN Attention Heatmap Enabled" : "Grad-CAM Disabled");
}

function toggleLiveCameraFeed() {
  const video = document.getElementById("visionVideoFeed");
  const btn = document.getElementById("liveCameraBtn");
  if (!video || !btn) return;

  if (liveCameraStream) {
    liveCameraStream.getTracks().forEach(t => t.stop());
    liveCameraStream = null;
    video.pause();
    btn.classList.remove("active");
    btn.innerHTML = "📹 Open Live Camera";
    drawLesionOnCanvas(currentDetectedCondition);
    showToast("Live camera feed stopped.");
    return;
  }

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
      .then(stream => {
        liveCameraStream = stream;
        video.srcObject = stream;
        video.play();
        btn.classList.add("active");
        btn.innerHTML = "⏹️ Stop Camera";
        showToast("Live Camera stream connected. Frame-by-frame lesion inspection active!");

        const container = document.getElementById("visionCanvasContainer");
        const canvas = document.getElementById("visionCanvas");
        if (container) container.style.display = "block";
        const ctx = canvas.getContext("2d");

        function renderFrame() {
          if (!liveCameraStream) return;
          if (video.readyState === video.HAVE_ENOUGH_DATA) {
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            // Draw real-time HUD bounding box over live frame
            ctx.strokeStyle = "#38bdf8";
            ctx.lineWidth = 2.5;
            ctx.strokeRect(200, 75, 230, 160);
            ctx.fillStyle = "#38bdf8";
            ctx.fillRect(200, 52, 190, 22);
            ctx.fillStyle = "#020617";
            ctx.font = "bold 11px monospace";
            ctx.fillText("LIVE SCAN: ACTIVE", 206, 67);
          }
          requestAnimationFrame(renderFrame);
        }
        requestAnimationFrame(renderFrame);
      })
      .catch(err => {
        console.warn("Camera access unavailable in environment:", err);
        showToast("Webcam unavailable in this sandbox environment. Simulating high-res field photo.");
        drawLesionOnCanvas(currentDetectedCondition);
      });
  } else {
    showToast("Webcam API not supported in this browser.");
  }
}

function transferVisionToTriage() {
  const spec = visionDiseaseSpecs[currentDetectedCondition] || visionDiseaseSpecs.lsd;
  
  // Set species
  const speciesInputs = document.querySelectorAll('input[name="species"]');
  speciesInputs.forEach(inp => {
    if (inp.value === spec.species) inp.checked = true;
  });

  // Check corresponding symptoms
  spec.symptoms.forEach(sym => {
    toggleSymptomCheckbox(sym, true);
  });

  // Fill Voice/Form notes
  const notes = document.getElementById("farmerVoiceNotes");
  if (notes) {
    notes.value = `[AI Vision Detection]: ${spec.name} detected with ${spec.band} confidence (${spec.score}%). Observed signs: ${spec.biomarkers.join(', ')}.`;
  }

  // Smooth scroll to submit button
  const submitBtn = document.getElementById("triageSubmitBtn") || document.querySelector("#symptom-screening button[type='submit']");
  if (submitBtn) {
    submitBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
    submitBtn.style.boxShadow = "0 0 16px rgba(22, 163, 74, 0.8)";
    setTimeout(() => { submitBtn.style.boxShadow = ""; }, 2500);
  }

  showToast(`✓ AI Vision findings for ${spec.name} transferred to 90-Second Intake!`);
}

// 3. Dynamic SEIR Outbreak Simulation
let seirPlayInterval = null;
let currentSeirDay = 0;

function updateSeirDay(dayVal) {
  currentSeirDay = parseInt(dayVal, 10);
  const lbl = document.getElementById("seirDayLabel");
  if (lbl) lbl.textContent = `Day ${currentSeirDay}`;

  // Mathematical SEIR Progression Model
  const isRingActive = ringVaxActive;
  let rt = isRingActive ? Math.max(0.65, 2.45 - (currentSeirDay * 0.13)) : 2.45;
  let inf = isRingActive ? 
    Math.round(12 + Math.max(0, currentSeirDay * 12 - (currentSeirDay > 3 ? (currentSeirDay - 3) * 14 : 0))) : 
    Math.round(12 * Math.pow(1.35, currentSeirDay));
  let vax = isRingActive ? Math.min(8400, currentSeirDay * 600) : 0;
  let eff = isRingActive ? Math.min(94.2, 4.5 + (currentSeirDay * 6.5)) : 4.5;

  const rtEl = document.getElementById("seirRtVal");
  const infEl = document.getElementById("seirInfVal");
  const vaxEl = document.getElementById("seirVaxVal");
  const effEl = document.getElementById("seirEfficacyVal");

  if (rtEl) {
    rtEl.textContent = rt.toFixed(2);
    rtEl.style.color = rt < 1.0 ? '#22c55e' : '#ef4444';
  }
  if (infEl) infEl.textContent = inf.toLocaleString();
  if (vaxEl) vaxEl.textContent = vax.toLocaleString();
  if (effEl) effEl.textContent = `${eff.toFixed(1)}%`;

  // Scale SVG outbreak radius on map
  const gisSvg = document.getElementById("gisSvgMap");
  if (gisSvg) {
    const nimgaonPulse = gisSvg.querySelector('circle[fill="#dc2626"]');
    if (nimgaonPulse) {
      const baseR = 8;
      const growthFactor = isRingActive ? Math.min(1.4, 1 + currentSeirDay * 0.03) : (1 + currentSeirDay * 0.09);
      nimgaonPulse.setAttribute('r', (baseR * growthFactor).toString());
    }
  }
}

function toggleSeirPlay() {
  const btn = document.getElementById("playSeirBtn");
  const slider = document.getElementById("seirDaySlider");

  if (seirPlayInterval) {
    clearInterval(seirPlayInterval);
    seirPlayInterval = null;
    if (btn) btn.innerHTML = "▶️ Run 14-Day Simulation";
    return;
  }

  currentSeirDay = 0;
  if (slider) slider.value = 0;
  updateSeirDay(0);
  if (btn) btn.innerHTML = "⏸️ Pause Simulation";

  seirPlayInterval = setInterval(() => {
    currentSeirDay++;
    if (currentSeirDay > 14) {
      clearInterval(seirPlayInterval);
      seirPlayInterval = null;
      if (btn) btn.innerHTML = "🔄 Replay Simulation";
      showToast("14-Day SEIR Outbreak Simulation Completed!");
      return;
    }
    if (slider) slider.value = currentSeirDay;
    updateSeirDay(currentSeirDay);
  }, 600);
}

// 4. 1962 MVU Audio Siren Synthesizer (Web Audio API)
function playMvuSirenTone() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = "sawtooth";
    gain.gain.setValueAtTime(0.12, ctx.currentTime);

    // Dual-frequency European/Indian emergency horn sweep
    const now = ctx.currentTime;
    for (let i = 0; i < 4; i++) {
      osc.frequency.setValueAtTime(700, now + i * 0.5);
      osc.frequency.linearRampToValueAtTime(950, now + i * 0.5 + 0.25);
      osc.frequency.linearRampToValueAtTime(700, now + i * 0.5 + 0.5);
    }

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start(now);
    osc.stop(now + 2.0);
    showToast("🚨 1962 MVU Emergency Vehicle Siren Triggered!");
  } catch (e) {
    console.warn("Web Audio not permitted:", e);
    showToast("🚨 1962 MVU Emergency Siren Active (Audio Muted)");
  }
}

// 5. Official 1962 WhatsApp Chatbot Simulator
function toggleWhatsAppChat() {
  const drawer = document.getElementById("whatsappDrawer");
  if (drawer) {
    drawer.classList.toggle("active");
  }
}

function sendWhatsAppQuickMsg(type) {
  const list = document.getElementById("whatsappMessagesList");
  if (!list) return;

  let userText = "";
  let botReply = "";

  if (type === 'voice') {
    userText = "🎙️ व्हॉइस मेसेज (०:१२): 'माझ्या गाईच्या अंगावर मोठ्या गाठी आल्या आहेत, ताप खूप आहे.'";
    botReply = `
      🙏 <strong>पशूसचेत १९६२ सहाय्यता केंद्र</strong><br>
      तुमचा व्हॉइस मेसेज प्राप्त झाला. प्राथमिक विश्लेषण:<br>
      ⚠️ <strong>संशयित रोग:</strong> लंपी त्वचा रोग (LSD - RED TIER)<br>
      👉 बाधित जनावराला कळपापासून वेगळे बांधा. संगमनेर फिरत्या पशुवैद्यकीय पथकाला (MVU 1962) अलर्ट पाठवला आहे.
    `;
  } else if (type === 'photo') {
    userText = "📷 फोटो पाठवला: nodule_lesion.jpg";
    botReply = `
      🔍 <strong>फोटो विश्लेषण पूर्ण:</strong><br>
      गाठींचा आकार २-४ सेमी असून लंपी रोगाची लक्षणे स्पष्ट दिसत आहेत.<br>
      ⏱️ डॉ. प्रदीप देशमुख (CVD संगमनेर) यांना सूचित केले आहे.
    `;
  } else if (type === 'status') {
    userText = "📋 केस स्टेटस: निमगाव जाळी अहवाल #SIG-9102";
    botReply = `
      📋 <strong>केस सद्यस्थिती:</strong><br>
      • स्थिती: ✅ पॅरा-व्हेट गणेश काळे यांनी पडताळणी केली.<br>
      • नमुना: #SAM-2026-AHM-0081 (RDDL पुणे लॅबमध्ये)<br>
      • कारवाई: ५ किमी परिसरात रिंग लसीकरण सुरू.
    `;
  }

  appendWhatsAppBubble(userText, 'outgoing');
  setTimeout(() => {
    appendWhatsAppBubble(botReply, 'incoming');
  }, 700);
}

function sendWhatsAppUserText() {
  const input = document.getElementById("whatsappUserInput");
  if (!input || !input.value.trim()) return;

  const text = input.value.trim();
  appendWhatsAppBubble(text, 'outgoing');
  input.value = "";

  setTimeout(() => {
    let reply = `
      🙏 <strong>पशूसचेत महाराष्ट्र शासन:</strong><br>
      आपला संदेश नोंदवला आहे: "<em>${text}</em>".<br>
      १९६२ फिरते पथक आपल्या गावाच्या संपर्कात आहे. आपत्कालीन मदतीसाठी थेट १९६२ वर डायल करा.
    `;
    appendWhatsAppBubble(reply, 'incoming');
  }, 800);
}

function appendWhatsAppBubble(content, direction) {
  const list = document.getElementById("whatsappMessagesList");
  if (!list) return;

  const now = new Date();
  const timeStr = `${now.getHours()}:${String(now.getMinutes()).padStart(2, '0')}`;

  const msgDiv = document.createElement("div");
  msgDiv.className = `whatsapp-msg ${direction}`;
  msgDiv.innerHTML = `
    <div>${content}</div>
    <div class="whatsapp-time">${timeStr}</div>
  `;
  list.appendChild(msgDiv);
  list.scrollTop = list.scrollHeight;
}
"""

with open('js/app.js', 'a', encoding='utf-8') as f:
    f.write(js_code_to_append)

print("js/app.js successfully updated with supercharged features.")

