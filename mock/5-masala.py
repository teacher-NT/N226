import os
os.system("cls")

import json

with open("mock/users.json") as file:
    users = json.load(file)
    print(f"{len(users)} ta ma'lumot bor")