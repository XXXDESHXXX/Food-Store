from unittest import TestCase, main

from database import session_maker
from models import User
from services.auth import create_user


class CreateUserTest(TestCase):
    def setUp(self) -> None:
        self.username = "testuser"
        self.password = "testpassword"

    def tearDown(self) -> None:
        with session_maker() as session:
            user = session.query(User).filter_by(username=self.username).first()
            if user:
                session.delete(user)

    def test_create_user(self, *args, **kwargs) -> None:
        create_user(self.username, self.password)
        with session_maker() as session:
            user = session.query(User).filter_by(username=self.username).first()
            self.assertIsNotNone(user)
            self.assertEqual(user.username, self.username)


if __name__ == "__main__":
    main()
