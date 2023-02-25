from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine("mysql+aiomysql://root:password@db:3306/employees?charset=utf8mb4")

async_session = async_sessionmaker(engine)
