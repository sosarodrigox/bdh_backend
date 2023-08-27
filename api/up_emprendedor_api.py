from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.unidades_productivas.emprendedores_api import Emprendedor, EmprendedorSinId, EmprendedorList
from repository.emprendedores_repository import EmprendedoresRepository

# Router:
emprendedores_api = APIRouter(
    prefix='/emprendedores', tags=['Emprendedores'])

# Repository:
emprendedores_repository = EmprendedoresRepository()

# Endpoints:


@emprendedores_api.get('', response_model=List[EmprendedorList])
def get_all(db=Depends(get_db)):
    return emprendedores_repository.get_all(db)


@emprendedores_api.get('/{id}', response_model=EmprendedorList)
def get_by_id(id: int, db=Depends(get_db)):
    emprendedor = emprendedores_repository.get_by_id(id, db)
    if emprendedor is None:
        raise HTTPException(
            status_code=404, detail="Emprendedor no encontrado")
    return emprendedor


@emprendedores_api.post('', response_model=Emprendedor)
def create(emprendedor: EmprendedorSinId, db=Depends(get_db)):
    return emprendedores_repository.create(emprendedor, db)
