from fastapi import FastAPI
from routes.taskRoute import task
from fastapi.middleware.cors import CORSMiddleware
from decouple import config # Modulo de python-decouple
import uvicorn

# Creación de la aplicación FastAPI
app = FastAPI(
    title="Task App",
    description="Task App using FARM stack - FastAPI, ReactJS, MongoDB ",
    version="0.1.0"
)


@app.get('/')
def welcome():
    return {"message": "Welcome to my FastAPI project"}

# Definicion de origins permitidos para establecer conexiones
origins = [
    config("FRONTEND_URL"),
]

# Definicion de middleware para manejar solicitudes de recursos cruzados (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Inclusión de rutas adicionales desde el conjunto de rutas 'task'
app.include_router(task)

# Ejecución del servidor Uvicorn
if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, log_level="info", reload=True)