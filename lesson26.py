# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:46:49 2023

@author: A
"""

# import random
# from uzwords import uz_words

# def get_word():
#     word = random.choice(uz_words)
#     while "-" in word or ' ' in word:
#         word = random.choice(uz_words)    
#     return word.upper()

# def display(user_letters,word):
#     display_letter=""
#     for letter in word:
#         if letter in user_letters:
#             display_letter += letter
#         else:
#             display_letter += "-"
#     return display_letter

# def play():
#     word = get_word()
#     # So'zdagi harflar
#     word_letters = set(word)
#     # Foydalanuvchi kiritgan harflar
#     user_letters = ''
#     print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
#     # print(word)
#     while word_letters:
#         print(display(user_letters,word))
#         if user_letters:
#             print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
        
#         letter = input("Ҳарф киритинг: ").upper()
#         if letter in user_letters:
#             print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
#             continue        
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} ҳарфи тўғри.")
#         else:
#             print("Бундай ҳарф йўқ.")
#         user_letters += letter
#     print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")

# play()

# random.choice()
# get_word()
# display()
# set()

# import random
# from uzwords import uz_words

# def get_word():
#     word = random.choice(uz_words)
#     while "-" in word or ' ' in word:
#         word = random.choice(uz_words)    
#     return word.upper()
# def display(user_letters, word):
#     display_letter = ""
#     for letter in word:
#         if letter in user_letters:
#             display_letter += letter
#         else:
#             display_letter += "-"
#     return display_letter

# def play():
#     word = get_word()
#     word_letters = set(word)
#     user_letters = ''
#     print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    
#     while word_letters:
#         print(display(user_letters, word))
#         if user_letters:
#             print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
        
#         letter = input("Ҳарф киритинг: ").upper()
#         if letter in user_letters:
#             print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
#             continue        
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} ҳарфи тўғри.")
#         else:
#             print("Бундай ҳарф йўқ.")
#         user_letters += letter
    
#     print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")

# play()

# word= 'Abdulatif'
# a=set(word.upper())

# import random
# car_brands=['toyota','Hyundai','Kia','GM','Mitsubishi','Rollse roys']
# def car():
#     a= random.choice(car_brands)
#     while "-" in a or ' ' in a:
#         a = random.choice(car_brands)    
#     return a.upper()


# def display(uletters,a):
#     fletter=""
#     for let in a.lower():
#         if let in uletters:
#             fletter += let
#         else:
#             fletter += "-"
#     return fletter





























