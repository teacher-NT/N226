
# a = 5

# if  a > 3 and a%2==1:
#     print("Salom")
#     print("Good morning")
# print("Hello")


# n = 10

# if n == 1:
#     print("Start")
# elif n == 2:
#     print("Continue")
# elif n == 3:
#     print("Stop")
# else:
#     print("Good bye")


# n = 1
# while n <= 10:
#     print(n, end=" ")
#     n += 1

# n = 10
# while n >=1:
#     print(n, end=" ")
#     n -= 1

# for i in range(10):
#     print(i, end=" ")

# for i in range(10, 20):
#     print(i, end=" ")

# for i in range(10, 100, 5):
#     print(i, end=" ")

# for i in range(10, 0, -1):
#     print(i,  end=" ")




import os
os.system("cls")

for i in range(1, 100):
    if i%3==0 and i%5==0:
        print(i, end=" ")
    print(". ", end="")
