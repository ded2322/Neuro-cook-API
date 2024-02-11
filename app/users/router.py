from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.dao.users_dao import UserDao
from app.shemas.users_shemas import SUserAuth
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dependencies import get_current_user

"""
Этот модуль позволяет создавать и аутентифицировать пользователя
"""

router = APIRouter(
    prefix="/user",
    tags = ["Пользователи"]
)

@router.post("/register",status_code=201)
async def register_user(user_data: SUserAuth):
    """
    Позоваляет создать пользователя, если его не существует
    """
    # проверка существует ли пользователь с похожим ником
    if await UserDao.find_one_or_none(name = user_data.user_name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Пользователь с таким ником уже существует")

    # хеширует пароль
    hashed_password = get_password_hash(user_data.password)
    # добавление нового пользователя в базу данных
    await UserDao.add(name=user_data.user_name,password= hashed_password)

    return {"message": "Пользователь успешно зарегистрирован"}

@router.post("/login")
async def login_user(response: Response,user_data: SUserAuth):
    """
    Позволяет пользователям войти в свои аккаунты и создает токен доступа
    """
    # аутентифицирует пользователя
    user = await authenticate_user(user_data.user_name,user_data.password)
    # создает токена доступа
    access_token = create_access_token({"sub": str(user.id)})
    # даем браузеру созданный токен доступа
    response.set_cookie("access_token",access_token,httponly=True)
    return {"access_token": access_token}

@router.post("/logout")
def logout_user(response:Response):
    """
    Позволяет выйти из аккаунта и удалить токен доступа
    """
    response.delete_cookie("access_token")
    return {"message": "вы вышли из аккаунта"}

@router.delete("/delete",status_code=204)
async def delete_user(user_data = Depends(get_current_user)):
    """
    Позволяет удалить запись об аккаунте из базы данных

    Удаляет данные только при условии, если у пользовтеля нет комментариев
    """
    await UserDao.delete(name = user_data["name"])
    return {"message":"вы удалили аккаунт"}

@router.put("/change")
async def update_data(new_name:str, user_data = Depends(get_current_user)):
    """
    НЕ РАБОТАЕТ
    Позволяет изменить имя пользователя
    """
    await UserDao.update_data(user_data["id"],"name",new_name)

    return {"message":"вы изменили имя"}
