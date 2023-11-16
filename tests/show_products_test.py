import io
from sys import stdout
from unittest import TestCase, main
from unittest.mock import patch

from database import session_maker
from services.io import show_products
from utils import create_test_product


class ShowProductsTest(TestCase):
    product = create_test_product()

    def setUp(self) -> None:
        with session_maker() as session:
            session.add(self.product)
            session.commit()
            session.refresh(self.product)

    def tearDown(self) -> None:
        with session_maker() as session:
            session.delete(self.product)
            session.commit()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_products(self, mock_stdout: stdout, *args, **kwargs) -> None:
        show_products()
        output = mock_stdout.getvalue()
        self.assertTrue(self.product.name in output)
        self.assertTrue(str(self.product.price) in output)
        self.assertTrue(str(self.product.amount) in output)


if __name__ == "__main__":
    main()
