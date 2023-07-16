# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:01:36 2023

@author: A
"""
# # import math
# # c=lambda pi,r: 2*pi*r
# # print(c(math.pi,20))

# a=lambda x,y: x*y
# print(a(2,3))


# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# def x(y):
#     return lambda a: a*y
# b=x(2)
# d=x(3)
# print(f"{d(3)} {b(3)}")


# from math import sqrt
# x=list(range(20))
# y=list(map(sqrt,x))


# x=list(range(15))
# def a(n):
#     return n**2
# print(list(map(a,x)))

# x=list(range(15))
# a=list(map(lambda y:y**2,x))
# print(a)
# a=[]
# for b in c:
#     a.append(b**2)

# x va y ni bir biriga qo`shish
# y=[5,7,8,9,10, ]
# x=[9,10,5,4,3,8]

# x_y=list(map(lambda a,b:a+b,x,y))
# print(x_y)


# fruits={'apple','kiwi','applepine','apricos'}
# print(list(map(lambda string:string.capitalize(),fruits)))

# # filtering even numbers
# import random as r 
# x=r.sample(range(20),5)
# def a(n):
#     return n%2==0
# a=list(filter(a,x))
# print(a)
# print(x)

# # filtering odd numbers
# import random as r 
# x=r.sample(range(20),5)
# def a(n):
#     return n%2!=0
# a=list(filter(a,x))
# print(a)
# print(x)


# bu filter and lambda yordamida juft sonnlarni topish
# import random as r
# x=r.sample(range(20),5)
# a=list(filter(lambda y:y%2==0,x))
# print(a)
# print(x)


# # bu filter and lambda yordamida toq sonnlarni topish
# import random as r
# x=r.sample(range(20),5)
# a=list(filter(lambda y:y%2!=0,x))
# print(a)
# print(x)

# royxatdagi m bn boshlangan so`zni topish
# car_brands={'toyota','Hundai','Kia','GM','Misubishi','Rolse roys'}
# a=list(filter(lambda string:string.lower().startswith('m'),car_brands))
# print(a)

# so`zlarga chegara qoyib, saralab olsih

# car_brands={'toyota','Hundai','Kia','GM','Misubishi','Rolse roys'}
# a=list(filter(lambda string:len(string)<=6,car_brands))
# print(a)





