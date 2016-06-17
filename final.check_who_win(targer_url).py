#-*- coding: utf-8 -*-

import urllib
import requests
import datetime
from bs4 import BeautifulSoup


def check_who_win(target_url):#경기 로그 url을 받아서, 진행합니다
    url = str(target_url) #혹시 모르니까 스트링으로 강제 형변환을 해줍니다.
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    win_tag = soup.find('div', style='position:relative; width:500px; margin:0px 0px 10px 0px; float:left;')

    check_tag = win_tag.table.td.string.next.next #처음 박스 시작하는 곳으로 이동해서 태그를 저장해줍니다.
    inn_cnt = 0 #이닝카운터(팀, H,B 등을 포함한)를 선언해서 몇 이닝까지 한경기인지 첫번째 와일뤂에서 세줍니다.
    blank_cnt = 0
    while inn_cnt<17: #최대 이닝수가 17개 입니다. 팀 + 12 + R + H + E + B
        if(check_tag.next.string =="\n"): #탐색 중간에 라인이 바뀌는 태그가 하나 있습니다. 그 놈을 강제로 넥스트 선언을 하고 카운트를 올려줍니다.
            if blank_cnt==2: #만약 익셉션 카운트 (blank_cnt)가 이미 두개라면 와일문을 탈출 합니다. (왜냐하면 마지막 탐색시에 라인 바뀌는거나 nbsp중 하나가 있습니다 (까먹음))
                 break
            blank_cnt = blank_cnt+1
            check_tag = check_tag.next
        elif(check_tag.next.string ==" "): #탐색 중간에 그냥 nbsp가 하나 있습니다. 그 놈 역시 강제로 넥스트로 선언을 하고, 위에서 선언한 카운트와 같은 카운트를 올려줍니다.
            if blank_cnt==2: #만약 익셉션 카운트 (blank_cnt)가 이미 두개라면 와일문을 탈출 합니다. (왜냐하면 마지막 탐색시에 라인 바뀌는거나 nbsp중 하나가 있습니다 (까먹음))
                break
            blank_cnt= blank_cnt+1
            check_tag = check_tag.next
        inn_cnt = inn_cnt + 1 #다 돌아가면 이닝 카운터를 세줍니다.
        check_tag = check_tag.next.string # 다음 라인으로 넘겨줍니다. 익셉션은 위에서 설명함.
        
    check_tag = check_tag.next.next
    box_cnt = 0 #이닝카운터 갯수만큼 돌아갈 박스 카운터를 선언해줍니다.
    blank_cnt = 0 #블랭크 카운터가 탈출값으로 다시 사용되기 때문에 0으로 초기화 해줍니다.
    while box_cnt < inn_cnt: #위와 굉장히 동일한 방법을 씁니다. 사실 함수로 선언할까 하다가 귀찮아서 안했습니다. (인자 값 전달이 귀찮음)
        if(check_tag.next.string =="\n"):
            if blank_cnt==2:
                break
            blank_cnt = blank_cnt+1
            check_tag = check_tag.next

        elif(check_tag.next.string ==" "):
            if blank_cnt==2:
                break
            blank_cnt= blank_cnt+1
            check_tag = check_tag.next

        if box_cnt == inn_cnt - 1: # 마지막 와일 문일 경우 실행됩니다.
            home_score = int(check_tag.next.string) # 홈 스코어라는 변수를 선언해주고 스트링값으로 받으니, 강제로 인티져로 형변환 해줍니다.
        box_cnt = box_cnt+1
        check_tag = check_tag.next.string
    
    check_tag = check_tag.next.next
    box_cnt = 0 #이닝카운터 갯수만큼 돌아갈 박스 카운터를 선언해줍니다.
    blank_cnt = 0 #블랭크 카운터가 탈출값으로 다시 사용되기 때문에 0으로 초기화 해줍니다.
    while box_cnt < inn_cnt: #위와 굉장히 동일한 방법을 씁니다. 사실 함수로 선언할까 하다가 귀찮아서 안했습니다. (인자 값 전달이 귀찮음)
        if(check_tag.next.string =="\n"):
            if blank_cnt==2:
                break
            blank_cnt = blank_cnt+1
            check_tag = check_tag.next

        elif(check_tag.next.string ==" "):
            if blank_cnt==2:
                break
            blank_cnt= blank_cnt+1
            check_tag = check_tag.next
        if box_cnt == inn_cnt - 1: # 마지막 와일 문일 경우 실행됩니다.
            away_score = int(check_tag.next.string) # 어웨이 스코어라는 변수를 선언해주고 스트링값으로 받으니, 강제로 인티져로 형변환 해줍니다.
        box_cnt = box_cnt+1
        check_tag = check_tag.next.string

    return (home_score-away_score) # 홈팀에서 어웨이 팀 점수를 뺀 인티져 값을 리턴합니다.
