# -*- coding: utf-8 -*-
"""
PashuSachet Authentication & Security Helpers
"""
import hashlib
import random
import string
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any

from backend.app.core.config import settings

def hash_dpdp_pii(val: str, salt: str = "PashuSachet-DPDP-2026") -> str:
    """One-way cryptographic hash for DPDP Act compliance."""
    if not val:
        return ""
    return hashlib.sha256(f"{val}:{salt}".encode("utf-8")).hexdigest()[:16]

def generate_numeric_otp(digits: int = 6) -> str:
    """Generate secure numeric OTP for farmer login."""
    return "".join(random.choices(string.digits, k=digits))

def normalize_phone(phone: str) -> str:
    """Normalize Indian mobile number to E.164 standard."""
    clean = "".join(ch for ch in phone if ch.isdigit() or ch == "+")
    if clean.startswith("0"):
        clean = "+91" + clean[1:]
    elif not clean.startswith("+"):
        if len(clean) == 10:
            clean = "+91" + clean
        else:
            clean = "+" + clean
    return clean

def verify_otp_hash(plain_otp: str, hashed_otp: str) -> bool:
    """Verify submitted OTP against SHA-256 hash."""
    return hashlib.sha256(plain_otp.encode("utf-8")).hexdigest() == hashed_otp

