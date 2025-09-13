from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.toke_schemas import TokenBase, TokenCreate, TokenResponse, ForgotPasswordRequest
from app.services import token_service, user_Service
from app.db.database import SessionLocal, engine, Base
from app.models import token
from app.utils.enviarCorreo import send_email


router = APIRouter(prefix="/token", tags=["token"])


#Dependencia para obtener una sesion de base de datos
#Esto asegura que la sesion se cierre correctamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/enviarRecuperacion")
def forgot_password(request: ForgotPasswordRequest, db:Session = Depends(get_db)):
    db_user = user_Service.get_user_by_email(db, request.email)
    
    if not db_user:
        return {"detail": "Si el correo existe, se enviará un enlace de recuperacion"}
    
    token = token_service.create_token(db=db, user_id=db_user.id)
    
    #ALERTA CONTINUAR POR AQUI
    enlace = f"http://localhost:5500/cambiarContraseña/cambiarContraseña.html?token={token.token}"
    
    
    #Esto envia el correo para que pueda recuperar la contraseaña
    subject = "Recupera tu contraseña"
    body = f"""
    <p>Hola,</p>
    <p>Haz clic en el siguiente enlace para restablecer tu contraseña:</p>
    <a href="{enlace}">{enlace}</a>
    <p>Este enlace expira en 1 hora.</p>
    """
    send_email(db_user.email, body, subject)
    
    return {"detail": "Si el correo existe, se enviará un elace de recuperación"}