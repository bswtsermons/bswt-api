from typing import Optional, List
from datetime import date

from sqlalchemy import Integer, String, Date, ForeignKey
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from bswt.sqlalchemy import db


class Service(db.Model):
    __tablename__ = 'service'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ministered_on: Mapped[date]
    date_series: Mapped[int] = mapped_column(default=1)
    subseries_title: Mapped[str]
    subseries_part: Mapped[Optional[int]]
    series_name: Mapped[Optional[str]]
    series_part: Mapped[Optional[int]]

    # minister_id: Mapped[int] = mapped_column(ForeignKey('minister.id'))
    # minister: Mapped['Minister'] = relationship(back_populates='services')

