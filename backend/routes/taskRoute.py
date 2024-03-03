from fastapi import APIRouter, HTTPException, status
from models.taskModel import Task, UpdateTask
from services import taskService
from typing import Union


task = APIRouter()


@task.get('/task/tasks', response_model=list[Task], tags=['task'])
async def get_tasks():
    try:
        tasks = await taskService.get_all_tasks()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to get all tasks. ERROR: {str(e)}")


@task.get('/task/getTask/{id}', response_model=Union[Task, str], tags=['task'])
async def get_task(id: str):
    task = await taskService.get_task_by_id(id)
    if task:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Task with id: {id} not found")    


@task.post('/task/createTask', response_model=Union[Task, str], tags=['task']) 
async def create_task(task: Task):
    task_found = await taskService.get_task_by_title(task.title)
    if task_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Task could not be created. Existing user: {task.title}")

    try:
        response = await taskService.create_task(task.dict())
        if response:
            return response
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Could not create the task")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create task. ERROR: {str(e)}")


@task.put('/task/updateTask/{id}', response_model=Union[Task, str], tags=['task'])
async def update_task(id: str, task: UpdateTask):
    task_found = await taskService.get_task_by_title(task.title)
    if task_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Task could not be updated. Existing user: {task.title}")
    
    response = await taskService.update_task_by_id(id, task)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")


@task.delete('/task/deleteTask/{id}', response_model=str, tags=['task'])   
async def remove_task(id: str):
    response = await taskService.delete_task_by_id(id)
    if response:
        return f"Successfull task {id} has been deleted"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Task with id: {id} not found")