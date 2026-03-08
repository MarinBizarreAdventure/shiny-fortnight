
from app.models.task import Task
from app.repository.task_repository import TaskRepository
from app.service.task_service import TaskService
import sys


def main():

    
    
    repo = TaskRepository()
    service = TaskService(repo)

    t1 = service.create_task("learn python")
    t2 = service.create_task("build api")
    t2 = service.create_task("pass interview")

    print("all tasks")
    
    for t in service.get_all_tasks():
        print(t.model_dump_json(indent=2))
    
    service.complete_task(1)

    service.delete_task(2)
    for t in service.get_all_tasks():
        print(t.model_dump_json(indent=2))

        
    # print("welcome into your task tracker")
    # print("usage task [create|get_by_id|get_all|delete|done] args")
    
    # if len(sys.argv) < 2:
    #     print("no arguments where provided")
    #     return  
    # if len(sys.argv) ==2 and sys.argv[1] == "get_all":
    #     tasks = service.get_all_tasks()
    #     for task in tasks:
    #         print(task.model_dump_json(indent=2))
    #     return
    # if len(sys.argv) == 3:
    #     if sys.argv[1] == "create":
    #         task = service.create_task(sys.argv[2])
    #         print(task.model_dump_json(indent=4))
    #         return 
    #     if sys.argv[1] == "get_by_id":
    #         try:
    #             task = service.get_by_id(sys.argv[2])
    #             print(task.model_dump_json(indent=4))
    #         except ValueError as e:
    #             print(e)
    #         return 
    #     if sys.argv[1] == "delete":
    #         result = service.delete_task(sys.argv[2])
    #         if result:
    #             print("task deleted succsesfully")
    #         else:
    #             print("task was not found")
    #         return 
    #     if sys.argv[1] == "done":
    #         try:
    #             result = service.complete_task(sys.argv[2])
    #             print(result.model_dump_json(indent=4))
    #         except ValueError as e:
    #             print(e)
    #         return 
        



if __name__ == "__main__":
    main()