#-*- coding: utf-8 -*-

import urllib
import requests
import re
import json
from bs4 import BeautifulSoup

url = "http://www.statiz.co.kr/player.php?opt=2&sopt=1"
soup = BeautifulSoup(urllib.urlopen(url).read(), 'lxml')
name = soup.find('div', style='position:relative; width:50%; margin:0px 0px 10px 0px; clear:both;')
starting_tag = first_name = name.table.next.next.string.next.next.next_sibling.next
next_tag = starting_tag.next_sibling
last_tag = next_tag.next_sibling
first_name = name.table.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.string
first_birth = first_name.next.string
first_name1 = name.table.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next_sibling.next_sibling.a.string.next
tag = starting_tag
data = []
cnt = 0
#print tag.next.string#이름
#print tag.next.next_sibling.string#생년월일
#print tag.next.next_sibling.next_sibling.next_sibling.string#war
while tag.next.string != "\n":
    filename = "player" + str(cnt+1)
    with open(filename) as f:
        data.append({
            "name": tag.next.string,
            "birthday": tag.next.next_sibling.string,
            "wpa": "0",
            "war": tag.next.next_sibling.next_sibling.next_sibling.string
        })
    print data
    tag = tag.next_sibling
    cnt = cnt + 1

    