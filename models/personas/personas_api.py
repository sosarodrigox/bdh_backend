from datetime import date
from pydantic import BaseModel


class PersonaSinId(BaseModel):
    apellido: str
    nombre: str
    cuil: str
    genero: str
    fecha_nacimiento: date
    nivel_educativo: str
    titulo_prof: str = None
    situacion_laboral: str
    saberes_experiencia: str
    curso_formacion_prof: str
    rol: str

    class Config:
        orm_mode = True


class Persona(PersonaSinId):
    id: int
