class Car(object):

    # We assume that the car moves one unit at a time
    def __init__(self):
        self.is_on = True;

        # self.x and self.y denote the position of the car
        self.x = 0;
        self.y = 0;

    def switch_off(self):
        self.is_on = False;

    def switch_on(self):
        self.is_on = True;

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1
    
    def move_forward(self):
        self.y += 1

    def move_backward(self):
        self.y -= 1

