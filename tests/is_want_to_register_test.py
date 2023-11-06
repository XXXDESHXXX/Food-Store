from unittest import TestCase, main
from unittest.mock import patch
from services.io import is_want_to_register


class IsWantToRegisterTest(TestCase):

    @patch("builtins.input", return_value="1")
    def test_valid_register_option(self, mock_input):
        self.assertTrue(is_want_to_register())

    @patch("builtins.input", return_value="2")
    def test_valid_login_option(self, mock_input):
        self.assertFalse(is_want_to_register())

    @patch("builtins.input", side_effect=["3", "1"])
    @patch("builtins.print")
    def test_invalid_option_then_valid_register_option(self, mock_print, mock_input):
        self.assertTrue(is_want_to_register())
        mock_print.assert_called_with("Invalid option selected")


if __name__ == '__main__':
    main()