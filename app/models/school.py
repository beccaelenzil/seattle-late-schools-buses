from flask import current_app
from app import db


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    address = db.Column(db.String)
    zip = db.Column(db.Integer)
    option_alt = db.Column(db.String)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    
