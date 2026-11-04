# -*- coding: utf-8 -*-
"""
SQLAlchemy Models Package Initialization
"""
from backend.app.core.database import Base
from backend.app.models.user import User, ProfileFarmer, ProfileVet, ProfileOfficer, ConsentEvent, AuthOtp
from backend.app.models.surveillance import (
    VillageSignal,
    ParaVetVerification,
    SampleTracking,
    MvuDispatchTicket,
    OutbreakCluster
)
from backend.app.models.animal import Animal, VaccinationRecord
from backend.app.models.clinical import Consultation, Prescription
from backend.app.models.audit import AuditLog

__all__ = [
    "Base",
    "User",
    "ProfileFarmer",
    "ProfileVet",
    "ProfileOfficer",
    "ConsentEvent",
    "AuthOtp",
    "VillageSignal",
    "ParaVetVerification",
    "SampleTracking",
    "MvuDispatchTicket",
    "OutbreakCluster",
    "Animal",
    "VaccinationRecord",
    "Consultation",
    "Prescription",
    "AuditLog"
]

