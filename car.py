import status
import random

import update_json

class Car(object):

    # We assume that the car moves one unit at a time
    def __init__(self, user_name, police_number):
        self.user = user_name
        self.police_number = police_number
        self.is_on = True;

        # Denote the position of the car
        self.x = 0;
        self.y = 0;

        # Denote the length and width of the car
        self.width = 1
        self.length = 1

    # def is_crash(self):
    # TODO: Load data from JSON file and notify the police if the car is crashed
    #     if (get_status() == status.CRASH):
    #         notify_police()          

    def stop_car(self):
        self.is_on = False

    def drive(self, movements):
        # TODO:
        # Send current position data to GUI
        improper_counts = 0
        prev_offset = 0
        offset = 0

        for i in range(len(movements)):
            # If the car is stop, don't move
            if (self.is_on == False):
                break

            self.x += 1
            self.y += movements[i]

            print(f"Coor-x = {self.x},  Coor-y = {self.y}")
            # TODO:
            # Send the car coordinate to the GUI

            curr_offset = 0
            if (i == 0):
                pass
            else:
                curr_offset = movements[i] - movements[i - 1]

            offset = abs(prev_offset - curr_offset)

            # Set tolerance as 5 units
            if (offset > 3):
                improper_counts += 1

            if (improper_counts > 4):
                update_json.is_squiggly(self)

            print(f"i = {i}   offset = {offset}")

            # TODO:
            # Check if there is any obstacle infront
            # If there is, call is_crashed()
            # Stop the car

def generate_movements(movement_count):
    movements = []
    for i in range(movement_count):
        movements.append(random.randint(-5, 5))
    
    return movements

user_name = ""
police_number = ""
tesla = Car(user_name, police_number)

# movements = []
# movements = generate_movements(10)
# tesla.drive(movements)

update_json.is_squiggly(tesla)
# update_json.is_crashed(tesla)