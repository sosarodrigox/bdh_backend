from pydantic import BaseModel
from datetime import datetime


class AsignacionEquipamientoSinId(BaseModel):
    id_equipamiento: int
    id_up: int
    cantidad: int
    valor_total: float

    class Config:
        orm_mode = True


class AsignacionEquipamiento(AsignacionEquipamientoSinId):
    id: int
