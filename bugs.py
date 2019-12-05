import requests
from bs4 import BeautifulSoup

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

'''for s in range(100):
    print(str(s)+"위")
    print("제목: " + title_arr[s] + "/ 가수 :"+artist_arr[s])'''
