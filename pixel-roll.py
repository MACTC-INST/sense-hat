from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

black = (0,0,0)
red = (255,0,0)

x = 4
y = 5

while True:    
    o = sense.get_orientation_degrees()

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

    x_speed = int(ap / 20)
    y_speed = int(ar / 20)
    
    new_x = x
    new_y = y

    # Ignore values close to 0
    if ap < -10:
        new_x -= 1
    elif ap > 10:
        new_x += 1

    if ar < -10:
        new_y += 1
    elif ar > 10:
        new_y -= 1

    # Set boundaries
    new_x = max(0,min(7,new_x))
    new_y = max(0,min(7,new_y))

    # Unlight old pixel
    sense.set_pixel(x,y,black)

    # Light new one
    x = new_x
    y = new_y
    sense.set_pixel(x,y,red)

    # Delay more/less depending on how steep ar/ap are:
    delay = .1 / max(max(1,abs(x_speed)), abs(y_speed))
    sleep(delay)
