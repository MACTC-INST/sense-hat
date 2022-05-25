import random

# Think about whether we want this object to directly interface
# with the sense hat or not
from sense_hat import SenseHat

class Pixel_Sand:
    """
    An object to represent a grain of pixel sand
    """

    def __init__(self, sense, x, y, rgb=False):
        self.sense = sense
        self.x = x
        self.y = y
        self.black = (0,0,0)

        # If RGB == False, pick a random color
        self.color = rgb
        if rgb == False:
            self.color = (random.randint(30,200),
            random.randint(50,200),
            random.randint(50,200))


    def update_position(self, x_offset, y_offset):
        """
        The main loop will calculate offset based on pitch/yaw
        and supply it here. Then we can calculate the new position.
        If it's our current position, do nothing
        If the new position is already taken, do nothing
        """
        pass
        
