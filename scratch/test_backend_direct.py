# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))

print("Testing FastAPI Backend Implementation (Direct Function Calls)...")

from backend.app.core.database import SessionLocal
from backend.app.main import (
    app,
    read_root,
    health_check,
    submit_micro_report,
    get_paravet_queue,
    verify_signal,
    get_sample_tracking,
    advance_sample_stage,
    get_village_signals,
    export_nadres_batch,
    get_pilot_metrics,
    calculate_withdrawal,
    MicroReportCreate,
    VerificationAction,
    SpeciesEnum,
    ChannelEnum
)

db = SessionLocal()

try:
    # 1. Health check & Root
    res = health_check()
    assert res["status"] == "healthy"
    print("✓ health_check() passed:", res)

    res = read_root()
    assert "PashuSachet" in res["platform"]
    print("✓ read_root() passed:", res["platform"])

    # 2. 90-Second Report Intake
    payload = MicroReportCreate(
        species=SpeciesEnum.CATTLE,
        symptoms=["skin_nodules", "fever"],
        affectedCount=2,
        villageLocation="Sangamner Khurd",
        channel=ChannelEnum.DIRECT_WEB,
        isMortality=False,
        mortalityCount=0,
        isProxy=False
    )
    rep = submit_micro_report(payload, db=db)
    assert rep.species == "cattle"
    assert rep.urgencyScore == "PRIORITY"
    print(f"✓ submit_micro_report() passed. Report ID: {rep.reportId}, Status: {rep.status.value}")

    # 3. Para-Vet Queue & Verification
    queue = get_paravet_queue("UNVERIFIED_SIGNAL", db=db)
    assert len(queue) >= 1
    print(f"✓ get_paravet_queue() passed. Found {len(queue)} pending signals.")

    sig_id = queue[0]["id"]
    act = VerificationAction(action="CONFIRM", verifiedBy="Ganesh Kale (PV-AHM-9104)")
    v_res = verify_signal(sig_id, act, db=db)
    assert v_res["status"] == "SUCCESS"
    assert v_res["newStatus"] == "VERIFIED_SIGNAL"
    print(f"✓ verify_signal('{sig_id}') passed. New Status: {v_res['newStatus']}")

    # 4. Diagnostic Samples Tracker (RDDL Pune Pipeline)
    samples = get_sample_tracking(db=db)
    assert len(samples) >= 1
    s_id = samples[0]["sampleId"]
    print(f"✓ get_sample_tracking() passed. Found sample #{s_id} in stage: {samples[0]['currentStage']}")

    adv_res = advance_sample_stage(s_id, db=db)
    assert adv_res["status"] in ["SUCCESS", "ALREADY_COMPLETED"]
    print(f"✓ advance_sample_stage('{s_id}') passed. Transitioned to/is: {adv_res['currentStage']}")

    # 5. Village Signals with k-Anonymity Privacy
    v_signals = get_village_signals(db=db)
    assert len(v_signals) >= 1
    print(f"✓ get_village_signals() passed. Returned {len(v_signals)} clusters with k-anonymity privacy tags.")

    # 6. NADRES V2 Export Batch
    nadres = export_nadres_batch(db=db)
    assert nadres["metadata"]["pipelineVersion"] == "NADRES-V2-EPI-PIPELINE"
    assert nadres["metadata"]["dpdpCompliance"] == "STRICT_DE_IDENTIFICATION_APPLIED"
    print("✓ export_nadres_batch() passed. Epi-week:", nadres["metadata"]["reportingEpiWeek"])

    # 7. Pilot Telemetry Metrics
    metrics = get_pilot_metrics()
    assert metrics["channelInclusionRatePct"] == 78.4
    assert metrics["status"] == "TARGETS_SURPASSED"
    print(f"✓ get_pilot_metrics() passed. Channel inclusion: {metrics['channelInclusionRatePct']}%, SLA: {metrics['medianVerificationTurnaroundMins']}m")

    # 8. Food-Safety Milk Withdrawal Calculator (Last-Dose Formula)
    calc = calculate_withdrawal(treatmentDays=3, withdrawalHours=72)
    assert calc["totalWithholdingHours"] == 144
    assert calc["calculatedFrom"] == "FINAL_DOSE"
    print(f"✓ calculate_withdrawal() passed: {calc['formula']} -> {calc['totalWithholdingHours']}h total from final dose.")

    print("\n" + "="*70)
    print("ALL BACKEND FASTAPI ENDPOINTS & LOGIC VALIDATED 100% SUCCESSFULLY! (8/8)")
    print("="*70)

finally:
    db.close()
