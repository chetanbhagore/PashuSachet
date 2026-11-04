const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log("=== COMPREHENSIVE PASHUSACHET FRONTEND RUNTIME AUDIT ===");

const htmlPath = path.join(__dirname, '..', 'index.html');
const jsPath = path.join(__dirname, '..', 'js', 'app.js');

const htmlContent = fs.readFileSync(htmlPath, 'utf8');
const jsContent = fs.readFileSync(jsPath, 'utf8');

// Parse HTML IDs and structure
const idRegex = /id=["']([^"']+)["']/g;
const validIds = new Set();
let match;
while ((match = idRegex.exec(htmlContent)) !== null) {
  validIds.add(match[1]);
}

console.log(`Loaded HTML with ${validIds.size} unique DOM IDs.`);

// Setup a robust DOM sandbox
const localStorageMock = {
  _store: {},
  getItem(k) { return this._store[k] || null; },
  setItem(k, v) { this._store[k] = String(v); },
  removeItem(k) { delete this._store[k]; },
  clear() { this._store = {}; }
};

const elementsMap = new Map();

function createElement(id, tag = 'div') {
  const elem = {
    id: id || '',
    tagName: tag.toUpperCase(),
    value: '',
    checked: false,
    textContent: '',
    innerHTML: '',
    style: {},
    className: '',
    classList: {
      _classes: new Set(),
      add(...cls) { cls.forEach(c => this._classes.add(c)); },
      remove(...cls) { cls.forEach(c => this._classes.delete(c)); },
      contains(c) { return this._classes.has(c); },
      toggle(c, force) {
        if (force === true) this._classes.add(c);
        else if (force === false) this._classes.delete(c);
        else if (this._classes.has(c)) this._classes.delete(c);
        else this._classes.add(c);
      }
    },
    children: [],
    attributes: {},
    getAttribute(attr) { return this.attributes[attr] || null; },
    setAttribute(attr, val) { this.attributes[attr] = String(val); },
    appendChild(child) {
      this.children.push(child);
      return child;
    },
    removeChild(child) {
      this.children = this.children.filter(c => c !== child);
      return child;
    },
    remove() {},
    addEventListener(evt, fn) {
      if (!this._listeners) this._listeners = {};
      if (!this._listeners[evt]) this._listeners[evt] = [];
      this._listeners[evt].push(fn);
    },
    dispatchEvent(evt) {
      const type = typeof evt === 'string' ? evt : evt.type;
      if (this._listeners && this._listeners[type]) {
        this._listeners[type].forEach(fn => fn(evt));
      }
    },
    scrollIntoView() {},
    click() {
      this.dispatchEvent({ type: 'click', target: this });
    },
    querySelector(sel) {
      return createElement();
    },
    querySelectorAll(sel) {
      return [createElement(), createElement()];
    },
    getContext() {
      return {
        clearRect() {},
        beginPath() {},
        moveTo() {},
        lineTo() {},
        setLineDash() {},
        arc() {},
        ellipse() {},
        fill() {},
        stroke() {},
        fillRect() {},
        strokeRect() {},
        fillText() {},
        measureText() { return { width: 50 }; },
        createRadialGradient() { return { addColorStop() {} }; },
        createLinearGradient() { return { addColorStop() {} }; },
        drawImage() {},
        getImageData(x, y, w, h) {
          return { data: new Uint8ClampedArray(w * h * 4) };
        },
        putImageData() {}
      };
    }
  };
  return elem;
}

validIds.forEach(id => {
  elementsMap.set(id, createElement(id));
});

