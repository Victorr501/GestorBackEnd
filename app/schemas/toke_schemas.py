from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#Esquema para crear un nuevo toke
#Lo que el frontend envia al backend
class TokenBase(BaseModel):
    user_id: int
    
class TokenCreate(TokenBase):
    pass #Aqui se pone si algun dia quisiera crear otros token

class TokenResponse(BaseModel):
    id: int
    token: str
    user_id: int
    create_at: datetime
    expires_at: datetime
    
    class Config:
        orm_mode = True

class ForgotPasswordRequest(BaseModel):
    email: EmailStr