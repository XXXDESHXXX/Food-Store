from unittest import TestCase, main
from unittest.mock import patch

from constants import MAX_USERNAME_LENGTH
from services.io import AuthIO
from validators import username_length_validator


class UsernameValidatorTest(TestCase):
    auth_io = AuthIO()

    @patch("builtins.input", return_value="USERTEST")
    def test_validate_username(self, *args, **kwargs) -> None:
        self.assertEqual(username_length_validator(self.auth_io.get_username)(), "USERTEST")

    def test_minimum_username_length(self) -> None:
        with self.assertRaises(ValueError) as e:
            get_username("User123")
        self.assertEqual(
            "Username length must be greater than 8 or equal to 48", e.exception.args[0]
        )

    def test_maximum_username_length(self) -> None:
        username = "3" * MAX_USERNAME_LENGTH + "1"
        with self.assertRaises(ValueError) as e:
            get_username(username)
        self.assertEqual(
            "Username length must be greater than 8 or equal to 48", e.exception.args[0]
        )


if __name__ == "__main__":
    main()
