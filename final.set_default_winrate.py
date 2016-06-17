#-*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
from pymongo import cursor
import urllib
import requests
import datetime
from bs4 import BeautifulSoup

client = MongoClient()
db = client['winrate']

collection = db.winrate

def set_default_winrate():
    inning = 1
    top_down = 1
    out_count = 0
    base = 0
    score_diff = -10

    while inning < 13:
        while top_down < 2:
            while out_count < 3:
                while base < 8:
                    while score_diff <11:
                        if top_down==1:
                            temp_top_down="초"
                        else :
                            temp_top_down="말"
                        total_inning = str(inning) + temp_top_down
                        empty_db = {
                        'state':total_inning + "-" + str(out_count) + "-" + str(base) + "-" + str(score_diff)
                        'win':'0',
                        'lose':'0'
                        }
                        a = collection.insert_one(empty_db)
                        print(a)
                        score_diff = score_diff+1
                    score_diff = -10
                    base= base +1
                base = 0
                out_count = out_count +1
            out_count = 0
            top_down = top_down +1
        top_down = 1
        inning = inning +1

set_default_winrate()
