from unittest import TestCase, main
from validators import validate_username


class UsernameValidatorTest(TestCase):
    def test_validate_username(self):
        self.assertEqual(validate_username("USERTEST"), None)

    def test_minimum_username_length(self):
        with self.assertRaises(ValueError) as e:
            validate_username("User123")
        self.assertEqual("Username length must be greater than 8 or equal to 48", e.exception.args[0])

    def test_maximum_username_length(self):
        username = (
            "3" * 51
        )
        with self.assertRaises(ValueError) as e:
            validate_username(username)
        self.assertEqual("Username length must be greater than 8 or equal to 48", e.exception.args[0])


if __name__ == "__main__":
    main()
