import requests
from bs4 import BeautifulSoup

temp_tlist = []
temp_alist = []

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
melon = requests.get('https://www.melon.com/chart/index.htm', headers = header) # 멜론차트 웹사이트
melon_html = melon.text
melon_parse= BeautifulSoup(melon_html, 'html.parser')

title = melon_parse.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
artist = melon_parse.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span > a:nth-child(1)')

for r in range(50):
    'print(title[r].text + " - " + artist[r].text)'
    temp_tlist.append(title[r].text)
    temp_alist.append(artist[r].text)


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
melon = requests.get('https://www.melon.com/chart/index.htm#params%5Bidx%5D=51', headers = header) # 멜론차트 웹사이트
melon_html = melon.text
melon_parse= BeautifulSoup(melon_html, 'html.parser')
title = melon_parse.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
artist = melon_parse.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span > a:nth-child(1)')

for r1 in range(50):
    'print(title[r1].text + " - " + artist[r1].text)'
    temp_tlist.append(title[r1].text)
    temp_alist.append(artist[r1].text)
