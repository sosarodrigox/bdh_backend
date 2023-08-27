from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models.equipamiento.asignacion_equipamiento_api import AsignacionEquipamientoSinId, AsignacionEquipamiento
from models.equipamiento.equipamiento_api import Equipamiento
from repository.asignacion_equipamiento_repository import AsignacionEquipamientoRepositorio
from repository.up_repository import UnidadesProductivasRepository
from repository.equipamiento_repository import EquipamientoRepository
from database import get_db

asignacion_equipamiento_api = APIRouter(
    prefix='/asignaciones', tags=['Asignaciones de Equipamiento'])

asignacion_equipamiento_repository = AsignacionEquipamientoRepositorio()
up_repository = UnidadesProductivasRepository()
equipamiento_reposotory = EquipamientoRepository()

# Equipamiento asignado a una UP particular:


@asignacion_equipamiento_api.get('/equipamiento/{id_up}', response_model=List[Equipamiento])
def get_equipamiento_up(id_up: int, db=Depends(get_db)):
    # Primero verifico que la up exista:
    if up_repository.get_by_id(id_up, db) is None:
        raise HTTPException(
            status_code=404, detail='La unidad productiva no existe')
    else:
        result = asignacion_equipamiento_repository.get_equipamiento_up(
            id_up, db)
        if result is None:
            raise HTTPException(
                status_code=404, detail='No hay equipamiento asignado a esta Unidad Productiva')
        return result


@asignacion_equipamiento_api.get('', response_model=List[AsignacionEquipamiento])
def get_all(db=Depends(get_db)):
    return asignacion_equipamiento_repository.get_all(db)


@asignacion_equipamiento_api.get('/{id_equipamiento}/{id_up}', response_model=AsignacionEquipamiento)
def get_by_id(id_equipamiento: int, id_up: int, db=Depends(get_db)):
    result = asignacion_equipamiento_repository.get_by_id(
        id_equipamiento, id_up, db)
    # Si el result es None levanta una excepción con código de error.
    if result is None:
        raise HTTPException(
            status_code=404, detail='Asignación de Equipamiento no encontrada')
    return result


@asignacion_equipamiento_api.post('', response_model=AsignacionEquipamiento, status_code=201)
def post(datos: AsignacionEquipamientoSinId, db=Depends(get_db)):
    result = asignacion_equipamiento_repository.create(db, datos)
    return result
