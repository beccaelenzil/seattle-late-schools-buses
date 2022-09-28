from flask import current_app
from app import db


class LateBus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    year = db.Column(db.Integer)
    route = db.Column(db.Integer)
    school = db.Column(db.String)
    duration= db.Column(db.Integer)
    units = db.Column(db.String)
    time = db.Column(db.String)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=True)
