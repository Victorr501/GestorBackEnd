from pydantic import BaseModel, EmailStr
from typing import Optional

#Esquema para crear un nuevo usuario
#Lo que el frontedn envai al backend
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    
#Esquema para la respuesta de la API
#Lo que el backend devuelve al frontend
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    
    class Config:
        from_attributes = True
        
#Esquema para el inicio de sesión
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
# Esquema para actualizar el usuario (solo nombre y email)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    
# Equema para actualizar el usaurio (contraseña)
class UserUpdatePassword(BaseModel):
    password : Optional[str] = None