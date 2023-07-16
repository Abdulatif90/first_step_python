# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:52:57 2023

@author: A
"""

# import json   # Json module ishlash uchun albatta birinchi import qilib olish kere
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000} # modullarda key va value qismlari mavjud boladi. ba {} qavs ichida yoziladi
# ##() qavs esa tulip yani ozgarmas royhat yaratish uchn ishlatiladi, [] bu esa o`zgaruvchan ro`yxat uchunb bu ikkovi ham lugat yaratishda ishlatilishi mumkin.
# """ buni Jsonga otkazish kerak"""
# data_json=json.dumps(data) # data dict json ga `otdi.
# # data_json=json.dumps(data,indent=5) # bu chap tomondan nechi qator tashlashlik uchun yoziladi
# # print(data_json)



# import json
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# """ buni Jsonga otkazish kerak va saqlash kerak"""

# with open('data.json','w') as file:
#     json.dump(data,file) # bu data dict. json ga dump methodi orqali yuklab data.json degan fayl yaratdik

# ### Jsondan Pythonga malumotlarni otkazishda .loads dan foydalanmiladi. lekin bir butun faylni esa Load bn bajariladi
# """ bu malumotni jsondan pythonga"""
# data=json.loads(data_json)  # yuqorida yarailga data_jsonnni pythonga otkazdik
# print(data)
  

# """ endi bunda fayli jsondan pythonga"""
# ### 1- usul file nomini togridan togri open buyrugiga berish
# with open ('data.json') as file:
#     data = json.load(file)
# print(data)
#a=data.json
# with open (a) as file:
#     data = json.load(file)
# print(data)


# import json

# # Read data from JSON file
# with open('students.json', 'r') as json_file:
#     data = json.load(json_file)
    
# # Access and print student information
# students = data['student']
# n=1
# for student in students:
#     student_info = f"{n}. ID: {student['id']}, Name: {student['name']}, Lastname: {student['lastname']}, Year: {student['year']}, Faculty: {student['faculty']}"
#     n+=1
#     print(student_info)


# import json

# with open('api-result.json','r') as file:
#     result = json.load(file)
    
# # print(result)


#     info= f"title of topics is {'title'}, and its extracts are {'extract'}"
# print(info)

    # import requests
    # import json
    
    # # URL ni o'rnating
    # url = "https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python"
    
    # # Maqolani olish uchun so'rovni amalga oshiring
    # response = requests.get(url)
    
    # # JSON ma'lumotni o'qiydigan o'zgaruvchiga saqlang
    # data = response.json()
    
    # # Maqola sarlavhasini va qisqa matnini olish
    # pages = data['query']['pages']
    # # for page_id in pages:
    # #     title = pages[page_id]['title']
    # #     extract = pages[page_id]['extract']
    # title=pages['13801']['title']
    # extract =pages['13801']['extract']
    #     # Sarlavha va qisqa matnni konsolga chiqaring
    # print(f"Sarlavha: {title}")
    # print(f"Qisqa matn: {extract}")
    