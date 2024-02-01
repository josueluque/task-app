from fastapi import FastAPI
from routes.taskRoute import task
import uvicorn

app = FastAPI(
    title="Task App",
    description="Task App using FARM stack - FastAPI, ReactJS, MongoDB ",
    version="0.1.0"
)


@app.get('/')
def welcome():
    return {"message": "Welcome to my FastAPI project"}

app.include_router(task)

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, log_level="info", reload=True)