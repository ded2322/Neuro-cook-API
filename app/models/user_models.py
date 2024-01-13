from sqlalchemy import BOOLEAN, INTEGER, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]



    def __str__(self):
        return f"User {self.name}"
