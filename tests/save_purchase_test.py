from unittest import TestCase, main

from database import session_maker
from models import User
from services.purchase_history import save_purchase
from utils import create_test_product


class SavePurchaseTest(TestCase):
    user = User(
        username="123456",
        password="123456789",
    )
    product = create_test_product()

    def setUp(self) -> None:
        with session_maker() as session:
            session.add_all((self.product, self.user))
            session.commit()
            session.refresh(self.product)
            session.refresh(self.user)

    def tearDown(self) -> None:
        with session_maker() as session:
            session.delete(self.product)
            session.delete(self.user)
            session.commit()

    def test_save_purchase(self, *args, **kwargs) -> None:
        amount = 2
        purchase = save_purchase(self.product.id, self.user.id, amount)
        self.assertEqual(purchase.user_id, self.user.id)
        self.assertEqual(purchase.product_id, self.product.id)
        self.assertEqual(purchase.amount, amount)
        with session_maker() as session:
            session.delete(purchase)
            session.commit()


if __name__ == "__main__":
    main()
