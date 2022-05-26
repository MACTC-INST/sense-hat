import random
from sense_hat import SenseHat
from time import sleep
from Pixel_Sand import Pixel_Sand

def get_offsets(sense):
    o = sense.get_orientation_degrees()

    x_offset, y_offset = 0,0

    # Adjust pitch to -90 (left) through 90 (right)
    # There is probably a mathier way to do this
    ap = o['pitch']
    if ap > 180:
        ap = 360-ap
    else: ap = -ap

    ar = o['roll']
    if ar > 200:
        ar = 360-ar
    else:
        ar = -ar

    # Not using these yet, but we might want to at some point
    x_speed = int(ap / 20)
    y_speed = int(ar / 20)

    # Ignore values close to 0
    if ap < -10:
        x_offset = -1
    elif ap > 10:
        x_offset = 1

    if ar < -10:
        y_offset = 1
    elif ar > 10:
        y_offset = -1

    acceleration = .1 / max(max(1,abs(x_speed)), abs(y_speed))
    return x_offset, y_offset, acceleration

def get_random_color():
    return [random.randint(50,255), 
        random.randint(50,255), 
        random.randint(50,255)]

if __name__ == "__main__":

    sense = SenseHat()
    sense.clear()

    # Use Red, White, Blue, Green for our colors
    #colors = [(255,0,0), (255,255,255), (0,0,255), (0,255,0)]

    # Use random colors
    colors = [get_random_color(), get_random_color(), 
        get_random_color(), get_random_color()]

    sand = []
    for y in range(0,4):
        # Make rows alternating colors
        rgb = colors[y % len(colors)]
        for x in range(0,8):
            # Make columns alternating colors
            #rgb = colors[x % len(colors)]

            # Attempt green gradient
            #rgb = (x*10 + y*40, 255-x*2-y*40, x*6 + y*40)

            sand.append(Pixel_Sand(sense, x, y, rgb))

    while True:
        x_offset, y_offset, acceleration = get_offsets(sense)
        for s in sand:
            s.update_position(x_offset, y_offset)

        # Delay more/less depending on how steep ar/ap are:
        sleep(acceleration)
