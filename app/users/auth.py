# проходит авторизация и аутентификация пользователя
# проверка идет
from datetime import datetime, timedelta

from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext

from app.config import settings
from app.dao.users_dao import UserDao

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str)->str:
    """
    создается хешированный пароль, из полученного пароля
    """
    return pwd_context.hash(password)

def verify_password(input_password, hashed_password)->bool:
    """
    Получает введенный пользователем пароль и хешированный пароль,
    и проверяет соответсвие
    """
    return pwd_context.verify(input_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Создание токена для авторизации
    """
    # копирование словара с данными в переменную которая декодируется
    to_encode = data.copy()
    # переменная в которую записывается срок жизни токена
    # сегодняшний день + 12 часов
    expire = datetime.utcnow() + timedelta(hours=12)
    #обновление данных в словаре, с учетом новой жизни токена
    to_encode.update({"exp": expire})
    # создание токена с учетом новых данных, секретного ключа и алгоритма
    return jwt.encode(to_encode, settings.SECRET_KEY,settings.ALGORITHM)


async def authenticate_user( name_user:str,password:str):
    """
    Аутентификация пользователя
    """
    # Ищет имя пользователял в базе данных, и все данные к нему
    user = await UserDao.find_one_or_none(name= name_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Такого пользователя не существует")

    # Если введенный пароль не соответствует паролю в бд вызывается ошибка
    if not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Неверный пароль")

    return user





