from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base #Importamos la base declarada
import secrets


class Calendario(Base):
    __tablename__ = "calendario"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), nullable=False, default="Mi calendario")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    #Relación 1 a 1 con User
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="calendario")