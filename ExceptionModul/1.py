import os
os.system("cls")

try:
    a = int(input("a = "))
    b = int(input("b = "))
    print(a / b)
except ValueError:
    print("Iltimos faqat butun son kiriting!")
except ZeroDivisionError:
    print("Sonni nolga bo'lish mumkin emas!")
else:
    print("Kod xatosiz ishladi")
finally:
    print("Try except tugadi")

# a = int(input("a = "))
# b = int(input("b = "))
# print(a / b)