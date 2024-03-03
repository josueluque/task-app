# Importación del módulo necesario para la conexión con MongoDB
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

# Establecimiento de la conexión con MongoDB
client = AsyncIOMotorClient(config("MONGO_URL"))
database = client.taskdb
collection = database.tasks