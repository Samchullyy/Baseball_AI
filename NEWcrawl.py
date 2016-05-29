#-*- coding:utf-8 -*-


import itertools
import requests
import urllib
import datetime
from bs4 import BeautifulSoup
import json
import codecs
import re


def test():
    url = "http://www.koreabaseball.com/Schedule/Game/BoxScore.aspx?leagueId=1&seriesId=0&gameId=20160524HHWO0&gyear=2016"
    source_url = requests.get(url)
    plain_text = source_url.text
    soup = BeautifulSoup(plain_text, )
    print soup
    get_ballpark = soup.find_all('p', {'class' : "ballpark"})#��Ʈ�� �ٲٰ� \\xao ������ ��ĭ ���ֱ�
    str_ballpark = str(get_ballpark)
    str_ballpark = str_ballpark.replace("\\xa0", "")
    str_ballpark = str_ballpark.replace(" ", "")
    print len(str_ballpark)
    print str_ballpark
    if len(str_ballpark) != 126:
        #get_player = soup.find_all('h4', {'class' : "bul h_wo"})
        get_player = soup.find_all('div', {'class' : "boxscore"})
        str_player = str(get_player)
        print str_player
        

