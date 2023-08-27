from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.ubicaciones.provincias_api import ProvinciaSinId, Provincia
from repository.provincias_repository import ProvinciasRepository

provincias_api = APIRouter(prefix='/provincias', tags=['Provincias'])
provincias_repository = ProvinciasRepository()


@provincias_api.get('', response_model=List[Provincia])
def get_all(db=Depends(get_db)):
    result = provincias_repository.get_all(db)
    return result


@provincias_api.get('/{id}', response_model=Provincia)
def get_by_id(id: int, db=Depends(get_db)):
    result = provincias_repository.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Provincia no encontrada')
    return result


@provincias_api.post('', response_model=Provincia, status_code=201)
def new(datos: ProvinciaSinId, db=Depends(get_db)):
    try:
        result = provincias_repository.agregar(db, datos)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@provincias_api.put('/{id}', response_model=Provincia)
def modify(id: int, datos: ProvinciaSinId, db=Depends(get_db)):
    result = provincias_repository.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Provincia no encontrada')
    return result


@provincias_api.delete('/{id}', status_code=204)
def borrar(id: int, db=Depends(get_db)):
    result = provincias_repository.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Provincia no encontrada')
    return
