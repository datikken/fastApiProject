from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime
import enum


class Gender(enum.Enum):
    M = 'M'
    F = 'F'


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = 'departments'

    dept_no: Mapped[int] = mapped_column(primary_key=True)
    dept_name: Mapped[str]


class Employee(Base):
    __tablename__ = 'employees'

    emp_no: Mapped[int] = mapped_column(primary_key=True)
    birth_date: Mapped[datetime.datetime]
    first_name: Mapped[str]
    last_name: Mapped[str]
    gender: Mapped[Gender]
    hire_date: Mapped[datetime.datetime]


class Title(Base):
    __tablename__ = 'titles'

    emp_no: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    from_date: Mapped[datetime.datetime]
    to_date: Mapped[datetime.datetime]


class Salary(Base):
    __tablename__ = 'salaries'

    emp_no: Mapped[int] = mapped_column(primary_key=True)
    salary: Mapped[int]
    from_date: Mapped[datetime.datetime]
    to_date: Mapped[datetime.datetime]
