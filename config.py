import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USER = os.getenv("DB_USER")
    DB_DSN = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:"
        f"{DB_PASSWORD}@"
        f"{DB_HOST}/"
        f"{DB_NAME}"
    )
