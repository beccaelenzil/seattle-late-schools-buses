from flask import current_app
from app import db


class LateBus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String)
    day = db.Column(db.String)
    year = db.Column(db.String)
    route = db.Column(db.String)
    school = db.Column(db.String)
    duration= db.Column(db.String)
    units = db.Column(db.String)
    time = db.Column(db.String)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=True)

    def to_dict(self):
        return {
                "month": self.month,
                "day": self.day,
                "year": self.year,
                "route": self.route,
                "school": self.school,
                "duration": self.duration,
                "units": self.units,
                "time": self.time,
        }