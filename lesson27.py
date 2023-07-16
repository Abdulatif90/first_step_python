# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 00:49:52 2023

@author: A
"""

# text='I like an apple because an apple is very delicious'
# new_text=text.replace('apple',' banana') # .replace bu funksiya avvalgi qiymatni yangi qiymatga almashtiradi. 1- eski qiymat, 2 - yangi qiymat
# print(new_text)



# text='Hello'
# result=text.isupper() # .isupper function so`zni barcah harflarini katta harfda yozilganligini tekshiradi. 
##agar hamma harfi katta harfda yozilgan bo`lsa, natija True bo`ladi. agar aralash yoki kichik harf bolsa False boladi
# print(result)


# a="ABDULATIF"
# b=a.isupper()
# print(b)  # natija true chiqdi

#.sub() funksiyasi bu alohida formalarda ishledi. nu doim re modulini chaqiradi.
# text = "I like apple. Apples are delicious."
# new_text = text.replace("apple", "orange", 1)  bu faqat 1 chi apple ni ornini almasihtiirish uchun
# print(new_text)

# import re

# new_text = re.sub(r'\bapple\b', 'orange', text, count=1)#r'\bapple\b'bu shu 1 chi apple so`zini ajratib olish uchun ishlatiladi.
# text = "I like apple. Apples are delicious."
# print(new_text)


# from transliterate import to_cyrillic,to_latin

# print(to_cyrillic('Abdulatif'))

 # from transliterate import to_cyrillic,to_latin



#transliterate D-Д foydalanuvchi nommi
#latcyrnew_bot

# from transliterate import to_cyrillic, to_latin
# import telebot

# TOKEN ='6319601980:AAFvFdM4YKo8oMWdkPHi-C1BKXpba_p0obY'
# bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     prompt= "Welcome, How are you!!!"
#     prompt+="\n input a text: "
#     bot.reply_to(message, prompt)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     ans=message.text
#     prompt= lambda ans: to_cyrillic(ans).title() if ans.isascii() else to_latin(ans).title()
#     # if ans.isascii():
#     #     prompt=to_cyrillic(ans)
#     # else:
#     #     prompt=to_latin(ans)
#     bot.reply_to(message, prompt(ans))
 
# bot.polling()


 
# text=input('enter a text: ')
# if text.isascii(): # isascii - bu sozlarni harflarini lotin tilida yani komp ning tilida tekshiradi.isascii bu komp. dagi lotin harf alifbosi
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))

# from bs4 import BeautifulSoup
# import requests

# # Make a request to a webpage
# response = requests.get('https://www.example.com')

# # Create a BeautifulSoup object to parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Select a specific HTML element
# element = soup.find('h1')

# # Extract the textual content using the .text attribute
# text_content = element.text

# print(text_content)
























