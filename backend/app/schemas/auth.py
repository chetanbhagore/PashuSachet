from typing import Optional
from pydantic import BaseModel

class OtpRequest(BaseModel):
    phone_number: str

class OtpVerify(BaseModel):
    phone_number: str
    otp: str
    role: Optional[str] = "farmer" # 'farmer', 'vet', 'officer', 'admin'
    full_name: Optional[str] = "Livestock Owner"
    village: Optional[str] = "Sangamner"
    taluka: Optional[str] = "Sangamner"
    district: Optional[str] = "Ahmednagar"

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    user_id: str
    phone_number: str
    full_name: str

class UserProfile(BaseModel):
    id: str
    phone_number: str
    role: str
    status: str
    language_pref: str
    full_name: Optional[str] = None
    village: Optional[str] = None
    taluka: Optional[str] = None
    district: Optional[str] = None

