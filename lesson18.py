# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 23:07:47 2023

@author: A
"""

import random

def son_top (x):
    tasodifiy_son = random.randint(1, 10)
    print(f"Men shunday {x} son o`yladim ")

    while True:
        taxmin = int(input(">>> "))
        if taxmin < tasodifiy_son:
            print("Xato! Men o'ylagan son bundan katta, boshqa kiriting >>>")
        elif taxmin > tasodifiy_son:
            print("Xato! Men o'ylagan son bundan kichik, boshqa kiriting >>>")
        else:
            print("Tabriklayman!")
            break
a=random.randint(0,10)
son_top(a)   

# names=[]

          
# print("make the list of the best friends.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     names.append(input( f"{n}-please, enter your best friend`s name:"))
#     ans= input("do you want to add another ? (yes/no)")
#     if ans !='no':
#         n+=1
#         continue
#     else:
#         break
# my_dict=dict(enumerate(names,start=1))   
# for name in names.items():
#     print(f"you have {name}")

# names = []

# print("Make the list of your best friends.")
# n = 1  # Variable to count names
# while True:
#     name = input(f"{n} - Please enter your best friend's name: ")
#     names.append(name)
#     ans = input("Do you want to add another? (yes/no) ")
#     if ans.lower() != 'no':
#         n += 1
#     else:
#         break
# print("you are the best friends:")
# my_dict = dict(enumerate(names, start=1))
# for n,name in my_dict.items():
#     print(name, end =' ,' )


# print("Make the list of your best friends.")
# names = {}
# n = 1  # Variable to count names
# while True:
#     name = input(f"{n} - Please enter your best friend's name: ")
#     names[n]=name
#     ans = input("Do you want to add another? (yes/no) ")
#     if ans.lower() != 'no':
#         n += 1
#     else:
#         break
# print("you are the best friends:")
# for n, name in names.items():
#     print(f"{n}-{name}", end =' ' )


# print("make our favorite list of brands: ")

# brands={}
# n = 1

# while True:
#     brand=input(f"{n}- please enter your lovely brand : ")
#     brands[n]= brand
#     prompts = input("would you like to add another one again? \n        yes/ no : ")
#     if prompts.lower() != 'no':
#         n+=1
#     else:
#         break
# print("you are the most favourite brnads:")
# for n, brand in brands.items():
#     print(f"{n}-{brand}", end =' ' )


# phones = ['iphone','Nokia','Matarola','Samsung']
# users ={}

# while phones:
#     x=phones.pop()
#     costs = input(f"enter cost of {x} :  ")
#     users[x]=int(costs)

# for x,costs in users.items():
#     print(f"{x} - {costs}")
 