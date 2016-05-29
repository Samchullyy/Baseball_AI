#-*- coding:utf-8 -*- 
 
import itertools 
import requests 
import urllib 
import datetime 
import bs4
import wx
from bs4 import BeautifulSoup 


def pastSpider(gyear) : 
    inputdays = datetime.date(gyear, 1, 1) 
    gamepermu = list(itertools.permutations(["WO", "LG", "SS", "SK", "HT", "HH", "LT", "NC", "KT", "DO"],2)) 
    home ="" 
    away ="" 
    double_header = 0 
    cnt = 0 
    baseUrl = "http://www.koreabaseball.com/Schedule/Game/BoxScore.aspx?leagueId=1&seriesId=0&gameId=" 
    while inputdays < datetime.date(gyear+1, 1, 1): 
        gamedays = str(inputdays) 
        month = gamedays[5:6] 
        day = gamedays[8:9] 
        while cnt<90: 
            home=gamepermu[cnt][0] 
            away=gamepermu[cnt][1] 
            while double_header < 2: 
                url = baseUrl + str(gyear) + str(month) + str(day) + str(home) + str(away) + str(double_header) +"&gyear=" +str(gyear) 
                source_code = requests.get(url) 
                plain_text = source_code.text 
                soup = BeautifulSoup(plain_text, ) 
                for link in soup: 
                    KBOUrl = "http://www.koreabaseball.com/Schedule/Game/BoxScore.aspx?leagueId=1&seriesId=0&gameId=20160522WOLG0&gyear=2016" 
                    soup = BeautifulSoup(urllib.urlopen(KBOUrl).read()) 
                    print soup 
        inputdays = inputdays + datetime.timedelta(days = 1) 


