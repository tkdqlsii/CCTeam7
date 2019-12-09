import pymysql
import requests


from bs4 import BeautifulSoup
def melon1():
    pw='gusgh4528'
     #테이블이 있는지 확인하는 모듈의 함수

    conn = pymysql.connect(host='localhost', user='root', password=pw,
                           db='testdb', charset='utf8')
    curs=conn.cursor()

    sql="truncate table melon"#데이터베이스 초기화 시킨다.
    curs.execute(sql)

    temp_tlist = []
    temp_alist = []
    temp_ilist=[]

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    melon = requests.get('https://www.melon.com/chart/index.htm', headers = header) # 멜론차트 웹사이트
    melon_html = melon.text
    melon_parse= BeautifulSoup(melon_html, 'html.parser')

    title = melon_parse.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
    artist = melon_parse.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span > a:nth-child(1)')
    img=melon_parse.select('#lst50 > td:nth-child(4) > div > a > img')
    for r in range(50):
        sep = 'feat'
        tmp = title[r].text.replace('(Feat',sep).replace('feat',sep).replace('Feat',sep).replace('(feat',sep).split(sep)[0]
        img_src=img[r].get("src")
        temp_tlist.append(tmp)
        temp_alist.append(artist[r].text)
        temp_ilist.append(img_src)

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    melon = requests.get('https://www.melon.com/chart/index.htm#params%5Bidx%5D=51', headers = header) # 멜론차트 웹사이트
    melon_html = melon.text
    melon_parse= BeautifulSoup(melon_html, 'html.parser')
    title = melon_parse.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
    artist = melon_parse.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span > a:nth-child(1)')
    img=melon_parse.select('#lst100 > td:nth-child(4) > div > a > img')
    for r1 in range(50):
        sep = 'feat'
        tmp = title[r1].text.replace('(Feat',sep).replace('feat',sep).replace('Feat',sep).replace('(feat',sep).split(sep)[0]
        img_src=img[r].get("src")
        temp_tlist.append(tmp)
        temp_alist.append(artist[r1].text)
        temp_ilist.append(img_src)

    sql="""INSERT INTO melon (title, artist, score,img) VALUES (%s, %s, %s ,%s)"""

    for r in range(100):
        rc=r+1
        curs.execute(sql,(temp_tlist[r],temp_alist[r], rc,temp_ilist[r]) )

    #데이터베이스 조회해서 확인하는 과정
    sql="select * from testdb.melon"
    curs.execute(sql)
    rows=curs.fetchall()

    conn.commit()
    conn.close()