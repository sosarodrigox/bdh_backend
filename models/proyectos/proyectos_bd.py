from sqlalchemy import Column, Enum, Integer, String
from database import BaseBd


class ProyectoBd(BaseBd):
    __tablename__ = 'proyectos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    eje = Column(Enum('P_limp.mant.reciclado', 'P_construccion.m.habit', 'P_textil.prod.manufa',
                 'P_agric.producc.alimento', 'P_comercializacion.comu', 'P_otras.actividades', name='eje_enum'), nullable=False)
    tipo_produccion = Column(
        Enum('productos', 'servicios', name='tipo_produccion_enum'), nullable=False)
    objetivo = Column(String(1024), nullable=False)
    descripcion = Column(String(1024), nullable=False)
    problematica = Column(String(1024), nullable=False)
    solucion = Column(String(1024), nullable=False)
    consumidores = Column(Enum('consumidor_final', 'organismo_municipal',
                          'organismo_provincial', 'empresa_privada', name='consumidores_enum'), nullable=False)
    cantidad_personas = Column(Integer, nullable=False)
    cantidad_up = Column(Integer, nullable=False)
    # TODO: Ver como calcular la  cantidad de personas y up
    # TODO: Agregar campo de proyectos_relacionados, organismos_articulacion
