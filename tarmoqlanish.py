# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:01:26 2024

@author: hp
"""

# if - >>>

avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar:
    # print(avto.title())   #>>> result =  Audi Bmw Volvo Kia Hyundai
    if avto =='bmw':
        print(avto.upper())
    else: 
        print(avto.title())
  
## ism = 'Ali'
## ism.lower() == 'ali'

## input ism

print("\n\n\n\n\n\n\n\n>>> ")


ism = input('Ismingiz nima?\n>>>')
if ism.lower() != 'ali':
    print(f"Uzur {ism.title()}, biz Alini kutyapmiz ")
else:
    print("Salom Ali, Tizimga hush kelibsiz!")
    
  # if >> sonlar
  
javob = float(input("12x6 nechiga teng? \n>>> "))
if javob != 72:
    print("Javob xato")
else:
    print("Topdingiz, \n Gap yo'q og'a siz eng zo'risiz, sizdan zo'ri yo'q ")
    
# >>>>

yosh = int(input("Yoshingiz nechida? \n\n>>>"))
if yosh >= 18:
    print("'Xush keldingiz Tog'o'o'o'o'o'o'o'o'! ")
else:
    print("\n Mumkinmas senga, Pashol naxxuye, sur bettan, eeeee-oneniii... ")
    
# >>>

login = input("Yangi lo'gin tanlang! \n\n>>>")
if len(login) <= 8:        # len - matn uzunligini tekshiradi.
    print("Login must contain at least 8 letters or symbols!")

# >>>

yil = int(input("Tug'ilgan yilingizni kiriting! \n\n>>>"))
if 2024-yil<18:   # hozirgi yildan foydalunivchi kiritgan yilni ayrish = yosh
    print(f"Yoshingiz {2024-yil}da ekan.")
    print('kirish mumkin emas')
else:
    print("Xush keldingiz!!!....")

# >>>

yosh = int(input("Yoshingiz nechida? \n\n>>>"))
if yosh >= 65:
        print("Siz COVID-19 risk guruhid ekansiz")
else:
    print("Vaksina ol 'Tvar'")
# >>>

x,y = 30,35
print("x>y") if x>y else print("x<y")







# AAAAAAAAAAA >>> amaliyot 






cars = ['toyota', 'mazda', 'hyundai', 'gm', 'byd', 'kia']
for car in cars:
    if car != "gm":
        print(car.upper())
    # if car == "byd":
    #     print(car.upper())
    else:
        print(car.title())

# >>>

login = input("Loginni Kiriting! \n\n>>>")
if login.lower() == "admin":
    print("Xush kelibsiz! Admin.\n Foydalunuvchilar ro'yhatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}!")







# >>> yemagan dastur

x = float(input("Birinchi sonni kiriting:\n\n>>> "))
y = float(input("Ikkinchi sonni kiriting:\n\n>>>"))
if x==y: print(f"Sonlar teng: {x}={y}")
else:
    print("Xar hil sonlar")
    








son = int(input("Istalgan sonni kiriting. \n\n>>>"))
if son<0:
    print("Manfiy son")
if son>0: 
    print("Musbat son")






































