from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.unidades_productivas.integrantes_bd import IntegranteBd
from database import BaseBd


class GrupoBd(BaseBd):
    __tablename__ = 'grupos'
    id = Column(Integer, primary_key=True)
    nombre_grupo = Column(String(100), nullable=False)
    representante_grupo_id = Column(Integer, ForeignKey(
        'personas.id', ondelete='SET NULL'), unique=True)

    # Relación con integrantes
    integrantes = relationship(
        "IntegranteBd", cascade="all, delete", back_populates='grupo')
