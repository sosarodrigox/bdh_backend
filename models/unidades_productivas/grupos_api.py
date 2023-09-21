from pydantic import BaseModel
from models.personas.personas_api import Persona

# from typing import List


class GrupoSinId(BaseModel):
    nombre_grupo: str
    representante_grupo_id: int
    cantidad_integrantes: int = 0

    class Config:
        orm_mode = True


class Grupo(GrupoSinId):
    id: int


class GrupoList(GrupoSinId):
    id: int
    representante_grupo_id: int


class CreateGrupoNuevoIntegrante(BaseModel):
    id_grupo: int
    id_nuevo_integrante: int

    class Config:
        orm_mode = True


class GrupoNuevoIntegrante(CreateGrupoNuevoIntegrante):
    id_nuevo_integrante: int
