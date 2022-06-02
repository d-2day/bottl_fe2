import requests
from bs4 import BeautifulSoup
html=requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
soup=BeautifulSoup(html.text,'html.parser')
divs=soup.find('table',{'class':'list_ranking'})
rankLst=divs.findAll('div')
import time
now=time.localtime()
print("인기영화 베스트 10 ({}년 {}월 {}일)\n".format(now.tm_year,now.tm_mon,now.tm_mday))
for i in range(10):
    title=rankLst[i].find('a')
    print("rank{:2d}:{}".format(i+1,title.text))
