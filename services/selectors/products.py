from sqlalchemy import select
from database import session_maker
from models import Product


def get_products() -> list[Product]:
    with session_maker() as session:
        query = select(Product)
        result = session.execute(query)
        return result.scalars().all()


def get_product_by_id(identifier: int) -> Product | None:
    with session_maker() as session:
        query = select(Product).where(Product.id == identifier)
        result = session.execute(query)
        return result.scalars().one_or_none()
