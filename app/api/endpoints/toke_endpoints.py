from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.toke_schemas import TokenBase, TokenCreate, TokenResponse, ForgotPasswordRequest, Recuperacion
from app.services import token_service, user_Service
from app.db.database import SessionLocal, engine, Base
from app.models import token
from app.utils.enviarCorreo import send_email
from app.utils.verificaciones import verificar_token


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
        #Se pone esto ya que el usuario no puede saber si lo ha escrito bien o mal por razones de seguridad
        return {"detail": "Si el correo existe, se enviará un elace de recuperación"}
    
    token = token_service.create_token(db=db, user_id=db_user.id)
    
    #ALERTA CONTINUAR POR AQUI
    enlace = f"http://localhost:5500/html/cambiarContrasena/cambiarContrasena.html?token={token.token}"
    
    
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


"""
Este lo que hace es verificar los datos, ya actualizar la contraseña usando el token y la contraseña
"""
@router.post("/recuperacion")
def recuperacion(request: Recuperacion, db: Session = Depends(get_db)):
    db_token = token_service.get_toke_by_string(db=db, token_str=request.token)
    
    if not verificar_token(db_token):
        raise HTTPException(status_code=400, detail="Token expirado")

    db_user = user_Service.update_user_password_token(db=db, password=request.password, id=db_token.user_id)
    
    if not db_user:
        raise HTTPException(status_code=404, detail="Error al actualizar el usuario")
    
    token_service.delete_token(db=db, token=db_token)
    
    return {"successs": True, "mensaje":"La contraseña se ha actualizado correctamente"}