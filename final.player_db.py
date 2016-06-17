#-*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
from pymongo import cursor
import requests
from bs4 import BeautifulSoup

client = MongoClient()
db = client['player']

collection = db.player

def crawl_player():
    base_url = "http://www.statiz.co.kr/player.php?opt=2&sopt="
    opt = 1
    while opt < 15:
        url = base_url + str(opt)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        player_table  = soup.find('div', style='position:relative; width:50%; margin:0px 0px 10px 0px; clear:both;')
        starting_tag = tag = player_table.table.next.next_sibling.next.next_sibling.next
        while tag.next.string != "\n": #마지막 태그 그냥 \n 나올때까지 돌려
            for link in tag('a'):
                player_url = link.get('href')
            player_name = tag.next.string
            birth = tag.next.next_sibling.string
            war = tag.next.next_sibling.next_sibling.next_sibling.string
            var = {'url': player_url, 'name': player_name, 'birth': birth, 'wpa': '0', 'war': war}
            #a = collection.insert_one(var)
            #print(a)
             
            
            tag = tag.next_sibling

        opt = opt +1

crawl_player()
