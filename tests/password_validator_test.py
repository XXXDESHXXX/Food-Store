from unittest import TestCase, main
from validators import validate_password


class PasswordValidatorTest(TestCase):
    def test_validate_password(self):
        self.assertEqual(validate_password("123456789"), None)

    def test_minimum_password_length(self):
        with self.assertRaises(ValueError) as e:
            validate_password("12345")
        self.assertEqual("Password length must be greater than 6 or equal to 256", e.exception.args[0])

    def test_maximum_password_length(self):
        password = (
            "3" * 257
        )
        with self.assertRaises(ValueError) as e:
            validate_password(password)
        self.assertEqual("Password length must be greater than 6 or equal to 256", e.exception.args[0])

    def test_prohibited_characters(self):
        with self.assertRaises(ValueError) as e:
            validate_password("{}12345678//.")


if __name__ == "__main__":
    main()
