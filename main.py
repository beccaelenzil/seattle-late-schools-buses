from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask_seeder import FlaskSeeder
from database import database

load_dotenv()

#def create_app(test_config=None):
app = Flask(__name__)
CORS(app)

app.url_map.strict_slashes = False
app.config["SQLALCHEMY_TRACK_MODIFISCATIONS"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI")

# Setup DB
database.init_app(app)

from app.models.late_bus import LateBus
from app.models.school import School

from app.routes import buses_bp, schools_bp, home_bp
from app.json_routes import buses_json_bp, schools_json_bp
app.register_blueprint(home_bp)
app.register_blueprint(buses_bp)
app.register_blueprint(schools_bp)
app.register_blueprint(buses_json_bp)
app.register_blueprint(schools_json_bp)

#return app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
