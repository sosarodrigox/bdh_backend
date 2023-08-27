# bdh_backend
#Pasos a seguir luego de clonar el repo:

* 1 - Usar el archivo .env-template para crear los entornos de desarrollo y producción
* 2 - Instala los requermientos: pip install -r requirements.txt
    - Si hay problemas con fastapi, uvicorn, sqlalchemy utilizar versión python: 3.10.9 (base:conda)
* Comentar el ambiente de desarrollo o de producción según cual se va a utilizar.
* Se ejecuta desde plataforma.py en la carpeta raiz (Play en VSC) o por terminal: uvicorn backend.plataforma:app
* Para hacer el deploy en render se debe comentar el entorno de desarrollo.

