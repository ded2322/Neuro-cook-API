from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

# данные для подключения к бд
#  driver://user:pass@localhost/dbname
# Передается алхимии бд
engine = create_async_engine(settings.DATABASE_URL)
# генератор сессий
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
