from ..models.employee import Employee
from ..database.connection import async_session
from sqlalchemy.sql import select
from fastapi.encoders import jsonable_encoder


class EmployeeService():
    async def get_employees(self):
        async with async_session.begin() as session:
            data = await session.execute(select(Employee))
            return [jsonable_encoder(row) for row in data.scalars()]

employeeService = EmployeeService()
