import random
from sense_hat import SenseHat
from time import sleep
from Visual_Band import Visual_Band

if __name__ == "__main__":

    sense = SenseHat()
    sense.clear()

    #b1 = Visual_Band(sense, 0)
    bands = []
    for x in range(0,8):
        bands.append(Visual_Band(sense, x))

    while True:
        #b1.update(random.randint(0,8))
        for b in bands:
            b.update(random.randint(0,8))
        sleep(.1)