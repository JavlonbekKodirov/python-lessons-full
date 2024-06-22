# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:11:36 2024

@author: hp
"""

talaba_0 = {
    'ism':'alijon',
    'familya':'shamsiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }
print(talaba_0)

print(talaba_0.items())

for key, value in talaba_0.items():
    print(f"Key: {key}")
    print(f"Value: {value} \n")


telefonlar = {
    'ali':'iPhone',
    'vali':'gallaxy',
    'olim':'redmi',
    'orif':'Huawei',
    'tolib':'honor',
    'bobur':'samsung',
    'jasur':'iPhone',
    'javlon':'redmi',
    'anvar':'iPhone'
    }

for key,value in telefonlar.items():
    print(f"{key.title()}ning telefoni {value}")


print("\n\n\n\n\n\n>>>")

print('Foydalanuvchilar quyidagi telfonlarni ishlatadi: ')
for tel in telefonlar.values():
    print(tel)
    
    
print('Foydalanuvchilar quyidagi telfonlarni ishlatadi: ')
for tel in set(telefonlar.values()):
    print(tel)    
  
    

toys = {'ball','car','lamp','ball','bear','car'}
print(toys)






    
    
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print("\n\n\n\n\n\n \n\n\n\n>>>>>")


print(mahsulotlar.keys())
print(mahsulotlar.values())
print(mahsulotlar.items())

# print(mahsulotlar.clear())

print("Do'kondagi mahsulotlar: \n")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

print("Mahsulotlar narhlari: \n")
for narh in mahsulotlar.values():
    print(narh)
  
print("Do'kondagi mahsulotlar: \n")
for mahsulot in mahsulotlar:   # .keys metodsiz ham key chiqadi
    print(mahsulot.title())

print("\n\n\n\n\n\n>>>>")

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
    
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")


print("\n\n\n\n\n\n>>>>")

print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar) :
    print(mahsulot.title())

print(mahsulotlar.keys())
print(telefonlar.values())



### >>>> amaliyot 


py_izoh_lugat = {'car':'mashina',
                 'map':'harita',
                 'cat':'mushuk',
                 'dog':'it',
                 'it':"U (jonsiz narsalarga)",
                 'push':'surmoq',
                 'pull':'tortmoq',
                 'mug':'krushka',
                 'nice':'chiroyli',
                 'bat':"ko'rshapalak",
                 'donkey':'eshshak',
                 'red':'qizil',
                 'look':'qaramoq',
                 'feed':'boqmoq, parvarish qilmoq',
                 'foot':'oyoq',
                 "apple":'olma'
                 }
for keys,values in sorted(py_izoh_lugat.items()):
    print(f"{keys.title()} - {values}")




## >>>

dav_poytaxt = {'uzbekistan':'tashkent',
               'qatar':'doha',
               'england':'london',
               'germany':'berlin',
               'azarbaijan':'baku',
               'russia':'moscow',
               'japan':'tokio',
               'china':'pijeng',
               'france':'paris',
               'australia':'kanberra',
               'turkey':'istanbul',
               'south korea':'seul'
               }
print("Davlatlar: ")
for keys in sorted(dav_poytaxt.keys()):
    print(keys.title())
print("Davlatlarning poytaxtlari: ")
for values in sorted(dav_poytaxt.values()):
    print(values.title())
    
## >>>

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:\n>>>').lower()
capital = dav_poytaxt.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")



#### >>>

# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")







