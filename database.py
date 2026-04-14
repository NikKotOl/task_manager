from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from tables import Base

engine = create_async_engine(url="sqlite+aiosqlite:///tasks.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print("БАЗА ОЧИЩЕНА")
        await conn.run_sync(Base.metadata.create_all)
        print("БАЗА ГОТОВА")

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print("БАЗА ОЧИЩЕНА")
