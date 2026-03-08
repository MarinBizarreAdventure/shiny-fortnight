from app.models.task import Task
from app.repository.task_repository import TaskRepository

class TaskService:
    def __init__(self,repo: TaskRepository):
        self.repo = repo
    
    def get_all_tasks(self) -> list[Task]:
        return self.repo.get_all()
    
    def get_by_id(self, task_id: int) -> Task:
        task = self.repo.get_by_id(task_id)
        if task is None:
            raise ValueError(f"No task found with ID: {task_id}")
        return task

    def create_task(self, title: str) -> Task:
        return self.repo.create(title)
    
    def complete_task(self, task_id: int) -> Task:
        task = self.repo.get_by_id(task_id)
        if task is None:
            raise ValueError(f"No task found with ID: {task_id}")
        task.done = True
        self.repo.update(task)
        return task
    
    def delete_task(self, task_id: int) -> bool:
        return self.repo.delete(task_id)