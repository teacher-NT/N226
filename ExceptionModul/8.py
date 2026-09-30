import os
os.system("cls")

# pip install opencv-python

import cv2

camera = cv2.VideoCapture(0)

# is_valid, image = camera.read()
# if is_valid:
#     cv2.imwrite("selfi.png", image)
#     print("Rasm saqlandi")
# else:
#     print("Kameraga ulanishda xatolik!")

while True:
    is_valid, image = camera.read()
    if is_valid:
        cv2.imshow("Kamera", image)
    if cv2.waitKey(1) & 0xfff == 32:
        break