# ייבוא ספריות חיצוניות
import sys

# הגדרת קבועים

# הגדרת משתנים
kids = {'Yarden': 'Charizard', 'Liya': 'Pikachu'}


def print_dict(dictionary):
    print(dictionary)


# קבלת קלט מהמשתמש
while True:
    print("הכנס את הפקודה בבקשה:")
    line = sys.stdin.readline().rstrip()
    if not line:
        continue

    input = line.split(' ')

    # הדפס את תוכן המילון
    if input[0][0] == 'l':
        print_dict(kids)

    # הוסף רשומה חדשה למילון
    elif input[0] == 'a':
        kids[input[1]] = input[2]
        print_dict(kids)

    # מחיקת רשומה מהמילון
    elif input[0] == 'd':
        kids.pop(input[1], None)
        print_dict(kids)

    elif input[0] == 'g':
        pokemon = kids.get(input[1], None)
        print(pokemon)