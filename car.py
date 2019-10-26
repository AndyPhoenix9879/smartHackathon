import status
import random

from update_json import *

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

    def switch_off(self):
        self.is_on = False;

    def switch_on(self):
        self.is_on = True;

    ## Movement of the car ##
    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1
    
    def move_forward(self):
        self.y += 1

    def move_backward(self):
        self.y -= 1

    # def is_crash(self):
    # TODO: Load data from JSON file and notify the police if the car is crashed
    #     if (get_status() == status.CRASH):
    #         notify_police()          
    def drive(self, x, y):
        self.x += x
        self.y += y
        
        print(f"Coor-x = {self.x},  Coor-y = {self.y}")

    def is_squiggly_movement(self, movements):
        # TODO:
        # Generate JSON File for the car position

        improper_counts = 0
        prev_offset = 0

        self.drive(self.x, self.y + movements[0])
        for i in range(1, len(movements)):
            self.drive(self.x + 1, self.y + movements[i])
            curr_offset = movements[i] - movements[i - 1]

            if (prev_offset > 0 and curr_offset < 0 or prev_offset < 0 and curr_offset > 0):
                offset = abs(prev_offset - curr_offset)

                # Set tolerance as 5 units
                if (offset > 5):
                    improper_counts += 1
        
        if (improper_counts > 4):
            return True

        return False

def generate_movements(movement_count):
    movements = []
    for i in range(movement_count):
        movements.append(random.randint(-5, 5))
    
    return movements

user_name = ""
police_number = ""
tesla = Car(user_name, police_number)

update_json.is_crashed(tesla)

# movements = generate_movements(10)

# print(*movements)

# print(tesla.is_squiggly_movement(movements))
# if (tesla.is_squiggly_movement(movements)):
#     notify()


# tesla.print_status()

