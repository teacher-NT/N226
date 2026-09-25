import os
os.system("cls")

# for i in range(10, 20, 2):
#     print(i)

# def numbers(a,b,c):
#     print(a+b+c)

# numbers(1,2,3)
# numbers(1,2,3,4,5,6)

# def numbers2(*sonlar):
#     print(sonlar)
#     y = sum(sonlar)
#     print(y)

# numbers2(1,2,3)
# numbers2(1,2,3,4,5,6,7)
# numbers2(1,2,3,4,5,6,7,8,9)


# def print_info(**student):
#     for k,q in student.items():
#         print(k,q)
#     # print(student)

# print_info(ism="Alisher", famiylasi="Navoiy", yoshi=25)


# def add_nums(a, b):
#     return a+b

# add_nums2 = lambda a,b: a+b

# print(add_nums(3,4))
# print(add_nums2(3,4))


# sonlar = [50,70,12,80,65,45,92,31]
# new = []
# for i in sonlar:
#     if i >= 60:
#         new.append(i)
# print(new)


# sonlar = [50,70,12,80,65,45,92,31]
# def check(n):
#     return n >= 60
# new = list(filter(check, sonlar))
# print(new)


# sonlar = [50,70,12,80,65,45,92,31]
# new = list(filter(lambda n: n>=60, sonlar))
# print(new)



ismlar = ['yaXyoBek', 'sHahrizoda', 'VazirA', 'ODILBEK', 'bunYOD', 'oQILJON']

ismlar = list(map(lambda n: n.title(), ismlar))
print(ismlar)

# matn = "     sAlom dunYO hello WORLD    "
# matn = matn.strip()
# print(matn.title())
# print(matn.capitalize())
# print(matn.upper())
# print(matn.lower())
# print(matn.split())