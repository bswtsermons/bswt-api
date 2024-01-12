from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# Base = declarative_base()
# Base.query = db_session.query_property()


# def init_db():
#     from models.service import Service
#     Base.metadata.create_all(bind=engine)
