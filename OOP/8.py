# https://www.geeksforgeeks.org/python/dunder-magic-methods-python/


import os
os.system("cls")

class Person:
    def __init__(self, n, a, ad):
        self.name = n
        self.age = a
        self.address = ad
        self.favourite_colors = ['red', 'green', 'black']

    def __str__(self):
        # print("__str__ metodi ishladi")
        return f"{self.name} {self.age} {self.address}"

    def __gt__(self, n):
        return self.age  > n

    def __lt__(self, n):
        return self.age < n

    def __eq__(self, n):
        return self.age == n

    def __add__(self,  n):
        self.age += n

    def __sub__(self, n):
        self.age -= n

    def __mul__(self, n):
        if n % 2==0:
            self.name = self.name.upper()
        else:
            self.name = self.name.lower()

    def __contains__(self, item):
        if item in self.favourite_colors:
            print(f"{item} yoqtirgan ranglar ichida bor")
            return True
        else:
            print(f"{item} yoqtirgan ranglar ichida yo'q")
            return False


p1 = Person("Ali", 12, "Toshkent")
# print(p1)

# print(5 > 3)
# print(p1 > 3, p1 > 20)
# print(p1 < 3, p1 < 20)
# print(p1 == 12)

# p1 + 2
# p1 - 5
# p1 * 3
# print(p1)

print("black" in p1)
print("blue" in p1)

    
