from unittest import TestCase, main
from services.calculator import calculate_price


class CalculatePriceTest(TestCase):
    def test_calculate_price(self) -> None:
        self.assertEqual(calculate_price(2, 2.5), 5)


if __name__ == '__main__':
    main()
