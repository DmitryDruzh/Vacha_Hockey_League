from django.shortcuts import render
from django.views.generic import ListView
from bs4 import BeautifulSoup
import requests

# Create your views here.

def all_news(requset):
    url = 'https://www.sports.ru/hockey/#menu-sub'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all('a', class_='h2')
    news = news[:5]
    news_urls = []
    for i in range(5):
        elem = {'title': news[i].text, 'url': news[i]['href']}
        news_urls.append(elem)

    return render(requset, 'news/all_news.html', {'news_urls': news_urls})