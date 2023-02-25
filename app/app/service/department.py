from ..database.models import Department
from ..database.connection import async_session
from sqlalchemy.sql import select
from fastapi.encoders import jsonable_encoder


class DepartmentService():
    async def get_departments(self):
        async with async_session.begin() as session:
            data = await session.execute(select(Department))
            return [jsonable_encoder(row) for row in data.scalars()]


departmentService = DepartmentService()
