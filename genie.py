import re
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chome/73.0.3683.86 safari/537.36'}
genie = requests.get('https://www.genie.co.kr/chart/top200/', headers = headers)
genie_html = genie.text
genie_parse = BeautifulSoup(genie_html, 'html.parser')

title = genie_parse.select('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis')
artist = genie_parse.select('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis')
songs = genie_parse.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text

for song in title:
    print(title.text.strip() + " - " + artist.text)
