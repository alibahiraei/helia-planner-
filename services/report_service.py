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