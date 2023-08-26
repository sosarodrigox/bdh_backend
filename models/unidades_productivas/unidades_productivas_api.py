from pydantic import BaseModel
from models.personas.personas_api import Persona


class UnidadProductivaSinId(BaseModel):
    persona_id: int
    denominacion_up: str
    tipo_up: str
    antiguedad_emprendimiento_meses: int
    antiguedad_emprendimiento_anios: int
    emprendimiento_formalizado: bool
    emprendimiento_activo: bool
    comercializacion_descripcion: str
    servicios_productos: str
    cantidad_integrantes: int = 0

    # TODO: Verificar valor default de cantidad de integrantes

    class Config:
        orm_mode = True


class UnidadProductiva(UnidadProductivaSinId):
    id: int
    persona: Persona


class UnidadProductivaList(UnidadProductivaSinId):
    id: int
    persona: Persona
