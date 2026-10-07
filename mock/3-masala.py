import os
os.system("cls")

import json

with open("mock/users.json") as file:
    users = json.load(file)

for user in users:
    if user['age'] >= 18:
        print(user)