from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.unidades_productivas.unidades_productivas_api import (
    UnidadProductivaSinId,
    UnidadProductiva,
    UnidadProductivaList,
)
from repository.proyectos_repository import ProyectosRepository
from repository.up_repository import UnidadesProductivasRepository

# Router:
up_api = APIRouter(prefix="/up", tags=["Unidades Productivas"])

# Repository:
up_repository = UnidadesProductivasRepository()
proyecto_repository = ProyectosRepository()

# Endpoints:


@up_api.get("", response_model=List[UnidadProductivaList])
def get_all(db=Depends(get_db)):
    return up_repository.get_all(db)


@up_api.get("/emprendedores", response_model=List[UnidadProductivaList])
def get_all(db=Depends(get_db)):
    return up_repository.get_emprendedores(db)


@up_api.get("/grupos", response_model=List[UnidadProductivaList])
def get_all(db=Depends(get_db)):
    return up_repository.get_grupos(db)


@up_api.get("/cooperativas", response_model=List[UnidadProductivaList])
def get_all(db=Depends(get_db)):
    return up_repository.get_cooperativas(db)


@up_api.get("/{id}", response_model=UnidadProductivaList)
def get_by_id(id: int, db=Depends(get_db)):
    up = up_repository.get_by_id(id, db)
    if up is None:
        raise HTTPException(status_code=404, detail="Unidad Productiva no encontrada")
    return up


@up_api.post("", response_model=UnidadProductivaList)
def create(up: UnidadProductivaSinId, db=Depends(get_db)):
    return up_repository.create(up, db)


@up_api.put("/{id_up}/{id_proyecto}", response_model=UnidadProductivaList)
def assing_project(id_up: int, id_proyecto: int, db=Depends(get_db)):
    # Verifico que el proyecto exista:
    proyecto = proyecto_repository.get_by_id(id_proyecto, db)
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    else:
        # Verifico que la unidad productiva no tenga un proyecto asignado:
        up = up_repository.get_by_id(id_up, db)
        if up.proyecto_id is not None:
            raise HTTPException(
                status_code=400,
                detail="La unidad productiva ya tiene un proyecto asignado",
            )
        else:
            # Asigno el proyecto a la unidad productiva:
            up_update_project = up_repository.update_project(id_up, id_proyecto, db)
            return up_update_project
