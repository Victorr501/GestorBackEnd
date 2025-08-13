from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Usaremos "mysql+mysqlconnector" como driver
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/Gestor"

#Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Crear una clase SessionLocal para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para los modelos declarativos de SQLAlchemy
Base = declarative_base()