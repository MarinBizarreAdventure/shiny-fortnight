from fastapi import FastAPI
from app.handlers.task_handler import router

app = FastAPI(title="Task Tracker API")
app.include_router(router)
