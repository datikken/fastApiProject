from app.app.models import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime


class Title(Base):
    __tablename__ = 'titles'

    emp_no: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    from_date: Mapped[datetime.datetime]
    to_date: Mapped[datetime.datetime]
