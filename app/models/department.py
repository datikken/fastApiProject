from app.models import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Department(Base):
    __tablename__ = 'departments'

    dept_no: Mapped[int] = mapped_column(primary_key=True)
    dept_name: Mapped[str]
