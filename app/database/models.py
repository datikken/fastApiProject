from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import inspect
import datetime
import enum


class Gender(enum.Enum):
    M = 'M'
    F = 'F'


class Base(DeclarativeBase):
    # TODO: decide maybe remove
    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class Employee(Base):
    __tablename__ = 'employees'

    emp_no: Mapped[int] = mapped_column(primary_key=True)
    birth_date: Mapped[datetime.datetime]
    first_name: Mapped[str]
    last_name: Mapped[str]
    gender: Mapped[Gender]
    hire_date: Mapped[datetime.datetime]


class Department(Base):
    __tablename__ = 'departments'

    dept_no: Mapped[int] = mapped_column(primary_key=True)
    dept_name: Mapped[str]
