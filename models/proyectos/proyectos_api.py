from pydantic import BaseModel


class ProyectoSinId(BaseModel):
    nombre: str
    eje: str
    tipo_produccion: str
    objetivo: str
    descripcion: str
    problematica: str
    solucion: str
    consumidores: str
    cantidad_personas: int = 0
    cantidad_up: int = 0

    class Config:
        orm_mode = True


class Proyecto(ProyectoSinId):
    id: int


class ProyectoList(ProyectoSinId):
    id: int
