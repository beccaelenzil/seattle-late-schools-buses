from flask import current_app
from app import db


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    address = db.Column(db.String)
    zip = db.Column(db.String)
    option_alt = db.Column(db.String)
    lat = db.Column(db.String)
    lng = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "address": self.address,
            "zip": self.zip,
            "option_alt": self.option_alt,
            "lat": self.lat,
            "lng": self.lng
        }
    
    @classmethod
    def make_all_schools_dict(cls):
        all_schools = cls.query.all()
        all_schools_dict = {}
        for school in all_schools:
            all_schools_dict[school.name] = school.to_dict()

        return all_schools_dict
