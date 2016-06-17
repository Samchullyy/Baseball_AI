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

def set_default_winrate(): # 윈레이트를 더할 엠티 디
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
                        'state':total_inning + "-" + str(out_count) + "-" + str(base) + "-" + str(score_diff),
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
    

def get_base(string):
    test = test.replace("무", "0") #무사 싫거든요 빼액! 0사 할거 거든요!
    out_counts = test[0:2]#무사, 1사, 2사 그래서 얘는 무조건 두개임

    colon_index = string.index(":")
    nbsp_index = string.index(" ")
    away_score = int(test[colon_index+1:len(test)+1])
    if string.count(" ")==2:
        base_index = string.index("루")
        base_str = stinrg[nbsp_index+1:base_index+1]
        if string == '1루':
            return 1
        elif string == '2루':
            return 2
        elif string == '3루':
            return 3
        elif string == '1,2루':
            return 4
        elif string == '1,3루':
            return 5
        elif string == '2,3루':
            return 6
        elif string == '만루':
            return 7
        else:
            return "뭔가 잘못 되었어!!"


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

        if box_cnt == inn_cnt - 4: # 마지막 와일 문일 경우 실행됩니다.
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
        if box_cnt == inn_cnt - 4: # 마지막 와일 문일 경우 실행됩니다.
            away_score = int(check_tag.next.string) # 어웨이 스코어라는 변수를 선언해주고 스트링값으로 받으니, 강제로 인티져로 형변환 해줍니다.
        box_cnt = box_cnt+1
        check_tag = check_tag.next.string

    return (home_score-away_score) # 홈팀에서 어웨이 팀 점수를 뺀 인티져 값을 리턴합니다.

def winrate_crawl(sy):
    base_url ="http://www.statiz.co.kr/boxscore.php?sy=" +str(sy)#sy에 있는 년도에 있는 시작일과 마지막일을 구하는 코드
    source_code = requests.get(base_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    trash_tag = soup.find('div', id='minimenu_list1')
    
    start = str(trash_tag.next_sibling.next.next.next.next_sibling.next.next_sibling.next.next.next.next_sibling.next)#start에 시작일에 박혀있는 href코드의 달과 날짜를 슬라이스로 반환하기 위해 스트링화
    end = str(trash_tag.next_sibling.next.next.next.next_sibling.next.next_sibling.next.next.next.next_sibling.next.next_sibling.next)#end에 마지막일에 박혀있는 href코드의 달과 날짜를 슬라이스로 반환하기 위해 스트링화
    end_day = datetime.date(sy, int(end[37:39]), int(end[47:49]))
    cnt = start = datetime.date(sy, int(start[37:39]), int(start[47:49]))#시작일 선언 cnt는 계속 변하는 수고 혹시 시작일이 필요 할 수 있으므로 start를 같이 선언해준다

    while cnt < end_day + datetime.timedelta(days = 1):#마지막날에서 1일을 더 더한 수 까지
        this_day = str(cnt)
        month = this_day[5:7] #이번 날짜의 달
        day = this_day[8:10] #이번 날짜의 일
        url = base_url + "&sm=" + str(month) + "&sd=" + str(day) #나중에 달과 일을 또 안쓰면 그냥 직접 넣는걸로 코드를 바꾸자
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        tag = soup.find('div', style='position:relative; width:465px; margin:0px 0px 10px 0px; float:left;')
        if tag == "None": #아예 경기가 없는 날은 지나 가자
            cnt = cnt + datetime.timedelta(days = 1)
            break # 이렇게 넘긴다.
        box_cnt = 0 
        opt_cnt = 1
        num_state = ""
        while tag.next_sibling.next.next.next.next.next.next.next.string != "일일 Best 5 (by WPa)": #마지막 박스는 항상 이놈이 온다. 그래서 이놈을 탈출 문으로 선언
            get_href = tag.next.next.next.next.next_sibling.next.next.next.next.next_sibling.next.next.next.next_sibling.next.next_sibling.next.next_sibling.next
            for link in get_href.find_all('a'):
                match = "http://www.statiz.co.kr/" + str(link.get('href')) #뒤에 오는 애가 /boxscore~~~ 로 시작해서 앞에 스탯티즈를 붙여준다.

                match_win = check_who_win(match) #check who win 메소드를 통해서 누가 이겼는지 가져온다 !

                if match_win == 0:
                    break#비긴건 볼필요 없당!
                
                match_source = requests.get(match)
                match_plain = match_source.text
                match_soup = BeautifulSoup(match_plain, 'html.parser')
                tag = match_soup.find('div', style='position:relative; width:100%; margin:0px 0px 10px 0px; clear:both;') #경기로그가 실제로 시작하는 곳을 지정해준다.
                while (tag.next.string !="\n"):
                    if tag.td.string != "":
                        state = tag.td.string #스테이트에 현재 스트링이 들어가 있음
                    state_num = state[0]
                    top_down = state[1]
                    tag_pitcher = tag.next.next_sibling
                    for link in tag_pitcher.find_all('a'):
                        pitcher_id = link.get('href')
                    if pitcher_id =="":
                        #교체
                        break
                    tag_hitter = tag_pitcher.next_sibling #사실 얘랑 얘 아래애는 필요 없는데 계산 귀찮아서 wpa 크롤에서 그대로 가져다 씁니다.
                    action = tag_hitter.next_sibling.next_sibling.string # 바로 위 주석 보세용
                    
                    before_state_tag = action.next.string
                    before_state = str(before_state_tag)
                    after_state_tag = before_state_tag.next.string
                    after_state = str(state).append(str(after_state_tag))

                    before_state = before_state.replace("무", "0") #무사 싫거든요 빼액! 0사 할거 거든요!
                    out_counts = before_state[0:2]#무사, 1사, 2사 그래서 얘는 무조건 두개임

                    colon_index = string.index(":")
                    nbsp_index = string.index(" ")
                    away_score = int(test[colon_index+1:len(test)+1])
                    total_inning = str(state_num) + top_down
                    if string.count(" ")==2:
                        base_index = string.index("루")
                        base_str = stinrg[nbsp_index+1:base_index+1]
                        base = get_base(base_str) #숫자로 바꾸어 주어요

                        home_score = int(string[base_index+2:colon_index])
                        score_diff = home_score-away_score
                        state_total = total_inning + "-" + str(out_counts) + "-" + str(base) + "-" + str(score_diff)
                        if match_win>0: #이기면 걍 다 이긴걸로 넣어요
                            db.winrate.update({state: state_total}, {inc : {win : 1}}, {upsert : True})
                        else:#지면 다 진걸로 넣어요
                            db.winrate.update({state: state_total}, {inc : {lose : 1}}, {upsert : True})

                    else:#루가 안들어가는거 도 정리 해줏메
                        home_score = int(test[nbsp_index+1:colon_index])
                        score_diff = home_score-away_score
                        state = total_inning + "-" + str(out_counts) + "-0-" + str(score_diff)
                        if match_win>0:
                            db.winrate.update({state: state_total}, {inc : {win : 1}}, {upsert : True})
                        else:
                            db.winrate.update({state: state_total}, {inc : {lose : 1}}, {upsert : True})
                            
                            



winrate_crawl(2015)

