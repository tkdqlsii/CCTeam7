import requests
import new
import pymysql

from bs4 import BeautifulSoup
#pw='당신의 비밀번호를 입력해주세요'
pw='root'
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

title_arr=[]
artist_arr=[]
img_arr=[]

# sep은 분리할 단어 replace로 모든 feat에 해당되는  대소문자 구분없이 feat라는 단어로 변경 후 분리
for link1 in bugs_parse.find_all(name="p",attrs={"class":"title"}):
    sep = "feat"
    tmp = link1.find('a').text.replace('(Feat',sep).replace('(feat',sep).replace('Feat',sep).split(sep)[0]
    title_arr.append(tmp)

for link1 in bugs_parse.find_all(name="p",attrs={"class":"artist"}):
    artist_arr.append(link1.find('a').text)

#이미지를 크롤링 해오는 파트
for link1 in bugs_parse.find_all(name="a",attrs={"class":"thumbnail"}):
    img_arr.append(link1.find('img').get("src"))


#출력부분 주석처리
"""for s in range(100):
    print(str(s)+"위")
    print("제목: " + title_arr[s] + "/ 가수 :"+artist_arr[s])"""

sql="""INSERT INTO bugs (title, artist, score, img) VALUES (%s, %s, %s, %s)"""

for r in range(100):
    rc=r+1
    curs.execute(sql,(title_arr[r],artist_arr[r], rc, img_arr[r]) )

conn.commit()
conn.close()
