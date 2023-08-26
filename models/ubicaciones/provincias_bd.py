from sqlalchemy import Column, Integer, String
from database import BaseBd


class ProvinciaBd(BaseBd):
    __tablename__ = 'provincias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
