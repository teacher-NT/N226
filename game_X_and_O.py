from random import choice
import os
os.system("cls")
def bosh_doska_hosil_qil():
    """
    3x3 o'lchamli ro'yxat hosil qiladi
    :param 
        None - hech narsa qaytarmaydi
    :return 
        list - Hosil bo'lgan ro'yxatni qaytaradi
    """
    doska = [1,2,3,4,5,6,7,8,9]
    return doska
    
def doskani_korsat(doska):
    """
    Doskani ekranga chiqaradi
    :param 
        doska
    :return
        None - hech narsa qaytarmaydi
    """
    print("+" + "-"*11 + "+")
    print(f"| {doska[0]} | {doska[1]} | {doska[2]} |")
    print("+" + "-"*11 + "+")
    print(f"| {doska[3]} | {doska[4]} | {doska[5]} |")
    print("+" + "-"*11 + "+")
    print(f"| {doska[6]} | {doska[7]} | {doska[8]} |")
    print("+" + "-"*11 + "+")

def foydalanuvchi_tanlasin(doska):
    """
    Foydalanuvchidan raqamni so'rab doskani o'zgartiradi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    if not bosh_maydonlar(doska):
        return
    n = int(input("Bo'sh katakni tanlang: "))
    if n>9 or n<1 or n not in doska:
        print("No'to'g'ri katak tanladingiz!!!")
        foydalanuvchi_tanlasin(doska)
    else:
        doska[n-1] = 'O'

def bosh_maydonlar(doska):
    """
    doskadagi bo'sh raqamlar ro'yxatini qaytaradi, ya'ni
    (0 va X bo'lmagan raqamlarni) qaytaradi 
    :param 
        doska
    :return 
        list - raqamlardan iborat bir o'lchamli roy'xat
    """
    free = []
    for i in range(1,10):
        if i in doska:
            free.append(i)
    return free
    
def golib_bormi(doska, belgi):
    """
    G'olib borligini aniqlaydi
    :param 
        doska
        blegi - X yoki 0. X - Kompyuter, 0 - foydalanuvchi
    :return
        bool - True agar g'olib mavjud bo'lsa, False g'olib bo'lmasa
    """
    if doska[0] == doska[1] == doska[2] == belgi:
        return True
    elif doska[3] == doska[4] == doska[5] == belgi:
        return True
    elif doska[6] == doska[7] == doska[8] == belgi:
        return True
    elif doska[0] == doska[3] == doska[6] == belgi:
        return True
    elif doska[1] == doska[4] == doska[7] == belgi:
        return True
    elif doska[2] == doska[5] == doska[8] == belgi:
        return True
    elif doska[0] == doska[4] == doska[8] == belgi:
        return True
    elif doska[2] == doska[4] == doska[6] == belgi:
        return True
    else:
        return False
   
def kompyuter_tanlasin(doska):
    """
    Kompyuter qolgan raqamlar orasidan tasodifiy tanlab,
    usha raqam o'niga X belgisini qo'yadi
    :param 
        doska
    :return 
        None - hech narsa qaytarmaydi
    """
    free = bosh_maydonlar(doska)
    if not free:
        return
    n = choice(free)
    doska[n-1] = 'X'

doska = bosh_doska_hosil_qil()

while bosh_maydonlar(doska):
    kompyuter_tanlasin(doska)
    os.system("cls")
    doskani_korsat(doska)
    if golib_bormi(doska, 'X'):
        print("Kompyuter yutdi!!!")
        break
    foydalanuvchi_tanlasin(doska)
    os.system("cls")
    doskani_korsat(doska)
    if golib_bormi(doska, 'O'):
        print("Siz yutdingiz!!!")
        break
else:
    print("Durrang!!!")