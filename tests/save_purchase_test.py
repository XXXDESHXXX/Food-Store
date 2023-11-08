from unittest import TestCase, main

from services.purchase_history import save_purchase


class SavePurchaseTest(TestCase):
    def test_valid_data(self) -> None:
        self.assertEqual(save_purchase("12456", 27.6, 27, 3), None)


if __name__ == "__main__":
    main()
