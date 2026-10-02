import os
os.system("cls")

file = open("myfile.txt", "a")
name = input("Name: ")
file.write(f"{name}\n")
print("Faylga yozildi")
file.close()

with open("myfile.txt", "a") as file:
    name = input("Name: ")
    file.write(f"{name}\n")
    print("Faylga yozildi")

print("Tugadi")