from app.dao.base import BaseDao
from app.models.recipe_models import Recipe


class RecipeDao(BaseDao):
    model = Recipe
