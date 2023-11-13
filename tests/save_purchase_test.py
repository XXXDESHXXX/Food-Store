from unittest import TestCase, main

from database import session_maker
from models import User, Product
from services.purchase_history import save_purchase


class SavePurchaseTest(TestCase):
    user = User(
        username="123456",
        password="123456789",
    )
    product = Product(
        price=10.99,
        amount=2,
        name="coffee",
    )

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
        purchase = save_purchase(self.product.id, self.user.id)
        self.assertEqual(purchase.user_id, self.user.id)
        self.assertEqual(purchase.product_id, self.product.id)
        with session_maker() as session:
            session.delete(purchase)
            session.commit()


if __name__ == "__main__":
    main()
