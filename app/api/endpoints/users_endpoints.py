from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schemas import UserCreate, User, UserLogin, UserUpdate, UserUpdatePassword
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
        
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
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


#Para el login del usuario y poder entrar a la apliacion
@router.post("/login", response_model=User)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    if not user_service.verfy_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    return db_user

#Para actualizar los parametro del usuario
@router.patch("/actualizar/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = user_service.update_user(db=db,user=user,id=user_id )
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Error al actualizar el usuario")
    
    return db_user

#Para actualizar la contraseña del usuario
@router.patch("/actualizar/contrasena/{user_id}", response_model=User)
def update_user_password(user_id: int, user: UserUpdatePassword, db: Session = Depends(get_db)):
    db_user = user_service.update_user_password(db=db, user=user, id=user_id)
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Error al actualizar el usuario")
    
    return db_user
    
    