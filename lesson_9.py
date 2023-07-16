# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:19:09 2023

@author: A
"""

#uests = ('Ali','Vali','Abror',"Tursun",'Kamol')
#for guest in guests:
#    #rint(guest)
#    print(guest,end=" ")

#friends= [] # bo'sh ro'yxat
#print(" who is your 5 best friends? " )
#for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#    friends.append(input(f"{n+1}-please, enter your friend`s name: "))
#for x in friends:
#    #print("hi!",x)
#    print('hi',x,end='  ')

#friends = []
#print("Who are your 5 best friends?")
#for n in range(5):
#    friends.append(input(f"{n+1} - Please enter your friend's name: "))

#first_iteration = True
#for x in friends:
#    if first_iteration:
#        print('Hi', end=' ')
#        first_iteration = False
#    print(x, end=' ')


#insonlar = []
#n = list(range(0, int(input("Bugun nechta inson bilan ko'rishtingiz:>>> "))))
#for son in n:
    #insonlar.append(input(f"{son+1}-ko'rishgan insoninggizni ismini kiriting:>>> ").capitalize())
#print("Bugun siz ko'rishgan insonlaringgiz.")
#for inson in insonlar:
    #print(inson)

#print(insonlar)
 

#while yosh != 'exit' or yosh != 'stop':
##    yosh = input("Yoshingizni kiriting:>>> ")
#    if yosh == 'exit' or yosh == 'stop':
#        break
#    elif int(yosh) <= 7:
#        print('Siz uchun bilet narxi 2000 so\'m')
#    elif 7 < int(yosh) <= 18:
#        print("Siz uchun chipta narxi 5000 so'm")
#    elif 18 < int(yosh) <= 65:
#        print("Siz uchun kirish 15000 so'm")
#    elif int(yosh) >= 65:
#        print("Sizga kirish bepul")
#print("Dastur tugadi.")


# print("Savdo dokonini yaratamiz va joy")
# bozor = {
#     "ichimliklar": {
#         'pepsi': 12000,
#         'cola': 8000,
#         'fanta': 13000,
#         'fensi': 6000,
#         'mors': 5000,
#         'kvars': 7000,
#         'sut': 6000,
#         'qatiq': 4000,
#         'suv': 3000
#     },
#     "yeguliklar": {
#         'lavash': 23000,
#         'shourma': 25000,
#         'hot-dog': 13000,
#         'burger': 21000,
#         'gam-burger': 26000,
#         'pitsa': 54000
#     },
#     "aralash": {
#         'semichka': 1000,
#         'kalbasa': 35000,
#         'tuxum': 1200,
#         'qurtop': 500,
#         'zi-zi': 4000,
#         'non': 3500
#     }
# }

# orders = []
# n = 1
# while True:
#     order = input(f"{n}-maxsulot nomini kiriting:>>> ")
#     if any(order in category for category in bozor.values()):
#         orders.append(order)
#     else:
#         print(f"We don't have '{order}' in our list. Please choose another item.")
#     prompt = input("Can I take your order? (Yes/No):>>> ")
#     n += 1
#     if prompt.lower() == 'no':
#         break
#     else:
#         print(f"Your all orders are as follows: {orders}")

# print("Your orders:", orders)

    
#     buyurtma = input(f"{n}-maxsulot nomini kiriting:>>> ")
#     for buyurtma in buyurtmalar:
#         if buyurtma in bozor:
#             buyurtmalar.append(buyurtma)
#     else:
#         print("Bizning menuda bunday taom yo`q")
#     yana = input("Yana buyurtmaga narsa qo'shasizmi. (xa/yo'q):>>> ")
#     if yana != 'xa':
#         break
# for x,y in buyurtmalar.items():
#     print(f"siz {x} {y} ga buyurtma berdingiz va sizdan umumiy {y} so'm bo'ldi" )    

#market={
#        'pepsi':12000,
#       'cola':8000,
#      'fanta':13000,
#       'fensi':6000,
#      'mors':5000,
#    'kvars':7000,
#       'sut':6000,
#       'qatiq':4000,
#        'suv':3000  }
#market=list(market)
#orders=[]
#n=1
#while True:
#    order = input(f"{n}-maxsulot nomini kiriting:>>> ")
#    for order in market:
#        if order in market:
#            orders.append(order)
#        else:
#            print("bizda bunday mahsulot yo`q, iltimos bohs mahsulot kiritng")
#    again = input("Yana buyurtmaga narsa qo'shasizmi. (xa/yo'q):>>> ")
#    n +=1
#    if again != 'xa':
#        break
#for x,y in orders.items():
#    print(f"siz {x} {y} ga buyurtma berdingiz va sizdan umumiy {y} so'm bo'ldi")
    

    






















