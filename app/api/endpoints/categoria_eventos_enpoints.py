from fastapi import APIRouter, Depends, HTTPException
from app.db.database import SessionLocal
from app.schemas.categoria_eventos_schemas import CategoriaBase
from sqlalchemy.orm import Session
from app.services.categoria_eventos_service import get_all


router = APIRouter(prefix="/categoria_eventos", tags=["categoria_eventos"])

#Dependencia para obtener una sesion de base de datos
#Esto asegura que la sesion se cierre correctamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#Ruta para pedir todas la categorias
@router.get("/", response_class=list[CategoriaBase])
def get_all_categorias(db: Session = Depends(get_db)):
    lista = get_all(db=db)
    
    if lista is None:
        raise HTTPException(status_code=404, detail="No se ha encontrado nada")
    
    return lista