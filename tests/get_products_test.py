from unittest import TestCase, main

from database import session_maker
from models import Product
from services.selectors.products import get_products


class GetProductsTest(TestCase):
    product = Product(
        price=10.99,
        amount=2,
        name="coffee",
    )

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


if __name__ == '__main__':
    main()
