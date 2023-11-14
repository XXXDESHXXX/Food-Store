from unittest import TestCase, main

from database import session_maker
from models import User
from services.selectors.user import get_user


class GetUserTest(TestCase):
    user = User(
        username="123456",
        password="123456789",
    )

    def setUp(self) -> None:
        with session_maker() as session:
            session.add(self.user)
            session.commit()
            session.refresh(self.user)

    def tearDown(self) -> None:
        with session_maker() as session:
            session.delete(self.user)
            session.commit()

    def test_get_user(self, *args, **kwargs):
        user = get_user(self.user.username)
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, self.user.id)
        self.assertEqual(user.username, self.user.username)
        self.assertEqual(user.password, self.user.password)


if __name__ == '__main__':
    main()
