from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schemas import UserCreate, User as UserSchema
from app.services import user_Service as user_service
from app.db.database import SessionLocal, engine, Base
from app.models import user as user_model

#Crear el router
router = APIRouter(prefix="/users", tags=["users"])

#Dependencia para obtener una sesion de base de datos
#Esto asegura que la sesion se cierre correctamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint para registrar un nuevo usuario
    """
    
    #Lógica para verificar si el usuario ya esiste... Por hacer
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya está registrado")
    
    #LLama a la función del servicio para crear el usuario en la base de datos
    db_user = user_service.create_user(db=db, user=user)
    return db_user