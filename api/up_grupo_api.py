from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.unidades_productivas.grupos_api import Grupo, GrupoSinId, GrupoList, GrupoNuevoIntegrante, CreateGrupoNuevoIntegrante
from repository.grupos_repository import GruposRepository
from repository.personas_repository import PersonasRepository
# from typing import List

# Router:
grupos_api = APIRouter(prefix='/grupos', tags=['Grupos'])

# Repository:
grupos_repository = GruposRepository()
personas_repository = PersonasRepository()

# Endpoints:


@grupos_api.get('', response_model=list[GrupoList])
def get_all(db=Depends(get_db)):
    grupos = grupos_repository.get_all(db)
    return grupos


@grupos_api.get('/{id}', response_model=Grupo)
def get_by_id(id: int, db=Depends(get_db)):
    grupo = grupos_repository.get_by_id(id, db)
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo no encontrado")
    return grupo


@grupos_api.post('', response_model=Grupo)
def create(grupo: GrupoSinId, db=Depends(get_db)):
    grupo = grupos_repository.create(grupo, db)
    if not grupo:
        raise HTTPException(status_code=400, detail="Error al crear el grupo")
    return grupo


@grupos_api.post('/nuevo', response_model=GrupoNuevoIntegrante, status_code=201)
def add_integrante(integrante: CreateGrupoNuevoIntegrante, db=Depends(get_db)):
    nuevo_integrante = personas_repository.get_by_id(
        integrante.id_nuevo_integrante, db)
    if nuevo_integrante.rol != 'no asignado':
        raise HTTPException(
            status_code=400, detail="El integrante ya está asignado a otra UP")
    grupo = grupos_repository.add_integrante(integrante, db)
    if not grupo:
        raise HTTPException(
            status_code=400, detail="Error al agregar nuevo integrante")
    return grupo
