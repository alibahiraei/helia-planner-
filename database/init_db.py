from database.database import Base, engine
import database.models

def init_database():
    Base.metadata.create_all(bind=engine)