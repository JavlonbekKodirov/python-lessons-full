# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 01:07:16 2024

@author: hp
"""

# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")


## 2>>>

# yosh = int(input("Yoshingiz nechida?\n>>>"))
# if yosh <=4 or yosh >=60:
#     print("Sizga kirish bepul.")
# elif yosh <= 18:
#     print("Sizga kirish 10 000 so'm")
# else:
#     print("Sizga kirish 20 000 so'm")

## 3 >>>

# x = float(input("Birinchi sonni kiriting:\n>>> "))
# y = float(input("Ikkinchi sonni kiriting:\n>>> "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


## >>>

# son = float(input("Juft son kiriting: "))

# if son%2 :
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")

# ## >>>

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")


# ## >>>

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else: 
#     print(f"{x}>{y}")

## >>>

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

## >>>

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# elif mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

### >>>

users = ['alisher1983','aziza','yasina','umar']

login = input("Yangi login tanlang:")

if login.lower() in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")

