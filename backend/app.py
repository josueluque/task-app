from fastapi import FastAPI
from routes.taskRoute import task

app = FastAPI()

@app.get('/')
def welcome():
    return {"message": "Welcome to my FastAPI project"}

app.include_router(task)
    