from p5 import *

# הגדרת משתנים
myFont = create_font("C:\\Windows\\Fonts\\Arial.ttf", 16)
x = 3


# אתחול חד-פעמי
def setup():
    size(400, 400)


# ציור (מחזורי)
def draw():
    global myFont

# הופכים את המחרוזת בשביל ימין לשמאל
string = "שלום עולמי!" [::-1]

    # בחירת רקע וצבע
    background("white")
    fill("blu")

    # בחירת גופן ומיקום
    text_font(myFont, 48)
    text_align("CENTER")

    # כתיבה למסך
    text(string, (x, 180))

    # תנועה
    x = x + 2


run()
