#-*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

url = "http://www.statiz.co.kr/boxscore.php?date=2016-05-31&stadium=%EA%B3%A0%EC%B2%99%EB%8F%94&hour=18&opt=5"
soup = BeautifulSoup(urllib.urlopen(url).read(), 'lxml')
state = soup.find('div', style='position:relative; width:100%; margin:0px 0px 10px 0px; clear:both;')
tag = state.next.next_sibling#테이블 긁음
tag1 = tag.next#빈칸
tag2 = tag1.next_sibling
#<tr><td class="tablehead_stz" colspan="30"><b>경기로그</b></td></tr>
tag3 = tag2.next_sibling.next
#<tr class="colhead_stz">
#<td>이닝</td>
#<td>투수</td>
#<td>타자</td>
#<td>P</td>
#<td width="200">결과</td>
#<td>이전상황</td><td>이후상황</td><td>LEV</td><td>REs</td><td>REa</td><td>WPe</td><td>WPa</td></tr>
tag4 = tag3.next_sibling.next
#<tr class="oddrow_stz"><td><b>1초</b></td><td><a href="player.php?name=%ED%94%BC%EC%96%B4%EB%B0%B4%EB%93%9C&amp;birth=1985-08-22">피어밴드</a></td>\
#<td>1 <a href="player.php?name=%EB%B0%B0%EC%98%81%EC%84%AD&amp;birth=1986-06-27">배영섭</a></td><td>2(1-0)</td>
#<td style="text-align:left"><span onclick='setPopup("popup/playlog.php?date=2016-05-31&amp;stadium=%EA%B3%A0%EC%B2%99%EB%8F%94&amp;hour=18&amp;res=42&amp;flag=1", this);
#' style="cursor:pointer">중견수 안타</span></td>
#<td style="font-size:8pt;">무사  0:0</td>
#<td style="font-size:8pt;">무사 1루 0:0</td><td><font color="black">0.87</font></td><td>0.555</td><td>0.398</td><td>46.5%</td><td>0.036</td></tr>
tag5 = tag4.next_sibling
#<tr class="oddrow_stz"><td></td>
#<td><a href="player.php?name=%ED%94%BC%EC%96%B4%EB%B0%B4%EB%93%9C&amp;birth=1985-08-22">피어밴드</a></td>
#<td>2 <a href="player.php?name=%EB%B0%95%ED%95%B4%EB%AF%BC&amp;birth=1990-02-24">박해민</a></td>
#<td>3(1-1)</td><td style="text-align:left"><span onclick='setPopup("popup/playlog.php?date=2016-05-31&amp;stadium=%EA%B3%A0%EC%B2%99%EB%8F%94&amp;hour=18&amp;res=48&amp;flag=1", this);
#' style="cursor:pointer">1루수 희생번트</span></td><td style="font-size:8pt;">무사 1루 0:0</td>
#<td style="font-size:8pt;">1사 2루 0:0</td><td><font color="black">1.44</font></td>
#<td>0.953</td><td>-0.228</td><td>48.2%</td><td>-0.018</td></tr>
tag6 = tag5.next_sibling

print tag4.prettify()