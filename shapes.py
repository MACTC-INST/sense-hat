from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
sense.clear()

red = (255,0,0)
black = (0,0,0)

start_x = 2
start_y = 2

square = []
square.append([red, red])
square.append([red, red])


for x in range(0,len(square)):
    for y in range(0, len(square[x])):
        sense.set_pixel(start_x + x, start_y + y, square[x][y])

