# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "http://ejje.weblio.jp/content/"

weblio_data = requests.get(url)

soup = BeautifulSoup(weblio_data.text,'html.parser')

#record = soup.findAll("div",class_ = 'summaryM descriptionWrp')

main_meaning = soup.findAll("td",class_ = 'squareCircle description')

#len1 = len(main_meaning)

#for i in range(len1):

   # print(main_)


word_meaning = soup.findAll("td",class_ = 'content-explanation')

len2 = len(word_meaning)

for i in range(len2):

    print(word_meaning[i].text)


#record = soup.findAll("td", attrs={'class_' : 'content-explanation'})

#print(record)
