
# print("Hello world!")
# print('Hayrli tong!')
# print('men "HP" markasidagi laptop sotib oldim')
# print("""Odami ersang, demagil odami,
# Oniki, yo'q g'amidin g'ami""")
# print("Odami ersang, \ndemagil odami, \nOniki, yo'q xalq \ng'amidin g'ami")
# print('Odami ersang, demagil odami, Oniki, yo\'q g\'amidin g\'ami')
# print("Odami ersang, demagil odami, Oniki, yo'q g'amidin g'ami")
# print(6+9*2)
# print(21//3)
# print(21/3)
# print(2**4)
# print("To'qqizning kvadrati", 9**2,"ga teng")
# print('89x89=',89**2)
# ism = "Javlonbek"
# familya = "Kodirov"
# yil = "2002.03.14"
# joy = "Namangan, Uchqo'rg'on"
# raqam = "+998 94 274 29 81"
# # print(ism, familya, yil, joy) 
# a=2
# b=3
# c=(a+b)**2
# print(c)
# matn = "Men yangi ⚽ sotib oldim"
# print (matn)
# print("Mening ismim " + ism)
# print(ism +' '+ familya)
# ism_sharif= f"{ism} {familya}"
# print(ism_sharif)
# print(f"Salom mening ismim {ism}.{ism_sharif}")
# print("Hello world")

# print("hello \tworld")
# print("Hello \nworld")


#       string metodlar
# ism = "Javlonbek"
# familya = "Kodirov"
# ism_sharif= f"{ism} {familya}"
# ism_sharif= ism_sharif.upper()


# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# # print(ism_sharif.capitalize())
# print(ism_sharif.casefold())
# print(ism_sharif.center())
# 
# meva='     olma    '
# print(meva)
# print("Men "+meva.lstrip()+"ni yaxshi ko'raman")
# print("Men "+meva.rstrip()+"ni yaxshi ko'raman")
# print("Men "+meva.strip()+"ni yaxshi ko'raman")

# INPUT
# ism = input("Ismingiz nima?")
# print("Assalamu aleykum" + ism)

# ism = input("Ismingiz nima?\n>>>")
# print("Assalomu aleykum, " + ism.title())
 
# amaliyot

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# manzil=f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil)

# print(manzil.upper())
# print(manzil.lower())
# print(manzil.title())
# print(manzil.capitalize())

# 2-qism

# print("Iltimos, quyidagi malumotlarni kiriting!:")
# kocha=input("Ko'changiz: ")
# mahalla=input("Mahallangiz: ")
# tuman=input("Tumaningiz: ")
# viloyat=input("Viloyatingiz: ")
# print(kocha.title()+" ko'chasi,\n "+ mahalla.title()+" mahallasi,\n "
#       +tuman.title()+" tumani,\n "+viloyat.title()+" viloyati,\n ")


# a = int("10")
# b = float("10")
# temp = str(36.6)

# print(type (a)) 
 
# aholi_soni = 7_594_765_654
# print("aholi soni", aholi_soni)


# x,y,z = 10,15,20
# print(y+x*z)

   # Constant qiymat

# radius = 30
# PI = 3.14159
# diametr = 2*radius
# print ("aylana uzunli=",PI*diametr)


# ism = "Javlonbek"
# yosh = 22
# # yosh = str(yosh)
# xabar = ism + ' ' + str(yosh) +' yoshda'

# print(xabar)

# tug_yil = int(input("Tug'ilgan yilingizni kiriting\n>>>"))
# yosh = 2024 - tug_yil

# print("Siz", yosh, "yoshda ekansiz")

#list 

# mevalar =['olma','anjir','shaftoli',"o'rik"]
# narxlar = [1200,1600,1800,2200,2500,3500]
# sonlar = ['bir','ikki',3,4,5] 
# ismlar = []
# print("Birinchi meva:", mevalar[0])
# print("Ikkinchi meva:", mevalar[-1])

# print("Birinchi meva", mevalar[0].upper())
# print("Birinchi meva", mevalar[0].title())

# print("birinchi narx:", narxlar[0])

# cars = []
# cars.append('Lacetti')
# cars.append('Malibu')
# cars.append('Tracker')
# cars.append('Nexia')
# # print(cars)

# del cars[0]
# # print(cars)
# cars.insert(0,"Nexia 3")

