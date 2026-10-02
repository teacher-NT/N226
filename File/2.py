import os
os.system("cls")


file = open("myfile.txt", "w")

# matn = "\nPython dasturlash tili ajoyib"
# file.write(matn)
# print("Faylga yozildi")


names = ['Yahyo', 'Shahrizoda', 'Oqiljon', 'Bunyod', 'Odilbek']
names = list(map(lambda n:n+"\n", names))
file.writelines(names)
print("Faylga yozildi")