import os
os.system("cls")

class Person:
    def __init__(self, n, a, ad):
        self.name = n
        self.age = a
        self.address = ad

    def __gt__(self, n):
        return self.age > n

class Employeer:
    def __init__(self, n, a, ad, s):
        self.name = n
        self.age = a
        self.address = ad
        self.salary = s

    def __gt__(self, n):
        return self.salary > n


p1 = Person('Ali', 25, 'Andijon')
print(p1 > 50)

e1 = Employeer("Madina", 28, "Namangan", 800)
print(e1 > 50)