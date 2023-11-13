from unittest import TestCase, main
from unittest.mock import patch

from constants import MAX_PASSWORD_LENGTH, MIN_PASSWORD_LENGTH
from services.io import AuthIO
from validators import password_length_validator


class PasswordValidatorTest(TestCase):
    auth_io = AuthIO()
    max_password = "3" * MAX_PASSWORD_LENGTH + "1"

    @patch("builtins.input", return_value="123456789")
    def test_validate_password(self, *args, **kwargs) -> None:
        self.assertEqual(password_length_validator(self.auth_io.get_password)(), "123456789")

    @patch("builtins.input", side_effect=["12345", "123456789"])
    @patch("builtins.print")
    def test_minimum_password_length(self, mock_print: callable, *args, **kwargs) -> None:
        self.assertEqual(password_length_validator(self.auth_io.get_password)(), "123456789")
        mock_print.assert_called_with(
            f"Password length must be greater than {MIN_PASSWORD_LENGTH} or equal to {MAX_PASSWORD_LENGTH}"
        )

    @patch("builtins.input", side_effect=[max_password, "123456789"])
    @patch("builtins.print")
    def test_maximum_password_length(self, mock_print: callable, *args, **kwargs) -> None:
        self.assertEqual(password_length_validator(self.auth_io.get_password)(), "123456789")
        mock_print.assert_called_with(
            f"Password length must be greater than {MIN_PASSWORD_LENGTH} or equal to {MAX_PASSWORD_LENGTH}"
        )

    @patch("builtins.input", side_effect=["{}123//.", "123456789"])
    def test_prohibited_characters(self, *args, **kwargs) -> None:
        self.assertEqual(password_length_validator(self.auth_io.get_password)(), "123456789")


if __name__ == "__main__":
    main()
