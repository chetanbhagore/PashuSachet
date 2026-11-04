import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    phone_number = Column(String(15), unique=True, index=True, nullable=False)
    role = Column(String(20), nullable=False, default="farmer") # 'farmer', 'vet', 'officer', 'admin'
    status = Column(String(20), nullable=False, default="active") # 'active', 'pending_verification', 'suspended'
    language_pref = Column(String(5), nullable=False, default="mr") # 'mr', 'hi', 'en'
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    farmer_profile = relationship("ProfileFarmer", back_populates="user", uselist=False, cascade="all, delete-orphan")
    vet_profile = relationship("ProfileVet", back_populates="user", uselist=False, cascade="all, delete-orphan")
    officer_profile = relationship("ProfileOfficer", back_populates="user", uselist=False, cascade="all, delete-orphan")
    consent_events = relationship("ConsentEvent", back_populates="user", cascade="all, delete-orphan")

class AuthOtp(Base):
    __tablename__ = "auth_otps"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    phone_number = Column(String(15), index=True, nullable=False)
    otp_hash = Column(String(128), nullable=False)
    attempts_remaining = Column(Integer, default=3)
    is_used = Column(Boolean, default=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class ProfileFarmer(Base):
    __tablename__ = "profiles_farmer"

    user_id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    village = Column(String(100), nullable=False)
    taluka = Column(String(100), nullable=False)
    district = Column(String(100), nullable=False)
    dairy_coop_member = Column(Boolean, default=False)
    dairy_coop_name = Column(String(100), nullable=True)

    user = relationship("User", back_populates="farmer_profile")

class ProfileVet(Base):
    __tablename__ = "profiles_vet"

    user_id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    qualification = Column(String(100), nullable=False, default="B.V.Sc & A.H.")
    msvc_reg_no = Column(String(50), unique=True, nullable=False)
    dispensary_name = Column(String(150), nullable=False)
    dispensary_type = Column(String(50), nullable=False, default="Government Dispensary")
    coverage_radius_km = Column(Integer, default=25)
    is_available = Column(Boolean, default=True)

    user = relationship("User", back_populates="vet_profile")

class ProfileOfficer(Base):
    __tablename__ = "profiles_officer"

    user_id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    full_name = Column(String(100), nullable=False)
    department_id = Column(String(50), unique=True, nullable=False)
    designation = Column(String(100), nullable=False, default="LDO")
    assigned_district = Column(String(100), nullable=False)

    user = relationship("User", back_populates="officer_profile")

class ConsentEvent(Base):
    __tablename__ = "consent_events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    purpose = Column(String(50), nullable=False)
    action = Column(String(20), nullable=False, default="GRANTED") # 'GRANTED', 'WITHDRAWN'
    policy_version = Column(String(20), nullable=False, default="v1.0")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="consent_events")

