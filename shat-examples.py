import random,time
from sense_hat import SenseHat
sense = SenseHat()

# Print something to the screen
#sense.show_message("Hello World!")

# Set pixels individually
X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

while True:
    sense.set_pixels(question_mark)
    time.sleep(5)
    
    c = 0
    while c < 200:
        random_mark = []
        for x in range(0,8):
            for y in range(0,8):
                random_mark.append([random.randint(0,255),
                            random.randint(0,255),
                            random.randint(0,255)])
                
        sense.set_pixels(random_mark)
        time.sleep(.1)
        c += 1
                            