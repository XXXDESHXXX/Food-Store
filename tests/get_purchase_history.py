from unittest import TestCase, main

from database import session_maker
from models import PurchaseHistory
from services.selectors.purchase_history import get_purchase_history
from utils import create_test_product, create_test_user


class GetPurchaseHistoryTest(TestCase):
    product = create_test_product()
    user = create_test_user()

    def setUp(self) -> None:
        with session_maker() as session:
            session.add_all((self.product, self.user))
            session.commit()
            session.refresh(self.product)
            session.refresh(self.user)
            self.purchase_history = PurchaseHistory(
                amount=2,
                user_id=self.user.id,
                product_id=self.product.id,
            )
            session.add(self.purchase_history)
            session.commit()
            session.refresh(self.purchase_history)

    def tearDown(self) -> None:
        with session_maker() as session:
            session.delete(self.purchase_history)
            session.delete(self.product)
            session.delete(self.user)
            session.commit()

    def test_get_purchase_history(self, *args, **kwargs) -> None:
        purchase_history = get_purchase_history(self.user.id)
        self.assertIsInstance(purchase_history, list)
        self.assertGreater(len(purchase_history), 0)
        self.assertEqual(
            any(map(lambda p: p.id == self.purchase_history.id, purchase_history)), True
        )


if __name__ == "__main__":
    main()
