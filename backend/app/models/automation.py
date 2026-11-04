# -*- coding: utf-8 -*-
"""
SQLAlchemy Models for Multichannel Automation:
WhatsApp Sessions, Telephony Call Logs, and Outbreak Broadcast Campaigns
"""
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Text, JSON
from backend.app.core.database import Base


class WhatsAppSession(Base):
    __tablename__ = "whatsapp_sessions"

    id = Column(String(64), primary_key=True, default=lambda: str(uuid.uuid4()))
    phone_number = Column(String(20), nullable=False, index=True)
    current_state = Column(String(32), nullable=False, default="IDLE")  # IDLE, AWAIT_SYMPTOMS, AWAIT_LOCATION, AWAIT_PHOTO
    selected_species = Column(String(32), nullable=True)
    extracted_symptoms = Column(JSON, nullable=True)
    audio_media_id = Column(String(128), nullable=True)
    image_media_id = Column(String(128), nullable=True)
    last_interaction = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)


class TelephonyCallLog(Base):
    __tablename__ = "telephony_call_logs"

    call_id = Column(String(64), primary_key=True, default=lambda: f"CALL-{uuid.uuid4().hex[:10].upper()}")
    caller_phone = Column(String(20), nullable=False, index=True)
    call_type = Column(String(32), nullable=False)  # 'INBOUND_MISSED', 'OUTBOUND_IVR', 'EPIDEMIC_BROADCAST'
    call_status = Column(String(32), nullable=False, default="QUEUED")  # 'QUEUED', 'RINGING', 'ANSWERED', 'FAILED', 'BUSY'
    duration_seconds = Column(Integer, default=0)
    dtmf_digits = Column(String(16), nullable=True)
    recorded_audio_url = Column(Text, nullable=True)
    asr_transcript = Column(Text, nullable=True)
    village_code = Column(String(32), nullable=True)
    dispatched_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class BroadcastCampaign(Base):
    __tablename__ = "broadcast_campaigns"

    campaign_id = Column(String(64), primary_key=True, default=lambda: f"OBD-{uuid.uuid4().hex[:8].upper()}")
    directive_id = Column(String(32), nullable=True)
    target_village = Column(String(64), nullable=False)
    target_count = Column(Integer, nullable=False, default=480)
    channel = Column(String(32), nullable=False, default="VOICE_OBD")  # 'VOICE_OBD', 'WHATSAPP_PUSH', 'SMS_CDAC'
    delivered_count = Column(Integer, default=0)
    failed_count = Column(Integer, default=0)
    status = Column(String(32), default="IN_PROGRESS")  # 'IN_PROGRESS', 'COMPLETED'
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

