from p5 import *

# הגדרת קבועים
SIZE = 1000

# הגדרת משתנים
x = 1000
y = 1000
target_x = 0
target_y = 0


# אתחול חד-פעמי
def setup():
    size(SIZE, SIZE)


# ציור (מחזורי)
def draw():
    global x, y, target_x, target_y

    if mouse_is_pressed:
        x = 0
        y = 0
        target_x = mouse_x
        target_y = mouse_y
        print(mouse_x, mouse_y)

    # בחירת רקע וצבע
    background("black")
    fill(random_uniform(255), random_uniform(255), random_uniform(255))

    # צורות
    circle(x, y, 50)

    # תנועה
    x = x + (target_x - x) / 20
    y = y + (target_y - y) / 20


run()
