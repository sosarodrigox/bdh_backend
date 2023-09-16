from pydantic import BaseModel


class AsignacionProyecto(BaseModel):
    id_equipamiento: int
    id_up: int

    class Config:
        orm_mode = True
