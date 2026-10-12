import os
os.system("cls")

class Student:
    def __init__(self, i, y, m):
        self.ism = i
        self.yosh = y
        self.manzil = m

    def info(self):
        print(f"{self.ism} {self.yosh} {self.manzil}")

s1 = Student('Alisher', 15, 'Buxoro')
s1.info()


s2 = Student('Bobur', 21, 'Andijon')
s2.info()
