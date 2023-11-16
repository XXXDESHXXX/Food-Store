from unittest import TestCase, main

from database import session_maker
from services.selectors.products import get_products
from utils import create_test_product


class GetProductsTest(TestCase):
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

    def test_get_products(self, *args, **kwargs) -> None:
        products = get_products()
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0)
        self.assertEqual(any(map(lambda p: p.id == self.product.id, products)), True)


if __name__ == "__main__":
    main()
