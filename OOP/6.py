import os
os.system("cls")

class Animal:
    def eat(self):
        print("Animal is eating...")

    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def eat(self):
        print("Dog is eating meat")

class Cat(Animal):
    pass

class Bird(Animal):
    def run(self):
        print("Bird run slowly...")

d1 = Dog()
d1.run()
d1.eat()

c1 = Cat()
c1.run()
c1.eat()

b1 = Bird()
b1.run()
b1.eat()