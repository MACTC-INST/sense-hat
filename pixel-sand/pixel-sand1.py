from sense_hat import SenseHat
from time import sleep
from Pixel_Sand1 import Pixel_Sand

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

    return x_offset, y_offset

if __name__ == "__main__":

    sense = SenseHat()
    sense.clear()

    red = (255,0,0)

    # Make pixel sand objects:
    p1 = Pixel_Sand(sense, 2, 2, red)

    while True:
        x_offset, y_offset = get_offsets(sense)
        p1.update_position(x_offset, y_offset)

        # Delay more/less depending on how steep ar/ap are:
        #delay = .1 / max(max(1,abs(x_speed)), abs(y_speed))
        delay = .05
        sleep(delay)
