from sqladmin import ModelView

from app.models.recipe_models import Recipe
from app.models.user_models import User


class UserAdmin(ModelView, model=User):

    name = "Пользователь"
    name_plural = "Пользователи"

    column_list = [User.id, User.name]
    column_details_exclude_list = [User.password]

    can_edit = False
    can_delete = False


class RecipeAdmin(ModelView, model=Recipe):
    name = "Рецепт"
    name_plural = "Рецепты"
    column_list = [Recipe.name_recipe, Recipe.text_preview]

