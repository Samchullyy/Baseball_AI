#-*- coding: utf-8 -*-

import urllib
import requests
import re
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
#for player in name:
#    tag
cnt = 0
while cnt <670:
    #if tag.next.string != " ":
        #print tag.next.string
        #tag = tag.next_sibling
    if cnt == 669:
        if tag.next.string =="\n":
            print "correct"
        else:
            print "wrong"
    tag = tag.next_sibling
    cnt = cnt+1


#print tag.next_sibling