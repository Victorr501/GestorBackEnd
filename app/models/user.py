from sqlalchemy import Column, Integer, String
from app.db.database import Base #Importamos la base declarada 

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    #Se especfica una longitud para el tipo de String en MySQL
    email = Column(String(225), unique=True, index=True)
    hashed_password = Column(String(225))