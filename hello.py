import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
melon = requests.get('https://www.melon.com/chart/index.htm', headers = header) # 멜론차트 웹사이트
melon_html = melon.text
melon_parse= BeautifulSoup(melon_html, 'html.parser')

title = melon_parse.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
artist = melon_parse.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')

rank = 50
for r in range(rank):
    print( rank +" : " +title[r].text + " - " + artist[r].text)