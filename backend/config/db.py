# Importación del módulo necesario para la conexión con MongoDB
from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import get_settings

settings = get_settings()

# Establecimiento de la conexión con MongoDB
client = AsyncIOMotorClient(settings.DATABASE_URI)
database = client[settings.MONGO_DB]
collection = database.tasks