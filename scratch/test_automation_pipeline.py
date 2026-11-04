# -*- coding: utf-8 -*-
"""
Test Suite for WhatsApp & Telephony Automation Engine
"""
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
sys.stdout.reconfigure(encoding='utf-8')

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_automation_pipeline():
    print("Testing WhatsApp & Telephony Automation Pipeline...")

    # 1. Test Meta Webhook Verification GET
    res = client.get("/api/v1/whatsapp/webhook?hub.mode=subscribe&hub.challenge=CHALLENGE_CODE_12345&hub.verify_token=PASHUSACHET_GOVT_WHATSAPP_TOKEN_2026")
    assert res.status_code == 200, f"Meta GET handshake failed: {res.status_code}"
    assert "CHALLENGE_CODE_12345" in res.text
    print("  ✓ PASSED: Meta WhatsApp Webhook Handshake (GET)")

    # 2. Test WhatsApp Incoming Text Message
    res = client.post("/api/v1/whatsapp/webhook", json={
        "from": "+919822018491",
        "type": "text",
        "body": "माझ्या गाईला ताप आहे आणि लाळ गळत आहे"
    })
    assert res.status_code == 200, f"WhatsApp text failed: {res.text}"
    data = res.json()
    assert "FMD" in data["replyMessage"] or "लाळ्या" in data["replyMessage"] or "लक्षणे" in data["replyMessage"]
    print("  ✓ PASSED: WhatsApp Vernacular Text Message Intake")

    # 3. Test WhatsApp Incoming Voice Note (Simulated ASR)
    res = client.post("/api/v1/whatsapp/webhook", json={
        "from": "+919822018491",
        "type": "voice",
        "body": "व्हॉइस मेसेज"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["msgType"] == "voice_response"
    assert "triageResult" in data
    print("  ✓ PASSED: WhatsApp Vernacular Voice Note ASR + ML Triage")

    # 4. Test WhatsApp Photo Intake (Lesion Detection)
    res = client.post("/api/v1/whatsapp/webhook", json={
        "from": "+919822018491",
        "type": "image",
        "body": "गाठीचा फोटो"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["detectedDisease"] == "LSD"
    assert data["confidencePct"] > 80.0
    print("  ✓ PASSED: WhatsApp Lesion Photo AI Computer Vision Detection")

    # 5. Test WhatsApp Outbound Messaging
    res = client.post("/api/v1/whatsapp/send", json={
        "to": "+919822018491",
        "message": "तुमच्या गाईचे औषध सुरू झाले आहे. ७२ तास दूध डेअरीमध्ये घालू नये."
    })
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "SENT_VIA_META_CLOUD_API"
    print("  ✓ PASSED: Outbound Proactive WhatsApp Notification")

    # 6. Test 1800-889-1962 Missed Call Ingress
    res = client.post("/api/v1/telephony/missed-call", json={
        "caller_phone": "+919822018491",
        "toll_free_number": "1800-889-1962"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "CALLBACK_QUEUED"
    assert data["tollFreeNumber"] == "1800-889-1962"
    print("  ✓ PASSED: 1800-889-1962 Missed Call Ingress & Automated Callback Queue")

    # 7. Test Voice IVR TwiML / VoiceXML Callback Generation
    res = client.post("/api/v1/telephony/ivr/callback?From=%2B919822018491")
    assert res.status_code == 200
    assert "application/xml" in res.headers["content-type"]
    assert "<Response>" in res.text
    assert "<Gather" in res.text
    assert "Polly.Aditi" in res.text
    print("  ✓ PASSED: 2-Way Marathi Voice IVR TwiML/VoiceXML Response Generation")

    # 8. Test Voice IVR DTMF Keypad Gather
    res = client.post("/api/v1/telephony/ivr/gather", json={
        "Digits": "9",
        "From": "+919822018491"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["selection"] == "EMERGENCY_1962"
    assert data["action"] == "DISPATCH_MVU_ALERT"
    print("  ✓ PASSED: Voice IVR DTMF Keypad Triage Routing (Emergency 9)")

    # 9. Test Outbreak Broadcast OBD (Robo-Call Campaign)
    res = client.post("/api/v1/telephony/outbreak-broadcast", json={
        "village_name": "निमगाव जाळी (Nimgaon Jali)",
        "disease_name": "Foot and Mouth Disease (FMD)",
        "radius_km": 5.0,
        "target_livestock_owners": 480
    })
    assert res.status_code == 200
    data = res.json()
    assert data["targetVillage"] == "निमगाव जाळी (Nimgaon Jali)"
    assert data["totalLivestockOwners"] == 480
    assert data["telephonyStats"]["callsInitiated"] == 480
    assert data["telephonyStats"]["successRatePct"] == 88.0
    print("  ✓ PASSED: 5km Outbreak Robo-Call OBD Campaign Dispatch")

    print("\nALL 9 MULTICHANNEL AUTOMATION TESTS PASSED CLEANLY!")

if __name__ == "__main__":
    test_automation_pipeline()
