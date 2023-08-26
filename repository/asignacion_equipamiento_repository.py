from sqlalchemy import and_, select
from sqlalchemy.orm import Session
from models.equipamiento.equipamiento_bd import EquipamientoBd
from models.equipamiento.asignacion_equipamiento_bd import AsignacionEquipamientoBd
from models.equipamiento.asignacion_equipamiento_api import AsignacionEquipamientoSinId


class AsignacionEquipamientoRepositorio():

    # Devuelve una lista con el Equipamiento asignado a una Unidad Productiva:
    def get_equipamiento_up(self, id_up, db: Session):
        equipamiento_up = db.query(EquipamientoBd).join(AsignacionEquipamientoBd).filter(
            AsignacionEquipamientoBd.id_up == id_up).all()
        if len(equipamiento_up) == 0:
            return None
        return equipamiento_up

    def get_all(self, db: Session):
        return db.execute(select(AsignacionEquipamientoBd).order_by(
            AsignacionEquipamientoBd.id_up)).scalars().all()

    def get_by_id(self, id_equipamiento: int, id_up: int, db: Session):
        result = db.execute(select(AsignacionEquipamientoBd).where(and_(
            AsignacionEquipamientoBd.id_equipamiento == id_equipamiento,
            AsignacionEquipamientoBd.id_up == id_up
        ))).scalar()
        return result

    def create(self, db: Session, datos: AsignacionEquipamientoSinId):
        nueva_asignacion_bd: AsignacionEquipamientoBd = AsignacionEquipamientoBd(
            **datos.dict())
        db.add(nueva_asignacion_bd)
        db.commit()
        return nueva_asignacion_bd
