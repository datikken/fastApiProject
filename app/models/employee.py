from app.models import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime
import enum


class Gender(enum.Enum):
    M = 'M'
    F = 'F'


class Employee(Base):
    __tablename__ = 'employees'

    emp_no: Mapped[int] = mapped_column(primary_key=True)
    birth_date: Mapped[datetime.datetime]
    first_name: Mapped[str]
    last_name: Mapped[str]
    gender: Mapped[Gender]
    hire_date: Mapped[datetime.datetime]
