from models import PurchaseHistory
from database import session_maker


def save_purchase(
    product_name: str, total_price: float, amount: int, user_id: int
) -> None:
    with session_maker() as session:
        purchase = PurchaseHistory(
            product_name=product_name,
            total_price=total_price,
            amount=amount,
            user_id=user_id,
        )
        session.add(purchase)
        session.commit()
        session.refresh(purchase)
