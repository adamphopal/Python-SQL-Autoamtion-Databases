#Python Requests Beginner Tutorial - GET Requests With Translate API
#Python Requests library to you by talking about how to perform GET requests to a language translation API
#Yandex Translate API: https://tech.yandex.com/translate/
#https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages
import requests
import os



API_KEY = 'trnsl.1.1.20190818T233142Z.5abb025208133d30.42e34c612304e6eed157dfe844fe28936b8fba49'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
words = input("Enter arabic text to translate into english:" )

params = dict(key=API_KEY, text=words, lang='ar-en') #translates text from arabic to englist
r = requests.get(url, params=params)
json = r.json()
print(json['text'][0])
