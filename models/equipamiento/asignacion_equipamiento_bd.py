from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from database import BaseBd


class AsignacionEquipamientoBd(BaseBd):
    __tablename__ = "asignacion_equipamiento"
    id_equipamiento = Column(Integer, ForeignKey(
        'equipamiento.id'), primary_key=True)
    id_up = Column(Integer, ForeignKey(
        'unidades_productivas.id'), primary_key=True)
    cantidad = Column(Integer, nullable=False, default=0)
    valor_total = Column(Float, nullable=False, default=0.0)

    # Relacion con equipamiento:
    equipamiento = relationship(
        'EquipamientoBd', passive_deletes=True, back_populates='unidad_productiva')
    # Relacion con unidades productivas:
    unidad_productiva = relationship('UnidadProductivaBd', cascade="all, delete",
                                     back_populates='equipamiento')
