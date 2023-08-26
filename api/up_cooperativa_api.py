from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.unidades_productivas.cooperativas_api import Cooperativa, CooperativaSinId, CooperativaList, CooperativaNuevoAsociado, CreateCooperativaNuevoAsociado
from repository.cooperativas_repository import CooperativasRepository
from repository.personas_repository import PersonasRepository
# from typing import List

# Router:
cooperativas_api = APIRouter(prefix='/cooperativas', tags=['Cooperativas'])

# Repository:
cooperativas_repository = CooperativasRepository()
personas_repository = PersonasRepository()

# Endpoints:


@cooperativas_api.get('', response_model=list[CooperativaList])
def get_all(db=Depends(get_db)):
    cooperativas = cooperativas_repository.get_all(db)
    return cooperativas


@cooperativas_api.get('/{id}', response_model=Cooperativa)
def get_by_id(id: int, db=Depends(get_db)):
    cooperativa = cooperativas_repository.get_by_id(id, db)
    if not cooperativa:
        raise HTTPException(
            status_code=404, detail="Cooperativa no encontrada")
    return cooperativa


@cooperativas_api.post('', response_model=Cooperativa)
def create(cooperativa: CooperativaSinId, db=Depends(get_db)):
    presidente = personas_repository.get_by_id(cooperativa.presidente_id, db)
    if presidente.rol != 'no asignado':
        raise HTTPException(
            status_code=400, detail="El presidente ya está asignado a otra UP")
    cooperativa = cooperativas_repository.create(cooperativa, db)
    if not cooperativa:
        raise HTTPException(
            status_code=400, detail="Error al crear la cooperativa")
    return cooperativa


@cooperativas_api.post('/nuevo', response_model=CooperativaNuevoAsociado, status_code=201)
def add_asociado(asociado: CreateCooperativaNuevoAsociado, db=Depends(get_db)):
    nuevo_asociado = personas_repository.get_by_id(
        asociado.id_nuevo_asociado, db)
    if nuevo_asociado.rol != 'no asignado':
        raise HTTPException(
            status_code=400, detail="El asociado ya está asignado a otra UP")
    cooperativa = cooperativas_repository.add_asociado(asociado, db)
    if not cooperativa:
        raise HTTPException(
            status_code=400, detail="Error al agregar nuevo asociado")
    return cooperativa
