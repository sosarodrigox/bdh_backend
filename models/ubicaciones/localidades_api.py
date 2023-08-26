from pydantic import BaseModel
from models.ubicaciones.provincias_api import Provincia

# Modelo para AGREGAR localidades


class LocalidadSinId(BaseModel):
    nombre: str
    provincia_id: int = None

    class Config:
        orm_mode = True


class LocalidadLista(BaseModel):
    nombre: str
    provincia: Provincia = None

    class Config:
        orm_mode = True


class Localidad(LocalidadSinId):
    id: int
