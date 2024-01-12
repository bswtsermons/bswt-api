from typing import Optional, List
from datetime import datetime

from sqlalchemy import Integer, String, Date, ForeignKey
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from bswt.sqlalchemy import Base


class Minister(Base):
    __tablename__ = 'minister'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[Optional[str]]

    services: Mapped[List['Service']] = relationship(
        back_populates='minister', cascade='all, delete-orphan'
    )
