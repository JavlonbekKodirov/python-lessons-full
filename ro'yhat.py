# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 06:54:57 2024

@author: hp
"""

cars = ['Bmw','mercedez benz','volvo','generel motors','tesla','audi']

# print(cars.sort())        # tartiblash


print(cars.sort(reverse=True))


print(sorted(cars))


print(sorted(cars, reverse=True))

sonlar = [12, 45, 23, 56, 998, 1, -5, -7.2]

# sonlar.sort()


# cars.reverse()


print(sonlar)

print(sorted(sonlar))

print(sorted(sonlar, reverse=True))

# len(cars)
# len(sonlar)   ro'yhat qanchaligini bilish uchun

print(list(range(0,10)))    # list yaratish uchun >>range<< ishlaydi
print(list(range(21,30)))

toq_sonlar = list(range(1,20,2))
print(toq_sonlar)
juft_sonlar = list(range(0,20,2))
print(juft_sonlar)
sanash = list(range(0,101,10))
print(sanash)
max_qiymat = max(toq_sonlar)
print(max_qiymat)
print(min(sanash))
print(sum(sanash))

# >>>> ro'yhatdan MALUM QISMINI OLISH


print(cars[0:3])

print(cars[2:4])

print(cars[1: ])


print(cars)

my_cars = cars

print(cars)
print(my_cars)
my_cars.remove('volvo')
print(my_cars)
my_cars[0] = 'Lacetti'



print(cars)

print(my_cars)

cars.append('BMW')

my_cars = cars[:]

print("\n\n\n\n\n\n\n\n\n\n\n\n\n ")
print(my_cars)
my_cars.remove('audi')
print(my_cars)
print(cars)

# >>>>> tuple

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

# toys[0] = 'teddy'                amalga oshirib bolmaydigon ozgarishklar
# print(toys.appen('teddy'))
# toys.remove('cars')

toys  = list(toys)      # tuple ni oddiy listga aylantarish 

toys.append('teddy')

print(toys)

# toys = tuple(toys)     qaytadan tuple listga aylantirish

print(toys)








