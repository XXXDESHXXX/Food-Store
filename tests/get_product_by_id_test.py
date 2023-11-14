from unittest import TestCase, main

from database import session_maker
from models import Product
from services.selectors.products import get_product_by_id


class GetProductByIdTest(TestCase):
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

    def test_get_product_by_id(self, *args, **kwargs) -> None:
        product = get_product_by_id(self.product.id)
        self.assertIsNotNone(product)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.id, self.product.id)
        self.assertEqual(product.price, self.product.price)
        self.assertEqual(product.amount, self.product.amount)
        self.assertEqual(product.name, self.product.name)


if __name__ == '__main__':
    main()
