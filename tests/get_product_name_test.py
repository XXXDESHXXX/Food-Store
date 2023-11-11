from unittest import TestCase, main
from unittest.mock import patch
from services.io import get_product_name


class GetProductNameTest(TestCase):
    @patch("builtins.input", return_value="milk")
    def test_valid_product_name(self, mock_input) -> None:
        self.assertEqual(get_product_name(), "milk")


if __name__ == '__main__':
    main()
