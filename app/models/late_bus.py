from flask import current_app
from app import db
from .school import School


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


    @classmethod
    def create_bus(cls, bus_json):
        school_dictionary = School.make_all_schools_dict()
        if bus_json["school"] in school_dictionary:
            school_id = school_dictionary[bus_json["school"]]["id"]
        else:
            school_id = None
            print(bus_json["school"], " not in schools database")
            
        new_bus = LateBus(
            month=bus_json["month"],
            day=bus_json["day"],
            year=bus_json["year"],
            route=bus_json["route"],
            school=bus_json["school"],
            duration=bus_json["duration"],
            units=bus_json["units"],
            time=bus_json["time"],
            school_id=school_id
            )
        return new_bus


    @classmethod
    def get_todays_late_buses_from_database(cls, todays_late_buses):
        day, month, year = todays_late_buses[0]["day"],todays_late_buses[0]["month"], todays_late_buses[0]["year"]
        todays_db_late_buses = LateBus.query.filter_by(day=day, month=month, year=year).all()
        print(todays_db_late_buses)
        todays_new_late_buses_json = []
        for bus in todays_db_late_buses:
            todays_new_late_buses_json.append(bus.to_dict())

        return todays_new_late_buses_json