const sandbox = {
  console: console,
  setTimeout: (fn, ms) => { fn(); return 1; },
  clearTimeout: () => {},
  setInterval: (fn, ms) => 1,
  clearInterval: () => {},
  localStorage: localStorageMock,
  AudioContext: function() {
    return {
      createOscillator() { return { connect() {}, start() {}, stop() {}, frequency: { setValueAtTime() {}, linearRampToValueAtTime() {} } }; },
      createGain() { return { connect() {}, gain: { setValueAtTime() {}, linearRampToValueAtTime() {} } }; },
      destination: {}
    };
  },
  webkitAudioContext: function() { return new sandbox.AudioContext(); },
  document: {
    getElementById(id) {
      if (!elementsMap.has(id)) {
        elementsMap.set(id, createElement(id));
      }
      return elementsMap.get(id);
    },
    querySelector(sel) {
      if (sel.startsWith('#')) return this.getElementById(sel.slice(1));
      return createElement();
    },
    querySelectorAll(sel) {
      return [createElement(), createElement()];
    },
    createElement(tag) {
      return createElement('', tag);
    },
    addEventListener(evt, fn) {
      if (!this._listeners) this._listeners = {};
      if (!this._listeners[evt]) this._listeners[evt] = [];
      this._listeners[evt].push(fn);
    },
    dispatchEvent(evt) {
      const type = typeof evt === 'string' ? evt : evt.type;
      if (this._listeners && this._listeners[type]) {
        this._listeners[type].forEach(fn => fn(evt));
      }
    }
  },
  window: {
    addEventListener(evt, fn) {},
    localStorage: localStorageMock,
    navigator: { onLine: true, mediaDevices: { getUserMedia: () => Promise.resolve({}) } }
  },
  navigator: { onLine: true, mediaDevices: { getUserMedia: () => Promise.resolve({}) } },
  alert: (msg) => {},
  confirm: (msg) => true,
  prompt: (msg) => '123'
};

sandbox.window.document = sandbox.document;
sandbox.global = sandbox;
sandbox.window.window = sandbox.window;

vm.createContext(sandbox);

// Execute app.js in sandbox
try {
  vm.runInContext(jsContent, sandbox);
  console.log("✓ app.js parsed and executed in sandbox successfully.");
} catch (e) {
  console.error("❌ Fatal error executing app.js:", e);
  process.exit(1);
}

// Trigger DOMContentLoaded
if (sandbox.document._listeners && sandbox.document._listeners['DOMContentLoaded']) {
  sandbox.document._listeners['DOMContentLoaded'].forEach(fn => fn());
  console.log("✓ DOMContentLoaded listeners triggered successfully.");
}

