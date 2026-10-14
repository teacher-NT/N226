import os
os.system("cls")


class A:
    def func(self):
        print("I'm A class")

class B:
    def func(self):
        print("I'm B class")

class C(A):
    pass

# c1 = C()
# c1.func()

class D:
    pass

class E(D, C):
    pass

# e1 = E()
# e1.func()
# print(E.__mro__)

class F(E, C):
    pass

f1 = F()
f1.func()