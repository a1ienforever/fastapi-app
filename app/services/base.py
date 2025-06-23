from sqlalchemy import select

from app.database import SessionDep


class BaseService:
    model = None

    @classmethod
    async def find_all(cls, session: SessionDep):
        query = select(cls.model)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def find_by_id(cls, session: SessionDep, model_id: int):
        query = select(cls.model).filter_by(id=model_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, session: SessionDep, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def create(cls, session: SessionDep, data: dict):
        query = cls.model(**data)
        session.execute(query)
        session.commit()

