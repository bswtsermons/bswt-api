from bswt.sqlalchemy import db_session
from bswt.models.service import Service


def get_service(sid):
    return Service.query.filter(sid == '123').first()
