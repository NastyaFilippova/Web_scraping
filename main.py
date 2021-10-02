import requests
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

res = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all('article')
# pprint(posts)
for post in posts:
    hubs = post.find_all('span', class_='tm-article-snippet__hubs-item')
    hub = {hub.text.lower() for hub in hubs}
    if hub & KEYWORDS:
        date = post.find('time').attrs.get('title')
        titles = post.find('h2')
        title = titles.text
        href = 'https://habr.com/' + titles.find('a').attrs.get('href')
        pprint(date)
        pprint(title)
        pprint(href)
        pprint('____________________')

