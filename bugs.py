import requests
import new
import pymysql

from bs4 import BeautifulSoup

pw='당신의 db의 비밀번호를 넣어주세요'
new.dbcheck()  #테이블이 있는지 확인하는 모듈의 함수
conn = pymysql.connect(host='localhost', user='root', password=pw,
                       db='testdb', charset='utf8')
curs=conn.cursor()


sql="truncate table bugs"#데이터베이스 초기화 시킨다.
curs.execute(sql)

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
bugs = requests.get('https://music.bugs.co.kr/chart/track/realtime/total', headers = header) # 벅스 실시간 차트 웹사이트
bugs_html = bugs.text
bugs_parse= BeautifulSoup(bugs_html, 'html.parser')

'cnt_artist=0'
title_arr=[]
artist_arr=[]

for link1 in bugs_parse.find_all(name="p",attrs={"class":"title"}):
    'cnt_artist+=1'
    title_arr.append(link1.find('a').text)

'cnt_artist=0'
for link1 in bugs_parse.find_all(name="p",attrs={"class":"artist"}):
    'cnt_artist+=1'
    artist_arr.append(link1.find('a').text)
'cnt_artist=0'

for s in range(100):
    print(str(s)+"위")
    print("제목: " + title_arr[s] + "/ 가수 :"+artist_arr[s])

sql="""
INSERT INTO bugs (title, artist, score)
VALUES (%s, %s, %s)
"""
for r in range(100):
    rc=r+1
    curs.execute(sql,(title_arr[r],artist_arr[r], rc) )



conn.commit()
conn.close()



