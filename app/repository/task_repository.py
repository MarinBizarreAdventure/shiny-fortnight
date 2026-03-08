from app.models.task import Task
from pydantic import TypeAdapter
import json
from pathlib import Path
class TaskRepository():
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.tasks: list[Task] = self._load()
        self._id_iterator: int = max((t.id for t in self.tasks), default=0)

    def _load(self) -> list[Task]:
        if Path(self.file_path).exists():
            with open(self.file_path, "r") as f:
                raw_data = json.load(f)
                adapter = TypeAdapter(list[Task])
                return adapter.validate_python(raw_data)
        return []
        

    def _save(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w") as f:
                # data_to_save = TypeAdapter(list[Task]).dump_python(self.tasks)
                data_to_save = [t.model_dump() for t in self.tasks]
                json.dump(data_to_save,f,indent = 4)
    


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
        self._save()
        return new_task
    
    def delete(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        self._save()
        return True
    
  
    def update(self, task: Task) -> Task:
        self._save()
        return task