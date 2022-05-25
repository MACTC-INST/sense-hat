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
        new_x = self.x + x_offset
        new_y = self.y + y_offset

        # Set boundaries
        new_x = max(0,min(7,new_x))
        new_y = max(0,min(7,new_y))
        if (self.x == new_x and self.y == new_y):
            # No change
            return
        
        if (self.sense.get_pixel(new_x, new_y) != [0,0,0]):
            # Something is already there
            return

        # Unlight old pixel
        self.sense.set_pixel(self.x,self.y,self.black)

        # Light new one
        self.x = new_x
        self.y = new_y
        self.sense.set_pixel(self.x,self.y,self.color)
        
