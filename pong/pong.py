from p5 import *

left_bar_y = 0
ball_x = 100
ball_y = 100
ball_dx = 2
ball_dy = 2

def setup():
    size(640, 480)


def draw():
    global ball_x, ball_y, ball_dx, ball_dy, left_bar_y
    background(150, 150, 150)

    if ball_x > 640:
        ball_dx = -2
    if ball_x < 0:
        ball_dx = 2
    if ball_y > 480:
        ball_dy = -2
    if ball_y < 0:
        ball_dy = 2

    rect(5, left_bar_y, 10, 80)
    circle(ball_x, ball_y, 20)

    ball_x += ball_dx
    ball_y += ball_dy

    if key_is_pressed and key == 'DOWN':
        left_bar_y += 3
    elif key_is_pressed and key == 'UP':
        left_bar_y -= 3

run()
