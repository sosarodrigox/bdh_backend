from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
# from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from models.personas.personas_bd import PersonaBd
from database import BaseBd


class AsociadoBd(BaseBd):
    __tablename__ = "asociados"

    # Constraint para evitar doble asignación a la cooperativa
    __table_args__ = (
        UniqueConstraint('id_persona', 'id_cooperativa',
                         name='unique_persona_cooperativa'),
    )

    id_persona = Column(Integer, ForeignKey('personas.id'), primary_key=True)
    id_cooperativa = Column(Integer, ForeignKey(
        'cooperativas.id'), primary_key=True)
    # rol = Column(Enum('no asignado', 'emprendedor', 'representante', 'integrante',
    #              'presidente', 'secretario', 'tesorero', 'asociado', name='rol_enum'), nullable=False, default='no asignado')

    persona = relationship(
        'PersonaBd', passive_deletes=True, single_parent=True, back_populates='cooperativa')
    cooperativa = relationship('CooperativaBd', cascade="all, delete",
                               back_populates='asociados')
