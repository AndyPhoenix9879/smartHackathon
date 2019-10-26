import json 
import datetime 

def generate_json(data):
    with open('car.json', 'w') as outfile:
        outfile.write(json.dumps(data, indent=4, sort_keys=True, default=str))
    outfile.close()

def is_crashed(Car):
    time = datetime.datetime.now()
    data = {
        "user_name": Car.user,
        "police_number": Car.police_number,
        "airbag_open": True,
        "is_squiggly": False,
        "time": time,
        "x_coordinate": Car.x,
        "y_coordinate": Car.y
    }
    generate_json(data)

def is_squiggly(Car):
    time = datetime.datetime.now()
    data = {
        "user_name": Car.user,
        "police_number": Car.police_number,
        "airbag_open": False,
        "is_squiggly": True,
        "time": time,
        "x_coordinate":Car.x,
        "y_coordinate": Car.y
    }
    generate_json(data)
