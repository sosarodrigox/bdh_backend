from pydantic import BaseModel
from models.personas.personas_api import Persona
# from typing import List


class CooperativaSinId(BaseModel):
    nombre_cooperativa: str
    presidente_id: int

    class Config:
        orm_mode = True


class Cooperativa(CooperativaSinId):
    id: int


class CooperativaList(CooperativaSinId):
    id: int
    presidente_id: int


class CreateCooperativaNuevoAsociado(BaseModel):
    id_cooperativa: int
    id_nuevo_asociado: int

    class Config:
        orm_mode = True


class CooperativaNuevoAsociado(CreateCooperativaNuevoAsociado):
    id_nuevo_asociado: int
