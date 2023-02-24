from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import inspect


class Base(DeclarativeBase):
    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class Department(Base):
    __tablename__ = 'departments'

    dept_no: Mapped[int] = mapped_column(primary_key=True)
    dept_name: Mapped[str]
