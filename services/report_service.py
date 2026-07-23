from datetime import date, timedelta

from sqlalchemy import select

from database.database import SessionLocal
from database.models import Task

class ReportService:

    @staticmethod
    def get_today_report():

        today = date.today()

        with SessionLocal() as session:

            tasks = session.scalars(

                select(Task).where(
                    Task.task_date == today
                )

            ).all()

        return tasks
    @staticmethod
    def get_today_score():

        tasks = ReportService.get_today_report()

        return sum(

            task.score

            for task in tasks

            if task.is_completed

        )
    @staticmethod
    def get_today_completed():

        tasks = ReportService.get_today_report()

        return len(

            [

                task

                for task in tasks

                if task.is_completed

            ]

        )
    @staticmethod
    def get_today_total():

        return len(

            ReportService.get_today_report()

        )
    @staticmethod
    def get_today_tasks():

        return ReportService.get_today_report()
    @staticmethod
    def get_total_score(tasks: list[Task]) -> int:

        return sum(

            task.score

            for task in tasks

            if task.is_completed

        )
    
    @staticmethod
    def get_tasks_between(
        start_date: date,
        end_date: date
    ) -> list[Task]:

        with SessionLocal() as session:

            result = session.scalars(

                select(Task).where(

                    Task.task_date >= start_date,

                    Task.task_date <= end_date

                )

            )

            return result.all()
        
    @staticmethod
    def get_completed_count(
        tasks: list[Task]
    ) -> int:

        return len(

            [

                task

                for task in tasks

                if task.is_completed

            ]

        )
    @staticmethod
    def get_possible_score(
        tasks: list[Task]
    ) -> int:

        return sum(

            task.score

            for task in tasks

        )
    @staticmethod
    def get_remaining_tasks(
        tasks: list[Task]
    ) -> list[Task]:

        return [

            task

            for task in tasks

            if not task.is_completed

        ]
    @staticmethod
    def get_completed_tasks(
        tasks: list[Task]
    ) -> list[Task]:

        return [

            task

            for task in tasks

            if task.is_completed

    ]