// Test All Real Interactive Features
const testSuite = [
  { name: '1. Persona: Shetkari (Farmer)', run: () => sandbox.activatePersona('farmer') },
  { name: '2. Persona: Pashu Sakhi (Para-Vet)', run: () => sandbox.activatePersona('paravet') },
  { name: '3. Persona: LDO Doctor (Vet)', run: () => sandbox.activatePersona('ldo') },
  { name: '4. Persona: District Collector', run: () => sandbox.activatePersona('collector') },
  { name: '5. Persona: State Epidemiologist (RDDL)', run: () => sandbox.activatePersona('rddl') },
  { name: '6. Species selection (cattle -> goat)', run: () => sandbox.syncSpecies('goat') },
  { name: '7. Toggle Symptom Val (fever, mouth_lesions)', run: () => { sandbox.toggleSymptomVal('fever'); sandbox.toggleSymptomVal('mouth_lesions'); } },
  { name: '8. AI Vision Lesion Detection (LSD)', run: () => sandbox.simulateVisionDetection('lsd') },
  { name: '9. AI Vision Lesion Detection (FMD)', run: () => sandbox.simulateVisionDetection('fmd') },
  { name: '10. AI Vision Lesion Detection (Mastitis)', run: () => sandbox.simulateVisionDetection('mastitis') },
  { name: '11. AI Vision Lesion Detection (Black Quarter)', run: () => sandbox.simulateVisionDetection('bq') },
  { name: '12. AI Vision Lesion Detection (PPR Goats)', run: () => sandbox.simulateVisionDetection('ppr') },
  { name: '13. AI Vision Lesion Detection (Babesiosis)', run: () => sandbox.simulateVisionDetection('babesiosis') },
  { name: '14. Thermal FLIR Mode Toggle', run: () => sandbox.toggleThermalMode() },
  { name: '15. Grad-CAM Mode Toggle', run: () => sandbox.toggleGradCamMode() },
  { name: '16. Transfer Vision to Triage Intake', run: () => sandbox.transferVisionToTriage() },
  { name: '17. Mortality Fields Toggle (Checked)', run: () => sandbox.toggleMortalityFields(true) },
  { name: '18. Proxy Reporting Fields Toggle (Checked)', run: () => sandbox.toggleProxyFields(true) },
  { name: '19. Missed Call Modal Open/Close', run: () => { sandbox.openMissedCallModal(); sandbox.closeMissedCallModal(); } },
  { name: '20. USSD Modal Open/Close', run: () => { sandbox.openUssdModal(); sandbox.closeUssdModal(); } },
  { name: '21. Voice IVR Modal Open/Close', run: () => { sandbox.openVoiceIvrModal(); sandbox.closeVoiceIvrModal(); } },
  { name: '22. Pashu Aadhar Modal Open/Close', run: () => { sandbox.openPashuAadharModal(); sandbox.closePashuAadharModal(); } },
  { name: '23. Emergency 1962 Modal Open/Close', run: () => { sandbox.openEmergencyModal(); sandbox.closeEmergencyModal(); } },
  { name: '24. Book Vet Modal For Animal & Vet', run: () => { sandbox.openBookModalForAnimal('Gauri', 'MH-24-9812'); sandbox.openBookModalForVet('Dr. Rameshwar Kute'); } },
  { name: '25. INAPH Pashu Aadhar Tag Lookup / Verify', run: () => {
    sandbox.document.getElementById('ndlmTagInput').value = '240019283741';
    sandbox.verifyNdlmTag();
  }},
  { name: '26. Para-Vet Confirm Signal', run: () => sandbox.confirmSignal(1) },
  { name: '27. Para-Vet Request Sample Kit', run: () => sandbox.requestSignalSample(1) },
  { name: '28. Para-Vet Dismiss Signal', run: () => sandbox.dismissSignal(2) },
  { name: '29. Advance Sample Tracker Phase', run: () => sandbox.advanceSampleStage('SMP-2026-041') },
  { name: '30. GIS Ring Vaccination Toggle', run: () => sandbox.toggleRingVaxRadius() },
  { name: '31. GIS Inspect Map Pin', run: () => sandbox.inspectMapPin('Rahata', 7, 'FMD', 'SURGE_CLUSTER') },
  { name: '32. SEIR Epidemiological Day Slider (Day 14)', run: () => sandbox.updateSeirDay(14) },
  { name: '33. MVU Siren Audio Playback', run: () => sandbox.playMvuSirenTone() },
  { name: '34. WhatsApp Chat Simulator Toggle', run: () => sandbox.toggleWhatsAppChat() },
  { name: '35. WhatsApp Quick Audio Message', run: () => sandbox.sendWhatsAppQuickMsg('voice') },
  { name: '36. WhatsApp Quick Photo Message', run: () => sandbox.sendWhatsAppQuickMsg('photo') },
  { name: '37. WhatsApp Quick Status Query', run: () => sandbox.sendWhatsAppQuickMsg('status') },
  { name: '38. Officer Decision Resolution (DEC-001)', run: () => sandbox.resolveOfficerDecision('DEC-001') },
  { name: '39. Officer Decision Resolution (DEC-002)', run: () => sandbox.resolveOfficerDecision('DEC-002') },
  { name: '40. Officer Decision Resolution (DEC-003)', run: () => sandbox.resolveOfficerDecision('DEC-003') },
  { name: '41. Prescribe Modal Open / Populate', run: () => sandbox.openPrescriptionModal('240019283741', 'Mastitis') },
  { name: '42. Prescribe Form Submit (Milk Withdrawal Calculation)', run: () => {
    sandbox.document.getElementById('rxDrug').value = 'oxytetracycline';
    sandbox.document.getElementById('rxDose').value = '10 ml IM';
    sandbox.document.getElementById('rxDays').value = '3';
    sandbox.document.getElementById('rxSpecies').value = 'cattle';
    sandbox.document.getElementById('rxAnimalTag').value = '240019283741';
    sandbox.document.getElementById('rxVetRegNo').value = 'MSVC/2012/03194';
    const prescribeForm = sandbox.document.getElementById('prescribeForm');
    prescribeForm.dispatchEvent({ type: 'submit', preventDefault() {} });
  }},
  { name: '43. NADRES V2 Batch Generation Export', run: () => sandbox.generateNadresExport() }
];

let passedCount = 0;
let failedCount = 0;

testSuite.forEach((t) => {
  try {
    t.run();
    console.log(`  ✓ PASSED: ${t.name}`);
    passedCount++;
  } catch (err) {
    console.error(`  ❌ FAILED: ${t.name} ->`, err.message);
    failedCount++;
  }
});

console.log("\n==================================================");
console.log(`TOTAL FEATURES AUDITED: ${testSuite.length}`);
console.log(`PASSED: ${passedCount}`);
console.log(`FAILED: ${failedCount}`);
console.log("==================================================");

if (failedCount > 0) {
  process.exit(1);
}
