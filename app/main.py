from fastapi import FastAPI
from database.connection import engine
from database.models import Base
from database.models import Department
from database.connection import async_session
from sqlalchemy.sql import select
from fastapi.responses import JSONResponse

app = FastAPI()


@app.on_event('startup')
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/department/all")
async def root():
    async with async_session.begin() as session:
        data = await session.execute(select(Department))
        depts = [row._asdict() for row in data.scalars()]
    return JSONResponse(content=depts)
