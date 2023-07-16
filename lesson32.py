# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:06:35 2023

@author: A
"""

class Product():
    __num_pro=0
    def __init__(self,pname,verse,made,year,cost):
        self.pname =pname
        self.verse=verse
        self.made=made
        self.cost=cost
        self.year=year
        Product.__num_pro+=1
    
    def get_info(self):
        return f"Product name:{self.pname}, kind of product : {self.verse} "\
               f"made of product: {self.made}, cost of product : {self.cost} "\
               f" production year :{self.year}"
    def __str__(self):
        return f"Product name:{self.pname}, kind of product : {self.verse} "\
               f"made of product: {self.made}, cost of product : {self.cost} "\
               f" production year :{self.year}"           
    def __repr__(self):
        return f"Product name:{self.pname}, kind of product : {self.verse} "\
               f"made of product: {self.made}, cost of product : {self.cost} "\
               f" production year :{self.year}"           


    def get_num_p(cls):
        return cls.__num_pro 
    def __eq__(self, y):
        return self.cost==y.cost
    def __le__(self,y):
        return self.cost<=y.cost
    def __lt__(self,y):
        return self.cost>y.cost



class Basket():
    
    def __init__(self,name):
        self.name=name  #  name  hususiyatini shunaqa self.name deb nomlab oldik buni self.---- boshqa nom bilan ham atash mumkin
        self.products=[]  # bu []  yani men ichi bosh ro`yhat tayorlab oldim
    def __repr__(self):  # bu __str__ bilan bir hil lekin buning afzalligimi mavjud
        return f"Name is {self.name}"
    def __len__(self): #  __len__ bu yuqorida yaratilgan products royxatini ichidagi elementlar sonini korsatadi
        return len(self.products)
    def __getitem__(self,index):#  bu index ozgarishimi mumkin ixtiyoriy boladi
        return self.products[index]
    def __setitem__(self,index,value):# bu value ham shunday bir qiymat holos uni boshqa nom bilan ham atash mumkin
        self.products[index]=value   # bu qatorda products dagi biror bir elementni biror bir qiymatga almashtiriladi
    def add_product(self,*brands): # bu method brands dagi maxsulotlarni  productsga qoshadu
         for product_name in brands: # product nomlarini brands ichidagi har bir elementlarga murojat qiladi.
             if isinstance(product_name, Product):
                 self.products.append(product_name)
             else:
                 return f" enter  another {product_name}"    
    def show_products(self):
        for product in self.products:
            print(product.get_info())         
fruits=Basket("AsiaMarket")
good1=Product('Paris-Bugatteu','cake','fruitly',2023,10000)
good2=Product('Mc Donalds','Shaikh','strawberry',2023,2800)
good3=Product('Starbacks','cafe','Lemonade',2023,1400)        
good4=Product('MOkky-Cokky','coce','chocolate',2023,2500)
fruits.add_product(good1,good2,good3,good4)# add_product method i uchun qiymatlarni kiritish kerak.
print(f"{len(fruits)}") # bunda Basket klass ichidagi itemslar miqdoriini korsatib beradi.
fruits.show_products() #  bunda products[] ichidagi items larni ko`rish uchun show_products funksiyasini chaqirish kere.


