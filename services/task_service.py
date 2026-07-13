from database.database import engine,Base,SessionLocal
from database.models import Task
from sqlalchemy import select
from sqlalchemy import select, func
from datetime import date



class TaskService:


    @staticmethod
    def get_total_score(
        selected_date: date
    ) -> int:

        with SessionLocal() as session:

            total = session.scalar(

                select(func.sum(Task.score)).where(
                    Task.task_date == selected_date,
                    Task.is_completed == True
                )

            )

            return total or 0
    

    @staticmethod
    def create_task(
        title: str,
        score: int,
        task_date: date
    ) -> Task | None:

        with SessionLocal() as session:

            if not title.strip():
                return None

            task = Task(
                title=title,
                score=score,
                task_date=task_date
            )

            session.add(task)
            session.commit()
            session.refresh(task)

            return task
    @staticmethod
    def get_tasks_by_date(
        selected_date: date
    ) -> list[Task]:

        with SessionLocal() as session:

            result = session.scalars(

                select(Task).where(
                    Task.task_date == selected_date
                )

            )

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




