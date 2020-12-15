from p5 import *

# הגדרת קבועים
SIZE = 1000
MAX_COLOR = 255


# אתחול חד-פעמי
def setup():
    size(SIZE, SIZE)


# ציור (מחזורי)
def draw():
    # בחירת רקע וצבע
    background("black")
    fill(random_uniform(MAX_COLOR), random_uniform(MAX_COLOR), random_uniform(MAX_COLOR))

    # צורות
    circle(SIZE / 2, SIZE / 2, 50)


run()
