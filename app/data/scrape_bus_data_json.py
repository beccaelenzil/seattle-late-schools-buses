from bs4 import BeautifulSoup
import urllib.request as urllib
import re

def parse_late_bus_data_json(soup, seattle_buses_json):
    paragraphs = soup.find_all('p')
    bus_pattern = re.compile("Route")
    date_pattern = re.compile(", 20")

    
    bus_list = []

    time = "am"

    for paragraph in paragraphs:
        paragraph = paragraph.get_text()
        if "Mid-Day Delays" == paragraph:
            time = "mid"
        elif "PM Delays" == paragraph:
            time = "pm"
        
        if bus_pattern.search(paragraph):
            bus_list.append(paragraph+" "+time)
        elif date_pattern.search(paragraph):
            date = paragraph

    date_pattern = re.compile("(January|February|March|April|May|June|July|August|September|October|November|December) (\d+), (\d\d\d\d)")
    date_match = date_pattern.search(date)

    late_buses = seattle_buses_json
    bus_pattern = re.compile("Route (\d+) – ([A-Za-z ]+) – (\d+) ([A-Za-z]+).*(am|mid|pm)")
    
    new_late_buses = []
    for bus in bus_list:
        bus_match = bus_pattern.search(bus)
        if bus_match:
            bus_dictionary = {}
            bus_dictionary["month"] = date_match[1]
            bus_dictionary["day"] = date_match[2]
            bus_dictionary["year"] = date_match[3]
            bus_dictionary["route"] = bus_match[1]
            bus_dictionary["school"] = bus_match[2]
            bus_dictionary["duration"] = bus_match[3]
            bus_dictionary["units"] = bus_match[4]
            bus_dictionary["time"] = bus_match[5]
            if bus_dictionary not in late_buses:
                late_buses.append(bus_dictionary)
                new_late_buses.append(bus_dictionary)
    
    return late_buses, new_late_buses