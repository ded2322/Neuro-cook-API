from fastapi import APIRouter, Depends, HTTPException, status

from app.dao.commenst_dao import CommentDao
from app.dao.recipe_dao import RecipeDao
from app.shemas.comments_shemas import SComment
from app.users.dependencies import get_current_user

router = APIRouter(
    tags=["комментарии"]
)


@router.post("/{id_post}-add_comments")
async def add_comment(id_post: int, user_input: SComment, data_user=Depends(get_current_user)):
    """
    Позволяет оставить комментарий к посту
    """
    # По переданному id ищет рецепт к котору относится комментарий
    post = await RecipeDao.find_one_or_none(id=id_post)
    # В случае отсутсвия поста вызывает ошибку
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Такого рецепта не существет")
    # Добавляет комментарий в базу данных
    await CommentDao.add(post_id=post["id"], text_comment=user_input.text_comment, user_name=(data_user["name"]))

    return {"message": "Комментарий успешно добавлен"}
