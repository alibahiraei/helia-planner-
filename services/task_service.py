from database.database import engine,Base,SessionLocal
from database.models import Task

class TaskService:

    @staticmethod
    def creat_task(title:str, score:int)->Task:
        with SessionLocal() as se:
            task=Task(title=title,score=score)
            se.add(task)
            se.commit()




