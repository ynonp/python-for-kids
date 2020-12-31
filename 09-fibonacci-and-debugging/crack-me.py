# הגדרת קבועים
import sys

# הגדרת משתנים
encrypted = "Sn{1%Stfr%fsi%^fwijs"
decrypted = ""

print("Enter the key please:")
key = int(sys.stdin.read(1)[0])

for i in range(0, len(encrypted)):
    decrypted += chr(ord(encrypted[i]) - key)

print(decrypted)
