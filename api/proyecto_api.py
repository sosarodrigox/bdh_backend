from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.proyectos.proyectos_api import ProyectoSinId, Proyecto, ProyectoList
from repository.proyectos_repository import ProyectosRepository

# Router:
proyectos_api = APIRouter(prefix="/proyectos", tags=["Proyectos"])

# Repository:
proyecto_repository = ProyectosRepository()

# Endpoints:


@proyectos_api.get("", response_model=List[ProyectoList])
def get_all(db=Depends(get_db)):
    return proyecto_repository.get_all(db)


# @proyectos_api.get('/emprendedores', response_model=list[ProyectoList])
# def get_all(db=Depends(get_db)):
#     return proyecto_repository.get_emprendedores(db)


# @proyectos_api.get('/grupos', response_model=list[ProyectoList])
# def get_all(db=Depends(get_db)):
#     return proyecto_repository.get_grupos(db)


# @proyectos_api.get('/cooperativas', response_model=list[ProyectoList])
# def get_all(db=Depends(get_db)):
#     return proyecto_repository.get_cooperativas(db)


@proyectos_api.get("/{id}", response_model=ProyectoList)
def get_by_id(id: int, db=Depends(get_db)):
    proyecto = proyecto_repository.get_by_id(id, db)
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


@proyectos_api.post("", response_model=ProyectoList)
def create(proyecto: ProyectoSinId, db=Depends(get_db)):
    return proyecto_repository.create(proyecto, db)


@proyectos_api.put("/{id}", response_model=ProyectoList)
def update(id: int, proyecto: ProyectoSinId, db=Depends(get_db)):
    return proyecto_repository.update(id, proyecto, db)
