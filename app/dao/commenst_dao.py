from app.dao.base import BaseDao
from app.models.comments_models import Comment


class CommentDao(BaseDao):
    model = Comment
