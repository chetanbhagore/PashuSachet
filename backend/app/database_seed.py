# -*- coding: utf-8 -*-
"""
PashuSachet Database Initialization & Demonstration Seeder
Seeds SQLite pashusachet.db with authentic rural Maharashtra livestock records.
"""
import sys, os
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.abspath("."))

from backend.app.core.database import engine, SessionLocal, init_db
from backend.app.models import (
    User, ProfileFarmer, ProfileVet, ProfileOfficer,
    Animal, VaccinationRecord, Prescription,
    VillageSignal, ParaVetVerification, SampleTracking, MvuDispatchTicket,
    OutbreakCluster, AuditLog
)

def seed_database():
    print("Initializing database schema...")
    init_db()
    
    db = SessionLocal()
    try:
        # Check if already seeded
        if db.query(Animal).first():
            print("Database already contains records. Skipping duplicate seeding.")
            return

        print("Seeding initial authentic demonstration records...")
        
        # 1. Registered Animals
        now = datetime.now(timezone.utc)
        gauri = Animal(
            pashu_tag="MH-24-9812",
            name="Gauri",
            species="Cattle (गाय)",
            breed="Gir Crossbred",
            age_years=3.5,
            sex="Female (Lactating)",
            village="Sangamner Khurd",
            taluka="Sangamner",
            district="Ahmednagar",
            owner_name="Ganesh Patil",
            owner_phone="+919822018491",
            is_insured=True,
            notes="Second lactation cow, average daily yield 14L. Milking twice daily."
        )
        raja = Animal(
            pashu_tag="MH-12-4401",
            name="Raja",
            species="Buffalo (म्हैस)",
            breed="Murrah",
            age_years=4.0,
            sex="Female (Lactating)",
            village="Nimgaon Jali",
            taluka="Sangamner",
            district="Ahmednagar",
            owner_name="Babanrao Vikhe",
            owner_phone="+919422219043",
            is_insured=True,
            notes="High-yield Murrah buffalo. Daily yield 16L."
        )
        chotu = Animal(
            pashu_tag="MH-18-3310",
            name="Chotu",
            species="Goat (शेळी)",
            breed="Osmanabadi",
            age_years=1.5,
            sex="Male",
            village="Ashwi",
            taluka="Sangamner",
            district="Ahmednagar",
            owner_name="Tukaram Shinde",
            owner_phone="+919822041092",
            is_insured=False,
            notes="Breeding buck. Healthy body conformation."
        )
        db.add_all([gauri, raja, chotu])
        db.flush()

        # 2. Vaccinations
        vax1 = VaccinationRecord(
            animal_id=gauri.id,
            disease="FMD (लाळ-खुरकूत)",
            vaccine_name="Raksha-Ovac Trivalent",
            batch_no="FMD-MH-8812",
            administered_at=now - timedelta(days=90),
            next_due_date=now + timedelta(days=90),
            administered_by="Dr. Rameshwar Kute (LDO)"
        )
        vax2 = VaccinationRecord(
            animal_id=gauri.id,
            disease="LSD (लम्पी त्वचा रोग)",
            vaccine_name="Goat Pox Vaccine (Uttarkashi Strain)",
            batch_no="GPV-2025-09",
            administered_at=now - timedelta(days=120),
            next_due_date=now + timedelta(days=245),
            administered_by="Dr. Rameshwar Kute (LDO)"
        )
        db.add_all([vax1, vax2])

        # 3. Active Clinical Prescription (With Milk Withdrawal)
        # Treatment: 3 days (72h) + Withdrawal Buffer: 72h = 144h total from prescription date
        rx = Prescription(
            animal_id=gauri.id,
            animal_tag="MH-24-9812",
            diagnosis="Acute Bovine Mastitis (Udder Swelling)",
            drug_name="Ceftiofur Sodium 500mg + Flunixin Meglumine",
            route="Intramammary Infusion + IM",
            treatment_days=3,
            withdrawal_hours=72,
            prescribed_at=now - timedelta(hours=18),
            withdrawal_end_time=now - timedelta(hours=18) + timedelta(hours=144),
            vet_name="Dr. Rameshwar Kute, B.V.Sc & A.H.",
            vet_msvc_no="MSVC/2012/03194",
            is_milk_withholding_active=True
        )
        db.add(rx)

        # 4. Village Signals
        sig1 = VillageSignal(
            channel="USSD",
            species="Cattle (गाय)",
            symptoms='["Blisters in mouth / Salivation", "Lameness"]',
            affected_count=3,
            village="Nimgaon Jali",
            taluka="Sangamner",
            district="Ahmednagar",
            status="VERIFIED_SIGNAL",
            urgency_level="CRITICAL",
            reporter_name="Kisan Gaikwad",
            t0_reported_at=now - timedelta(hours=3),
            t1_verified_at=now - timedelta(hours=2),
            verified_by="Ganesh Kale (PV-AHM-9104)",
            vitals_note="Temp 104.5°F measured"
        )
        sig2 = VillageSignal(
            channel="VOICE_IVR",
            species="Cattle (गाय)",
            symptoms='["Skin nodules / Lumps", "High Fever"]',
            affected_count=2,
            village="Ashwi",
            taluka="Sangamner",
            district="Ahmednagar",
            status="UNVERIFIED_SIGNAL",
            urgency_level="URGENT",
            reporter_name="Babanrao Vikhe",
            t0_reported_at=now - timedelta(minutes=40)
        )
        sig3 = VillageSignal(
            channel="DIRECT_WEB",
            species="Goat (शेळी)",
            symptoms='["Sudden Weakness / Collapse"]',
            affected_count=2,
            village="Kotul",
            taluka="Akole",
            district="Ahmednagar",
            is_mortality=True,
            mortality_count=2,
            status="UNVERIFIED_SIGNAL",
            urgency_level="CRITICAL",
            reporter_name="Santosh Deshmukh",
            t0_reported_at=now - timedelta(minutes=20)
        )
        db.add_all([sig1, sig2, sig3])
        db.flush()

        # 5. Diagnostic Samples (RDDL Pune Pipeline)
        sample1 = SampleTracking(
            signal_id=sig1.id,
            sample_barcode="SMP-PUN-8104",
            animal_tag="MH-24-9812",
            sample_type="Vesicular Swab & Serum in VTM",
            disease_suspected="Foot and Mouth Disease (FMD)",
            current_stage="IN_TRANSIT_LAB",
            cold_chain_status="Maintained 2°C - 8°C in Ice Gel Shipper #CS-441",
            destination_lab="Regional Disease Diagnostic Laboratory (RDDL Pune)",
            t0_sample_needed_at=now - timedelta(hours=4),
            t1_collected_at=now - timedelta(hours=3),
            t2_dispatched_at=now - timedelta(hours=1)
        )
        db.add(sample1)

        # 6. MVU 1962 Dispatch Ticket
        mvu1 = MvuDispatchTicket(
            signal_id=sig3.id,
            ticket_number="1962-MH-9104",
            assigned_unit="MVU Unit 14 (Akole / Sangamner Beat)",
            vehicle_reg="MH-17-BV-1962",
            driver_pilot_name="Sachin Deshmukh",
            attending_ldo="Dr. Shailesh More",
            target_village="Kotul (Akole Taluka)",
            emergency_reason="Post-Loss Sudden Mortality (2 Caprine Deaths)",
            eta_minutes=25,
            dispatch_status="EN_ROUTE"
        )
        db.add(mvu1)

        # 7. Outbreak Cluster Surge Detection Record
        cluster1 = OutbreakCluster(
            taluka="Sangamner",
            village="Nimgaon Jali",
            disease_name="Foot and Mouth Disease (FMD)",
            signal_count=4,
            radius_km=4.8,
            is_surge=True,
            is_anonymized=False,
            ring_vax_recommended=True
        )
        cluster2 = OutbreakCluster(
            taluka="Sangamner",
            village=None,
            disease_name="Unspecified Indigestion / Minor signs",
            signal_count=2,
            radius_km=8.0,
            is_surge=False,
            is_anonymized=True,
            ring_vax_recommended=False
        )
        db.add_all([cluster1, cluster2])

        # Commit all
        db.commit()
        print("Database seeded 100% successfully with authentic rural livestock records!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()

