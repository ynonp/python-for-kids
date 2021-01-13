from p5 import *

def setup():
    size(400, 600)

def draw():
    background(0, 0, 0)
    fill(100, 40, 231)
    for x in range(0, 400, 50):
        circle(x, 50, 20)


run()
