#-*- coding: utf-8 -*-

import urllib
import requests
from bs4 import BeautifulSoup

url = "http://www.statiz.co.kr/boxscore.php?date=2016-05-31&stadium=%EA%B3%A0%EC%B2%99%EB%8F%94&hour=18&opt=5"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'html.parser')
state = soup.find('div', style='position:relative; width:100%; margin:0px 0px 10px 0px; clear:both;')

starting_tag = state.next.next_sibling.next.next_sibling.next_sibling.next
tag = startinf_tag
state = ""
while tag_now=="":
    if tag_now.td.string != "":
        state = tag_now.td.string#이닝이 한줄에 한번만 나와서 업뎃 될 경우만 바꿈
    top_down = state[1]
    tag_pitcher = tag_now.next.next_sibling
    for link in tag_pitcher.find('a'):
        pitcher_id = link.get('href')
    tag_hitter = tag_pitcher.next_sibling
    for link in tag_hitter.find('a'):
        hitter_id = link.get('href')
    if pitcher_id =="":
        #교체
        break
    action = tag_hitter.next_sibling.next_sibling.string
    before_state_tag = action.next.string
    before_state = str(state).append(str(before_state_tag))
    after_state_tag = before_state_tag.next.string
    after_state = str(state).append(str(after_state_tag))
    winrate_diff = #두개 긁어서 차이 만듬
    if state[1]=="초" :
        if winrate_diff > 0:
            #타자wpa 불러서 거기다가 winrate_diff만큼 더하기
            #투수wpa 불러서 - 하기
        else:
            #투수wpa 불러서 거기다가 winrate_diff만큼 더하기
            #타자wpa 불러서 - 하기
    else :
        if winrate_diff < 0:
            #타자wpa 불러서 거기다가 winrate_diff만큼 더하기
            #투수wpa 불러서 - 하기
        else:
            #투수wpa 불러서 거기다가 winrate_diff만큼 더하기
            #타자wpa 불러서 - 하기
        
    tag_now = tage_now.next_sibling
