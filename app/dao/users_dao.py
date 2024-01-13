from sqlalchemy import delete

from app.dao.base import BaseDao
from app.database import async_session_maker
from app.models.user_models import User


class UserDao(BaseDao):
    model = User

    @classmethod
    async def delete_user(cls,**user_id):
        #Попытка создать возможность удлаить аккаунт, но при этом отсавить комментарии
        try:
            async with async_session_maker() as session:
                user_delete = delete(cls.model).filter_by(**user_id)
                user_delete.deleted = True
                await session.execute(user_delete)
                await session.commit()

        except Exception as e:
            print(f"{str(e)}")
        return
