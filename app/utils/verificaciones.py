from datetime import datetime, timedelta
from fastapi import HTTPException

def verificar_token(token_obj):
    
    ahora = datetime.utcnow()
    
    if token_obj is None:
        return False


    if ahora > token_obj.expires_at:
        return False

    return True