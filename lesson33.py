# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 05:37:34 2023

@author: A
"""

# with open('hello.txt') as file :   # with bilan ishlatishi kerak chunki funksiyalar bajarilgandan keyin, avtomat file yopiladi
#     hi = file.read()
# print(hi)

# hi =hi.strip()
# hi=hi.replace('\n','') # .replace('x','y')  x ni y bilan almash tirish function

# print(hi)

# ex_goods='products/exports/goods.txt' # bu papkani ichidagilarni ochish
# with open(ex_goods) as file :
#     for line in file:
        #print(line)
    #items=file.readlines() # file qatorma qator alohida oqish uchun ishlatiladi.
# print(items)   
# print(len(items)) # items ichidagi attributlar soni
        #print(file.readlines()) # bu yo ozgaruvchiga yuklash kerak yoki shu holatda ham print ga bersa ham boladi

# items=[item.rstrip() for item in items] # .rstrip  o`ng tarafdagi bosh joylarni ochiradi.
# print(items) #  for item in items manosi bu items ichidagi har bir elementni tekshiradi va item.rstrip() funksiyasini bajaradi.

# yangi fayl ichiga yozish:

# file_name='new_file.txt' # yangi file ga nom berildi
# name='Sharipov Abdulatif'
# birtday =1990


# with open(file_name,'w') as file : # bu fayldan kn 'w' yani 'write' funksiyasi ishlatildi
#                             ## bunda ehtiyot bolish kerak , sabab agar fileni nomlashda kompda shunga oxshash nom bolsa ichidagi malumotlarni ochirib yuboradi. 
#     file.write(name)
#     file.write(str(birtday)) # doim mant korinishida sahlaydi shuning uchun sonlarni ham str bilan matn korinishiga otkazib olishimiz kerak.
#     """matnlarni alohida qatorlarga yozish"""
#     # file.write(name+'\n')  
#     # file.write(str(birtday+'\n'))

# #file_name='new_file.txt' # yangi file ga nom berildi
# name='Sharipov Abdulatif'
# birtday =1990

            ### bu usulda alohida file nomi ozgaruvchiga yuklanmaydi. togridan togri fayl yaratadi
# with open('my data.py','w') as file : # bu fayldan kn 'w' yani 'write' funksiyasi ishlatildi
#                             ## bunda ehtiyot bolish kerak , sabab agar fileni nomlashda kompda shunga oxshash nom bolsa ichidagi malumotlarni ochirib yuboradi. 
#     file.write(name)
#     file.write(str(birtday)) # doim mant korinishida sahlaydi shuning uchun sonlarni ham str bilan matn korinishiga otkazib olishimiz kerak.
#     """matnlarni alohida qatorlarga yozish"""
#     # file.write(name+'\n')  
#     # file.write(str(birtday+'\n')) 

# Abdulatif='Abdulaitifsh90'
# name = 'Abdulatif'
# Surname='Sharipov'
# birtday = str(1990)
# with open(Abdulatif,'a') as file : # a= append shuning uchun malumot qoshilish mumkin, # bu a yani append funksiyasi orqali mavjud faylga malumot kiritadi, agar mavjud bolmasa yangi yaratadi va kiritadi

#     """ fayllarga malumot qoshish"""    
#     file.write('Birth place:Andijan\n')
#     file.write((str(1990)+'\n'))

# import pickle   # bu modul obyekt yoki ruyxatlarni shunday saqlash uchun ishlatiladi.lekin bu fayl ni faqat Python oqishi mumkin
 
# student1 = {"name":"Alijon","Surname":"Valiyev","birth year": 2000}
# #talaba2 = {"name":"Hasan","Surname":"Alimov","birth year": 2001}

# with open('friends','wb') as file:   #''wb' -  write binary  yani 2 lik sanoq sistemasida yoz degani
#     pickle.dump(student1,file)  #pickle.dump  dump bu malumotlar omborini yaratish, student 1  o`zgaruvchini file ichida pickle korinishida saqlaydi.
    
    
# import pickle
 
# #student1 = {"name":"Alijon","Surname":"Valiyev","birth year": 2000}
# student2 = {"name":"Hasan","Surname":"Alimov","birth year": 2001}

# with open('best friend','wb') as file:
#     pickle.dump(student2,file)
    
# import pickle

# # Seriyalizatsiya uchun obyekt
# data = {'name': 'John', 'age': 30, 'city': 'Tashkent'}

# # Faylni ochish uchun o'rganadigan rejim
# with open('data.pickle', 'wb') as file:
#     # Obyektni seriyalizatsiya qilish va faylga yozish
#     pickle.dump(data, file)


# while True:
#     book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
#     if not book:
#         break
#     with open("books.txt", "a") as file:
#         file.write(book + "\n")
       
# while True:
#     family_members= input('enter your family members ( press the enter button to stop) :')
#     if not family_members:
#         break
#     with open('My family.txt','a') as file:
#         file.write(family_members +'\n')









