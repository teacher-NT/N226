import os
os.system("cls")
import json

# cars = [
#     {
#         "brand": "BMW",
#         "Model": 'M8',
#         "max_speed": 300
#     },
#     {
#         "brand": "Porche",
#         "Model": '911',
#         "max_speed": 350
#     },
#     {
#         "brand": "Mersedes",
#         "Model": 'CLS63',
#         "max_speed": 320
#     }
# ]

# with open("cars.txt", "w") as file:
#     # file.write(cars)
#     json.dump(cars, file, indent=4)
#     print("Faylga yozildi")




with open("cars.json") as file:
    # cars = file.read()
    cars = json.load(file)
    print(cars)