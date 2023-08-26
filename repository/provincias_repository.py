import sqlalchemy
from models.ubicaciones.provincias_bd import ProvinciaBd
from models.ubicaciones.provincias_api import ProvinciaSinId
from sqlalchemy.orm import Session
from sqlalchemy import select


class ProvinciasRepository():

    def get_all(self, db: Session):
        return db.execute(select(ProvinciaBd).order_by(ProvinciaBd.nombre)).scalars().all()
        

    def get_by_id(self, db: Session, id: int):
        result = db.execute(select(ProvinciaBd).where(
            ProvinciaBd.id == id)).scalar()
        return result

    def agregar(self, db: Session, datos: ProvinciaSinId):
        nueva_entidad_bd: ProvinciaBd = ProvinciaBd(**datos.dict())
        try:
            db.add(nueva_entidad_bd)
            db.commit()
        except sqlalchemy.exc.IntegrityError as e:
            raise RuntimeError(f'Error al agregar una provincia: {e}')
        return nueva_entidad_bd

    def modificar(self, db: Session, id: int, datos: ProvinciaSinId):
        entidad: ProvinciaBd = self.get_by_id(db, id)
        if entidad is None:
            return None
        for k, v in datos.dict(exclude_unset=True).items():
            setattr(entidad, k, v)
        db.commit()
        return entidad

    def borrar(self, db: Session, id: int):
        entidad: ProvinciaBd = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad
