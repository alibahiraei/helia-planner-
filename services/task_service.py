from database.database import engine,Base,SessionLocal
from database.models import Task
from sqlalchemy import select
from sqlalchemy import select, func



class TaskService:


    @staticmethod
    def get_total_score() -> int:

        with SessionLocal() as session:

            total = session.scalar(
                select(func.sum(Task.score))
                .where(Task.is_completed == True)
            )

            return total or 0

    @staticmethod
    def create_task(title:str, score:int)->Task:
        with SessionLocal() as se:
            task=Task(title=title,score=score)
            if not title.strip():
                return
            se.add(task)
            se.commit()
    @staticmethod
    def get_all_task()->list[Task]:
        with SessionLocal() as se:
            result=se.scalars(select(Task))
            return result.all()
    @staticmethod
    def update_task_status(task_id: int, completed: bool) -> None:
        with SessionLocal() as se:
        
            task = se.get(Task, task_id)

            if task is None:
                return

            task.is_completed = completed

            se.commit()
    @staticmethod
    def delete_task(task_id: int) -> None:
        with SessionLocal() as session:

            task = session.get(Task, task_id)

            if task is None:
                return

            session.delete(task)

            session.commit()




