# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath("."))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from starlette.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_vision_detect():
    print("Testing Vision Detection Endpoint (/api/v1/vision/detect)...")
    for hint in ["lsd", "fmd", "mastitis", "bq", "ppr", "babesiosis"]:
        resp = client.post("/api/v1/vision/detect", json={"condition_hint": hint, "species": "cattle"})
        assert resp.status_code == 200, f"Failed on {hint}: {resp.text}"
        data = resp.json()
        assert "primaryCondition" in data
        assert len(data["boundingBoxes"]) >= 1
        assert data["thermalInflammationIndexC"] >= 38.0
        assert len(data["differentialDiagnoses"]) >= 2
        assert len(data["keyBiomarkers"]) >= 2
        assert data["actionProtocolMr"] != ""
        print(f"  ✓ {hint.upper()}: {data['primaryCondition']} ({data['confidenceBand']}, {data['confidenceScorePct']}%)")

def test_seir_simulation():
    print("Testing SEIR Epidemiological Simulation (/api/v1/epidemiology/seir-simulation)...")
    # Day 0 baseline
    r0 = client.post("/api/v1/epidemiology/seir-simulation", json={"day": 0, "ring_vax": False})
    assert r0.status_code == 200
    d0 = r0.json()
    assert d0["rEffective"] == 2.45
    assert d0["compartments"]["infectious"] == 12

    # Day 14 with ring vaccination
    r14 = client.post("/api/v1/epidemiology/seir-simulation", json={"day": 14, "ring_vax": True})
    assert r14.status_code == 200
    d14 = r14.json()
    assert d14["rEffective"] < 1.0  # Epidemic suppressed
    assert d14["containmentEfficacyPct"] > 80.0
    print(f"  ✓ SEIR Outbreak suppressed: R_t dropped from {d0['rEffective']} to {d14['rEffective']} with {d14['containmentEfficacyPct']}% containment efficacy")

def test_mvu_telematics():
    print("Testing MVU Live Fleet Telematics (/api/v1/telematics/mvu-fleet)...")
    resp = client.get("/api/v1/telematics/mvu-fleet")
    assert resp.status_code == 200
    data = resp.json()
    assert data["vehicleReg"] == "MH-17-BV-1962"
    assert data["targetVillage"] == "Nimgaon Jali (Cluster Surge Zone)"
    assert 2.0 <= data["coldChainTelemetry"]["vaccineCarrierTempC"] <= 8.0
    print(f"  ✓ MVU #{data['vehicleReg']} en route to {data['targetVillage']} | Cold-Chain: {data['coldChainTelemetry']['vaccineCarrierTempC']}°C")

def test_whatsapp_bot():
    print("Testing WhatsApp Bot Simulation (/api/v1/whatsapp/webhook)...")
    # Voice note message
    resp_v = client.post("/api/v1/whatsapp/webhook", json={"type": "voice", "body": "गाठी आल्या आहेत"})
    assert resp_v.status_code == 200
    assert "लंपी" in resp_v.json()["replyMessage"]

    # Status check
    resp_s = client.post("/api/v1/whatsapp/webhook", json={"type": "text", "body": "माझ्या केसची स्थिती सांगा"})
    assert resp_s.status_code == 200
    assert "पडताळणी पूर्ण केली" in resp_s.json()["replyMessage"]
    print("  ✓ WhatsApp 2-way bot webhook successfully validated.")

if __name__ == "__main__":
    test_vision_detect()
    test_seir_simulation()
    test_mvu_telematics()
    test_whatsapp_bot()
    print("\n🎉 ALL SUPERCHARGED BACKEND ENDPOINTS VALIDATED CLEAN!")
