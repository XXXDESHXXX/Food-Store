from datetime import datetime

from database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "auth_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(48), unique=True)
    password: Mapped[str] = mapped_column(String(256))
    purchase_histories: Mapped[list["PurchaseHistory"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"User(" f"{self.id=}," f"{self.username=}," f"{self.password=})"


class PurchaseHistory(Base):
    __tablename__ = "purchase_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("auth_user.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    user: Mapped[User] = relationship(back_populates="purchase_histories")

    def __repr__(self):
        return (
            f"PurchaseHistory("
            f"{self.id=},"
            f"{self.created_at=},"
            f"{self.user_id=},"
            f"{self.product_id})"
        )


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float]
    name: Mapped[str] = mapped_column(String(256), unique=True)
    amount: Mapped[int]

    def __repr__(self):
        return (
            f"Product("
            f"{self.id=},"
            f"{self.price=},"
            f"{self.name=},"
            f"{self.amount=},"
            f"{self.history_id=})"
        )
