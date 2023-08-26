from pydantic import BaseModel
from models.personas.personas_api import Persona


class EmprendedorSinId(BaseModel):
    persona_id: int

    class Config:
        orm_mode = True


class Emprendedor(EmprendedorSinId):
    id: int


class EmprendedorList(EmprendedorSinId):
    id: int
    persona: Persona
