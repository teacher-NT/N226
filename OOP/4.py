import os
os.system("cls")


class Boat:
    def swim(self):
        print("Boat is swimming...")

class Plane:
    def fly(self):
        print("Plane is flying...")

    def swim(self):
        print("Plane can swim...")

class Duck(Plane, Boat):
    pass
    # def swim(self):
    #     print("Duck is swimming...")

d1 = Duck()
d1.fly()
d1.swim()