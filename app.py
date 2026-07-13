from database.database import Base,engine
from database.models import Task
from services.task_service import TaskService
from ui.hom import show_home

Base.metadata.create_all(bind=engine)


tasks=TaskService.get_all_task()
show_home(tasks)

