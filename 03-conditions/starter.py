from p5 import *
from random import randint

color = 0

def setup():
    global color

    size(640, 480)
    color = randint(0, 10)


def draw():
    if color > 5:
        background(0, 255, 0)
    else:
        background(255, 0, 0)


run()
