from sqlalchemy.orm import Session
from app.models import categoria_eventos

def get_all(db: Session):
    return db.query(categoria_eventos).all()