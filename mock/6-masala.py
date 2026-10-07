import os
os.system("cls")

matn = "salom dunyo salom python dunyo salom"

result = {}

words = matn.split()
print(words)
for word in words:
    if word not in result:
        result[word] = 0
    result[word] += 1

print(result)

