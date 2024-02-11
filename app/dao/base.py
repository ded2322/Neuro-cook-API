from sqlalchemy import delete, insert, select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.logger import logger

class BaseDao:
    model = None

    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**kwargs)
            result = await session.execute(query)
            return result.mappings().one_or_none()
    @classmethod
    async def show_table(cls):
        try:
            async with async_session_maker() as session:
                query = select(cls.model)
                result = await session.execute(query)
                return result.mappings().all()
        except (SQLAlchemyError,Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc:"
            elif isinstance(e, Exception):
                msg = "Unknown Exc:"
            msg += " can't show table"
            logger.error(msg, extra={"table":cls.model.__table__},exc_info=True)

            return None


    @classmethod
    async def add(cls, **data):
        try:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            async with async_session_maker() as session:
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()
        except (SQLAlchemyError,Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc:"
            elif isinstance(e, Exception):
                msg = "Unknown Exc:"

            msg +="Cannot insert data into table"
            logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
            return None


    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            try:
                query = delete(cls.model).filter_by(**filter_by)
                await session.execute(query)
                await session.commit()
            except (SQLAlchemyError, Exception) as e:
                if isinstance(e, SQLAlchemyError):
                    msg = "Database Exc:"
                elif isinstance(e, Exception):
                    msg = "Unknown Exc:"

                msg += "Cannot delete data into table"
                logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
                return None

    @classmethod
    async def update_data(cls,id_user,column,update_data):
        async with async_session_maker() as session:
            try:

                query = await session.get(cls.model,id_user)
                setattr(query,column,update_data)
                await session.commit()
            except (SQLAlchemyError, Exception) as e:
                if isinstance(e, SQLAlchemyError):
                    msg = "Database Exc:"
                elif isinstance(e, Exception):
                    msg = "Unknown Exc:"

                msg += "data update error"
                logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
                return None