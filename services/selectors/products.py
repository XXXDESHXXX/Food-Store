from sqlalchemy import select
from database import session_maker
from models import Product


def get_products() -> list[Product]:
    with session_maker() as session:
        query = (select(Product))
        result = session.execute(query)
        return result.scalars().all()


def get_product_name() -> list[Product]:
    with session_maker() as session:
        query = (select(Product.name))
        result = session.execute(query)
        return result.scalars().all()
    

def get_product_amount() -> list[str]:
    with session_maker() as session:
        query = (select(Product.amount))
        result = session.execute(query)
        return result.scalars().all()


def get_product_price() -> list[str]:
    with session_maker() as session:
        query = (select(Product.price))
        result = session.execute(query)
        return result.scalars().all()


if __name__ == '__main__':
    data = get_products()
    print(data)
