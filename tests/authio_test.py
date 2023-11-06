from unittest import TestCase, main
from unittest.mock import patch

from services.io import AuthIO


class AuthIOTest(TestCase):
    @patch("builtins.input", side_effect=["valid_username"])
    def test_get_valid_username(self, mock_input):
        auth_io = AuthIO()
        username = auth_io.get_username()
        self.assertEqual(username, None)

    @patch("builtins.input", side_effect=["invalid_username", "valid_username"])
    def test_get_invalid_username(self, mock_input):
        auth_io = AuthIO()
        username = auth_io.get_username()
        self.assertEqual(username, None)

    @patch("builtins.input", side_effect=["valid_password"])
    def test_get_valid_password(self, mock_input):
        auth_io = AuthIO()
        password = auth_io.get_password()
        self.assertEqual(password, None)

    @patch("builtins.input", side_effect=["invalid_password", "valid_password"])
    def test_get_invalid_password(self, mock_input):
        auth_io = AuthIO()
        password = auth_io.get_password()
        self.assertEqual(password, None)


if __name__ == "__main__":
    main()



