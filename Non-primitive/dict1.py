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

# for i in car:
#     print(i, car[i])

# print(car['rangi'])
# print(car.get('rangi', "Bunday kalit yo'q"))

# kalitlar = car.keys()
# print(kalitlar)

# qiymatlar = car.values()
# print(qiymatlar)
# if "Matiz" in qiymatlar:
#     print("Bor")
# else:
#     print("Yo'q")

# k = car.pop("model")
# print(car)
# print(k)

# k = car.popitem()
# print(car)
# print(k)

# print(car.items())
# for i in car:
#     print(i, car[i])
# for k, q in car.items():
#     print(k, q)

# car['model'] = "Spark"
# car["narx"] = 1500
# car["rang"] = "Yashil"
car.update({"model": "Spark", "narx":1500, 'rang':"Yashil"})
# print(car)