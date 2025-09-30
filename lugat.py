car_0 = {'model' : 'ferrari', 'rang' : 'qizil'}
print(car_0['model'])
print(car_0['rang'])

en_uz = {'apple' : 'olma', 'apricot' : "o'rik", 'banana' : 'banan'}
print(f"Apple - {en_uz['apple']}")
print(en_uz['apricot'])

mevalar = {'olma' : 12000, 'tarvuz' : '15000', 'qovun' : '24300'}
print(f"Olmaning narxi - {mevalar['olma']} so'm")

talaba_0 = {'ism' : 'izzatbek', 'yosh' : 23, 't_yil' : 2002}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['yosh']} yoshda,\
 {talaba_0['t_yil']}-yilda tug'ilgan")

# Lug'atga yangi kalit so'z va qiymat qo'shish
talaba_0['kurs'] = 1
talaba_0['fakultet'] = 'dasturiy injiniring'
# talaba_0['ism'] = 'john'

print(talaba_0)

# Bo'sh lug'at yaratish
talaba_1 = {}
talaba_1['ism'] = 'alex'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 22
print(f"{talaba_1['ism'].title()},\
 {talaba_1['yosh']} yoshda,\
 {talaba_1['kurs']}-kursda o'qiydi")

# Lug'atdagi biror bir qiymatni yangilash
talaba_1['ism'] = 'smith'
print(f"{talaba_1}")

# Lug'atdagi elementlarni o'chirish
