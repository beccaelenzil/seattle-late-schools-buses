import os
from flask import Blueprint, json, jsonify, make_response
from .data.scrape_bus_data import *
from .seeds.seed_schools import *

home_bp = Blueprint("home", __name__, url_prefix="/")
buses_bp = Blueprint("bus", __name__, url_prefix="/buses")
schools_bp = Blueprint("task", __name__, url_prefix="/schools")


@home_bp.route("", methods=["GET"])
def homepage():
    return "Welcome to Seattle Late School Buses"


@schools_bp.route("", methods=["GET"])
def get_schools_db():
    school_dictionary = School.make_all_schools_dict()
    return make_response(jsonify(school_dictionary), 200)


@buses_bp.route("", methods=["GET"])
def get_buses_db():
    late_buses = LateBus.query.all()
    late_buses_json = []
    for bus in late_buses:
        bus_dict = bus.to_dict()
        bus_dict["id"] = bus.id
        bus_dict["school_id"] = bus.school_id
        late_buses_json.append(bus_dict)
    return make_response(jsonify(late_buses_json), 200)


@buses_bp.route("", methods=["POST"])
def post_buses_to_db():
    # scrape late bus data
    url = 'https://www.seattleschools.org/departments/transportation/latebus'
    todays_new_late_buses = parse_late_bus_data(scrape_late_bus_data(url))
    if not todays_new_late_buses:
        return make_response({"message":"no late buses today"}, 200)

    # get date
    todays_db_late_buses = LateBus.get_todays_late_buses_from_database(todays_new_late_buses)

    # add new buses to database
    new_late_buses = []
    for bus in todays_new_late_buses:
        if bus not in todays_db_late_buses:
            try:
                new_bus = LateBus.create_bus(bus)
                db.session.add(new_bus)
                db.session.commit()  
                print("Adding Bus:", bus["route"])
                new_late_buses.append(new_bus.to_dict())
            except Exception as e:
                print("bus could not be added")

    if not new_late_buses:
        return make_response({"message":"todays late buses have already been added"}, 200)
    
    return make_response(jsonify(new_late_buses), 201)
        
