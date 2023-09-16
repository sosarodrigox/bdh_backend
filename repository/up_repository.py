from models.unidades_productivas.unidades_productivas_api import UnidadProductivaSinId
from models.unidades_productivas.unidades_productivas_bd import UnidadProductivaBd
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select


class UnidadesProductivasRepository:
    def get_all(self, db: Session):
        return (
            db.execute(
                select(UnidadProductivaBd).order_by(UnidadProductivaBd.persona_id)
            )
            .scalars()
            .all()
        )

    def get_emprendedores(self, db: Session):
        return (
            db.execute(
                select(UnidadProductivaBd)
                .filter(UnidadProductivaBd.tipo_up == "emprendedor")
                .order_by(UnidadProductivaBd.persona_id)
            )
            .scalars()
            .all()
        )

    def get_grupos(self, db: Session):
        return (
            db.execute(
                select(UnidadProductivaBd)
                .filter(UnidadProductivaBd.tipo_up == "grupo")
                .order_by(UnidadProductivaBd.persona_id)
            )
            .scalars()
            .all()
        )

    def get_cooperativas(self, db: Session):
        return (
            db.execute(
                select(UnidadProductivaBd)
                .filter(UnidadProductivaBd.tipo_up == "cooperativa")
                .order_by(UnidadProductivaBd.persona_id)
            )
            .scalars()
            .all()
        )

    def get_by_id(self, id: int, db: Session):
        return (
            db.execute(select(UnidadProductivaBd).filter(UnidadProductivaBd.id == id))
            .scalars()
            .first()
        )

    def create(self, up: UnidadProductivaSinId, db: Session):
        nueva_entidad_bd: UnidadProductivaBd = UnidadProductivaBd(**up.dict())
        db.add(nueva_entidad_bd)
        db.commit()
        return nueva_entidad_bd

    def update_project(self, id_up: int, id_proyecto: int, db: Session):
        up = (
            db.execute(
                select(UnidadProductivaBd).filter(UnidadProductivaBd.id == id_up)
            )
            .scalars()
            .first()
        )
        up.proyecto_id = id_proyecto
        db.commit()
        db.refresh(up)
        return up
