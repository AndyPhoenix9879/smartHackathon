import json 
import datetime 
x,y = map(int,input("X:Y:").split())
time = datetime.datetime.now()
file = open ("car.json","w")

c = {
    "airbag_open": True ,
    "time": time,
    "x_coordinate": x,
    "y_coordinate": y
}
file.write(json.dumps(c, indent=4, sort_keys=True, default=str))
file.close()