# del cars[-1]
# # print(cars)

# cars.remove("Malibu")

# # print(cars)

# hayvonlar =['it', 'qo\'y', 'mushuk', 'sigir', 'quyon', 'mushuk']
# # print(hayvonlar)

# hayvonlar.remove('it')
# # print(hayvonlar)
# del hayvonlar[2]
# # print(hayvonlar)

# # print(hayvonlar)

# bozorlik = ["yog\'", 'un', 'piyoz', 'banan', "go\'sht"]

# # print(bozorlik)

# mahsulot = bozorlik.pop(1)
# # print("Men bugun bozordan " + mahsulot.upper() + " sotib oldim")
# # print("Olinmagan mahsulotlar: ", bozorlik)


# mahsulot2 = bozorlik.pop()

# # print(bozorlik)


# cars = ['BMW','Mersedes Benz','Volvo','GMuzb','Tesla','Audi']

# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)


# print(sorted(cars))  = asl ro'yhatga tegmay o'zgartiradi

# print(sorted(cars, reverse=True))


# sonlar = [12, 211,233,322,323,87,876,96,2, -1]

# # print(sorted(sonlar, ))

# # print(len(sonlar))  = uzunlik uchun

# # list yashash uchun list(range(a,b))
# sonlar2 = list(range(1,20))   
# print(sonlar2)

# toq_sonlar = list(range(1,20,2))
# print(toq_sonlar)

# # harflarda ishlamadi
# # harflar = list(range(a,t))
# # print(harflar)

# juft_sonlar = list(range(0,20,2))
# print(juft_sonlar)

# sanash = list(range(0,101,10))
# print(sanash)

# # eng katta qiymatni aniqlash
# max_qiymat = max(toq_sonlar)
# print(max_qiymat)

# print(sum(sanash))


# cars = ['BMW','Mersedes Benz','Volvo','GMuzb','Tesla','Audi']

# # print(cars[0:3])  ['BMW', 'Mersedes Benz', 'Volvo']

# # print(cars[:4])   ['BMW', 'Mersedes Benz', 'Volvo', 'GMuzb']

# my_cars = cars
# # print(cars)
# # print(my_cars)

# my_cars.remove('Volvo')
# # print(my_cars)
# my_cars[0] = 'Damas' 
# # print(my_cars)

# # print(cars)   ['Damas', 'Mersedes Benz', 'GMuzb', 'Tesla', 'Audi']

# cars.append("BMW")

# # print(cars)  ['Damas', 'Mersedes Benz', 'GMuzb', 'Tesla', 'Audi', 'BMW']
# # print(my_cars)  ['Damas', 'Mersedes Benz', 'GMuzb', 'Tesla', 'Audi', 'BMW']


# # copy qilish
# cars = ['BMW','Mersedes Benz','Volvo','GMuzb','Tesla','Audi']

# my_cars = cars[:]

# # print(my_cars)
# # print(cars)

# my_cars.remove("Volvo")
# my_cars.remove("GMuzb")
# # print(my_cars)   ['BMW', 'Mersedes Benz', 'Tesla', 'Audi']
# # print(cars)      ['BMW', 'Mersedes Benz', 'Volvo', 'GMuzb', 'Tesla', 'Audi']
# # copy qilindi - done

# # tuple  - o'zgarmas ro'yxat

# toys = ('bus','car','bear','dino','lizard')

# # print(toys[0])

# # toys[0] = 'teddy'
# # toys.append('teddy')
# # print(toys)

# toys = list(toys) #tuble  ni o'zgartirish

# print(type(toys))
# toys.append('teddy')
# print(toys)


# sikl
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'OLim']
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print("Hayr", mehmon)
 



   
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'OLim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-may kuni nahorgi oshga taklif qilamiz")
#     print("Hurmat bilan Kodirovlar oilasi\n")


# sonlar = list(range(1,11))

# for son in sonlar:
#     print(f"{son} ning kvatrati {son**2} ga teng")
    

# sonlar = list(range(0,10))
# sonlar_kvadrati = []
# for son in sonlar: # har bie son uchun
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range (5): # n bu yerda 0 dan 5 gacha sonlarni oladi 
#     dostlar.append(input(f"{n+1}-do\'stingizning ismini kiriting: \n>>>"))
#     print(dostlar)
    

    


















