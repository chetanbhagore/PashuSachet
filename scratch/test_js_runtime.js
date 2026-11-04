// Comprehensive Node.js DOM Simulator to test js/app.js runtime
const fs = require('fs');

const htmlContent = fs.readFileSync('index.html', 'utf-8');

// Minimal mock DOM
class MockElement {
  constructor(tag, id = '') {
    this.tagName = tag.toUpperCase();
    this.id = id;
    this.className = '';
    const self = this;
    this.classList = {
      add: (c) => { self.className += ' ' + c; },
      remove: (c) => { self.className = self.className.replace(c, '').trim(); },
      contains: (c) => self.className.includes(c),
      toggle: (c) => {
        if (self.className.includes(c)) self.className = self.className.replace(c, '').trim();
        else self.className += ' ' + c;
      }
    };
    this.remove = () => {};
    this.style = {};
    this.attributes = {};
    this.children = [];
    this.innerHTML = '';
    this.textContent = '';
    this.value = '';
    this.checked = false;
    this.listeners = {};
  }
  setAttribute(k, v) { this.attributes[k] = v; }
  getAttribute(k) { return this.attributes[k] || null; }
  removeAttribute(k) { delete this.attributes[k]; }
  addEventListener(evt, fn) {
    if (!this.listeners[evt]) this.listeners[evt] = [];
    this.listeners[evt].push(fn);
  }
  removeEventListener(evt, fn) {
    if (this.listeners[evt]) {
      this.listeners[evt] = this.listeners[evt].filter(f => f !== fn);
    }
  }
  dispatchEvent(evt) {
    const list = this.listeners[evt.type] || [];
    list.forEach(fn => fn(evt));
  }
  appendChild(child) { this.children.push(child); }
  removeChild(child) { this.children = this.children.filter(c => c !== child); }
  querySelector(sel) { return null; }
  querySelectorAll(sel) { return []; }
  scrollIntoView() {}
  focus() {}
  reset() {}
  getContext() {
    return {
      clearRect: () => {},
      fillRect: () => {},
      strokeRect: () => {},
      beginPath: () => {},
      arc: () => {},
      fill: () => {},
      stroke: () => {},
      moveTo: () => {},
      lineTo: () => {},
      ellipse: () => {},
      fillText: () => {},
      createLinearGradient: () => ({ addColorStop: () => {} }),
      createRadialGradient: () => ({ addColorStop: () => {} }),
      getImageData: () => ({ data: new Uint8ClampedArray(640 * 320 * 4) }),
      putImageData: () => {},
      drawImage: () => {}
    };
  }
}

// Extract all IDs from HTML
const idRegex = /id=["']([^"']+)["']/g;
const domElements = {};
let match;
while ((match = idRegex.exec(htmlContent)) !== null) {
  const id = match[1];
  domElements[id] = new MockElement('div', id);
}

// Special inputs
if (domElements['onsetDays']) domElements['onsetDays'].value = '2';
if (domElements['tempInput']) domElements['tempInput'].value = '102.5';
if (domElements['affectedCount']) domElements['affectedCount'].value = '1';
if (domElements['villageLocation']) domElements['villageLocation'].value = 'Sangamner';

const mockDocument = {
  getElementById: (id) => domElements[id] || null,
  querySelector: (sel) => {
    if (sel.startsWith('#')) return domElements[sel.slice(1)] || null;
    return new MockElement('div');
  },
  querySelectorAll: (sel) => {
    if (sel === '.lang-btn') return [new MockElement('button'), new MockElement('button')];
    if (sel === '.dist-pill') return [new MockElement('div'), new MockElement('div')];
    if (sel === 'input[name="symptom"]') return [new MockElement('input'), new MockElement('input')];
    if (sel === 'input[name="species"]') return [new MockElement('input')];
    if (sel.includes('data-i18n')) return [new MockElement('span')];
    if (sel.includes('data-withdrawal-end')) return [];
    return [];
  },
  createElement: (tag) => new MockElement(tag),
  addEventListener: (evt, fn) => {
    if (evt === 'DOMContentLoaded') setTimeout(fn, 10);
  }
};

class MockAudioContext {
  constructor() { this.currentTime = 0; this.destination = {}; }
  createOscillator() {
    return {
      type: 'sine',
      frequency: { setValueAtTime: () => {}, linearRampToValueAtTime: () => {} },
      connect: () => {},
      start: () => {},
      stop: () => {}
    };
  }
  createGain() {
    return {
      gain: { setValueAtTime: () => {} },
      connect: () => {}
    };
  }
}

const mockWindow = {
  document: mockDocument,
  localStorage: {
    store: {},
    getItem: (k) => mockWindow.localStorage.store[k] || null,
    setItem: (k, v) => { mockWindow.localStorage.store[k] = v; },
    removeItem: (k) => { delete mockWindow.localStorage.store[k]; }
  },
  sessionStorage: {
    store: {},
    getItem: (k) => mockWindow.sessionStorage.store[k] || null,
    setItem: (k, v) => { mockWindow.sessionStorage.store[k] = v; },
    removeItem: (k) => { delete mockWindow.sessionStorage.store[k]; }
  },
  addEventListener: () => {},
  AudioContext: MockAudioContext,
  webkitAudioContext: MockAudioContext,
  speechSynthesis: {
    speak: () => {},
    getVoices: () => []
  },
  webkitSpeechRecognition: class {
    constructor() { this.lang = ''; }
    start() {}
    stop() {}
  },
  print: () => {}
};

