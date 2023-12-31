from unittest import TestCase, main
from unittest.mock import patch
from services.io import get_amount


class GetAmountTest(TestCase):
    @patch("builtins.input", return_value="35")
    def test_get_amount(self, *args, **kwargs) -> None:
        self.assertEqual(get_amount(), "35")


if __name__ == "__main__":
    main()
