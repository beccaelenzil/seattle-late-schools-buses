from bs4 import BeautifulSoup
import urllib.request as urllib
import os
import datetime
import re
import pprint
import json

pp = pprint.PrettyPrinter(width=41, compact=True)
 
def scape_late_bus_data(url): 
    # web scraping
    late_busses = url
    page = urllib.urlopen(late_busses)
    soup = BeautifulSoup(page, "html.parser")
    return soup

def parse_late_bus_data(soup, seattle_buses_json):
    paragraphs = soup.find_all('p')
    bus_pattern = re.compile("Route")
    date_pattern = re.compile(", 20")

    
    bus_list = []

    for paragraph in paragraphs:
        paragraph = paragraph.get_text()
        if bus_pattern.search(paragraph):
            bus_list.append(paragraph)
        if date_pattern.search(paragraph):
            date = paragraph

    date_pattern = re.compile("(January|February|March|April|May|June|July|August|September|October|November|December) (\d+), (\d\d\d\d)")
    date_match = date_pattern.search(date)

    late_buses = seattle_buses_json
    bus_pattern = re.compile("Route (\d+) – ([A-Za-z ]+) – (\d+) ([A-Za-z]+)")
    
    for bus in bus_list:
        bus_dictionary = {}
        bus_match = bus_pattern.search(bus)
        bus_dictionary["month"] = date_match[1]
        bus_dictionary["day"] = date_match[2]
        bus_dictionary["year"] = date_match[3]
        bus_dictionary["route"] = bus_match[1]
        bus_dictionary["school"] = bus_match[2]
        bus_dictionary["duration"] = bus_match[3]
        bus_dictionary["units"] = bus_match[4]
        if bus_dictionary not in late_buses:
            late_buses.append(bus_dictionary)
    
    return late_buses



with open('seattle_buses.json', 'r') as openfile:
    seattle_buses_json = json.load(openfile)

url = 'https://www.seattleschools.org/departments/transportation/latebus'

late_buses = parse_late_bus_data(scape_late_bus_data(url), seattle_buses_json)

with open('seattle_buses.json', 'w') as outfile:
    json.dump(late_buses, outfile)





pp.pprint(late_buses)

