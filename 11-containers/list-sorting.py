# הגדרת משתנים
numbers = [1, 105, 34, 65, 2]

# הדפסה למסך של הרשימה
print(numbers)

# מיון והדפסה למסך
numbers.sort()
print(numbers)

# הוספת מספר בתחילת הרשימה
numbers.insert(0, 77)
print(numbers)

# הדפסה של האיברים ברשימה אחד אחד
for number in numbers:
    print(number)
