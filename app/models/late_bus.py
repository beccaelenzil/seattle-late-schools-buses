from flask import current_app
from app import db


class LateBus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String)
    time = db.Column(db.String)
    school_name = db.Column(db.String)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
