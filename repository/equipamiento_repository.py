from models.equipamiento.equipamiento_api import EquipamientoSinId
from models.equipamiento.equipamiento_bd import EquipamientoBd
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select


class EquipamientoRepository():

    def get_all(self, db: Session):
        return db.execute(select(EquipamientoBd).order_by(EquipamientoBd.descripcion_principal)).scalars().all()

    def get_by_id(self, id: int, db: Session):
        return db.execute(select(EquipamientoBd).filter(EquipamientoBd.id == id)).scalars().first()

    def create(self, equipamiento: EquipamientoSinId, db: Session):
        nuevo_equipamiento_bd: EquipamientoBd = EquipamientoBd(
            **equipamiento.dict())
        db.add(nuevo_equipamiento_bd)
        db.commit()
        return nuevo_equipamiento_bd

    def modify(self, id: int, datos: EquipamientoSinId, db: Session):
        equipamiento: EquipamientoBd = self.get_by_id(id, db)
        if equipamiento is None:
            return None
        for k, v in datos.dict(exclude_unset=True).items():
            setattr(equipamiento, k, v)
        db.commit()
        return equipamiento

    def delete(self, id: int, db: Session):
        equipamiento: EquipamientoBd = self.get_by_id(id, db)
        if equipamiento is None:
            return None
        db.delete(equipamiento)
        db.commit()
        return equipamiento
