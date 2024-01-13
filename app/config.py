from typing import Literal

from pydantic_settings import BaseSettings


class settings(BaseSettings):
    MODE: Literal["DEV","TEST","PROD"]
    LOG_LEVEL:str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    URL_CACHE: str
    @property
    def DATABASE_URL(self):

        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = '.env'

settings = settings()

