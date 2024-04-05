<div align="center">

<h2>
 TaskApp ✅📝
</h2>

![Python Badge](https://img.shields.io/badge/Python-090a15?logo=python)
![FastAPI Badge](https://img.shields.io/badge/FastAPI-000?logo=fastapi)
![GitHub issues](https://img.shields.io/github/issues/josueluque/task-app)
![GitHub forks](https://img.shields.io/github/forks/josueluque/task-app)
![GitHub PRs](https://img.shields.io/github/issues-pr/josueluque/task-app)

</div>

## About the app

#### Task App developed with:

- _FastAPI_ -> Framework para crear APIs web con Python. Destacado por su alta velocidad, tipado estático y generación automática de documentación interactiva en Swagger.
- _React_ -> La Biblioteca de JavaScript para construir interfaces de usuario interactivas y dinámicas.
- _MongoDB_ -> Base de datos NoSQL escalable y flexible, para el manejo de los datos (crear, eliminar, modificar y obtener las tareas)
- _Uvicorn_ -> Servidor web ASGI (Asynchronous Server Gateway Interface) para aplicaciones Python, utilizado para ejecutar aplicaciones FastAPI de forma asíncrona y eficiente.

## Installation 🔧

#### Backend

> [!IMPORTANT]
> Before running the `docker compose up -d` command, you must define the database environment variables in the .env file.

```
# Fork or clone this respository
git clone https://github.com/josueluque/task-app.git

cd task-app/backend
docker compose up -d
```

> (_Recomended_) -> Create virtual environment with [Anaconda](https://www.anaconda.com/download)

```
# Install all project dependencies
pip install -r requirements.txt
```

#### Start Backend 🚀

```
python app.py
```

<details>
	<summary>Enviroment variables</summary>
	
- MongoDB:
	```py
  MYSQL_HOST= localhost
  MYSQL_USER= root
  MYSQL_PASSWORD= mysql
  MYSQL_PORT= 3306
  MYSQL_DB= userdb
	```

- JWT and Secret key:
  ```py
  JWT_SECRET='secret'
  JWT_ALGORITHM='HS256'
  SECRET_KEY='secret_key'
  ```
- Admin:
  ```py
  # User Admin
  ADMIN_EMAIL="admin@gmail.com"
  ADMIN_PASSWORD="admin"
  ```
  </details>

#### Client

```
cd task-app/client
npm install
```

#### Start client 🚀

```
npm run dev
```

## Documentation

- [![FastAPI][fastapi-badge]][fastapi-url]
- [![React][react-badge]][react-url]
- [![MongoDB][mongodb-badge]][mongodb-url]
- [![Anaconda][anaconda-badge]][anaconda-url]
- [![Docker][docker-badge]][docker-url]
- [![Pydantic][pydantic-badge]][pydantic-url]

<!-- Variables -->

[fastapi-badge]: https://img.shields.io/badge/fastapi-000?style=for-the-badge&logo=fastapi
[fastapi-url]: https://fastapi.tiangolo.com/
[anaconda-badge]: https://img.shields.io/badge/anaconda-000?style=for-the-badge&logo=anaconda
[anaconda-url]: https://docs.anaconda.com/free/anaconda/configurations/switch-environment/
[docker-badge]: https://img.shields.io/badge/docker-000?style=for-the-badge&logo=docker
[docker-url]: https://docs.docker.com/
[pydantic-badge]: https://img.shields.io/badge/pydantic-000?style=for-the-badge&logo=pydantic
[pydantic-url]: https://docs.pydantic.dev/latest/
[react-badge]: https://img.shields.io/badge/react-000?style=for-the-badge&logo=react
[react-url]: https://es.react.dev/
[mongodb-badge]: https://img.shields.io/badge/mongodb-000?style=for-the-badge&logo=mongodb
[mongodb-url]: https://www.mongodb.com/docs/manual/crud/
