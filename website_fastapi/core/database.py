from typing import Generator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from website_fastapi.core.configs import get_settings
settings = get_settings()

DB_URL: str = 'postgresql://postgres:'
 
engine = create_engine(settings.DB_URL)


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# async def create_tables() -> None:
#     import models.__all_models
#     print('criando tabelas')
#     async with engine.begin() as conn:
#         await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
#         await conn.run_sync(settings.DBBaseModel.metadata.create_all)
