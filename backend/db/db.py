from motor.motor_asyncio import AsyncIOMotorClient
    
client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client.taskdb
collection = database.tasks
