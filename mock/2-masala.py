import os
os.system("cls")

data = [("Ali", 85), ("Vali", 92), ("Sami", 77)]

result = {}
for i in data:
    print(i)
    result[i[0]] = i[1]

print(result)