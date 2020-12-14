from p5 import *

x = 200
y = 250


def setup():
    size(640, 480)


def draw():
    triangle(x, y - 25, x, y + 25, x + 50, y)


run()

