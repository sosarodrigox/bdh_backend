from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from database import BaseBd


class LocalidadBd(BaseBd):
    __tablename__ = 'localidades'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    provincia_id = Column(Integer, ForeignKey(
        'provincias.id'))

    provincia = relationship('ProvinciaBd')
