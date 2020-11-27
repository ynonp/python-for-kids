from p5 import *

x = 0

def setup():
    size(640, 480)


def draw():
    global x
    background(255, 255, 255)

    fill(255, 0, 0)
    rect(x, 10, 40, 40)

    x = x + 2

    if x > 600:
        x = 0

run()
