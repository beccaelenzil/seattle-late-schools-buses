# Seattle Late School Buses API

This API scrapes data from [https://www.seattleschools.org/departments/transportation/latebus/](https://www.seattleschools.org/departments/transportation/latebus/)

It is deployed here: [https://seattle-school-buses.herokuapp.com/](https://seattle-school-buses.herokuapp.com/)

## Quick Start

1. Clone this repository.
1. Create and activate a virtual environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
1. Install the `requirements.txt`
    - `pip install -r requirements.txt`
1. Create the following postgres database on your machine:
    - `seattle_school_buses`
1. Create a `.env` file with the following line:
    - `SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/seattle_school_buses`
1. Apply migrations to the database:
    - `flask db upgrade`
1. Run the server
    - `flask run`

## Endpoints

| Route | Response Code | Response Body | Example Response Body |
|--|--|--|--|
|`GET` `/schools`| `200`| JSON where the keys are school names, and the values are a dictionary that includes the details for each school.|`{"Adams": {"address":"6110 28th Ave NW","id":42,"lat":"47.6732465522865","lng":"-122.39295255961478","name":"Adams","option_alt":"N/A","type":"elementary school","zip":"98107"},...}` |
|`GET` `/buses` | `200`| A list of all late bus dictionaries. |`[{"day":"23","duration":"40","id":1,"month":"September","route":"268","school":"South Shore","school_id":39,"time":"am","units":"minutes","year":"2022"},{"day":"23","duration":"35","id":2,"month":"September","route":"379","school":"Rainier Beach","school_id":12,"time":"am","units":"minutes","year":"2022"},...]`|
|`POST` `/buses` | `201`| A list of a the new late buses dictionaries added to the database.| `[{"day":"24","duration":"30","id":245,"month":"October","route":"1787","school":"Lowell","school_id":73,"time":"am","units":"minutes","year":"2022"}]` |
| - | `200`|The response where there is no new buses data to add to the database |`{"message":"no new buses"}` |
| - | `400`|Error response with information about the `error`. |`{"message": f"buses could not be added {error}"` |


#### Resources

File Structure: https://codersdiaries.com/blog/flask-project-structure