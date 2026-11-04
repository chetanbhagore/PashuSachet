# -*- coding: utf-8 -*-
"""
Telephony Automation Router:
Handles Toll-Free 1800-889-1962 Missed-Call Ingress,
2-Way Marathi Voice IVR (TwiML/VoiceXML), and Outbreak OBD Robo-Calls.
"""
from typing import Dict, Any, Optional
from fastapi import APIRouter, Body, Response, Query
from pydantic import BaseModel, Field
from backend.app.services.automation_service import automation_service

router = APIRouter(prefix="/api/v1/telephony", tags=["Telephony Automation"])


class MissedCallPayload(BaseModel):
    caller_phone: str = Field(..., example="+919822018491")
    timestamp: Optional[str] = None
    toll_free_number: str = "1800-889-1962"


class IvrGatherPayload(BaseModel):
    Digits: Optional[str] = "1"
    CallSid: Optional[str] = "CA123456789"
    From: Optional[str] = "+919822018491"
    SpeechResult: Optional[str] = None


class OutbreakBroadcastRequest(BaseModel):
    village_name: str = Field(..., example="निमगाव जाळी (Nimgaon Jali)")
    disease_name: str = Field(..., example="Foot and Mouth Disease (FMD)")
    radius_km: float = 5.0
    target_livestock_owners: int = 480


@router.post("/missed-call")
def handle_missed_call(payload: MissedCallPayload):
    """
    Inbound Missed-Call Hook (Toll-Free 1800-889-1962).
    Registers zero-cost farmer trigger and enqueues an automated outbound voice callback.
    """
    return automation_service.handle_missed_call(payload.caller_phone)


@router.post("/ivr/callback")
def handle_ivr_callback(
    From: Optional[str] = Query("+919822018491"),
    CallSid: Optional[str] = Query("CA123456789")
):
    """
    Twilio / Exotel Voice Callback Handshake.
    Returns high-fidelity Marathi TwiML / VoiceXML instructions for the automated call.
    """
    twiml_xml = automation_service.generate_ivr_twiml_callback(From)
    return Response(content=twiml_xml, media_type="application/xml")


@router.post("/ivr/gather")
def handle_ivr_gather(payload: IvrGatherPayload = Body(...)):
    """
    Gathers farmer's keypad DTMF or spoken Marathi input,
    runs automated clinical routing, and initiates 1962 MVU if critical.
    """
    digits = payload.Digits or "1"
    caller = payload.From or "+919822018491"
    return automation_service.handle_ivr_gather(digits, caller)


@router.post("/outbreak-broadcast")
def trigger_outbreak_broadcast(req: OutbreakBroadcastRequest):
    """
    Trigger Automated Outbound Dialer (OBD Robo-Call) to all livestock owners
    within 5km of an active outbreak epicenter.
    """
    return automation_service.trigger_outbreak_broadcast(
        village_name=req.village_name,
        disease_name=req.disease_name,
        target_count=req.target_livestock_owners
    )
