from sqlalchemy.orm import Session
from app.db.database import engine, Base
from app.models.categoria_eventos import Categoria_eventos

categoria_inicaieles = [
    {"nombre": "Gasto", "color": "#0000FF"},       # azul
    {"nombre": "Nomina", "color": "#00FF00"},      # verde
    {"nombre": "Ingreso", "color": "#808080"},     # gris
    {"nombre": "Pago Mensual", "color": "#FFFF00"} # amarillo
]

def init_categorias(db: Session):
    for cat in categoria_inicaieles:
        exists = db.query(Categoria_eventos).filter_by(nombre= cat["nombre"]).first()
        if not exists:
            nuevo_cat = Categoria_eventos(**cat)
            db.add(nuevo_cat)
    
    db.commit()
    print("Categorias iniciales creadas o ya existentes.")
    
if __name__ == "__main__":
    db = Session(bind=engine)  
    init_categorias(db)
    db.close