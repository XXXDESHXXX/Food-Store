from sqlalchemy import select
from database import session_maker
from models import PurchaseHistory


def get_purchase_history(user_id: int) -> list[PurchaseHistory]:
    with session_maker() as session:
        query = (
            select(PurchaseHistory)
            .where(PurchaseHistory.user_id == user_id)
            .order_by(PurchaseHistory.created_at.desc())
        )
        result = session.execute(query)
        return result.scalars().all()
