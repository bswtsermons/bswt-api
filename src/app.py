Rrom datetime import datetime

from flask import Flask, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

# from bswt.sqlalchemy import db_session
# # from bswt.service import get_service
from bswt.models.service import Service
from bswt.models.minister import Minister
# from bswt.models.minister import Minister
from bswt.sqlalchemy import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/service", methods=['POST'])
def create_service():
    service = Service(
        ministered_on=datetime.fromisoformat(request.form['ministered_on']),
        date_series=request.form['date_series'],
        subseries_title=request.form['subseries_title']
    )
    db.session.add(service)
    db.session.commit()

    return redirect(url_for("service_detail", id=service.id))


@app.route("/service/<int:id>", methods=['GET'])
def service_detail(id: int):
    # return get_service('123'), 200
    # return Service.query.filter(id == '123').first()
    service = db.get_or_404(Service, id)
    print(service)
    
    return {
        'ministered_on': service.ministered_on
    }


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
