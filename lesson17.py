# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 21:03:32 2023

@author: A
"""

# ism = input ("Ismingiz nima? ")
# savol= f"Salom,{ism.title()}.Yoshingiz nechida ? "
# yosh = input(savol)
# yosh=int(yosh)
# height=input("boyingiz necha metr? ")
# height=float(height)
# print("Sizning yoshingiz ",yosh,", bo`yingiz esa ",height)

# number = 1
# while number <= 10:
#     number=int(number)
#     if number%2==0:
#         print(number,end=" ")
#     else:
#         print("\n",number)
#     number+=1
# print('dastur tugadi !')

# prompt= "enter any number "
# prompt+= "(if you stop this process, please enter the word 'Exit'): "
# value = ''
# while value.lower() != 'exit':
#     value=input (prompt)
#     if value != 'exit':
#         print(float(value)**2)
# print('finish the process!')

# prompt= "enter any number "
# prompt+= "(if you stop this process, please enter the word 'Exit'): "
# Motion = True
# while Motion:
#     value=input (prompt)
#     if value.lower() == 'exit':
#         Motion=False
#     else:
#         print(float(value)**2)
# print('finish the process!')


# prompt= "enter any number "
# prompt+= "(if you stop this process, please enter the word 'Exit'): "

# while True :
#     value=input (prompt)
#     if value.lower() == 'exit':
#         break
#     else:
#         print(float(value)**2)
# print('finish the process!')

# cars = ['bmw', 'mercedes', 'audi', 'toyota']
# for car in cars:
#     if car=='toyota':
#         break
#     else:
#         print(car)        

# cars = ['bmw', 'mercedes', 'audi', 'toyota']
# for car in cars:
#     if car=='audi':
#         continue
#     else:
#         print(car)        
        
# number=0
# while number <25:
#     number +=1
#     if number == 15:
#         continue
#     else:
#         print(f"{number *2}")


# prompt= "enter your readable books "
# prompt+= "(if you stop this process, please enter the word 'stop'): "
# Motion = True
# while Motion:
#     value=input (prompt)
#     if value.lower() == 'exit':
#         Motion=False
#     else:
#         print(f"these are your loved books: {value}")
# print('finish the process!')

# prompt= "enter your age "
# prompt+= "(if you stop this process, please enter the word 'stop'): "
# age = True
# while age:
#     a=input(prompt)
#     value=int(a)
#     if value<7:
#         print("entrance fee -2000")
#     elif 7<=value<=18 :
#         print('entrance fee -3000')
#     elif 18<value<=65 :
#         print('entrance fee -10000')
#     elif value>65:
#         print("entrance fee is free")
#     elif a.lower() == 'exit':
#             age=False
#     else:
#             print(f"these are your loved books: {value}")

# print('finish the process!')



# prompt = "Enter your age (if you want to stop this process, please enter the word 'stop'): "

# while True:
#     age = input(prompt)
    
#     if age.lower() == 'stop':
#         break
    
#     try:
#         value = int(age)
        
#         if value < 7:
#             print("Entrance fee: 2000")
#         elif 7 <= value <= 18:
#             print("Entrance fee: 3000")
#         elif 18 < value <= 65:
#             print("Entrance fee: 10000")
#         else :
#             print("Entrance fee is free")
        
#     except ValueError:
#         print("Invalid input! Please enter a valid age or 'stop' to exit.")

# print("Finish the process!")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.lower()=='exit':
#         print("dasturni to`xtatish uchun 'exit' deb yozganligingiz uchun, dastur jarayoni yakunlandi!")
#         break
            
#     try:
#         qiymat=float(qiymat)
        
#         if qiymat<0:
#             print('Iltimos,manfiy son kiritmangiz!')
#             continue
#         else:
#             ildiz = float(qiymat)**(0.5)
#             print(f"{qiymat} ning ildizi {ildiz} ga teng")
#     except ValueError:
#         print("Noto`gri formatda son kiritingiz. Iltimos, musbat son kiriting yoki dasturni to`xtatish uchun 'exit' deb yozing")

# print("Making the best friends` list")
# names=[]
# n=1
# while True:
#     prompt=f"{n}-Please,enter your one of the best friedds- "
#     name=input(prompt)
#     names.append(name)
#     again=input('add your friend`s name? (yes/no) >>>' )
#     n+=1
#     if again!= 'yes':
#         break
# print('your best friends: ')
# for name in names:
#    print(name.title() ,end=' ')

# print('keep saving information of your friends ')
# friends={}
# a=True
# while a :
#     name = input ('Please, enter your friend`s name -')
#     age= input ('Please, enter your friend`s age  -')
#     friends[name]=int(age)
#     prompt=input('do you want to add your friend`s data? (yes/no)>>>')
#     if prompt!='yes':
#         a=False
# print('your best friends information:')
# for name,age in friends.items() :
#     print(f"{name.title()} is {age},",end=' ')        


# t_shirts=['NIKE','ADIDAS','PUMA','PAVON']
# costed_tshirt={}
# while t_shirts:
#     brand=t_shirts.pop()
#     cost = input(f"please, enter {brand}`s price >>> ")
#     costed_tshirt[brand]=int(cost)
# print(costed_tshirt)
    
# print("acceptance orders: ")
# orders=[]
# n=1
# while True :
#     order=input(f"{n}- enter the first your order: ")
#     orders.append(order)
#     prompt=input("do you  give an order again? (yes/no) ")
#     n+=1
#     if prompt!='yes':
#         break
#     else:
#         continue
# print('list of orders')
# for order in orders :
#     print(order.title(), end=', ')


# print('keep saving information  ')
# e_bazar={}
# a=True
# while a :
#     k = input ('Please, enter your order`s name -')
#     v= input ('Please, enter your order`s cost  -')
#     e_bazar[k]=int(v)
#     prompt=input('do you want to add your another order? (y/n)>>>')
#     if prompt!='y':
#         a=False
# print('your lis of order:')
# for k,v in e_bazar.items() :
#     print(f"{k.title()} is {v},",end=' ') 
    
#    
    
    
                     


    
    
    
    
    

    
    

        
    







