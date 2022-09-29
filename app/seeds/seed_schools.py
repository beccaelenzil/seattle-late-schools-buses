from flask_seeder import Seeder
from app.models.school import School
from app.models.late_bus import LateBus
from app import db


def seed_schools(schools):
    for school in schools:
        try:
            new_school = School(
                    name=school["name"],
                    type=school["type"],
                    address=school["address"],
                    zip=school["zip"],
                    option_alt=school["option_alt"],
                    lat=school["lat"],
                    lng=school["lng"]
            )
        
        
            print("Adding school:", school["name"])
            db.session.add(new_school)
            db.session.commit()
        except Exception as error:
            print("School Could Not be Added:", school["name"], error)

def seed_buses(buses):
    #print("******",buses)
    for bus in buses:
        school_dictionary = School.make_all_schools_dict()
        try:
            if bus["school"] in school_dictionary:
                school_id = school_dictionary[bus["school"]]["id"]
            else:
                school_id = None
                print(bus["school"], " not in schools database")
            
            new_bus = LateBus(
                month=bus["month"],
                day=bus["day"],
                year=bus["year"],
                route=bus["route"],
                school=bus["school"],
                duration=bus["duration"],
                units=bus["units"],
                time=bus["time"],
                school_id=school_id
                )

            print("Adding Bus:", bus["route"])
            db.session.add(new_bus)
            db.session.commit()
        except Exception as error:
            print("Bus Could Not be Added:", bus["route"], error)
            