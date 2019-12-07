import requests
import pymysql
import new #table이 있는지 확인하는 모듈
from bs4 import BeautifulSoup

pw='gusgh4528'
new.dbcheck()  #테이블이 있는지 확인하는 모듈의 함수
conn = pymysql.connect(host='localhost', user='root', password=pw,
                       db='testdb', charset='utf8')
curs=conn.cursor()

sql="truncate table genie"#데이터베이스 초기화 시킨다.
curs.execute(sql)

temp_gtlist = []
temp_galist = []
temp_gilist=[]
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200'
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    sep = 'feat'
    title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
    artist = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
    img_url="http:"+song.find('img').get("src")
    tmp = title.replace('(feat',sep).replace('(Feat',sep).replace('Feat',sep).split(sep)[0]
    temp_gtlist.append(tmp.strip())
    temp_galist.append(artist)
    temp_gilist.append(img_url)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&pg=2'
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    sep = 'feat'
    title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
    artist = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
    img_url="http:"+song.find('img').get("src")
    tmp = title.replace('(feat',sep).replace('(Feat',sep).replace('Feat',sep).split(sep)[0]
    temp_gtlist.append(tmp.strip())
    temp_galist.append(artist)
    temp_gilist.append(img_url)

sql="""INSERT INTO genie (title, artist, score,img) VALUES (%s, %s, %s,%s)"""
for r in range(100):
    rc=r+1
    curs.execute(sql,(temp_gtlist[r],temp_galist[r], rc,temp_gilist[r]) )

conn.commit()
conn.close()

