# Baseball_AI
For the purpose of doing group term project on S.E.
Pseudornadom:변영재, hummer91 :정지암, mobydick 전준 , antimoto: 승면형 

이 프로젝트는 각 선수의 경기 기여도를 면밀히 파악하기 위핸 세이버 메트릭스 스탯인 WPA를 자동으로 구하는 프로그램을 위해 시작하였습니다.

관심있는 사람은 누구나 피드백을 주시기 바랍니다. 

This project is about computing WR and WPA of KBO players simultaneously. Please contact to any owners if you are interested!

#0503 Requirement Specification 완료, 크롤링 위한 DB 구축 및 환경 설정 시작

#0523 Crawling이 간편한 파이썬으로 급하게 선회, 1주일간 시도 끝에 드디어 연도를 입력하면 그 날짜 전체 * 10P2(10개 팀 홈, 어웨이) * 2(더블헤더) 만큼 날짜별로 계산하여, 1월 1일 부터 12월 31일까지 전부다 탐색하는 것 까지 완성

해야하는 것들 : UI wxGlade 통해 개발중, Crawling 한 것들 Parsing을 통해 유의미한 데이터로 만들어야 함, DB 고민중, 서버 고민중


#0607 Python 2.7 에서 몽고 디비를 읽을때, 무조건 아스키로 읽는 문제 발견 다같이 자바로 넘어갈지, 3.5로 넘어갈지 고민중

#0609 Java 크롤링이 생각보다 복잡하여, 시간이 촉박해 불가능하다고 판정, 일단은 파이썬 3.5 로 크롤링하고, 자바 UI로 나타내는것으로 결정
한꺼번에 exe 하나로 못 만들더라도, 두개의 exe 로 만들도록 합의

#0610 실시간 크롤링인 셀레니움이 제대로 실행이 됬다가 안됬다가 하는 문제 발생 - > 일단 실시간 크롤링을 포기 (추후 업데이트 예정)

#0616 크롤링 과 UI 다 완성 이유는 알 수 없는 이유로 우리가 가진 노트북 3개에서는 실행이 안됨
 영재네 집에 있는 컴퓨터에서 동영상으로 찍어 발표하기로 결정
 
 #0618 계기가 된 강의는 끝났지만, 좀 더 업데이트 하고 싶은 부분이 많음. 일단 크롤링을 아예 자바로 넘기던가, 파이썬을 자바 exe 로 읽던가 둘중 하나를 고려. 두번째로 실시간 크롤링을 가능케 하는 selenium에 대해서 좀 더 탐구, 항시 가능하도록 연구. 세번째로 리콰이어먼트에 있었던 excel 관련 내용을 추가 (사회인 야구). 네번째로, wpa 뿐만 아니라 다른 세부 스탯들도 실시간으로 구하는 것에 대하여 연구. 5번째로 디비를 mongo에서 다른 db로 옮길지를 고려.(sql문을 사용하는게 아무래도 편할거 같음). 마지막으로 UI를 좀 이쁘게 하는것으로!

#0618 소감 : 이번학기 내내 이 프로젝트에 대해서 고민하고, 뭔가를 했던거 같다. 모인 네명이 너무 다 초짜라서 아마 다른팀이라면 안했을 (결과물을 보니 후덜덜했다...) 실수들과 시행착오가 많았던것 같다. 이번 프로젝트덕에 기말고사 공부를 하나도 못해서, 사실 원망스럽기도 했지만 교수님을 계속 찾아가고 피드백도 받으면서 많은걸 배우고, 또 느낀것 같다. 과목으로 다루는 프로젝트는 마지막이지만, 이제 시작인 것에 부끄럽고, 또 이제라도 시작해서 감사하다. 3학점 전공 이상의 무언가를 얻어간다.
