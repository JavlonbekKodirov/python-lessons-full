# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:03:38 2024

@author: hp
"""

# MAVZU STRING

ism = "Javlon"


shahar = "Uchqo'rg'on"
viloyat = "Namangan"

matn = "Men yangi  💻  sotib oldim"
smayl = "😂"

print(matn)

#  >>>>>
ism = "Ahmad"
print("Mening ismim " + ism)

ism = "Ahad"
familya = "Qayum"
print(ism +' ' + familya)

    # f - string

ism = "Ahad"
familya = "Qayum"
ism_sharif = f"{ism} {familya}"
print(ism_sharif)

print("Code:  " + 'print(f"Mening ismim {ism}")')
print("Natija: " + f"Mening ismim {ism}")

print("\n\n\n\n\n\n\n\n\n\n")

print(f"Mening ismim {ism}")

print(ism_sharif)

# >>>>

ism = "James"
familya = "Bond"
print(f"Salom, Mening ismim {ism}. {ism} {familya}!")

# Mahsus belgilar

print("Hello world!")
print("Hello \tworld!")   # uzun bo'shliq
print(" ")
print("Hello \nworld!")    # qatot tashlash

# string medotlar

print(" ")

ism = "Monk"
familya = "Edriyan"
ism_sharif = f"{ism} {familya}"
ism_sharif = ism_sharif.upper()
print("print(ism_sharif.upper())")
print(ism_sharif.upper())
print(" ")
print(ism_sharif.title())
print(" ")
print(ism_sharif.capitalize())
print(" \n\n\n\n\n\n\n")

#  >>>>

meva  = "      olma     "
print(meva)

print("men "+ meva.lstrip() + "ni yaxshi ko'raman")
print("men "+ meva.rstrip() + "ni yaxshi ko'raman")
print("men "+ meva.strip() + "ni yaxshi ko'raman")
print("men "+ meva + "ni yaxshi ko'raman")

# Input savol so'rash


print("\n\n\n\n\n\n\n\n\n")

ism = input("Ismingizni nima?\n>>>")
print("Assalomu aleykum, " + " Janob " + ism.title())

viloyat = input(" Janob " + ism.title() + ", Qaysi viloyatdansiz?\n>>>")
tuman = input("Janob " + ism.title() + ", Qaysi tumandansiz?\n>>>")

print('\n\n\n\n\n\n\n\n\n\n\n\n' "Janob " + ism.title() + """,\n Sizning yashash manzilingiz: 
O'zbekiston Respublikasi, \n""" + viloyat.title() + " viloyati,\n" + tuman.title() + " tumani.")

tasdiq = input("Malumotlar to'g'ri ekanligini tasdiqlaysizmi?\n>>>")
print(tasdiq.title() + "\n\n\n\n\n E'tiboringiz uchun rahmat!")






