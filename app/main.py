from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.database.connection import engine
from app.service.employee import employeeService
from app.service.department import departmentService
from app.models import Base

app = FastAPI()


@app.on_event('startup')
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/employee/all")
async def employees():
    emps = await employeeService.get_employees()
    return JSONResponse(content=emps)


@app.get("/department/all")
async def departments():
    depts = await departmentService.get_departments()
    return JSONResponse(content=depts)
