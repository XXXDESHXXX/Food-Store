from unittest import TestCase, main
from unittest.mock import patch

from services.io import get_amount
from validators import validate_amount


class AmountValidatorTest(TestCase):
    @patch("builtins.input", return_value="254")
    def test_valid_amount(self, *args, **kwargs) -> None:
        self.assertEqual(validate_amount(get_amount)(), "254")

    @patch("builtins.input", return_value="abc")
    @patch("builtins.print")
    def test_invalid_amount(self, mock_print, *args, **kwargs) -> None:
        get_amount()
        mock_print.assert_called_with(
            "abc is not valid amount"
        )


if __name__ == '__main__':
    main()
