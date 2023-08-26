from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.equipamiento.equipamiento_api import EquipamientoSinId, Equipamiento
from repository.equipamiento_repository import EquipamientoRepository

# Router:
equipamiento_api = APIRouter(
    prefix='/equipamiento', tags=['Equipamiento'])

# Repository:
equipamiento_repository = EquipamientoRepository()


# Endpoints:


@equipamiento_api.get('', response_model=list[Equipamiento])
def get_all(db=Depends(get_db)):
    return equipamiento_repository.get_all(db)


@equipamiento_api.get('/{id}', response_model=Equipamiento)
def get_by_id(id: int, db=Depends(get_db)):
    equipamiento = equipamiento_repository.get_by_id(id, db)
    if equipamiento is None:
        raise HTTPException(
            status_code=404, detail="Equipamiento no encontrado")
    return equipamiento


@equipamiento_api.post('', response_model=Equipamiento, status_code=201)
def create(equipamiento: EquipamientoSinId, db=Depends(get_db)):
    return equipamiento_repository.create(equipamiento, db)


@equipamiento_api.put('/{id}', response_model=Equipamiento)
def put(id: int, equipamiento: EquipamientoSinId, db=Depends(get_db)):
    result = equipamiento_repository.modify(id, equipamiento, db)
    if result is None:
        raise HTTPException(
            status_code=404, detail='Equipamiento no encontrado, no se puede modificar')
    return result


@equipamiento_api.delete('/{id}')
def delete(id: int, db=Depends(get_db)):
    result = equipamiento_repository.delete(id, db)
    if result is None:
        raise HTTPException(
            status_code=404, detail='Equipamiento no encontrado, no se puede eliminar')
    return result
