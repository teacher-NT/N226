import os
os.system("cls")


class Pilot:
    def manage_plane(self):
        print("Uchunvchi samolyotni boshqarmoqda")

class Cheff(Pilot):
    def cook(self):
        print("Oshpaz ovqat tayyorlamoqda")


class Human(Cheff):
    pass

h1 = Human()
h1.cook()
h1.manage_plane()