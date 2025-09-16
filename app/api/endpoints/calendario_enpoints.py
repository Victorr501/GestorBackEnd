from fastapi import APIRouter, Depends, HTTPException, status
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.calendario_schemas import CalendarBase, CalendarCreate, CalendarResponse, CalendarUpdate
from app.services import calendario_service



router = APIRouter(prefix="/calendario", tags=["calendario"])

#Dependencia para obtener una sesion de base de datos
#Esto asegura que la sesion se cierre correctamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{id}", response_model=CalendarResponse)
def get_by_ID(id: int, db: Session = Depends(get_db)):
    db_calendario = calendario_service.get_by_ID(db=db, id=id)
    
    if db_calendario is None:
        raise HTTPException(status_code=404, detail="Calendario no encontrado")
    
    return db_calendario