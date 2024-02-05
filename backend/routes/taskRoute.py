from fastapi import APIRouter, HTTPException
from models.taskModel import Task, UpdateTask
from services import taskService


task = APIRouter()


#TODO: Hacer el crud, Agregar exceptions, Completar decoradores

@task.get('/task/tasks')
async def get_tasks():
    tasks = await taskService.get_all_tasks()
    return tasks


@task.get('/task/getTask/{id}', response_model=Task)
async def get_task(id: str):
    task = await taskService.get_task_by_id(id)
    if task:
        return task
    raise HTTPException(404, f"Task with id {id} not found")    


@task.post('/task/createTask', response_model=Task)
async def create_task(task: Task):
    task_found = await taskService.get_task_by_title(task.title)
    if task_found:
        raise HTTPException(409, "Task already exists")

    response = await taskService.create_task(task.dict())
    # print(response)
    if response:
        return response
    raise HTTPException(404, f"Could not create the task")


@task.put('/task/updateTask/{id}', response_model=Task)
async def update_task(id: str, task: UpdateTask):
    response = await taskService.update_task_by_id(id, task)
    if response:
        return response
    raise HTTPException(404, f"Task with id {id} not found")


@task.delete('/task/deleteTask/{id}')   
async def remove_task(id: str):
    response = await taskService.delete_task_by_id(id)
    if response:
        return f"Successfull task {id} has been deleted"
    raise HTTPException(404, f"Task with id {id} not found")