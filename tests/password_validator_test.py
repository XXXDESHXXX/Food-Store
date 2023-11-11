from unittest import TestCase, main

from constants import MAX_PASSWORD_LENGTH
from validators import get_password


class PasswordValidatorTest(TestCase):
    def test_validate_password(self) -> None:
        self.assertEqual(get_password("123456789"), None)

    def test_minimum_password_length(self) -> None:
        with self.assertRaises(ValueError) as e:
            get_password("12345")
        self.assertEqual(
            "Password length must be greater than 6 or equal to 256",
            e.exception.args[0],
        )

    def test_maximum_password_length(self) -> None:
        password = "3" * MAX_PASSWORD_LENGTH + "1"
        with self.assertRaises(ValueError) as e:
            get_password(password)
        self.assertEqual(
            "Password length must be greater than 6 or equal to 256",
            e.exception.args[0],
        )

    def test_prohibited_characters(self) -> None:
        with self.assertRaises(ValueError):
            get_password("{}12345678//.")


if __name__ == "__main__":
    main()
