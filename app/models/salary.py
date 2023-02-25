from app.app.models import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime


class Salary(Base):
    __tablename__ = 'salaries'

    emp_no: Mapped[int] = mapped_column(primary_key=True)
    salary: Mapped[int]
    from_date: Mapped[datetime.datetime]
    to_date: Mapped[datetime.datetime]
