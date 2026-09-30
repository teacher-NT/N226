import os
os.system("cls")

# pip install wikipedia-api 
# pip3 install wikipedia-api

from wikipediaapi import Wikipedia

wiki = Wikipedia(user_agent='Dastur', language='uz')
data = wiki.page('Apple')
print(data.summary)
# print(data.text)
# print(data.images)
# print(data.links)