# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 22:49:35 2023

@author: A
"""

# x=10
# print(type(x))
# def salom():
#     print('Assalomu alaykum')
# salom()

# class Car():
#     def __init__(self,brand_name,color,pyear):
#         self.brand=brand_name 
#         self.color=color
#         self.p_year=pyear
#     def get_brand(self):
#         return self.brand
#     def get_name(self):
#         return self.color
#     def get_pyear(self):
#         return self.p_year
#     def get_year(self,cyear):
#         return cyear -self.p_year
    
# car1 = Car('Toyota','blue',2018)



class user():
    def __init__(self,nic_name,name,surname,e_mail,p_number):
        self.nic_name= nic_name
        self.name= name
        self.surname= surname
        self.e_mail= e_mail
        self.p_number=p_number
    def nic_name(self):
        return self.nic_name
    def name(self):
        return self.name
    def surname(self):
        return self.surname
    def e_mail(self):
        return self.e_mail
    def p_number(self):
        return self.p_number
    def intro (self):
        print(f"User: {self.nic_name}  full name: {self.name} {self.surname}  e-mail: {self.e_mail}  phone number : {self.p_number}")
user1= user('Abdulatifsh90','Abdulatif','Sharipov','abdulatifsh90@gmail.com','01083169495')
user1.intro()
       
    
    
        
        
        