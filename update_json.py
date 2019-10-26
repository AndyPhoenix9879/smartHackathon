import json 
import datetime 

from car import Car

def generate_json(data):
    with open('car.json', 'w') as outfile:
        outfile(json.dumps(data, indent=4, sort_keys=True, default=str))
    outfile.close()

def is_crashed(car):
    time = datetime.datetime.now()
    data = {
        "user_name": car.user,
        "police_number": car.police_number,
        "airbag_open": True,
        "is_squiggly": False,
        "time": time,
        "x_coordinate": car.x,
        "y_coordinate": car.y
    }
    generate_json(data)

def is_squiggly(car):
    time = datetime.datetime.now()
    data = {
        "user_name": car.user,
        "police_number": car.police_number,
        "airbag_open": False,
        "is_squiggly": True,
        "time": time,
        "x_coordinate":car.x,
        "y_coordinate": car.y
    }
    generate_json(data)
