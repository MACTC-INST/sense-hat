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

    return x_offset, y_offset

if __name__ == "__main__":

    sense = SenseHat()
    sense.clear()

    colors = [(255,0,0), (255,255,255), (0,0,255), (0,255,0)]

    sand = []
    for y in range(0,4):
        rgb = colors[y % len(colors)]
        for x in range(0,8):
            #rgb = colors[x % len(colors)]
            #rgb = (x*10 + y*40, 255-x*2-y*40, x*6 + y*40)
            sand.append(Pixel_Sand(sense, x, y, rgb))

    while True:
        x_offset, y_offset = get_offsets(sense)
        for s in sand:
            s.update_position(x_offset, y_offset)

        # Delay more/less depending on how steep ar/ap are:
        #delay = .1 / max(max(1,abs(x_speed)), abs(y_speed))
        delay = .05
        sleep(delay)
