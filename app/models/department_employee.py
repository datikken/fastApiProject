from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime



class DepartmentEmployee(Base):
    __tablename__ = "dept_emp"

    dept_no: Mapped[int] = mapped_column(ForeignKey("departments.dept_no"), primary_key=True)
    emp_no: Mapped[int] = mapped_column(
        ForeignKey("employees.emp_no"), primary_key=True
    )
    from_date: Mapped[datetime.datetime]
    to_date: Mapped[datetime.datetime]
    department: Mapped[Department] = relationship()
    employee: Mapped[Employee] = relationship()


