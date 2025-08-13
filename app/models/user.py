from sqlalchemy import Column, Integer, String
from app.db.database import Base #Importamos la base declarada 

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=Truem, index=True)
    hashed_password = Column(String)