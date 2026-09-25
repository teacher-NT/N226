import os
os.system("cls")

# def salom_ber():
#     print("Salom hammaga")

# salom_ber()
# salom_ber()
# salom_ber()



# def add_two_nums(a: int, b: int, d=0):
#     c = a + b + d
#     print(c)

# add_two_nums(4, 5)
# # add_two_nums("Salom", "Dunyo")
# # add_two_nums("Salom", 5)
# add_two_nums(4,5,7)


def powers(a, b) -> tuple:
    c = a**b
    n = a*b
    return c, n

print(powers(2, 3))
n,m = powers(3, 4)
print(n,m)

