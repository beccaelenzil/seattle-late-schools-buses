from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)