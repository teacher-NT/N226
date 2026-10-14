import os
os.system("cls")


class Animal:
    def eat(self):
        print("Animal is eating...")

    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def sound(self):
        print("Dog is barking...")

    def run(self):
        print("Dog is running...")

d1 = Dog()
d1.eat()
d1.run()
d1.sound()