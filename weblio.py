# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib

print('input word')

input_word = input()

url = "http://ejje.weblio.jp/content/"+input_word

weblio_data = requests.get(url)

soup = BeautifulSoup(weblio_data.text,'html.parser')

word_meaning = soup.findAll("td",class_ = 'content-explanation')

len2 = len(word_meaning)

for i in range(len2):

    print(word_meaning[i].text)
