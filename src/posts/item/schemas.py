from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Item(Base):

    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    name: Mapped[str] = mapped_column(nullable=True)
    point: Mapped[float] = mapped_column(default=400.0)
    price: Mapped[float] = mapped_column(nullable=True)
