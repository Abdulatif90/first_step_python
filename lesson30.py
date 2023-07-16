# # -*- coding: utf-8 -*-
# """
# Created on Wed Jul  5 22:47:05 2023

# @author: A
# """

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
       
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
# inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
# # class Talaba(Shaxs):
# #     """Talaba klassi"""
# #     def __init__(self, ism, familiya,passport,tyil):
# #         """Talabaning xususiyatlari"""
# #         super().__init__(ism, familiya,passport,tyil)
# # talaba = Talaba("Valijon","Aliyev","FA112299",2000)
# # print(talaba.get_info())
# # print(talaba.get_age(2021))
# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def __init__(self,uy,kocha,tuman,viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
    
#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
# talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
# print(talaba.idraqam.get_manzil())
# print(talaba.info.tuman)



# from uuid import uuid4 

class ParentClass:
    def __init__(self):
        self.parent_attribute = "Parent Attribute"

    def parent_method(self):
        print("Parent Method")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Calling the parent class's constructor
        self.child_attribute = "Child Attribute"

    def child_method(self):
        super().parent_method()  # Calling the parent class's method
        print("Child Method")
        print('hi bro')
    
    def qanaqa 
        
child = ChildClass()
child.child_method()
 