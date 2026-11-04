# -*- coding: utf-8 -*-
"""
PashuSachet Configuration & Settings
"""
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "PashuSachet (Gram Signal System)"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./pashusachet.db")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "pashusachet-mahadahd-supersecret-production-key-2026")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Integrations
    RDDL_PUNE_API_URL: str = "https://rddl-pune.dahd.maharashtra.gov.in/api/v2"
    NADRES_V2_ENDPOINT: str = "https://nivedi.res.in/Nadres_v2/api/v1/ingest"
    BHARAT_PASHUDHAN_API_URL: str = "https://inaph.ndlm.dahd.gov.in/api/v1"
    HELPLINE_1962_GATEWAY: str = "https://mvu1962.maharashtra.gov.in/api/dispatch"
    
    # Default District Pilot Scope
    PILOT_DISTRICT: str = "Ahmednagar"
    PILOT_TALUKA: str = "Sangamner"
    DEFAULT_LANGUAGE: str = "mr"

    class Config:
        case_sensitive = True

settings = Settings()

