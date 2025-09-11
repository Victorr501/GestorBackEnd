from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base #Importamos la base declarada 

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    #Se especfica una longitud para el tipo de String en MySQL
    name = Column(String(225))
    email = Column(String(225), unique=True, index=True)
    hashed_password = Column(String(225))
    
    #Relación 1 a n: un usuario puede tener varios tokens
    tokens = relationship("Toke", back_populates="user", cascade="all, delte-orphan")