import os
os.system("cls")

import random as rd

# print(rd.randint(1, 100))

ismlar = ['Yaxyobek', 'Odilbek', 'Bunyod', 'Oqiljon', 'Musammirshoh', 'Vazira']

# ism = rd.choice(ismlar)
# print(ism)

# tanlangan = rd.choices(ismlar, k=3)
# print(tanlangan)


# tanlangan = rd.sample(ismlar, k=3)
# print(tanlangan)


rd.shuffle(ismlar)
print(ismlar)