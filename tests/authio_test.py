from unittest import TestCase
from unittest.mock import patch
from services.io import AuthIO


class AuthIOTest(TestCase):
    def setUp(self):
        self.auth_io = AuthIO()

    @patch("builtins.input", side_effect=["username"])
    def test_get_username_valid(self, mock_input):
        username = self.auth_io.get_username()
        self.assertEqual(username, "username")

    @patch("builtins.input", side_effect=[""])
    @patch("builtins.print")
    def test_get_username_invalid(self, mock_print, mock_input):
        username = self.auth_io.get_username()
        self.assertEqual(username, "")

        mock_print.assert_called_once_with("Invalid username")
        mock_input.assert_has_calls([patch.call("Enter a username: "), patch.call("Enter a usernames: ")])

    @patch("builtins.input", side_effect=["password"])
    def test_get_password_valid(self, mock_input):
        password = self.auth_io.get_password()
        self.assertEqual(password, "password")

    @patch("builtins.input", side_effect=[""])
    @patch("builtins.print")
    def test_get_password_invalid(self, mock_print, mock_input):
        password = self.auth_io.get_password()
        self.assertEqual(password, "password")

    @patch("builtins.input", side_effect=[""])
    @patch("builtins.print")
    def test_get_password_invalid(self, mock_print, mock_input):
        password = self.auth_io.get_password()
        self.assertEqual(password, "")

        mock_print.assert_called_once_with("Invalid password")
        mock_input.assert_has_calls([patch.call("Enter a password"),])
