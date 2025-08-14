from fastapi import FastAPI
from app.api.endpoints import users_endpoints #Importa tu modelo de endpoints de suaurios
from app.db.database import Base, engine #Importa la base de datos y el motor de SQLAlchemy
from app.models import user as user_model #Importa el modelo de usaurio par aque SQLAlchemy lo conozca

#Crear la instancia de la aplicacion FastAPI
app = FastAPI()

#Evento de inicio que se ejecuta cuando el servidor arranca
@app.on_event("startup")
def create_db_tables():
    """
    Funcio que crea todas las tablas de la base de datos
    Si no esisten, usando los modelos de SQLAlchemy
    """
    
    print("Verificando y creando tablas de la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creados o ya existentes. La aplicación está lista")
    
#EndPoints
#endpoints de usuarios
app.include_router(users_endpoints.router, prefix="/api/v1")

#endpoint ráiz
@app.get("/")
def read_root():
    return {"message": "Welcome to the GestorBackEnd API"}