import json 
import datetime 

def generate_json(data):
    try:
        with open('car.json', 'r') as json_file:
            file = json.load(json_file)

        file["cars"].append(data["cars"][0])

        with open('car.json', 'w') as json_file:
            json_file.write(json.dumps(file, indent=4, default=str))
        json_file.close()
    except:
        with open('car.json', 'w') as json_file:
            json_file.write(json.dumps(data, indent=4, default=str))
        json_file.close()

def is_crashed(Car):
    time = datetime.datetime.now()
    time = time.strftime("%dth %B, %Y - %H:%M")
    data = {
        "cars": [{
            "user_name": Car.user,
            "police_number": Car.police_number,
            "is_crashed": True,
            "is_squiggly": False,
            "time": time,
            "x_coordinate": Car.x,
            "y_coordinate": Car.y
        }]
    }
    generate_json(data)

def is_squiggly(Car):
    time = datetime.datetime.now()
    time = time.strftime("%dth %B, %Y - %H:%M")
    data = {
        "cars": [{
            "user_name": Car.user,
            "police_number": Car.police_number,
            "is_crashed": False,
            "is_squiggly": True,
            "time": time,
            "x_coordinate":Car.x,
            "y_coordinate": Car.y
        }]
    }
    generate_json(data)
