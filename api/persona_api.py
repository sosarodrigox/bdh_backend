import re
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.personas.personas_api import Persona, PersonaSinId
from repository.personas_repository import PersonasRepository

# Router:
personas_api = APIRouter(
    prefix='/personas', tags=['Personas'])

# Repository:
personas_repository = PersonasRepository()


# Endpoints:


@personas_api.get('', response_model=List[Persona])
def get_all(db=Depends(get_db)):
    return personas_repository.get_all(db)


@personas_api.get('/{id}', response_model=Persona)
def get_by_id(id: int, db=Depends(get_db)):
    persona = personas_repository.get_by_id(id, db)
    if persona is None:
        raise HTTPException(
            status_code=404, detail="Persona no encontrada")
    return persona


@personas_api.post('', response_model=Persona, status_code=201)
def create(persona: PersonaSinId, db=Depends(get_db)):
    if len(persona.cuil) > 11:
        raise HTTPException(
            status_code=400, detail='El CUIL no puede tener más de 11 caracteres')
    if not re.match(r'^\d+$', persona.cuil):
        raise HTTPException(
            status_code=400, detail='El CUIL solo puede tener caracteres numéricos sin puntos ni guiones')
    return personas_repository.create(persona, db)


@personas_api.put('/{id}', response_model=Persona)
def put(id: int, persona: PersonaSinId, db=Depends(get_db)):
    if len(persona.cuil) > 11:
        raise HTTPException(
            status_code=400, detail='El CUIL no puede tener más de 11 caracteres')
    if not re.match(r'^\d+$', persona.cuil):
        raise HTTPException(
            status_code=400, detail='El CUIL solo puede tener caracteres numéricos sin puntos ni guiones')
    result = personas_repository.modify(id, persona, db)
    if result is None:
        raise HTTPException(
            status_code=404, detail='Persona no encontrada, no se puede modificar')
    return result


@personas_api.delete('/{id}')
def delete(id: int, db=Depends(get_db)):
    result = personas_repository.delete(id, db)
    if result is None:
        raise HTTPException(
            status_code=404, detail='Persona no encontrada, no se puede eliminar')
    return result
