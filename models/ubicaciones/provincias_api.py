from pydantic import BaseModel

# Modelo para AGREGAR provincias


class ProvinciaSinId(BaseModel):
    nombre: str

    class Config:
        orm_mode = True

# Modelo para mostrar provincias


class Provincia(ProvinciaSinId):
    id: int
