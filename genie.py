import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200'
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
    artist = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
    print(title.strip() + " - " +artist)

    
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&pg=2'
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    title = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text
    artist = song.find('td',{'class':'info'}).find('a',{'class':'artist ellipsis'}).text
    print(title.strip() + " - " +artist)