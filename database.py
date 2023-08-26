from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Carga las variables de entorno desde el archivo .env
from dotenv import load_dotenv
load_dotenv()

# Obtiene la variable de entorno para la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Motor de conexión:
engine = create_engine(DATABASE_URL, echo=True)

# Sesión para acceder a la conexión con la BD.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Clase base para manejar las entidades con el ORM
BaseBd = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_all():
    BaseBd.metadata.create_all(bind=engine)


def drop_all():
    BaseBd.metadata.drop_all(bind=engine)
