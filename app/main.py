from fastapi import FastAPI
from app.api.endpoints import users_endpoints, toke_endpoints #Importa tu modelo de endpoints de suaurios
from app.db.database import Base, engine #Importa la base de datos y el motor de SQLAlchemy
from fastapi.middleware.cors import CORSMiddleware

#Esto se importa para create_all sepa que modelos cargar
from app.models import user as user_model #Importa el modelo de usaurio par aque SQLAlchemy lo conozca
from app.models import token as tokens_model
from app.models import calendario as calendario_model

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
app.include_router(toke_endpoints.router, prefix="/api/v1")

#Permite las peticiones de todos los puerto a traves del navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # el origen de tu frontend
    allow_credentials=True,
    allow_methods=["*"],   # o restringe a ["POST"]
    allow_headers=["*"],
)

#endpoint ráiz
@app.get("/")
def read_root():
    return {"message": "Welcome to the GestorBackEnd API"}

