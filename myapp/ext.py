from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate

db = SQLAlchemy()
from myapp import models

def init_ext(app):
    db.init_app(app)

    se = Session()

    se.init_app(app)

    migrate = Migrate(app=app, db=db)