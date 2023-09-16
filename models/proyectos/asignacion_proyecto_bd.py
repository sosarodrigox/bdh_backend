from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database import BaseBd


class AsignacionProyectoBd(BaseBd):
    __tablename__ = "asignacion_proyecto"
    id_proyecto = Column(Integer, ForeignKey("proyecto.id"), primary_key=True)
    id_up = Column(Integer, ForeignKey("unidades_productivas.id"), primary_key=True)

    # Relacion con proyecto:
    proyecto = relationship(
        "ProyectoBd", passive_deletes=True, back_populates="unidad_productiva"
    )
    # Relacion con unidades productivas:
    unidad_productiva = relationship(
        "UnidadProductivaBd", cascade="all, delete", back_populates="proyecto"
    )
