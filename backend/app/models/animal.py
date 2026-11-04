# -*- coding: utf-8 -*-
"""
PashuSachet Animal Registry & Digital Pashu Aadhar Models
"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class Animal(Base):
    __tablename__ = "animals"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    pashu_tag = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    species = Column(String(50), nullable=False)
    breed = Column(String(100), nullable=True)
    age_years = Column(Float, nullable=False, default=2.0)
    sex = Column(String(20), nullable=False, default="Female")
    
    village = Column(String(100), nullable=False)
    taluka = Column(String(100), nullable=False, default="Sangamner")
    district = Column(String(100), nullable=False, default="Ahmednagar")
    
    owner_name = Column(String(100), nullable=False, default="Ganesh Patil")
    owner_phone = Column(String(20), nullable=False, default="+919822018491")
    is_insured = Column(Boolean, default=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    vaccinations = relationship("VaccinationRecord", back_populates="animal", cascade="all, delete-orphan")
    prescriptions = relationship("Prescription", back_populates="animal", cascade="all, delete-orphan")

class VaccinationRecord(Base):
    __tablename__ = "vaccination_records"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    animal_id = Column(String(36), ForeignKey("animals.id"), nullable=False, index=True)
    disease = Column(String(100), nullable=False)  # 'FMD', 'LSD', 'Brucellosis', 'Anthrax', 'HS', 'BQ'
    vaccine_name = Column(String(100), nullable=False)
    batch_no = Column(String(50), nullable=False)
    administered_at = Column(DateTime, nullable=False)
    next_due_date = Column(DateTime, nullable=False)
    administered_by = Column(String(100), nullable=False, default="Dr. Rameshwar Kute (LDO)")

    animal = relationship("Animal", back_populates="vaccinations")

