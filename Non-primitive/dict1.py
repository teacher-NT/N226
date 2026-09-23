import os
os.system("cls")

car = {
    "brand": "GM",
    "model": "Matiz",
    "yil": 2010,
    "narx": 2000,
    "rang": "Qizil"
}
# car["model"] = 'Spark'
# car['probeg'] = 300000
# print(car)
# print(car["model"])
# print(car["yil"])


# if "Matiz" in car:
#     print("Yes")
# else:
#     print("No")

for i in car:
    print(i, car[i])