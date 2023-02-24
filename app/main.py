from fastapi import FastAPI
from database.connection import engine
from database.models import Base
from database.models import Department
from database.connection import async_session
from sqlalchemy.sql import select

app = FastAPI()


@app.on_event('startup')
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    async with async_session.begin() as session:
        stmt = select(Department)
        data = await session.scalars(stmt)
        for dep in data.all():
            print(dep.dept_name)
    return data.all()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
