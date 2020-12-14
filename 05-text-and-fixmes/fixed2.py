from p5 import *

# הגדרת קבועים
MIN_COLOR = 0
MAX_COLOR = 255

# הגדרת משתנים
color_r = MIN_COLOR
color_g = MAX_COLOR
color_b = MIN_COLOR


# אתחול חד-פעמי
def setup():
    size(400, 400)


# ציור (מחזורי)
def draw():
    global color_r, color_g, color_b

    # בחירת רקע וצבע
    background("black")
    fill(color_r, color_g, color_b)

    # צורות
    for x in [0, 175, 350]:
        rect(x, 150, 50, 50)

    # שינויי צבע
    color_r = color_r + 1
    color_g = color_g - 1
    color_b = color_b + 1

    if color_r >= MAX_COLOR:
        color_r = MIN_COLOR

    if color_g <= MIN_COLOR:
        color_g = MAX_COLOR

    if color_b >= MAX_COLOR:
        color_b = MIN_COLOR


run()
