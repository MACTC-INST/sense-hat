import os, pprint, random, time
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
x = 0
y = 0

while True:
    event = sense.stick.wait_for_event(emptybuffer=True)
    new_x = x
    new_y = y
    print (f"j: {event.action} {event.direction}")

    if event.direction == "up":
        new_y -= 1
    elif event.direction == "down":
        new_y += 1
    elif event.direction == "left":
        new_x -= 1
    elif event.direction == "right":
        new_x += 1

    # Stop at boundaries
    new_x = max(0,min(7,new_x))
    new_y = max(0,min(7,new_y))
    
    # Unlight old pixel
    sense.set_pixel(x,y,black)

    # Light new one
    x = new_x
    y = new_y
    sense.set_pixel(x,y,green)

    time.sleep(0.1)
