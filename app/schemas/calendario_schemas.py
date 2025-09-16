from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Lo que el frontend enviará al backend para crear un calendario
class CalendarBase(BaseModel):
    title: str

# Para crear un calendario (hereda de CalendarBase)
class CalendarCreate(CalendarBase):
    pass

# Para actualizar un calendario (por si luego lo necesitas)
class CalendarUpdate(BaseModel):
    description: Optional[str] = None

# Lo que devuelve el backend al frontend
class CalendarResponse(BaseModel):
    id: int
    title: str
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True