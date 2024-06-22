# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:20:21 2024
#16-dars: NESTING
Javlonbek Kodirov


"""

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'karobka':'avtomat'
        }
car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'karobka':'mexanika'
        }
car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'karobka':'mexanika'
        }

car = car0
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, {car['narh']}$")

car = car1
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, {car['narh']}$")

car = car2
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, {car['narh']}$")

cars = [car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")

print(cars[0]['model'])   ### ro'yhat ichidagi lugatga murojat

print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2024,
        'narh':None,
        'km':0,
        'karobka':'avto'
        }
    malibus.append(new_car)
    
for malibu in malibus[:3]:
    malibu['rang']='qizil'

for malibu in malibus:
    print(malibu)
    
for malibu in malibus[3:6]:
    malibu['rang']='qora'
    
for malibu in malibus:
    print(malibu)

for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['karobka']='mehanika'
    
for malibu in malibus:
    print(malibu)

for malibu in malibus:
    if malibu['karobka']=='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000

for malibu in malibus:
    print(malibu)

#>>>>

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini \
biladi: ")
    for til in tillar :
        print(til.upper())
        
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini \
biladi:", end=' ')
    for til in tillar :
        print(f"{til.upper()}", end=' ')
        print(til.upper(), end=' ')      # bu medot ham ish berdi 


# >>>>


hamkasblar = {
    'ali':{'familya':'valiyev',
            't_yil':1995,
            'malumot':'oliy',
            'tillar':['python','c++']
            },
    'vali':{'familya':'aliyev',
            't_yil':2001,
            'malumot':'o\'rta-maxsus',
            'tillar':['html','css','js']
            },
    'hasan':{'familya':'husanov',
            't_yil':1999,
            'malumot':'maxsus',
            'tillar':['python','php']
            }
    }
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familya'].title()}, "
          f"{info['t_yil']}-yilda tug'ilgan."
          f"Malumoti: {info['malumot']}.\n"
          "Quyidagi dasturlash tillarini biladi: ", end='')
    for til in info['tillar']:
        print(til.upper(), end=' ')
        
        
        









































