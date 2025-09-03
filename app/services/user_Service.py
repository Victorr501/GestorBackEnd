from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user_schemas import UserCreate, UserUpdate
from passlib.context import CryptContext

#Intancia para gestionar el hashing de contraseñas
pws_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pws_context.hash(password)

def create_user(db: Session, user: UserCreate):
    #Encripta la contraseña antes de gardarla
    hashed_password = get_password_hash(user.password)
    #Crea una instancia del modelo de SQLAlchemy
    db_user = UserModel(email=user.email, hashed_password=hashed_password, name =user.name)
    
    
    #Añade el objeto a la sesión y lo garda en la base de datos
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # Actualiza el objeto para que tenga el ID generado
    return db_user

"""
Coge un usuario por el correo
"""
def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

"""
Verificar la contraseña
"""
def verfy_password(plain_password, hashed_password):
    return pws_context.verify(plain_password, hashed_password)

""""
Actualizar parametro de usuario
"""
def update_user(db: Session, user: UserUpdate, id: int):
    #Buscar el usuario por su id para que este devuelva el usuario que queremos actualizar
    db_user = db.query(UserModel).filter(UserModel.id == id).first()
    
    if not db_user:
        return None
    
    #Actualizar los parametro de este usuario
    if user.email is not None:
        db_user.email = user.email
    if user.name is not None:
        db_user.name = user.name
        
    #Guardar los cambios en la base de datos
    db.commit()
    db.refresh(db_user)
    
    #Devuelve el objeto de usuario actualizado
    return db_user