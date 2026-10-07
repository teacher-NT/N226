import os
os.system("cls")

try:
    with open("mock/data.txt") as file:
        lst = []
        for i in file:
            n = len(i)-1
            if i[n] == '\n':
                i = i[:n]
            lst.append(i)
        print(lst)
except FileNotFoundError:
    print("Fayl topilmadi")