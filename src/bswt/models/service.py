from sqlalchemy import Column, Integer, String
from bswt.sqlalchemy import Base

class Service(Base):
    __tablename__ = 'service'
    sid = Column(Integer, primary_key=True)