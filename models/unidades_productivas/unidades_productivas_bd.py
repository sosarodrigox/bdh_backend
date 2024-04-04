from sqlalchemy import Column, Boolean, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import BaseBd
from models.proyectos.proyectos_bd import ProyectoBd


class UnidadProductivaBd(BaseBd):
    __tablename__ = "unidades_productivas"
    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer, ForeignKey("personas.id"))
    denominacion_up = Column(String(250), nullable=False)
    tipo_up = Column(
        Enum("emprendedor", "grupo", "cooperativa", name="tipo_up_enum"), nullable=False
    )
    antiguedad_emprendimiento_meses = Column(Integer, nullable=False)
    antiguedad_emprendimiento_anios = Column(Integer, nullable=False)
    emprendimiento_formalizado = Column(Boolean, nullable=False)
    emprendimiento_activo = Column(Boolean, nullable=False)
    comercializacion_descripcion = Column(String(1024), nullable=False)
    servicios_productos = Column(String(1024), nullable=False)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"), nullable=True)

    grupo_id = Column(Integer, ForeignKey("grupos.id"), nullable=True)

    # Relacion con personas
    persona = relationship("PersonaBd", back_populates="unidades_productivas")
    # Relacion con proyectos
    proyecto = relationship("ProyectoBd")

    # Relacion con grupos:
    # TODO: Ver como unir la UP con el grupo
    grupo = relationship(
        "GrupoBd",
    )

    # Relacion con asignacion_equipamiento:
    equipamiento = relationship(
        "AsignacionEquipamientoBd",
        cascade="all, delete",
        passive_deletes=True,
        back_populates="unidad_productiva",
    )
