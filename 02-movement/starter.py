from p5 import *

x = 0

def setup():
    size(640, 480)

def draw():
    global x

    background(0, 100, 10)
    fill('orange')
    rect(x, 0, 50, 50)

    x = x + 1

run()

