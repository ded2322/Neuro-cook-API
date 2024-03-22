from fastapi import APIRouter, Depends
from core.generate.generate_recipe import generate_recipe

router = APIRouter(
    tags=["Генерация рецепта"]
)


@router.post("/generate")
def generate_recipe(recipe=Depends(generate_recipe)):
    """
    Позволяет генерировать рецепты на основе переданных пользователем продуктов
    """
    if not recipe:
        return "Fail generate"
    return recipe
