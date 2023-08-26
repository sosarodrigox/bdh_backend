from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from models.ubicaciones.localidades_api import LocalidadSinId
from models.ubicaciones.provincias_bd import ProvinciaBd
from models.ubicaciones.localidades_bd import LocalidadBd
from sqlalchemy.orm import Session


class LocalidadesRepository():

    def get_all(self, db: Session):
        return db.execute(select(LocalidadBd, ProvinciaBd).join(ProvinciaBd, isouter=True)).scalars().all()

    def get_by_id(self, db: Session, id: int):
        return db.execute(select(LocalidadBd).where(LocalidadBd.id == id)).scalar()

    def agregar(self, db: Session, datos: LocalidadSinId):
        nueva_localidad_bd: LocalidadBd = LocalidadBd(**datos.dict())
        try:
            db.add(nueva_localidad_bd)
            db.commit()
        except IntegrityError.exc.IntegrityError as e:
            raise RuntimeError(f'Error al agregar una provincia: {e}')
        return nueva_localidad_bd

    def modificar(self, db: Session, id: int, datos: LocalidadSinId):
        localidad: LocalidadBd = self.get_by_id(db, id)
        if localidad is None:
            return None

        for k, v in datos.dict(exclude_unset=True).items():
            setattr(localidad, k, v)

        db.commit()
        return localidad

    def borrar(self, db: Session, id: int):
        localidad: LocalidadBd = self.get_by_id(db, id)
        if localidad is None:
            return None
        db.delete(localidad)
        db.commit()
        return localidad
