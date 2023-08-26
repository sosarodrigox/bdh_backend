from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
# from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from models.personas.personas_bd import PersonaBd
from database import BaseBd


class IntegranteBd(BaseBd):
    __tablename__ = "integrantes"

    # Constraint para evitar doble asignación al grupo
    __table_args__ = (
        UniqueConstraint('id_persona', 'id_grupo',
                         name='unique_persona_grupo'),
    )

    id_persona = Column(Integer, ForeignKey('personas.id'), primary_key=True)
    id_grupo = Column(Integer, ForeignKey('grupos.id'), primary_key=True)
    # rol = Column(Enum('no asignado', 'emprendedor', 'representante', 'integrante',
    #              'presidente', 'secretario', 'tesorero', 'asociado', name='rol_enum'), nullable=False, default='no asignado')

    persona = relationship(
        'PersonaBd', passive_deletes=True, single_parent=True, back_populates='grupo')
    grupo = relationship('GrupoBd', cascade="all, delete",
                         back_populates='integrantes')
