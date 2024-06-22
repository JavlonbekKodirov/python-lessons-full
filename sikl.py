# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 07:43:52 2024

@author: hp
"""

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
print("Salom",mehmonlar[0])
print("Salom",mehmonlar[1])
print("Salom",mehmonlar[2])
print("\n\n\n\n")

for mehmon in mehmonlar:
    print("Salom ", mehmon, " honadonimizga hush kelibsiz")
    print("Haayr", mehmon)
    
print("\n\n\n\n")
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 - dekabr kuni bo'lib o'tadigon naxorgi oshga taklif qilamiz")
    #   f"...{..}..."  bu ko'dni biz qavs ichida koplab amal bajarganda ishlatamiz
    # matn va variables(o'zgaruvchi) larni kema-ket consulga chiqarish uchun
    print("Hurmat bilan, Kodirovlar oilasi\n")

print("\n\n\n\n")

## >>>
# sonlar = list(range(1,11))

# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
    #>>>>
sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)

print("\n\n\n\n\n")



dostlar = []
print("5 ta eng yaqin do'stingizni kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}- do'stingizning ismini kiriting:\n\n>>>"))
print(dostlar)


    
    
    
    
    
    
    
    
    
    
    

    