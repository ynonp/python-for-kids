from p5 import *

ball_x = 0
ball_y = 0

def setup():
    size(640, 400)

def draw():
    global x, y

    background(100, 100, 100)

    fill(255, 0, 0)
    circle(ball_x, ball_y, 20)

    ball_x += 1
    ball_y += 2
    

run()


