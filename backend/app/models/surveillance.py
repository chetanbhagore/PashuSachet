# -*- coding: utf-8 -*-
"""
PashuSachet Surveillance & Gram Signal System Models
Implements Section 2.7 DDL from BACKEND_ARCHITECTURE_PLAN.md
"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class VillageSignal(Base):
    __tablename__ = "village_signals"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    channel = Column(String(20), nullable=False, default="DIRECT_WEB")  # 'USSD', 'VOICE_IVR', 'DIRECT_WEB', 'PROXY_WEB'
    species = Column(String(30), nullable=False)
    symptoms = Column(Text, nullable=False)  # JSON-encoded array or comma-delimited
    affected_count = Column(Integer, nullable=False, default=1)
    
    village = Column(String(100), nullable=False, index=True)
    taluka = Column(String(100), nullable=False, index=True)
    district = Column(String(100), nullable=False, default="Ahmednagar", index=True)
    
    is_mortality = Column(Boolean, default=False)
    mortality_count = Column(Integer, default=0)
    is_proxy = Column(Boolean, default=False)
    proxy_name = Column(String(100), nullable=True)
    proxy_role = Column(String(50), nullable=True)
    
    reporter_phone_hash = Column(String(64), nullable=True)
    reporter_name = Column(String(100), nullable=True)
    
    status = Column(String(30), nullable=False, default="UNVERIFIED_SIGNAL", index=True)  # 'UNVERIFIED_SIGNAL', 'VERIFIED_SIGNAL', 'DISMISSED_BENIGN', 'SAMPLE_REQUESTED'
    urgency_level = Column(String(20), nullable=False, default="MODERATE")  # 'CRITICAL', 'URGENT', 'MODERATE', 'ABSTENTION'
    vitals_note = Column(String(200), nullable=True)
    
    t0_reported_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    t1_verified_at = Column(DateTime, nullable=True)
    verified_by = Column(String(100), nullable=True)
    dismissal_reason = Column(String(200), nullable=True)

    verifications = relationship("ParaVetVerification", back_populates="signal", cascade="all, delete-orphan")
    samples = relationship("SampleTracking", back_populates="signal", cascade="all, delete-orphan")
    mvu_tickets = relationship("MvuDispatchTicket", back_populates="signal", cascade="all, delete-orphan")

class ParaVetVerification(Base):
    __tablename__ = "para_vet_verifications"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    signal_id = Column(String(36), ForeignKey("village_signals.id"), nullable=False, index=True)
    paravet_id = Column(String(50), nullable=False)
    paravet_name = Column(String(100), nullable=False, default="Ganesh Kale")
    beat_cluster = Column(String(100), nullable=False, default="Sangamner Cluster")
    
    action = Column(String(30), nullable=False)  # 'CONFIRM', 'DISMISS', 'ADD_VITALS', 'REQUEST_SAMPLE'
    clinical_findings = Column(Text, nullable=True)
    rectal_temp_f = Column(Float, nullable=True)
    verified_species = Column(String(30), nullable=True)
    action_duration_seconds = Column(Integer, default=25)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    signal = relationship("VillageSignal", back_populates="verifications")

class SampleTracking(Base):
    __tablename__ = "sample_tracking"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    signal_id = Column(String(36), ForeignKey("village_signals.id"), nullable=True)
    sample_barcode = Column(String(50), unique=True, nullable=False, index=True)
    animal_tag = Column(String(50), nullable=True)
    sample_type = Column(String(100), nullable=False)  # 'Vesicular Swab', 'Serum', 'Nasal Swab', 'Milk Specimen'
    disease_suspected = Column(String(100), nullable=False)
    
    current_stage = Column(String(30), nullable=False, default="SAMPLE_NEEDED", index=True)
    # 'SAMPLE_NEEDED', 'SAMPLE_COLLECTED', 'IN_TRANSIT_LAB', 'LAB_TESTING', 'RESULTED_AND_ACTION_TAKEN'
    
    cold_chain_status = Column(String(100), default="Maintained 2°C - 8°C in Ice Gel Shipper")
    destination_lab = Column(String(150), default="Regional Disease Diagnostic Laboratory (RDDL Pune)")
    
    lab_result = Column(Text, nullable=True)
    closure_action = Column(Text, nullable=True)
    farmer_sms_sent = Column(Boolean, default=False)
    
    t0_sample_needed_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    t1_collected_at = Column(DateTime, nullable=True)
    t2_dispatched_at = Column(DateTime, nullable=True)
    t3_testing_at = Column(DateTime, nullable=True)
    t4_resulted_at = Column(DateTime, nullable=True)

    signal = relationship("VillageSignal", back_populates="samples")

class MvuDispatchTicket(Base):
    __tablename__ = "mvu_dispatch_tickets"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    signal_id = Column(String(36), ForeignKey("village_signals.id"), nullable=True)
    ticket_number = Column(String(50), unique=True, nullable=False, index=True)
    
    assigned_unit = Column(String(100), default="MVU Unit 14 (Sangamner / Akole Beat)")
    vehicle_reg = Column(String(20), default="MH-17-BV-1962")
    driver_pilot_name = Column(String(100), default="Sachin Deshmukh")
    attending_ldo = Column(String(100), default="Dr. Shailesh More")
    
    target_village = Column(String(100), nullable=False)
    emergency_reason = Column(String(200), nullable=False)
    eta_minutes = Column(Integer, default=25)
    dispatch_status = Column(String(30), default="AUTO_PRENOTIFIED")  # 'AUTO_PRENOTIFIED', 'EN_ROUTE', 'ON_SITE', 'RESOLVED'
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    signal = relationship("VillageSignal", back_populates="mvu_tickets")

class OutbreakCluster(Base):
    __tablename__ = "outbreak_clusters"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    taluka = Column(String(100), nullable=False, index=True)
    village = Column(String(100), nullable=True)
    disease_name = Column(String(100), nullable=False)
    signal_count = Column(Integer, default=1)
    radius_km = Column(Float, default=5.0)
    is_surge = Column(Boolean, default=False)
    is_anonymized = Column(Boolean, default=False)
    ring_vax_recommended = Column(Boolean, default=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

