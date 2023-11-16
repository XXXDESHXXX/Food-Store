from unittest import TestCase, main

from database import session_maker
from services.auth import authenticate
from utils import create_test_user


class AuthenticateTest(TestCase):
    user = create_test_user()

    def setUp(self) -> None:
        with session_maker() as session:
            session.add(self.user)
            session.commit()
            session.refresh(self.user)

    def tearDown(self) -> None:
        with session_maker() as session:
            session.delete(self.user)
            session.commit()

    def test_authenticate(self, *args, **kwargs):
        user = authenticate(self.user.username, self.user.password)
        self.assertEqual(user.id, self.user.id)


if __name__ == "__main__":
    main()
