from flask import Flask
from bswt.sqlalchemy import db_session
from bswt.service import get_service

app = Flask(__name__)

@app.route("/service", methods=['GET'])
def app_get_service():
    return get_service('123'), 200

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()