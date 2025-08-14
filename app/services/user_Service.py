from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user_schemas import UserCreate
from passlib.context import CryptContext

#Intancia para gestionar el hashing de contraseñas
pws_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pws_context.hash(password)

def create_user(db: Session, user: UserCreate):
    #Encripta la contraseña antes de gardarla
    hashed_password = get_password_hash(user.password)
    #Crea una instancia del modelo de SQLAlchemy
    db_user = UserModel(email=user.email, hashed_password=hashed_password)
    
    
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