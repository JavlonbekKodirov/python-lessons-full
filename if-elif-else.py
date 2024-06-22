# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:34:12 2024

@author: hp
"""

# if-elif-else
son = 50
if son<0:
    print("manfiy son")
else:
    print("musbat son")    



# >>>

# yosh = int(input("Yoshingiz nechida?\n>>>"))
# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5 000 so'm")
# elif yosh<=18:
#     print("Sizga kirish 8 000 so'm")
# else:
#     print("sizga kirish 10 000 so'm")
   
    
# yosh = int(input("Yoshingiz nechida?\n>>>"))
# if yosh<=4:
#     narx =0
# elif yosh<=12:
#     narx =5000
# elif yosh<=18:
#     narx = 8000
# else:
#     narx = 10000
# print(f"Sizga kirish {narx} so'm")

# #>>>

# kun = input("Bugun nima kun?\n>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")
    

# # >>>

# kun = input("Bugun nima kun?\n>>>")
# harorat = float(input("Havo harorati qanday?\n>>>"))
# if kun.lower() =='yakshanba' and harorat>= 30:
#     print("Bugun bolla bilan tog'ga boramiz.")
# elif kun.lower()=='yakshanba' and harorat<=30:
#     print("Uyda dam olamiz.")

# # >>>

# kun = input("Bugun nima kun?\n>>>")
# harorat = float(input("Havo harorati qanday?\n>>>"))
# if (kun.lower() =='yakshanba' or kun.lower()=='shanba') and harorat>= 30:
#     print("Bugun bolla bilan tog'ga boramiz.")
# elif (kun.lower() =='yakshanba' or kun.lower()=='shanba') and harorat<=30:
#     print("Uyda dam olamiz.")

# # >>> 

# narh = 15000
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
# print(f"Jami {narh} so'm ")


# # >>>

# narh = 15000
# choy = True
# salat = 0
# non = True
# kompot = True
# assorti = 1

# if choy: 
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti :
#     print("Mijoz assorti oldi")
#     narh = narh + 15000
# print(f"Jami {narh} so'm bo'ldi.")

# # >>>
# menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
# ovqat = input("Nima ovqat yeysiz?\n>>>")
# if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo'q.")
# else:
#     print("Buyurtma qabul qilindi.")
    
# >>.

menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
buyurtmalar = ['osh','somsa','manti','shashlik']

if buyurtmalar: 
    for taom in buyurtmalar: 
        if taom in menu: 
            print(f"Menuda {taom} bor.")
        else: 
            print(f"Kechirasiz, menuda {taom} yo'q.")






























