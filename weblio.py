# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
def Research(input_word):
    meaning=""
    weblio_data = requests.get("http://ejje.weblio.jp/content/"+input_word)
    soup = BeautifulSoup(weblio_data.text,'html.parser')
    word_meanings = soup.findAll("td",class_ = 'content-explanation')
    len2 = len(word_meanings)
    for i in range(len2):
        meaning+=word_meanings[i].text
    return meaning
