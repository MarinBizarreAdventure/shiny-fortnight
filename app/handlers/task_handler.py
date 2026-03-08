from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.service.task_service import TaskService
from app.repository.task_repository import TaskRepository


class CreateTaskRequest(BaseModel):
    title: str


router = APIRouter()


repo = TaskRepository("tasks.json")
service = TaskService(repo)

def get_service() ->TaskService:
    return service

@router.get("/tasks")
def get_all(service: TaskService = Depends(get_service)):
    return service.get_all_tasks()


@router.get("/tasks/{task_id}")
def get_task_by_id(task_id: int, service: TaskService = Depends(get_service)):
    try:
        return service.get_by_id(task_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/tasks")
def create_task(request: CreateTaskRequest, service: TaskService = Depends(get_service)):
    return service.create_task(request.title)


@router.patch("/tasks/{task_id}/done")
def complete_task(task_id: int, service: TaskService = Depends(get_service)):
    try:
        return service.complete_task(task_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, service: TaskService = Depends(get_service)):
    result = service.delete_task(task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message":"Task deleted"}