from sqlalchemy import select
from database import session_maker
from models import User


def get_user(username: str) -> User | None:
    with session_maker() as session:
        query = select(User).where(User.username == username)
        result = session.execute(query)
        return result.scalar_one_or_none()
