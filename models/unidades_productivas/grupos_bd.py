from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.unidades_productivas.integrantes_bd import IntegranteBd
from database import BaseBd


class GrupoBd(BaseBd):
    __tablename__ = "grupos"
    id = Column(Integer, primary_key=True)
    nombre_grupo = Column(String(100), nullable=False)
    representante_grupo_id = Column(
        Integer, ForeignKey("personas.id", ondelete="SET NULL"), unique=True
    )
    cantidad_integrantes = Column(Integer, nullable=False)

    # Relación con integrantes
    integrantes = relationship(
        "IntegranteBd", cascade="all, delete", back_populates="grupo"
    )

    def __init__(self, nombre_grupo, representante_grupo_id, cantidad_integrantes=0):
        super().__init__(
            nombre_grupo=nombre_grupo,
            representante_grupo_id=representante_grupo_id,
            cantidad_integrantes=cantidad_integrantes + 1,
        )
