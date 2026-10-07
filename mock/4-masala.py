import os
os.system("cls")

import json

data = [{"name": "Ali"}, {"name": "Vali"}]

with open("foydalanuvchilar.json", "w") as file:
    json.dump(data, file, indent=4)
    print("Faylga yozildi")