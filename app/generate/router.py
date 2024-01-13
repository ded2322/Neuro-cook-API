from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from app.generate.dependencies import generate_recipe
from app.users.dependencies import get_current_user

router = APIRouter(
    tags=["Генерация рецепта"]
)

#celery -A app.tasks.celery:celery worker --loglevel=INFO --pool=solo
@router.post("/generate")
#при желании можно подключить обязательную авторизацию пользователя, user=Depends(get_current_user)
def generate_recipe(recipe = Depends(generate_recipe)):
    """
    Позволяет генерировать рецепты на основе переданных пользователем данных

    Отадет в виде txt файла
    """
    return FileResponse(path=recipe, filename="generate_recipe.txt")
