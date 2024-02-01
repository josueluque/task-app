from db.db import collection
from models.taskModel import Task


#TODO: Agregar las funciones de consulta y agregar docstrings

async def get_tasks():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))

    return tasks

async def add_new_task(task):
    new_task = await collection.insert_one(task)
    create_task = await collection.find_one({'_id': new_task.inserted_id})
    return create_task