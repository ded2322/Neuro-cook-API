import logging
from fastapi import APIRouter, Depends

from core.generate.generate_recipe import generate_recipe


router = APIRouter(
    tags=["Генерация рецепта"]
)
LOGGER = logging.getLogger(__name__)
@router.post("/generate")
def generate_recipe(recipe = Depends(generate_recipe)):
    LOGGER.info("--Generate recipe--")
    """
    Позволяет генерировать рецепты на основе переданных пользователем продуктов
    """
    if not recipe:
        LOGGER.info("--Fail generate--")
        return "Fail generate"
    return recipe
