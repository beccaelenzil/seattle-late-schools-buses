import datetime
from flask import Blueprint, request, jsonify, json, Response, make_response
from sqlalchemy.types import DateTime
from sqlalchemy.sql.functions import now
import requests
import os
from .data.scrape_bus_data import *


home_bp = Blueprint("home", __name__, url_prefix="/")
buses_bp = Blueprint("bus", __name__, url_prefix="/buses")
schools_bp = Blueprint("task", __name__, url_prefix="/schools")

def read_school_data():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    schools_url = os.path.join(SITE_ROOT, "data", "seattle_schools_dictionary.json")
    schools= json.load(open(schools_url))
    return schools, schools_url

def read_bus_data():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    buses_url = os.path.join(SITE_ROOT, "data", "seattle_buses.json")
    buses= json.load(open(buses_url))
    return buses, buses_url

MONTHS = {
    "January": "1",
    "February": "2",
    "March": "3",
    "April": "4",
    "May": "5",
    "June": "6",
    "July": "7",
    "August": "8",
    "September": "9",
    "October": "10",
    "November": "11",
    "December": "12"
}

@home_bp.route("", methods=["GET"])
def homepage():
    return "Welcome to Seattle Late School Buses"

@schools_bp.route("", methods=["GET"])
def get_schools():
    schools, schools_url = read_school_data()
    return schools

@buses_bp.route("", methods=["GET"])
def get_buses():
    late_buses, buses_url = read_bus_data()
    return make_response(jsonify(late_buses), 200)

@buses_bp.route("/<month>/<day>/<year>", methods=["GET"])
def get_specific_date_buses(day, month, year):
    late_buses, buses_url = read_bus_data()
    date_buses = []
    for bus in late_buses:
        if bus["day"] == day and MONTHS[bus["month"]] == month and bus["year"] == year:
            date_buses.append(bus)

    return make_response(jsonify(date_buses), 200)

@buses_bp.route("/today", methods=["GET"])
def get_todays_buses():
    late_buses, buses_url = read_bus_data()
    today = datetime.datetime.now()
    todays_buses = []
    for bus in late_buses:
        if bus["day"] == str(today.day) and MONTHS[bus["month"]] == str(today.month) and bus["year"] == str(today.year):
            todays_buses.append(bus)

    return make_response(jsonify(todays_buses), 200)


@buses_bp.route("", methods=["POST"])
def post_buses():
    late_buses, buses_url = read_bus_data()
    url = 'https://www.seattleschools.org/departments/transportation/latebus'
    late_buses = parse_late_bus_data(scrape_late_bus_data(url), late_buses)
    with open(buses_url, 'w') as f:
        json.dump(late_buses, f)
    return make_response(jsonify(late_buses), 201)