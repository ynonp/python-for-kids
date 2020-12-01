from p5 import *

# הגדרת משתנים
my_font = create_font("C:\\Windows\\Fonts\\Arial.ttf", 16)
x = 3


# אתחול חד-פעמי
def setup():
    size(400, 400)


# ציור (מחזורי)
def draw():
    global my_font, x

    # הופכים את המחרוזת בשביל ימין לשמאל
    string = "שלום עולמי!" [::-1]

    # בחירת רקע וצבע
    background("white")
    fill("blue")

    # בחירת גופן ומיקום
    text_font(my_font, 48)
    text_align("CENTER")

    # כתיבה למסך
    text(string, (x, 180))

    # תנועה
    x = x + 2


run()
