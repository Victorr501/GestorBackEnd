from app.db.database import Base
from sqlalchemy import Column, Integer, String

class Categoria_eventos(Base):
    __tablename__ = "categorias_eventos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, index=True)
    color = Column(String(7)) #Estara escrito en exagesimal
    
    
