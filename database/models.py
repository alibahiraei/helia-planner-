from sqlalchemy import Integer,String,DateTime,Boolean
from sqlalchemy.orm import mapped_column,Mapped 
from database.database import Base
from datetime import datetime


class Task (Base):
    __tablename__="tasks"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String)
    score:Mapped[int] = mapped_column(Integer)
    is_active:Mapped[bool]= mapped_column(Boolean,default=True)
    created_at:Mapped[datetime] = mapped_column(DateTime,default= datetime.now)

