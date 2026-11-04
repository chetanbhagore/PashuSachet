from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel

class AnimalCreate(BaseModel):
    name: Optional[str] = "Gauri"
    species: str = "cattle"
    breed: str = "Gir"
    gender: str = "female"
    birth_date: Optional[date] = None
    age_months_estimated: int = 36
    lactation_status: str = "in_milk"
    bharat_pashudhan_id: Optional[str] = None
    photo_url: Optional[str] = None

class AnimalResponse(BaseModel):
    id: str
    ps_tag: str
    bharat_pashudhan_id: Optional[str] = None
    owner_id: str
    name: Optional[str] = None
    species: str
    breed: str
    gender: str
    age_months_estimated: int
    lactation_status: str
    photo_url: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

