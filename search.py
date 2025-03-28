import streamlit as st
import os
import json
import webbrowser as wb

#Вместо кнопок ссылки
from PIL import Image

icon = Image.open("1296 logo2.png")
banner=Image.open("spravka1296banner.png")

PAGE_CONFIG = {"page_title":"Проект (Справка (The Sprawkah project))", 
               "page_icon":icon, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.image(banner)
#os.chdir(r"C:\Users\asm\Desktop\То да сё\! НеОбязан")  #папка с проектом

with open(r"json/alltags.json",'r') as fl:
    alltags=json.load(fl)["tags"]



namesrch=st.text_input("Поиск по имени",placeholder="Пусто")  
tagsrch=st.multiselect("Поиск по меткам",alltags,placeholder="Пусто")


for i in os.listdir("json"):
   with open(fr"json/{i}","r") as fl:
       current=json.load(fl)
       if (namesrch.lower() in current["name"].lower() or namesrch=='') and (set(tagsrch) <= set(current["tags"]) or tagsrch==[]) and (current["name"]!="alltags"):
           #st.write(current["name"])
            if current["origurl"]=='':
               st.write(current["name"])
            elif current["origurl"][0:2]=="C:":             #место, где хранятся файлы на компе
                #ФАЙЛЫ С КОМПА И КНОПКИ ОТКЛЮЧЕНЫ
#                if st.button(current["name"],help="Этот документ хранится локально, а не на сайте школы",icon="💾"):
#                    wb.open_new_tab(current["origurl"])
#            elif st.button(current["name"]):
#               wb.open_new_tab(current["origurl"])
               continue
            else:
                st.markdown( f'[{current["name"]}](%s)'% current["origurl"])

                
                
                
                                
                
