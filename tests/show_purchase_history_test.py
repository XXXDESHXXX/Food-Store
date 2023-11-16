import io
from sys import stdout
from unittest import TestCase, main
from unittest.mock import patch

from humanize import naturalday

from database import session_maker
from models import PurchaseHistory
from services.io import show_purchase_history
from utils import create_test_product, create_test_user


class ShowPurchaseHistoryTest(TestCase):
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

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_purchase_history(self, mock_stdout: stdout, *args, **kwargs) -> None:
        show_purchase_history(user_id=self.user.id)
        output = mock_stdout.getvalue()
        self.assertTrue(naturalday(self.purchase_history.created_at) in output)
        self.assertTrue(str(self.purchase_history.amount) in output)
        self.assertTrue(str(self.purchase_history.product.price) in output)


if __name__ == "__main__":
    main()
