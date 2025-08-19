from pydantic import BaseModel, EmailStr

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