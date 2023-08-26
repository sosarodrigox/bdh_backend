from models.unidades_productivas.grupos_api import Grupo, GrupoSinId, GrupoNuevoIntegrante
from models.unidades_productivas.grupos_bd import GrupoBd
from models.personas.personas_bd import PersonaBd
from sqlalchemy.orm import Session
from sqlalchemy import select


class GruposRepository():
    def get_all(self, db: Session):
        return db.execute(select(GrupoBd).order_by(GrupoBd.nombre_grupo)).scalars().all()

    def get_by_id(self, id: int, db: Session):
        return db.execute(select(GrupoBd).where(GrupoBd.id == id)).scalar_one_or_none()

    def create(self, grupo: GrupoSinId, db: Session):
        nuevo_grupo: GrupoBd = GrupoBd(**grupo.dict())
        db.add(nuevo_grupo)
        db.commit()
        return nuevo_grupo

    def add_integrante(self, integrante: GrupoNuevoIntegrante, db: Session):
        grupo: GrupoBd = self.get_by_id(integrante.id_grupo, db)
        nuevo_integrante: PersonaBd = db.execute(
            select(PersonaBd).where(PersonaBd.id == integrante.id_nuevo_integrante)).scalar_one_or_none()

        if grupo and nuevo_integrante:
            # Asignamos el rol "integrante" al nuevo integrante
            nuevo_integrante.rol = 'integrante'
            # TODO: Ver nuevo_integrante.grupo_id = integrante.id_grupo (no funciona)
            # # Asignamos el grupo_id al nuevo integrante
            # nuevo_integrante.grupo_id = integrante.id_grupo
            db.commit()
            return integrante
        else:
            return None
