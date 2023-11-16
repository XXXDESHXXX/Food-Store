from unittest import TestCase, main
from unittest.mock import patch

from constants import MAX_USERNAME_LENGTH, MIN_USERNAME_LENGTH
from services.io import AuthIO
from validators import username_length_validator


class UsernameValidatorTest(TestCase):
    auth_io = AuthIO()
    max_username = "3" * MAX_USERNAME_LENGTH + "1"

    @patch("builtins.input", return_value="USERTEST")
    def test_validate_username(self, *args, **kwargs) -> None:
        self.assertEqual(
            username_length_validator(self.auth_io.get_username)(), "USERTEST"
        )

    @patch("builtins.input", side_effect=["USER", "VALID_USER"])
    @patch("builtins.print")
    def test_minimum_username_length(self, mock_print: print, *args, **kwargs) -> None:
        self.assertEqual(
            username_length_validator(self.auth_io.get_username)(), "VALID_USER"
        )
        mock_print.assert_called_with(
            f"Username length must be greater than {MIN_USERNAME_LENGTH} or equal to {MAX_USERNAME_LENGTH}"
        )

    @patch("builtins.input", side_effect=[max_username, "VALID_USER"])
    @patch("builtins.print")
    def test_maximum_username_length(self, mock_print: print, *args, **kwargs) -> None:
        self.assertEqual(
            username_length_validator(self.auth_io.get_username)(), "VALID_USER"
        )
        mock_print.assert_called_with(
            f"Username length must be greater than {MIN_USERNAME_LENGTH} or equal to {MAX_USERNAME_LENGTH}"
        )


if __name__ == "__main__":
    main()
