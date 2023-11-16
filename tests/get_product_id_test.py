from unittest import TestCase, main
from unittest.mock import patch
from services.io import get_product_id


class GetProductNameTest(TestCase):
    @patch("builtins.input", return_value=1)
    def test_get_id(self, *args, **kwargs) -> None:
        self.assertEqual(get_product_id(), 1)


if __name__ == "__main__":
    main()
