from database import session_maker
from models import PurchaseHistory


def save_purchase(product_id: int, user_id: int, amount: int) -> PurchaseHistory:
    with session_maker() as session:
        purchase = PurchaseHistory(
            product_id=product_id,
            user_id=user_id,
            amount=amount,
        )
        session.add(purchase)
        session.commit()
        session.refresh(purchase)
    return purchase
