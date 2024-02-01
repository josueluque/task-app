from fastapi import APIRouter, HTTPException
from models.taskModel import Task
from services import taskService


task = APIRouter()


#TODO: Hacer el crud, Agregar exceptions, Completar decoradores

@task.get('/task/tasks')
async def get_tasks():
    tasks = await taskService.get_tasks()
    return tasks

@task.get('/task/getTask/{id}')
async def get_task(id: int):
    return {"data": id}

@task.post('/task/createTask')
async def create_task(task: Task):
    response = await taskService.add_new_task(task.dict())
    if response:
        return response
    raise HTTPException(400, "error")
    
    # print(task)
    # return {"data": "Task created"}

@task.put('/task/editTask/{id}')
async def update_task(id: int, data):
    return {"data": f"Task {id} has been updated"}

@task.delete('/task/deleteTask/{id}')
async def delete_task(id: int):
    return {"data": f"Task {id} has been deleted"}