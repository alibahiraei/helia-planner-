from database.database import Base,engine
from database.models import Task
from services.task_service import TaskService

Base.metadata.create_all(bind=engine)

TaskService.creat_task(title='ورزش کردن',score=10)