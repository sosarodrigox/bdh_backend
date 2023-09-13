from pydantic import BaseModel
from datetime import datetime


class AsignacionEquipamientoSinId(BaseModel):
    id_equipamiento: int
    id_up: int
    fecha_asignacion: datetime
    cantidad: int
    valor_total: float

    class Config:
        orm_mode = True


class AsignacionEquipamiento(AsignacionEquipamientoSinId):
    id_equipamiento: int
    id_up: int
