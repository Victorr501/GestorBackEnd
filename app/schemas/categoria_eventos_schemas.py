from pydantic import BaseModel

#Es lo que devuelve al frontend
class CategoriaBase(BaseModel):
    id: int
    nombre: str
    color: str

class CategoriaCreate(CategoriaBase):
    pass
  

