from pydantic import BaseModel


class EquipamientoSinId(BaseModel):
    tipo: str
    descripcion_principal: str
    descripcion_secundaria: str
    potencia_valor: float
    potencia_unidad: str
    valor:  float

    class Config:
        orm_mode = True


class Equipamiento(EquipamientoSinId):
    id: int
