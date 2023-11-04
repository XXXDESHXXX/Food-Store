from models import User
from database import session_maker
from services.io import AbstractAuthIO
from services.selectors.user import get_user


def create_user(username: str, password: str) -> None:
    with session_maker() as session:
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)


def authenticate(username: str, password: str) -> User | None:
    user = get_user(username)
    if user is None or user.password != password:
        return None
    return user


def log_in(auth_io: AbstractAuthIO) -> User:
    user = authenticate(auth_io.get_username(), auth_io.get_password())
    if user is None:
        print("The user with the provided credentials was not found.")
        return log_in(auth_io)
    return user
