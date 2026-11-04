# -*- coding: utf-8 -*-
"""
PashuSachet Clinical Tele-Triage & Food-Safety Prescription Models
"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class Consultation(Base):
    __tablename__ = "consultations"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    animal_tag = Column(String(50), nullable=False, index=True)
    farmer_name = Column(String(100), nullable=False)
    farmer_phone = Column(String(20), nullable=False)
    vet_name = Column(String(100), nullable=False, default="Dr. Rameshwar Kute")
    consultation_type = Column(String(30), nullable=False, default="field")  # 'field', 'clinic', 'tele'
    status = Column(String(30), nullable=False, default="SCHEDULED")  # 'SCHEDULED', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED'
    preferred_date = Column(String(20), nullable=False)
    clinical_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    animal_id = Column(String(36), ForeignKey("animals.id"), nullable=True)
    animal_tag = Column(String(50), nullable=False, index=True)
    
    diagnosis = Column(String(150), nullable=False)
    drug_name = Column(String(150), nullable=False)
    route = Column(String(50), nullable=False, default="Intramammary Infusion + IM")
    
    treatment_days = Column(Integer, nullable=False, default=3)
    withdrawal_hours = Column(Integer, nullable=False, default=72)
    
    prescribed_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    withdrawal_end_time = Column(DateTime, nullable=False)
    
    vet_name = Column(String(100), nullable=False, default="Dr. Rameshwar Kute, B.V.Sc & A.H.")
    vet_msvc_no = Column(String(50), nullable=False, default="MSVC/2012/03194")
    
    is_milk_withholding_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    animal = relationship("Animal", back_populates="prescriptions")

