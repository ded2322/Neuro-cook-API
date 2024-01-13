from pydantic import BaseModel

"""
С помощью библиотеки pydantic, позволяет провалидировать данные
"""


class SUserAuth(BaseModel):
    user_name: str
    password: str
