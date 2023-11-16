from models import User, Product


def create_test_user() -> User:
    return User(
        username="123456",
        password="123456789",
    )


def create_test_product() -> Product:
    return Product(
        price=10.99,
        amount=2,
        name="testproduct",
    )
