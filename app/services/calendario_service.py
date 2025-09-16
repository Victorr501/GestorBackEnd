from app.models.calendario import Calendario
from sqlalchemy.orm import Session
import secrets

#para crearlo cuando se cree el usuario
def create_calendario(db: Session, user_id: int ):
    
    db_calendario = Calendario(
        user_id = user_id,
    )
    
    db.add(db_calendario)
    db.commit()
    db.refresh(db_calendario)
    
    return db_calendario

#Buscar el calendario por el id del usaurio
def find_by_user_id(db: Session, user_id: int):
    return db.query(Calendario).filter(Calendario.user_id == user_id).first()


#para eliminar el calendario cuando se elimine el usuario
def delete_calendario(db: Session, calendario: Calendario):
    db.delete(calendario)
    db.commit()
    
#buscar el calendario por el id
def get_by_ID(db: Session, id: int):
    return db.query(Calendario).filter(Calendario.id == id).first()

