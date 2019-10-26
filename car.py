import random
import datetime

import simulation
import update_json

class Car(object):

    def __init__(self, user_name, police_number):
        self.user = user_name
        self.police_number = police_number
        self.is_on = True;

        # Denote the position of the car
        self.x = 620;
        self.y = 620;

    def drive(self, accident_type):
        self.x = 620;
        self.y = 620;
        
        simulation.run_car(self, self.x, self.y, accident_type)

    def generate_squiggly_movements(self, movement_count):
        random.seed(datetime.datetime.now())
        self.movements = []
        for i in range(movement_count):
            self.movements.append(random.randint(-7, 7))

    def generate_straight_movements(self, movement_count):
        random.seed(datetime.datetime.now())
        self.movements = []

        offset = random.randint(-7, 7)
        for i in range(movement_count):
            if i > 20 and i < 30:
                self.movements.append(offset)
            else:
                self.movements.append(0)