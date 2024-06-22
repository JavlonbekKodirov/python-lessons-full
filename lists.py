# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 00:41:35 2024

@author: hp
"""

mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']
#            0    ,    1   ,    2     ,     3    

narxlar = [1200, 1800, 10900, 22000, 3600, -25, 64.2]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = [ ]

print(mevalar[0])
print(mevalar[2])
print("print(mevalar[3])")
print(mevalar[3])
print("print(mevalar[-1])")
print(mevalar[-1])

print(mevalar[0].upper())
print(mevalar[0].title())

print(narxlar[0] + narxlar[1])

print(mevalar)

print(" \n\n\n\n\n\n\n\n")


mevalar[0] = 'anor'
print(mevalar[0])

mevalar[-1] = 'uzum'
print(mevalar[-1])


# append - ro'yxatga yangi qo'shish

mevalar.append("tarvuz")
mevalar.append("o'rik")
print(mevalar)

mevalar.insert(0, "banan")
print(mevalar)

mevalar.insert(3, 'ananas')
print(mevalar)

print("\n\n\n>>>")
cars =[]

cars.append('Lacetti')
cars.append('Nexia')
cars.append('Malibu')
cars.append('Tracker')

del cars[0]

cars.insert(0,'Nexia 3')
del cars[1]

print(cars)
print(">>>\n\n\n")
cars.remove("Malibu")
print(cars)

print(">>>\n\n\n")

hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
print(hayvonlar)
hayvonlar.remove("mushuk")
print(hayvonlar)

print(">>>\n\n\n\n")

bozorlik = ['yog\'', 'un', 'piyoz', 'banan', 'go\'sht']
print(bozorlik)

mahsulot = bozorlik.pop(1)

print(">>>\n\n Men " + mahsulot + " sotib oldim")


print(">>>\n\n Olinmagan mahsulotlar: ", bozorlik, " qoldi.")


mahsulot2 = bozorlik.pop()
print(bozorlik)



narxlar.remove(-25)
print(narxlar)
narxlar.remove(64.2)
print(narxlar)

narxlar[0] = narxlar[0] + 2000
print(narxlar)
 





























