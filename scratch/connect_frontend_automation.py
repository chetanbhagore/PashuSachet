# -*- coding: utf-8 -*-
"""
Connect frontend JavaScript (app.js) to the live Multichannel Automation APIs:
/api/v1/whatsapp/webhook and /api/v1/telephony/missed-call & outbreak-broadcast.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update simulateMissedCallCallback to ping live backend API
old_missed_call = '''function simulateMissedCallCallback() {
  const statusEl = document.getElementById("ivrCallStatus");
  if (!statusEl) return;

  statusEl.innerHTML = `<span style="color:#d97706;">⏳ शेतकरी क्रमांक +91 98220 18491 कडून 1800-889-1962 वर १ रिंग दिली गेली... कॉल कट झाला.</span>`;

  setTimeout(() => {
    statusEl.innerHTML = `<span style="color:#2563eb;">📞 पशूसचेत सर्व्हरकडून त्वरित कॉल-बॅक! कॉल कनेक्ट झाला... मराठी IVR ऑडिओ सुरू आहे.</span>`;
    speakMarathiVoice("नमस्कार शेतकरी बंधू, पशूसचेत कॉल सहाय्यता केंद्रात आपले स्वागत आहे. तुमच्या जनावराची लक्षणे सांगा.");
  }, 1000);'''

new_missed_call = '''function simulateMissedCallCallback() {
  const statusEl = document.getElementById("ivrCallStatus");
  if (!statusEl) return;

  statusEl.innerHTML = `<span style="color:#d97706;">[टोल-फ्री १८००-८८९-१९६२] शेतकरी क्रमांक +91 98220 18491 कडून १ रिंग... कॉल कट झाला.</span>`;

  // Trigger backend telephony automation API
  if (typeof fetch !== 'undefined') {
    fetch('/api/v1/telephony/missed-call', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ caller_phone: '+919822018491', toll_free_number: '1800-889-1962' })
    }).catch(() => {});
  }

  setTimeout(() => {
    statusEl.innerHTML = `<span style="color:#2563eb;">[कॉल-बॅक जोडला] पशूसचेत ऑटोमेटेड कॉलिंग गेटवेकडून त्वरित कॉल-बॅक! २-Way मराठी IVR सुरू...</span>`;
    speakMarathiVoice("नमस्कार शेतकरी बंधू, पशूसचेत कॉल सहाय्यता केंद्रात आपले स्वागत आहे. तुमच्या जनावराची लक्षणे सांगा.");
  }, 1000);'''

if old_missed_call in js:
    js = js.replace(old_missed_call, new_missed_call)
    print("✓ Updated simulateMissedCallCallback to call backend telephony API")

# 2. Update sendWhatsAppUserText to connect to live /api/v1/whatsapp/webhook
old_wa_user = '''function sendWhatsAppUserText() {
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
}'''

new_wa_user = '''function sendWhatsAppUserText() {
  const input = document.getElementById("whatsappUserInput");
  if (!input || !input.value.trim()) return;

  const text = input.value.trim();
  appendWhatsAppBubble(text, 'outgoing');
  input.value = "";

  if (typeof fetch !== 'undefined') {
    fetch('/api/v1/whatsapp/webhook', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ from: '+919822018491', type: 'text', body: text })
    })
    .then(r => r.json())
    .then(data => {
      const reply = data && data.replyMessage ? data.replyMessage.replace(/\\n/g, '<br>') :
        '🙏 <strong>पशूसचेत महाराष्ट्र शासन:</strong><br>आपला संदेश नोंदवला आहे. १९६२ फिरते पथक संपर्कात आहे.';
      appendWhatsAppBubble(reply, 'incoming');
    })
    .catch(() => {
      let reply = `
        🙏 <strong>पशूसचेत महाराष्ट्र शासन:</strong><br>
        आपला संदेश नोंदवला आहे: "<em>${text}</em>".<br>
        १९६२ फिरते पथक आपल्या गावाच्या संपर्कात आहे. आपत्कालीन मदतीसाठी थेट १९६२ वर डायल करा.
      `;
      appendWhatsAppBubble(reply, 'incoming');
    });
  } else {
    setTimeout(() => {
      let reply = `
        🙏 <strong>पशूसचेत महाराष्ट्र शासन:</strong><br>
        आपला संदेश नोंदवला आहे: "<em>${text}</em>".<br>
        १९६२ फिरते पथक आपल्या गावाच्या संपर्कात आहे. आपत्कालीन मदतीसाठी थेट १९६२ वर डायल करा.
      `;
      appendWhatsAppBubble(reply, 'incoming');
    }, 800);
  }
}'''

if old_wa_user in js:
    js = js.replace(old_wa_user, new_wa_user)
    print("✓ Updated sendWhatsAppUserText to call backend WhatsApp webhook")

# 3. Update executeSmsBroadcast to also trigger /api/v1/telephony/outbreak-broadcast
old_sms_broadcast = '''function executeSmsBroadcast() {
  const pBarCont = document.getElementById("smsProgressBarContainer");
  const pBar = document.getElementById("smsProgressBar");
  const pPct = document.getElementById("smsProgressPercent");
  const btn = document.getElementById("btnSendSmsBlast");
  
  if (pBarCont) pBarCont.style.display = "block";
  if (btn) btn.disabled = true;

  let progress = 0;
  const interval = setInterval(() => {
    progress += 20;
    if (pBar) pBar.style.width = `${progress}%`;
    if (pPct) pPct.textContent = `${progress}%`;
    if (progress >= 100) {
      clearInterval(interval);
      setTimeout(() => {
        showToast(`✓ ${currentBroadcastCount} SMS यशस्वीरित्या पाठवले! (CDAC Gateway)`);
        closeVillageSmsModal();
        if (btn) btn.disabled = false;
        if (pBar) pBar.style.width = "0%";
      }, 500);
    }
  }, 120);
}'''

new_sms_broadcast = '''function executeSmsBroadcast() {
  const pBarCont = document.getElementById("smsProgressBarContainer");
  const pBar = document.getElementById("smsProgressBar");
  const pPct = document.getElementById("smsProgressPercent");
  const btn = document.getElementById("btnSendSmsBlast");
  
  if (pBarCont) pBarCont.style.display = "block";
  if (btn) btn.disabled = true;

  // Trigger backend OBD robo-call broadcast API
  if (typeof fetch !== 'undefined') {
    fetch('/api/v1/telephony/outbreak-broadcast', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        village_name: currentBroadcastVillage,
        disease_name: "Foot and Mouth Disease (FMD)",
        radius_km: 5.0,
        target_livestock_owners: currentBroadcastCount
      })
    }).catch(() => {});
  }

  let progress = 0;
  const interval = setInterval(() => {
    progress += 20;
    if (pBar) pBar.style.width = `${progress}%`;
    if (pPct) pPct.textContent = `${progress}%`;
    if (progress >= 100) {
      clearInterval(interval);
      setTimeout(() => {
        showToast(`✓ ${currentBroadcastCount} SMS व स्वयंचलित व्हॉइस रोबो-कॉल यशस्वीरित्या प्रसारित!`);
        closeVillageSmsModal();
        if (btn) btn.disabled = false;
        if (pBar) pBar.style.width = "0%";
      }, 500);
    }
  }, 120);
}'''

if old_sms_broadcast in js:
    js = js.replace(old_sms_broadcast, new_sms_broadcast)
    print("✓ Updated executeSmsBroadcast to trigger OBD outbreak broadcast API")

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Saved updated js/app.js")
