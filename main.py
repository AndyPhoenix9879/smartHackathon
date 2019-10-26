import json

import constants
from car import *

# Define the user_name and the police_number
user_name = "curious_hackers"
police_number = "CUHK-1234"

# Reset the 'car.json' file at the beginning
with open('car.json', 'w') as file:
    file.write("")
file.close()

car = Car(user_name, police_number)
car.generate_squiggly_movements(80)
car.drive(constants.SQUIGGLY)

car.generate_straight_movements(80)
car.drive(constants.CRASHED)