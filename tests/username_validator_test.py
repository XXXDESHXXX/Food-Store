from unittest import TestCase, main

from constants import MAX_USERNAME_LENGTH
from validators import get_username


class UsernameValidatorTest(TestCase):
    def test_validate_username(self) -> None:
        self.assertEqual(get_username("USERTEST"), None)

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
