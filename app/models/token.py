from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base #Importamos la base declarada
from datetime import datetime, timedelta, timezone
import secrets

class Token(Base):
    __tablename__ = "token"
    
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(225), unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) #La foren key
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    expires_at = Column(DateTime, default=lambda: datetime.now(timezone.utc) + timezone(hours=1))
    
    #Relacion inversa con el usuario
    user = relationship("User", back_populates="tokens")
    
    @staticmethod
    def generate_token():
        return secrets.token_urlsafe(32)
    