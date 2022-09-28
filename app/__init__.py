from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.url_map.strict_slashes = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    
    # import models for Alembic Setup
    from app.models.late_bus import LateBus

    # Setup DB
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.late_bus import LateBus
    from app.models.school import School

    from .routes import buses_bp, schools_bp, home_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(buses_bp)
    app.register_blueprint(schools_bp)

    return app
