from fastapi import APIRouter, HTTPException, status
from models.taskModel import Task, UpdateTask
from services import taskService
from typing import Union


task = APIRouter(
    prefix="/task",
    tags=['task']
)


@task.get('/tasks', response_model=list[Task])
async def get_tasks():
    try:
        tasks = await taskService.get_all_tasks()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to get all tasks. ERROR: {str(e)}")


@task.get('/getTask/{id}', response_model=Union[Task, str])
async def get_task(id: str):
    task = await taskService.get_task_by_id(id)
    if task:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Task with id: {id} not found")    


@task.post('/createTask', response_model=Union[Task, str]) 
async def create_task(task: Task):
    task_found = await taskService.get_task_by_title(task.title)
    if task_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Task could not be created. Existing task: {task.title}")

    try:
        response = await taskService.create_task(task.model_dump())
        if response:
            return response
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Could not create the task")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create task. ERROR: {str(e)}")


@task.put('/updateTask/{id}', response_model=Union[UpdateTask, str])
async def update_task(id: str, task: UpdateTask):
    task_found = await taskService.get_task_by_title(task.title)
    task_found_id = await taskService.get_task_by_id(id)

    if task_found and task_found_id["title"] != task.title:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Task could not be updated. Existing task: {task.title}")
    
    response = await taskService.update_task_by_id(id, task)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found")


@task.delete('/deleteTask/{id}', response_model=str)   
async def remove_task(id: str):
    response = await taskService.delete_task_by_id(id)
    if response:
        return f"Successfull task {id} has been deleted"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Task with id: {id} not found")