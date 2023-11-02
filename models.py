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
    amount: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("auth_user.id"))

    def __repr__(self):
        return (
            f"""
            PurchaseHistory(
            {self.id=},
            {self.product_name=},
            {self.amount=},
            {self.created_at=},
            {self.user_id=})
            """
        )


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(256), unique=True)
    amount: Mapped[int] = mapped_column()
    product_id: Mapped[int] = mapped_column(ForeignKey("purchase_history.id"))

    def __repr__(self):
        return (
            f"""
            Products(
            {self.id=},
            {self.product_name=},
            {self.amount=})
            """
        )