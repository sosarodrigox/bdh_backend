from models.proyectos.proyectos_api import ProyectoSinId
from models.proyectos.proyectos_bd import ProyectoBd
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select


class ProyectosRepository():

    def get_all(self, db: Session):
        return db.execute(select(ProyectoBd).order_by(ProyectoBd.nombre)).scalars().all()

    # def get_emprendedores(self, db: Session):
    #     return db.execute(select(ProyectoBd).filter(ProyectoBd.tipo_up == 'emprendedor').order_by(ProyectoBd.persona_id)).scalars().all()

    # def get_grupos(self, db: Session):
    #     return db.execute(select(ProyectoBd).filter(ProyectoBd.tipo_up == 'grupo').order_by(ProyectoBd.persona_id)).scalars().all()

    # def get_cooperativas(self, db: Session):
    #     return db.execute(select(ProyectoBd).filter(ProyectoBd.tipo_up == 'cooperativa').order_by(ProyectoBd.persona_id)).scalars().all()

    def get_by_id(self, id: int, db: Session):
        return db.execute(select(ProyectoBd).filter(ProyectoBd.id == id)).scalars().first()

    def create(self, up: ProyectoSinId, db: Session):
        nuevo_proyecto_bd: ProyectoBd = ProyectoBd(**up.dict())
        db.add(nuevo_proyecto_bd)
        db.commit()
        return nuevo_proyecto_bd

    def update(self, id: int, up: ProyectoSinId, db: Session):
        proyecto_bd: ProyectoBd = db.execute(
            select(ProyectoBd).filter(ProyectoBd.id == id)).scalars().first()
        proyecto_bd.nombre = up.nombre
        proyecto_bd.tipo_up = up.tipo_up
        proyecto_bd.persona_id = up.persona_id
        db.commit()
        return proyecto_bd
