import json
import folium
from folium.plugins import MarkerCluster


my_map = folium.Map(location=(47.606, -122.332), zoom_to=3.5)  

with open('current_seattle_buses.json', 'r') as openfile:
    buses = json.load(openfile)
    
with open('seattle_schools_json.json', 'r') as openfile:
    schools = json.load(openfile)

for bus in buses:
    if bus["school"] in schools:
        latitude = schools[bus["school"]]["latitude"]
        longitude = schools[bus["school"]]["longitude"]
        string = bus["route"]
        folium.Marker(location=[latitude, longitude], popup=string).add_to(my_map)

my_map
print(my_map)
