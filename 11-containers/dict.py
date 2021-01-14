# ייבוא ספריות חיצוניות
import sys

# הגדרת קבועים

# הגדרת משתנים
kids = {'1': 'Niv', '2': 'Noam', '3': 'Yarden'}

for key in kids.keys():
    print(key)

for record in kids.values():
    print(record)

for item in kids.items():
    print(item)

# kids['4'] = 'samy'

# קבלת קלט מהמשתמש
print("Enter a number please:")
input = sys.stdin.read(1)[0]

# חיפוש במילון והדפסת ערך בהתאם
kid = kids.get(input)
if kid is not None:
    print(kid)
else:
    print("YotamkiPumpki")

