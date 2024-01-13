from sqlalchemy import INTEGER, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"))
    text_comment: Mapped[str]
    user_name: Mapped[str] = mapped_column(ForeignKey("user.name"))




    def __str__(self):
        return f"Name user {self.user_name}, post {self.post_id}"
