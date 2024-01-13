from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_cache.decorator import cache

from app.dao.recipe_dao import RecipeDao
from app.shemas.recipe_shemas import SPost
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/recipes",
    tags=["Страницы рецепта"]
)


@router.get("/{id_recipe}")
@cache(expire=60)
async def post_recipe(id_recipe: int):
    """
    Осущетсвляет поиск поста по id в url
    """
    # По переданному в url id ищит рецепт
    recipe = await RecipeDao.find_one_or_none(id=id_recipe)

    if not recipe:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такого поста не сущетствует")

    return recipe


@router.get("/")
async def show_recipe():
    """
    Показывает все доступыне рецeпты в базе данных
    """

    all_recipe = await RecipeDao.show_table()
    #В случае если база данных пуста выдает ошибку
    if not all_recipe:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="База данных пуста милорд")

    return all_recipe


@router.post("/add_recipe")
async def add_recipe(data_recipe: SPost, post=Depends(get_current_user)):
    """
    Добавление рецепта в базу данных

    Только при наличии доступного токена
    """
    # Проверяет наличие в базе данных схожих записей по имени
    name_recipe = await RecipeDao.find_one_or_none(name_recipe=data_recipe.name_recipe)
    if name_recipe:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Рецепт с таким названием уже существует")

    await RecipeDao.add(name_recipe=data_recipe.name_recipe, text_preview=data_recipe.text_preview,
                        text_post=data_recipe.text_post)

    return {"message": "Рецепт успешно добавлен"}


@router.delete("/delete_recipe")
async def delete_recipe(recipe_name: str, user=Depends(get_current_user)):
    """
    Позволяет удалить рецепты и все прекрепленыне комментарии
    """
    #проверяем наличие рецепта в базе данных
    name_recipe = await RecipeDao.find_one_or_none(name_recipe=recipe_name)
    if not name_recipe:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такого рецепта не существует")

    #удаляет рецепт по id
    await RecipeDao.delete(name_recipe = recipe_name)

    return {"message": "Рецепт успешно удален"}
