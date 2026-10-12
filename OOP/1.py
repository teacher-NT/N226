import os
os.system("cls")

# class Student:
#     pass

# s1 = Student()
# a = 1
# b = 4.5
# c = "salom"

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(s1))


# class Student:
#     ism = 'Begzod'
#     yosh = 13
#     manzil = 'Toshkent'

# # print(ism)

# s1 = Student()
# print(s1.ism, s1.yosh)



class Student:
    ism = 'Begzod'
    yosh = 13
    manzil = 'Toshkent'

    def info(self):
        print(f"{self.ism} {self.yosh} {self.manzil}")

s1 = Student()
s1.info()


s2 = Student()
s2.info()
