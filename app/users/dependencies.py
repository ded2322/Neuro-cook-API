"""
В этом модуле проверяется токен (куки) в браузере
"""
from fastapi import Depends, HTTPException, Request, status
from jose import jwt

from app.config import settings
from app.dao.users_dao import UserDao
from app.shemas.users_shemas import SUserAuth


def get_token(request: Request):
    """
    Проверяет наличие токена в браузере
    """
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def get_current_user(token: str = Depends(get_token)):
    """
    Вызывает проверку токена, расшифровыет его,
    ищет по id юзера и позращет при наличии строку из бд
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UserDao.find_one_or_none(id=int(user_id))
    return user

