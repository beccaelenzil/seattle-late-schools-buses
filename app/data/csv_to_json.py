import csv
import pprint
import json

pp = pprint.PrettyPrinter(width=41, compact=True)

with open('cleaned_school_list.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    schools = []
    for row in csv_reader:
        schools.append(dict(row))

new_schools = []
for school in schools:
    school_dict = {}
    school_dict["number"] = school["Number"]
    school_dict["name"] = school["School"]
    school_dict["type"] = school["Type"]
    school_dict["address"] = school["Street Address"]
    school_dict["zip"] = school["Zip Code"]
    school_dict["option_alt"] = school["option_alt"]
    school_dict["lat"] = school["longitude"]
    school_dict["lng"] = school["latitude"]
    new_schools.append(school_dict)

pp.pprint(new_schools)

with open('seattle_schools_list.json', 'w') as outfile:
     json.dump(new_schools, outfile)


print("")

school_json = {}
for school in new_schools:
     school_json[school["name"]]= school

pp.pprint(school_json)


with open('seattle_schools_dictionary.json', 'w') as outfile:
     json.dump(school_json, outfile)

