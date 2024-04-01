from config.db import collection
from models.taskModel import Task
from bson import ObjectId


async def get_all_tasks():
    tasks = []
    # Recupera todas las tareas de la colección MongoDB
    cursor = collection.find({})
    # document (dict) contiene los datos recuperados del documento de la base de datos MongoDB
    async for document in cursor:
        # Por cada documento crea una instancia de la clase Task utilizando los datos del documento y la agrega a la lista 'tasks'
        # * El doble asterisco ** se conoce como "desempaquetado de diccionario" o "keyword arguments unpacking" 
        # * Task(**document) está creando una instancia de la clase Task utilizando los datos del 'document' como argumentos para inicializar la instancia.
        # * Es útil si los campos del documento se corresponden directamente con los atributos de la clase (en este caso de la clase Task)
        tasks.append(Task(**document))  
    return tasks


async def get_task_by_id(id):
    # Busca una tarea en la base de datos por su identificador único (_id)
    # * find_one() busca un único documento que coincida con el filtro proporcionado.
    # * "_id": ObjectId(id)}, buscará un documento cuyo _id coincida con el valor proporcionado en id. 
    # * La función ObjectId() se utiliza para convertir el valor de id en un objeto ObjectId que MongoDB pueda entender.
    task = await collection.find_one({"_id": ObjectId(id)})
    return task


async def create_task(task):
    # Inserta una nueva tarea en la colección
    # * insert_one() -> inserta un nuevo documento (tarea) en la base de datos
    new_task = await collection.insert_one(task)
    # Busca la tarea recién creada por su identificador único (_id)
    # * collection.find_one(...) -> método para buscar un documento en una colección de MongoDB que cumpla con ciertos criterios de búsqueda.
    # * new_task.inserted_id -> devuelve el _id del documento recién insertado.
    created_task = await collection.find_one({"_id": new_task.inserted_id})
    return created_task


async def get_task_by_title(title):
    task = await collection.find_one({"title": title})
    return task


async def update_task_by_id(id: str, data):
    # Filtrar los datos para eliminar los campos con valores None
    task = {key: value for key, value in data.dict().items() if value is not None}
    print(task)
    # Actualizar el documento en la colección MongoDB
    # * collection.update_one(...) -> método que actualiza un único documento que cumple con ciertos criterios.
    # * {"$set": task} -> se especifica cómo se deben actualizar los campos del documento. 
    # * En MongoDB, $set es un operador de actualización que establece los valores de los campos especificados en el diccionario task.
    # * Example: Si quisiera actualizar solo el campo 'completed' haria: {"$set": {"completed": True}}
    await collection.update_one({"_id": ObjectId(id)}, {"$set": task})

    task_updated = await get_task_by_id(id)
    return task_updated


async def delete_task_by_id(id):
    # * delete_one() -> para eliminar un documento de la colección según el _id proporcionado.
    await collection.delete_one({"_id": ObjectId(id)})
    return True