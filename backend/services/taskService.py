from db.db import collection
from models.taskModel import Task
from bson import ObjectId


#TODO: Agregar las funciones de consulta y agregar docstrings

async def get_all_tasks():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks


async def get_task_by_id(id):
    task = await collection.find_one({"_id": ObjectId(id)})
    return task


async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({"_id": new_task.inserted_id})
    return created_task


async def get_task_by_title(title):
    task = await collection.find_one({"title": title})
    return task


async def update_task_by_id(id: str, data):
    task = {key: value for key, value in data.dict().items() if value is not None}
    print(task)
    await collection.update_one({"_id": ObjectId(id)}, {"$set": task})
    document = await collection.find_one({"_id": ObjectId(id)})
    return document


async def delete_task_by_id(id):
    await collection.delete_one({"_id": ObjectId(id)})
    return True