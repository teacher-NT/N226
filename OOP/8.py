import os
os.system("cls")

class Person:
    def __init__(self, n, a, ad):
        self.name = n
        self.age = a
        self.address = ad

    def __str__(self):
        print("__str__ metodi ishladi")
        return f"{self.name} {self.age} {self.address}"

    def __gt__(self, n):
        return self.age  > n

    def __lt__(self, n):
        return self.age < n

    def __eq__(self, n):
        return self.age == n

p1 = Person("Ali", 12, "Toshkent")
# print(p1)

print(5 > 3)
print(p1 > 3, p1 > 20)
print(p1 < 3, p1 < 20)
print(p1 == 12)

    
