from sqlalchemy import INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.shemas.recipe_shemas import SPost


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name_recipe: Mapped[str]
    text_preview: Mapped[str]
    text_post: Mapped[str]

    def to_read_model(self) -> SPost:
        return SPost(
            name_recipe=self.name_recipe,
            text_preview=self.text_preview,
            text_post=self.text_post
        )

    def __str__(self):
        return f"Recipe id {self.id}"
