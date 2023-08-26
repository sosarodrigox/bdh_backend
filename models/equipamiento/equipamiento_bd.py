from sqlalchemy import Column, Enum, Integer, String, Float
from sqlalchemy.orm import relationship
from database import BaseBd


class EquipamientoBd(BaseBd):
    __tablename__ = "equipamiento"
    id = Column(Integer, primary_key=True)
    tipo = Column(Enum("MAQUINA", "HERRAMIENTA", "INSUMO",
                  name='tipo_eq_enum'), nullable=False)
    descripcion_principal = Column(String(100), nullable=False)
    descripcion_secundaria = Column(String(100), nullable=True)
    potencia_valor = Column(Float, nullable=True)
    potencia_unidad = Column(String(50), nullable=True)
    valor = Column(Float, nullable=True, default=0.0)

    # Relacion con asignacion_equipamiento:
    unidad_productiva = relationship(
        'AsignacionEquipamientoBd', passive_deletes=True, back_populates='equipamiento')
