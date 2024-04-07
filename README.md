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

- _FastAPI_ -> Framework para crear la API. Provee una alta velocidad, tipado estático y generación automática de documentación interactiva en Swagger.
- _React_ -> La Biblioteca de JavaScript para la construcción de la interfaz de usuario.
- _MongoDB_ -> Base de datos NoSQL, para el manejo de los datos de manera escalable y flexible.
- _Uvicorn_ -> Servidor web ASGI (Asynchronous Server Gateway Interface) para aplicaciones Python, utilizado para ejecutar la app FastAPI de forma asíncrona y eficiente.

## Installation 🔧

### Step 1: Backend

```
# (RECOMENDED): Create virtual environment with Anaconda 
conda create --name NAME-VIRTUAL-ENVIROMENT python=3

# Fork or clone this respository
git clone https://github.com/josueluque/task-app.git

# Install all project dependencies
pip install -r requirements.txt
```

> [!IMPORTANT]
> Before running the `docker compose up -d` command, you must run the `invoke env` command

```
cd task-app/backend

# Generate environment variables for the backend
invoke env

docker compose up -d
```
  
#### Start Backend 🚀

```
python app.py
```



### Step 2: Client
> [!IMPORTANT]
> Before running the `npm install` command, you must have the npm package installed.

```
cd task-app/client
# Ensure that all project dependencies are available and ready for use.
npm install

# Generate environment variables for the client
npm generate:env
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
