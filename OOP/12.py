import os
os.system("cls")

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def kick(self):
        pass

    @abstractmethod
    def jump(self):
        pass


class Ironman(Player):
    def fly(self):
        print("Ironman is flying...")

    def run(self):
        print("Running...")

    def kick(self):
        print("Kicking...")

    def jump(self):
        print("Jumping...")


i1 = Ironman()
i1.fly()