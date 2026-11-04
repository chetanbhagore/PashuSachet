# -*- coding: utf-8 -*-
"""
PashuSachet DPDP Act Audit & Compliance Models
"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, Text
from backend.app.core.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    actor_id = Column(String(50), nullable=False, index=True)
    actor_role = Column(String(30), nullable=False)
    action = Column(String(50), nullable=False)  # 'VERIFY_SIGNAL', 'SIGN_PRESCRIPTION', 'EXPORT_NADRES', 'CONSENT_GRANTED'
    resource_type = Column(String(50), nullable=False)
    resource_id = Column(String(50), nullable=False)
    ip_address = Column(String(50), default="127.0.0.1")
    dpdp_purpose = Column(String(100), default="DISEASE_SURVEILLANCE_AND_TREATMENT")
    details = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), index=True)

