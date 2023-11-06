from datetime import datetime

from database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "auth_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(48), unique=True)
    password: Mapped[str] = mapped_column(String(256))

    def __repr__(self):
        return (
            f"""
            User(
            {self.id=},
            {self.username=},
            {self.password=})
            """
        )


class PurchaseHistory(Base):
    __tablename__ = "purchase_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(256))
    total_price: Mapped[float] = mapped_column()
    amount: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("auth_user.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))

    def __repr__(self):
        return (
            f"""
            PurchaseHistory(
            {self.id=},
            {self.total_price=}
            {self.product_name=},
            {self.amount=},
            {self.created_at=},
            {self.user_id=})
            """
        )


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column()
    product_name: Mapped[str] = mapped_column(String(256), unique=True)
    amount: Mapped[int] = mapped_column()
    history_id: Mapped[int] = mapped_column()

    def __repr__(self):
        return (
            f"""
            Product(
            {self.id=},
            {self.price=},
            {self.product_name=},
            {self.amount=}
            {self.history_id=})
            """
        )
