from models.unidades_productivas.cooperativas_api import Cooperativa, CooperativaSinId, CooperativaNuevoAsociado
from models.unidades_productivas.cooperativas_bd import CooperativaBd
from models.personas.personas_bd import PersonaBd
from sqlalchemy.orm import Session
from sqlalchemy import select


class CooperativasRepository():
    def get_all(self, db: Session):
        return db.execute(select(CooperativaBd).order_by(CooperativaBd.nombre_cooperativa)).scalars().all()

    def get_by_id(self, id: int, db: Session):
        return db.execute(select(CooperativaBd).where(CooperativaBd.id == id)).scalar_one_or_none()

    def create(self, grupo: CooperativaSinId, db: Session):
        nueva_cooperativa: CooperativaBd = CooperativaBd(**grupo.dict())
        db.add(nueva_cooperativa)
        db.commit()
        return nueva_cooperativa

    def add_asociado(self, asociado: CooperativaNuevoAsociado, db: Session):
        cooperativa: CooperativaBd = self.get_by_id(
            asociado.id_cooperativa, db)
        nuevo_asociado: PersonaBd = db.execute(
            select(PersonaBd).where(PersonaBd.id == asociado.id_nuevo_asociado)).scalar_one_or_none()

        if cooperativa and nuevo_asociado:
            # Asignamos el rol "asociado" al nuevo integrante
            nuevo_asociado.rol = 'asociado'

            # TODO: Ver nuevo_integrante.grupo_id = integrante.id_grupo (no funciona)
            # # Asignamos el cooperativa_id al nuevo integrante
            # nuevo_asociado.cooperativa_id = asociado.id_cooperativa
            db.commit()
            return asociado
        else:
            return None
