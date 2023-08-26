from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import BaseBd


class EmprendedorBd(BaseBd):
    __tablename__ = 'emprendedores'
    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer, ForeignKey(
        'personas.id', ondelete='CASCADE'), unique=True)

    persona = relationship(
        "PersonaBd", back_populates="emprendedor", uselist=False)
