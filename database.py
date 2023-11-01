from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import Config

Base = declarative_base()

engine = create_engine(Config.DB_DSN)
session_maker = sessionmaker(engine)


def create_tables() -> None:
    Base.metadata.create_all(engine)
