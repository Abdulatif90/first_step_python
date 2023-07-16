# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 05:10:26 2023

@author: A
# """

while True:
    try:
        yosh = input("Yoshingizni kiriting ('exit' dan chiqish uchun): ")
        if yosh.lower() == 'exit':
            break
        yosh = int(yosh)
    except ValueError:
        print("Iltimos, butun son kiriting!")
    else:
        print(f"Siz {2021 - yosh} yilda tug'ilgansiz")


