from typing import Optional
from pydantic import BaseModel
from models.personas.personas_api import Persona
from models.unidades_productivas.grupos_api import Grupo


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
    proyecto_id: Optional[int] = None
    grupo_id: Optional[int] = None

    class Config:
        orm_mode = True


class UnidadProductiva(UnidadProductivaSinId):
    id: int
    persona: Persona
    grupo_id: Optional[int] = None


class UnidadProductivaList(UnidadProductivaSinId):
    id: int
    persona: Persona
    # grupo: Optional[Grupo] = None
    grupo: Optional[Grupo] = None
