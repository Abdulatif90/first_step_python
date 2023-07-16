# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 05:26:52 2023

@author: A
"""

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
        
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
# talaba1=Talaba('Sharipov','Abdulatif',1990)
# print(talaba1.get_info())

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
# talaba1=Talaba('Sharipov','Abdulatif',1990)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())




# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
# matem=matematika.get_students()
# m=Talaba.get_info(talaba1)
# print(f"Matematike darsida {matematika.talabalar_soni} ta o`quvchi bor")
# print(f"Ularning ma`lumoti quyidagilar: {matem}")
# print(f"Ularning ma`lumoti quyidagilar: {m}")

# class Cars():
#     def __init__(self,car_name,color,p_year,costs):
#         self.car_name =car_name
#         self.color=color
#         self.p_year=p_year
#         self.costs=costs
#     def get_info(self):
#         """ full information of the car"""
#         return f"This car`s name is {self.car_name.upper()},its color is {self.color}, and it was produced in {self.p_year} and its cost is {self.costs}$."        
# x=Cars('Toyota','blue',2022,38000).get_info()
# print(x)        
# class Autosalon():
#     def __init__(self,salon_name,address,brands,prices):
#         self.a_name=salon_name
#         self.address=address
#         self.brand=brands
#         self.price=prices
#         self.km=0
        
#     def set_km(self, km):
       
#         if km > 0:
#             self.km += km
#         else:
#             print("You entered an invalid number of kilometers.")
#     def get_info(self):
#         return f"Your salon`s name is {self.a_name}, its address is {self.address}, brands are {self.brand},{self.price} $,{self.km} km"


# salon = Autosalon('Afrosiyob', 'A.Temur st, 19 home', 'Toyota', 90000)

# km_input = int(input("Enter the car's km: "))
# salon.set_km(km_input)

# salon_info = salon.get_info()
# print(salon_info)
#       # 

            
        
        
                





























