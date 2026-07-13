from sqlalchemy import Integer,String,DateTime,Boolean,Date
from sqlalchemy.orm import mapped_column,Mapped 
from database.database import Base
from datetime import datetime,date


class Task (Base):
    __tablename__="tasks"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100),nullable=False)
    score:Mapped[int] = mapped_column(Integer)
    task_date: Mapped[date] = mapped_column(
    Date,
    default=date.today
)
    is_active:Mapped[bool]= mapped_column(Boolean,default=True)
    created_at:Mapped[datetime] = mapped_column(DateTime,default= datetime.now)
    is_completed: Mapped[bool] = mapped_column(
    Boolean,
    default=False
)

