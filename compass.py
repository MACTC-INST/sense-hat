from sense_hat import SenseHat
from time import sleep

# See this article on calibration
# https://raspberrytips.com/sense-hat-tutorial-2/

sense = SenseHat()

while True:
    print(f"North: {sense.get_compass()}")