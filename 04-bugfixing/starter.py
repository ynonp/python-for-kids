from p5 import *

x = 100

def setup():
    size(640, 480)


def draw():
    global x
    background(100, 100, 100)
    if key_is_pressed:
        if key == 'RIGHT':
            x += 10
        if key == 'LEFT':
            x -= 10
    rect(x, 100, 100, 100)


def key_pressed(event):
    global x

    if event.key == 'RIGHT':
        x += 10

    if event.key == 'LEFT':
        x -= 10


run()