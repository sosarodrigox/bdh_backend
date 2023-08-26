from fastapi import APIRouter, Depends, HTTPException
from models.ubicaciones.localidades_api import LocalidadSinId, Localidad, LocalidadLista
from database import get_db
from repository.localidades_repository import LocalidadesRepository

localidades_api = APIRouter(prefix='/localidades', tags=['Localidades'])
localidad_repository = LocalidadesRepository()


@localidades_api.get('', response_model=list[LocalidadLista])
def get_all(db=Depends(get_db)):
    return localidad_repository.get_all(db)


@localidades_api.get('/{id}', response_model=Localidad)
def get_by_id(id: int, db=Depends(get_db)):
    result = localidad_repository.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Localidad no encontrada')
    return result


@localidades_api.post('', response_model=Localidad, status_code=201)
def new(datos: LocalidadSinId, db=Depends(get_db)):
    try:
        result = localidad_repository.agregar(db, datos)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@localidades_api.put('/{id}', response_model=Localidad)
def modify(id: int, datos: LocalidadSinId, db=Depends(get_db)):
    result = localidad_repository.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Localidad no encontrada')
    return result


@localidades_api.delete('/{id}', status_code=204)
def borrar(id: int, db=Depends(get_db)):
    result = localidad_repository.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Localidad no encontrada')
    return
