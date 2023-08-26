from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.orm import relationship
from database import BaseBd


class PersonaBd(BaseBd):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    apellido = Column(String(50), nullable=False)
    nombre = Column(String(50), nullable=False)
    cuil = Column(String(11), nullable=False, unique=True)
    genero = Column(String(50), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    nivel_educativo = Column(String(50), nullable=False)
    titulo_prof = Column(String(50), default="NO POSEE")
    situacion_laboral = Column(String(20), nullable=False)
    saberes_experiencia = Column(String(2), nullable=False, default="NO")
    curso_formacion_prof = Column(String(2), nullable=False, default="NO")
    rol = Column(Enum('no asignado', 'emprendedor', 'representante', 'integrante',
                 'presidente', 'secretario', 'tesorero', 'asociado', name='rol_enum'), nullable=False, default='no asignado')

    # TODO: Relacion con la tabla ubicaciones

    # Relaciones con otras tablas
    # Emprendedores:
    emprendedor = relationship(
        "EmprendedorBd", back_populates="persona", uselist=False)
    # Grupos:

    # # Relación con GrupoBd como representante
    # grupo_representante = relationship("GrupoBd", back_populates="representante_grupo", uselist=False, foreign_keys=[
    #                                    GrupoBd.representante_grupo_id])

    # Relación con IntegrantesBd como integrante
    grupo = relationship(
        "IntegranteBd", cascade="all, delete", passive_deletes=True, back_populates='persona')

    # Relación con AsociadosBd como asociado
    cooperativa = relationship(
        "AsociadoBd", cascade="all, delete", passive_deletes=True, back_populates='persona')

    # # Cooperativas:
    # cooperativa_presidente = relationship(
    #     'CooperativaBd', back_populates='presidente', foreign_keys=[CooperativaBd.presidente_id])
    # cooperativa_secretario = relationship(
    #     'CooperativaBd', back_populates='secretario', foreign_keys=[CooperativaBd.secretario_id])
    # cooperativa_tesorero = relationship(
    #     'CooperativaBd', back_populates='tesorero', foreign_keys=[CooperativaBd.tesorero_id])
    # cooperativa_asociado = relationship(
    #     'CooperativaBd', back_populates='asociados')

    # Unidades Productivas:
    unidades_productivas = relationship(
        "UnidadProductivaBd", back_populates="persona")

    @property
    def full_name(self):
        return f"{self.apellido}_{self.nombre}"
