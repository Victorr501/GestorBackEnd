from app.models.token import Token
from sqlalchemy.orm import Session
import secrets
from datetime import datetime, timedelta, timezone

def create_token(db:Session, user_id: int, hours_valid: int = 1 ) -> Token:
    
    token_str = secrets.token_urlsafe(32)
    
    db_token = Token(
        token=token_str,
        user_id=user_id,
        expires_at = datetime.now(timezone.utc) + timedelta(hours=hours_valid)
    )
    
    db.add(db_token)
    db.commit()
    db.refresh(db_token) #refrescar para obtener ID generado
    
    return db_token

def delete_token(db: Session, token: Token):
    if token is None:
        return False
    db.delete(token)
    db.commit()
    return True
    
def get_toke_by_string(db: Session, token_str: str):
    return db.query(Token).filter(Token.token == token_str).first()