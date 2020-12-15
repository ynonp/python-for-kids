from p5 import *

# הגדרת קבועים
MAX_COLOR = 255
SIZE = 1000
BOMB_RADIUS = 50

# הגדרת משתנים
bomb_x = 0
bomb_y = 0
interceptor_x = 0
interceptor_y = 0
interceptor_ready = True


# שיגור פצצה חדשה
def release_bomb():
    global bomb_x, bomb_y

    bomb_x = random_uniform(SIZE - BOMB_RADIUS, BOMB_RADIUS)
    bomb_y = 0


# אתחול חד-פעמי
def setup():
    size(SIZE, SIZE)


# ציור (מחזורי)
def draw():
    global bomb_x, bomb_y, interceptor_x, interceptor_y, interceptor_ready

    # בחירת רקע וצבע
    background("cyan")

    # שגר פצצה חדשה אם פגענו בקרקע
    if (bomb_x == 0) or (bomb_y > SIZE):
        release_bomb()

    # שיגור מיירט
    if mouse_is_pressed and (interceptor_ready is True):
        interceptor_ready = False
        interceptor_x = mouse_x
        interceptor_y = SIZE

    # זיהוי פגיעה
    if (abs(bomb_x - interceptor_x) < 20) and (abs(bomb_y - interceptor_y) < 20):
        fill("red")
        rect(bomb_x - 100, bomb_y + 100, 200, 200)
        interceptor_ready = True
        release_bomb()

    else:

        # ציור הפצצה
        fill("black")
        circle(bomb_x, bomb_y, BOMB_RADIUS)
        line(bomb_x, bomb_y, bomb_x + 35, bomb_y - 35)

        # ציור המיירט
        if interceptor_ready is False:
            fill("blue")
            triangle(interceptor_x, interceptor_y, interceptor_x + 20, interceptor_y, interceptor_x + 10, interceptor_y - 20)
            rect(interceptor_x, interceptor_y, 20, BOMB_RADIUS)

    # תנועה
    bomb_y = bomb_y + 10

    if interceptor_ready is False:
        interceptor_y = interceptor_y - 25
        if interceptor_y < -BOMB_RADIUS:
            interceptor_ready = True


run()
