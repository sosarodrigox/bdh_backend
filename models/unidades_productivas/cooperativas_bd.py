from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.unidades_productivas.asociados_bd import AsociadoBd
from database import BaseBd


class CooperativaBd(BaseBd):
    __tablename__ = 'cooperativas'
    id = Column(Integer, primary_key=True)
    nombre_cooperativa = Column(String(250), nullable=False)
    presidente_id = Column(Integer, ForeignKey(
        'personas.id', ondelete='SET NULL'), nullable=False, unique=True)
    secretario_id = Column(Integer, ForeignKey(
        'personas.id', ondelete='SET NULL'), unique=True)
    tesorero_id = Column(Integer, ForeignKey(
        'personas.id', ondelete='SET NULL'), unique=True)

    # Relación con asociados
    asociados = relationship(
        "AsociadoBd", cascade="all, delete", back_populates='cooperativa')
