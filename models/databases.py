from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_NAME


engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db():
    from models.model import Person, Quests, Side_info, Level_info, Quests_steps
    Base.metadata.create_all(engine)
