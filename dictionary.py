# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:11:55 2024

@author: hp
"""


## >>>


car_0 = {'model':'Ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])

eng_uz = {'apple':'olma','apricot':'o\'rik','banana':'banan'}
print(eng_uz['apple'])
print(eng_uz['banana'])
print(eng_uz['apricot'])

mevalar = {'olma':10000,'tarvuz':8000,'qovun':10000}
print(f"Olmaning narhi {mevalar['olma']} so'm")
print(mevalar['qovun'])


talaba_0 = {'ism':'javlon kodirov','yosh':22,'t_yil':2002}
print(f"{talaba_0['ism'].title()},\
   {talaba_0['t_yil']}-yilda tuguilgan,\
   {talaba_0['yosh']} yoshda")
print(talaba_0)
del talaba_0['yosh']
print(talaba_0)

print(eng_uz)
del eng_uz['apple']
print(eng_uz)


talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika'
print(talaba_0)

talaba_0['ism'] = 'Javlonbek'
print(talaba_0)

talaba_1 = {}
print(talaba_1)

talaba_1['ism']='qobil rasulov'
talaba_1['kurs']= 3
talaba_1['yosh']= 24
print(talaba_1)

talaba_1['kurs'] = 4
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")



telefonlar = {
    'ali':'iphone',
    'vali':'gallaxy',
    'olim':'redme',
    'orif':'Huawei',
    'tolib':'honor',
    'bobur':'samsung',
    }
print(telefonlar)

phone = telefonlar.get('murot','bunday ism mavjud emas')

print(phone)


# phone = telefonlar.get('hasan')
# print(phone)


















































