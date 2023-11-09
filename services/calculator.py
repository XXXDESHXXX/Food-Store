from services.selectors.products import get_product_price
from services.io import get_amount


def calculate() -> float:
    amount = get_amount()
    price = get_product_price()
    return price * int(amount)

