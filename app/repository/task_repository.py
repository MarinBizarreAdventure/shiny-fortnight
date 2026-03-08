from app.models.task import Task

class TaskRepository():
    def __init__(self):
        self.tasks: list[Task] = []
        self._id_iterator: int = 0

    def get_new_id(self) -> int:
        self._id_iterator += 1
        return self._id_iterator
    
    def get_all(self) -> list[Task]:
        return self.tasks
    
    def get_by_id(self, task_id: int) -> Task | None:
        return next((t for t in self.tasks if t.id == task_id), None)
    
    def create(self, title: str) -> Task:
        new_task = Task(id=self.get_new_id(),title=title)
        self.tasks.append(new_task)
        return new_task
    
    def delete(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        return True
    
  
