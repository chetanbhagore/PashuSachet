# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))

print("Testing FastAPI Backend Implementation with TestClient & SQLite...")

from starlette.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

# 1. Health check & Root
res = client.get("/health")
assert res.status_code == 200, f"Health check failed: {res.text}"
print("✓ /health passed:", res.json())

res = client.get("/")
assert res.status_code == 200, f"Root endpoint failed: {res.text}"
print("✓ / root endpoint passed:", res.json()["platform"])

# 2. 90-Second Report Intake
payload = {
    "species": "cattle",
    "symptoms": ["skin_nodules", "fever"],
    "affectedCount": 2,
    "villageLocation": "Sangamner Khurd",
    "channel": "DIRECT_WEB",
    "isMortality": False,
    "mortalityCount": 0,
    "isProxy": False
}
res = client.post("/api/v1/reports/90s", json=payload)
assert res.status_code == 201, f"Report intake failed: {res.text}"
report_data = res.json()
print("✓ POST /api/v1/reports/90s passed. Report ID:", report_data["reportId"])

# 3. Para-Vet Queue & Verification
res = client.get("/api/v1/paravet/queue")
assert res.status_code == 200, f"Paravet queue failed: {res.text}"
queue = res.json()
print(f"✓ GET /api/v1/paravet/queue passed. {len(queue)} reports in queue.")

sig_id = queue[0]["id"]
verify_payload = {
    "action": "CONFIRM",
    "verifiedBy": "Ganesh Kale (PV-AHM-9104)"
}
res = client.post(f"/api/v1/paravet/verify/{sig_id}", json=verify_payload)
assert res.status_code == 200, f"Verify action failed: {res.text}"
print(f"✓ POST /api/v1/paravet/verify/{sig_id} passed. Status: {res.json()['newStatus']}")

# 4. Diagnostic Samples Tracker (RDDL Pune Pipeline)
res = client.get("/api/v1/samples/track")
assert res.status_code == 200, f"Sample track failed: {res.text}"
samples = res.json()
print(f"✓ GET /api/v1/samples/track passed. {len(samples)} samples tracked.")

sample_id = samples[0]["sampleId"]
res = client.post(f"/api/v1/samples/advance/{sample_id}")
assert res.status_code == 200, f"Advance sample failed: {res.text}"
print(f"✓ POST /api/v1/samples/advance/{sample_id} passed. Current stage: {res.json()['currentStage']}")

# 5. Village Signals with k-Anonymity
res = client.get("/api/v1/surveillance/village-signals")
assert res.status_code == 200, f"Village signals failed: {res.text}"
v_signals = res.json()
print(f"✓ GET /api/v1/surveillance/village-signals passed. {len(v_signals)} clusters returned.")

# 6. NADRES V2 Export Batch
res = client.get("/api/v1/surveillance/nadres-export")
assert res.status_code == 200, f"NADRES export failed: {res.text}"
nadres = res.json()
print(f"✓ GET /api/v1/surveillance/nadres-export passed. Epi-week: {nadres['metadata']['reportingEpiWeek']}")

# 7. Pilot Telemetry Metrics
res = client.get("/api/v1/telemetry/metrics")
assert res.status_code == 200, f"Telemetry metrics failed: {res.text}"
metrics = res.json()
print(f"✓ GET /api/v1/telemetry/metrics passed. Inclusion: {metrics['channelInclusionRatePct']}%, SLA: {metrics['medianVerificationTurnaroundMins']}m")

# 8. Food-Safety Milk Withdrawal Calculator (Last-Dose Formula)
rx_payload = {"treatmentDays": 3, "withdrawalHours": 72}
res = client.post("/api/v1/clinical/calculate-withdrawal", json=rx_payload)
assert res.status_code == 200, f"Withdrawal calc failed: {res.text}"
calc = res.json()
assert calc["totalWithholdingHours"] == 144, "Formula calculation mismatch!"
print(f"✓ POST /api/v1/clinical/calculate-withdrawal passed: {calc['formula']} -> {calc['totalWithholdingHours']}h total.")

# 9. ML Triage Engine Evaluation
triage_payload = {
    "species": "cattle",
    "symptoms": ["nodules", "high_fever"],
    "duration_days": 2,
    "rectal_temp_f": 104.2
}
res = client.post("/api/v1/triage/evaluate", json=triage_payload)
assert res.status_code == 200, f"Triage evaluate failed: {res.text}"
triage_res = res.json()
print(f"✓ POST /api/v1/triage/evaluate passed. Primary condition: {triage_res['primary_condition']['name_en'] if triage_res['primary_condition'] else 'None'}")

print("\n" + "="*70)
print("ALL BACKEND FASTAPI ENDPOINTS & SQLITE DB VALIDATED 100% SUCCESSFULLY! (9/9)")
print("="*70)
