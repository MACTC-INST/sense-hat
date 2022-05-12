import os, random,time
from sense_hat import SenseHat
sense = SenseHat()

p = os.path.dirname(os.path.abspath(__file__))

# Documentation at https://pythonhosted.org/sense-hat/api/

# Set pixels via array
def set_pixels_question():
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
    sense.set_pixels(question_mark)

# Fill screen with random colors
def set_pixels_random():
    random_mark = []
    for x in range(0,8):
        for y in range(0,8):
            random_mark.append([random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255)])
            
    sense.set_pixels(random_mark)

def load_picture():
    pixels = sense.load_image(f'{p}/amogus.png')
    
# Examples 
# Anything more than 1 line gets a function

# Print something to the screen (scrolling)
#sense.show_message("Hello World!")

# Set a single pixel (x, y, r, g, b)
#sense.set_pixel(0,0,255,0,0)

while True:  
    set_pixels_question()
    time.sleep(5)
    c = 0
    while c < 200:
        set_pixels_random()
        time.sleep(.1)
        c += 1