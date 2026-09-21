import os
os.system("cls")

set1 = {19,18,16,35,12,18,12}
# set1[2] = 7
# print(set1[2])

# print(set1)

set2 = {'olma', 'anor', 'banan', 'gilos', 'shaftoli'}

# if 'banan' in set2:
#     print("Yes")
# else:
#     print("No")

# for i in set2:
#     print(i, end=" ")


# =======================================
# https://www.w3schools.com/PYTHON/python_ref_set.asp

set3 = {'Damas', 'Gentra', 'Nexia', 'Spark', 'Chempion'}

# set3.add('BMW')
# print(set3)

# set3.remove('Spark')
# print(set3)

# set3.discard("Matiz")
# print(set3)

# m = set3.pop()
# print(set3)
# print(m)

# set3.clear()
# print(set3)

# set4 = set3.copy()
# set4.add("Buggati")
# print(set3)
# print(set4)

set4 = {'Damas', "Captiva", 'Cobalt', 'Tracker', 'Malibu'}

# set3.update(set4)
# print(set3)

# set5 = set3.union(set4)
# print(set5)
# print(set3)


sonlar1 = {1,2,3,4,5,6}
sonlar2 = {4,5,6,7,8,9}

natija = sonlar1.intersection(sonlar2)
print(natija)

natija2 = sonlar1 & sonlar2
print(natija2)

# sonlar1.intersection_update(sonlar2)
# print(sonlar1)

# natija = sonlar1.difference(sonlar2)
# print(natija)

# sonlar1.difference_update(sonlar2)
# print(sonlar1)

# natija = sonlar1.symmetric_difference(sonlar2)
# print(natija)

# sonlar1.symmetric_difference_update(sonlar2)
# print(sonlar1)

sonlar1 = {1,2,3,4,5,6,7,8,9,10,11,12}
sonlar2 = {8,3,5,7}

# print(sonlar2.issubset(sonlar1))

# print(sonlar1.issuperset(sonlar2))

