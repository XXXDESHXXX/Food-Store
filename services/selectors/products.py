from sqlalchemy import select
from database import session_maker
from models import Product


def get_products() -> list[Product]:
    with session_maker() as session:
        query = (select(Product))
        result = session.execute(query)
        return result.scalars().all()
