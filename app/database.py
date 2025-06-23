import asyncio
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app import model
from app.settings import Settings

settings = Settings()

print(settings.db_url)

engine = create_async_engine(settings.db_url, echo=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)



async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(model.Base.metadata.drop_all)
        await conn.run_sync(model.Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(setup_database())
