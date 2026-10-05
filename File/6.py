import os
os.system("cls")

with open("N226/File/image.jpg", "rb") as file:
    pixels = list(file.read())
    print(len(pixels))
    # for i in pixels:
    #     print(i, end=' ')