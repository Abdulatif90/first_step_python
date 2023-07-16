# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:18:59 2023

@author: A
"""

# print('Keling, o`ylagan sonni topish o`ynaymiz!\n1 dan 10 gacha sonlar orasidan bir son o`yladim, topishga harakat qiling?')

# import random as r
# def a(d):
#     n=0
#     while True:
#         n+=1
#         b=int(input("o`ylagan soningizni kiriting: "))
#         if b>x:
#             print('Men o`ylagan son bundan kichikroq!')    
#         elif b<x:
#             print("Men o`ylagan son bundan kattaroq!") 
#         else:
#             break
#     return n    
#     print(f"Siz {n}  ta taxmin bilan to`g`ri  topdingiz.Tabriklayman!")   
# x=r.randint(0,10)
# a(x)

import random as r

def pc(y):
    input(f"1 dan {y} gacha sonlar orasidan bir son o`ylang, topishga harakat qilaman: ")
    a=0
    b=y
    n=0
    while True:
        n+=1
        if a!=b:
            x=r.randint(a,b)
        else:
            a=b
            print(f"{a}")
            break
        prompts=input(f"{x} togri (t),katta bolsa (+), kichik bolsa (-) ".lower())
        if prompts=='-':
            b=x-1
        elif prompts=='+':
            a=x+1
        else:
            break
    print(f"men {n}  ta taxmin bilan to`g`ri  topdim!")   
    return n  
pc(10)
    
    