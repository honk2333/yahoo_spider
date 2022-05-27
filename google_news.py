from bs4 import BeautifulSoup
from urllib import request
from numpy import cfloat, short
import requests
import re
import json
import hashlib


def google_news(page):
    # 设置代理
    proxies = {'http': '114.212.85.117:808', 'https': '114.212.85.117:808'}
    response =  requests.get('https://newsapi.org/v2/top-headlines?category=sports&from=2022-04-26&to=2022-05-26&apiKey=402e82bbd8c744a0a2a8024de374e877&pageSize=100&language=en&page='+str(page), proxies=proxies)
    res = response.json()
    print(res.keys())
    # print(res)
    if res['status'] != 'ok':
        print(res)
        exit(1)
    print(res['totalResults'])
    articles = res['articles']

    # records = {}
    records = json.load(open('./google_sports.json','r'))
    tmp = {}
    md5 = hashlib.md5()
    print('当前总新闻数：', len(records))
    print('发现新闻数：', len(articles))
    for article in articles:
        record = {
                'title':article['title'], 
                'summary':article['description'], 
                'url':article['url'], 
                'category':'Sports', 
                'image':{'height':None,'width':None,'url':article['urlToImage']} 
                }
        md5.update(record['title'].encode(encoding='utf-8'))
        id = md5.hexdigest()
        tmp.update({id:record})
        # id += 1
    records.update(tmp)
    print('更新后总新闻数：', len(records))
    json.dump(records, open('./google_sports.json','w'))

if __name__ == '__main__':
    for i in range(8):
        google_news(i)