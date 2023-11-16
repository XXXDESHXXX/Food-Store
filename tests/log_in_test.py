from unittest import TestCase, main
from unittest.mock import patch

from database import session_maker
from services.auth import log_in
from services.io import AuthIO
from utils import create_test_user


class LogInTest(TestCase):
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

    @patch("services.io.AuthIO.get_password", side_effect=["INVALID", user.password])
    @patch("services.io.AuthIO.get_username", side_effect=["INVALID", user.username])
    def test_log_in(self, *args, **kwargs):
        user = log_in(AuthIO())
        self.assertEqual(user.id, self.user.id)


if __name__ == "__main__":
    main()
