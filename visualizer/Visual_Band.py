import random
from sense_hat import SenseHat


class Visual_Band:
    """
    An object to represent and display an eq band
    sense = a sense hat object
    display_x = which column display is in
    color = color (rgb array) to use for display
    """

    def __init__(self, sense, display_x, color=False):
        self.sense = sense
        self.display_x = display_x
        self.amplitude = 0
        self.black = (0,0,0)

        if color == False:
            self.color = (random.randint(30,200),
            random.randint(50,200),
            random.randint(50,200))

    def update(self, amplitude):
        # Assume amplitude is normalized to 0-7
        self.amplitude = max(0,min(7,amplitude))

        self.clear_band()
        for y in range (7, 7- amplitude,-1):
            self.sense.set_pixel(self.display_x, y, self.color)

    def clear_band(self):
        for y in range(0,8):
            self.sense.set_pixel(self.display_x, y, self.black)