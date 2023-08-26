from dotenv import load_dotenv
import os
from api.up_emprendedor_api import emprendedores_api
from api.asignacion_equipamiento_api import asignacion_equipamiento_api
from api.unidad_productiva_api import up_api as unidades_productivas_api
from api.equipamiento_api import equipamiento_api
from api.persona_api import personas_api
from api.ubi_provincia_api import provincias_api
from api.ubi_localidad_api import localidades_api
from api.up_grupo_api import grupos_api
from api.up_cooperativa_api import cooperativas_api
from api.proyecto_api import proyectos_api

from fastapi.middleware.cors import CORSMiddleware
import database
from fastapi import FastAPI
import uvicorn

import models.equipamiento.asignacion_equipamiento_bd
import models.unidades_productivas.unidades_productivas_bd
import models.equipamiento.equipamiento_bd
import models.unidades_productivas.emprendedores_bd
import models.ubicaciones.localidades_bd
import models.ubicaciones.provincias_bd
import models.personas.personas_bd
import models.unidades_productivas.grupos_bd
import models.unidades_productivas.cooperativas_bd
import models.proyectos.proyectos_bd

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene las variables de entorno para usarlas en tu aplicación
DATABASE_URL = os.getenv("DATABASE_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")


# Crea las tablas que corresponden a las entidades definidas en los modelos de BD.
database.create_all()

# Crea servidor FastAPI
app = FastAPI()

# # Rutas endopoints
app.include_router(asignacion_equipamiento_api)
app.include_router(unidades_productivas_api)
app.include_router(equipamiento_api)
app.include_router(emprendedores_api)
app.include_router(provincias_api)
app.include_router(localidades_api)
app.include_router(personas_api)
app.include_router(grupos_api)
app.include_router(cooperativas_api)
app.include_router(proyectos_api)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run('plataforma:app', reload=True)
