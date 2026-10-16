import os
os.system("cls")

# a = 12
# b = "salom"
# c = ['apple', 'banan', 'cherry']

# print(a * 3)
# print(b * 3)
# print(c * 3)

# print(len(b))
# print(len(c))



class Animal:
    def sound(self):
        print("Hello everyone!")

class Dog(Animal):
    def sound(self):
        print("Welcome to home!")

class Cat(Animal):
    pass

a1 = Animal()
d1 = Dog()
c1 = Cat()
a1.sound()
d1.sound()
c1.sound()