mockDocument.body = new MockElement('body');
global.window = mockWindow;
global.document = mockDocument;
global.localStorage = mockWindow.localStorage;
global.sessionStorage = mockWindow.sessionStorage;
global.AudioContext = mockWindow.AudioContext;
global.webkitAudioContext = mockWindow.webkitAudioContext;
global.speechSynthesis = mockWindow.speechSynthesis;
global.SpeechSynthesisUtterance = class { constructor(t) { this.text = t; } };
global.requestAnimationFrame = (fn) => setTimeout(fn, 16);
global.alert = (msg) => console.log('ALERT:', msg);
global.prompt = () => '123456';
global.navigator = { mediaDevices: { getUserMedia: () => Promise.resolve({}) } };
global.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve({}) });

console.log("Loading js/app.js...");
try {
  const code = fs.readFileSync('js/app.js', 'utf-8');
  eval(code);
  console.log("✓ js/app.js evaluated without syntax or top-level execution errors!");
} catch (err) {
  console.error("✗ ERROR executing js/app.js:", err);
  process.exit(1);
}

// Test key functions
setTimeout(() => {
  console.log("\nTesting interactive handlers:");

  const tests = [
    ["switchRole('vet')", () => switchRole('vet')],
    ["switchRole('farmer')", () => switchRole('farmer')],
    ["activatePersona('farmer')", () => activatePersona('farmer')],
    ["activatePersona('paravet')", () => activatePersona('paravet')],
    ["activatePersona('ldo')", () => activatePersona('ldo')],
    ["activatePersona('collector')", () => activatePersona('collector')],
    ["activatePersona('rddl')", () => activatePersona('rddl')],
    ["openMissedCallModal()", () => openMissedCallModal()],
    ["closeMissedCallModal()", () => closeMissedCallModal()],
    ["openUssdModal()", () => openUssdModal()],
    ["closeUssdModal()", () => closeUssdModal()],
    ["openPashuAadharModal()", () => openPashuAadharModal()],
    ["closePashuAadharModal()", () => closePashuAadharModal()],
    ["toggleRingVaxRadius()", () => toggleRingVaxRadius()],
    ["inspectMapPin('Nimgaon Jali', 4, 'FMD', 'SURGE_CLUSTER')", () => inspectMapPin('Nimgaon Jali', 4, 'FMD', 'SURGE_CLUSTER')],
    ["simulateVisionDetection('lsd')", () => simulateVisionDetection('lsd')],
    ["simulateVisionDetection('fmd')", () => simulateVisionDetection('fmd')],
    ["simulateVisionDetection('mastitis')", () => simulateVisionDetection('mastitis')],
    ["simulateVisionDetection('bq')", () => simulateVisionDetection('bq')],
    ["simulateVisionDetection('ppr')", () => simulateVisionDetection('ppr')],
    ["simulateVisionDetection('babesiosis')", () => simulateVisionDetection('babesiosis')],
    ["toggleThermalMode()", () => toggleThermalMode()],
    ["toggleGradCamMode()", () => toggleGradCamMode()],
    ["transferVisionToTriage()", () => transferVisionToTriage()],
    ["updateSeirDay(7)", () => updateSeirDay(7)],
    ["playMvuSirenTone()", () => playMvuSirenTone()],
    ["toggleWhatsAppChat()", () => toggleWhatsAppChat()],
    ["sendWhatsAppQuickMsg('voice')", () => sendWhatsAppQuickMsg('voice')],
    ["sendWhatsAppQuickMsg('photo')", () => sendWhatsAppQuickMsg('photo')],
    ["sendWhatsAppQuickMsg('status')", () => sendWhatsAppQuickMsg('status')],
    ["quickLogin('farmer')", () => quickLogin('farmer')],
    ["quickLogin('paravet')", () => quickLogin('paravet')],
    ["quickLogin('vet')", () => quickLogin('vet')],
    ["quickLogin('officer')", () => quickLogin('officer')],
    ["quickLogin('admin')", () => quickLogin('admin')],
    ["logoutUser()", () => logoutUser()],
  ];

  let passed = 0;
  tests.forEach(([name, fn]) => {
    try {
      fn();
      console.log(`  ✓ ${name}`);
      passed++;
    } catch (e) {
      console.error(`  ✗ FAIL ${name}:`, e.message, e.stack);
    }
  });

  console.log(`\nPassed ${passed} / ${tests.length} interactive functions!`);
  if (passed === tests.length) {
    console.log("ALL INTERACTIVE FUNCTIONS PASSED CLEANLY IN DOM SIMULATOR!");
  }
  process.exit(passed === tests.length ? 0 : 1);
}, 50);
