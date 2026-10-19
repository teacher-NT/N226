import os
os.system("cls")

class BankAccount:
    def __init__(self, i, b):
        self.ism = i
        self.__balans = b

    def get_balans(self, parol):
        if parol == "qwerty":
            print(f"{self.ism}ning balansi: {self.__balans}$")
        else:
            print("Parol xato!")

    def change_balans(self, n, parol):
        if parol == "qwerty":
            self.__balans += n
        else:
            print("Parol xato! Balans o'zgarmadi.")

b1 = BankAccount("Yaxyobek", 1200)
print(b1.ism)
# print(b1.__balans)
b1.change_balans(500, "qwerty")
b1.get_balans("qwerty")

