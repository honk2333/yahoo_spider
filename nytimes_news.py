from bs4 import BeautifulSoup
from urllib import request
from numpy import cfloat, short
import requests
import re
import json
import hashlib
import os
import sys

def nytimes_news(year, month):
    if month < 10:
        mm = '0' + str(month)
    else:
        mm = str(month)
    path = './nytimes_news/'+str(year) + mm + '.json'
    if os.path.exists(path):
        res = json.load(open(path,'r'))
    else:
        # 设置代理
        proxies = {'http': '114.212.85.117:808', 'https': '114.212.85.117:808'}
        response =  requests.get('https://api.nytimes.com/svc/archive/v1/'+str(year)+'/'+str(month)+'.json?api-key=OoLcpwv7nSQ9XUJ5jxt3sZZBZzGHzuZA', proxies=proxies)
        res = response.json()
        # print(res.keys())
        # if month < 10:
        #     month = '0' + str(month)
        # else:
        #     month = str(month)
        json.dump(res, open('./nytimes_news/'+str(year) + mm + '.json','w'))


    articles = res['response']['docs']
    # records = {}
    records = json.load(open('./nytimes_news/nytimes_news.json','r'))
    tmp = {}
    # md5 = hashlib.md5()
    print('当前总新闻数：', len(records))
    print('发现新闻数：', len(articles))
    for article in articles:
        if article['type_of_material'] != 'News':
            continue
        if len(article['multimedia']) == 0 :
            continue
        # if article['document_type'] != 'article':
        #     continue
        id = article['_id']
        # print([0].keys())
        # for pic in article['multimedia']:
        #     print(pic)
        record = {
                'title':article['headline']['print_headline'], 
                'summary': article['abstract'],
                'url':article['web_url'], 
                'category': article['section_name'], 
                'image':{'heigh':article['multimedia'][0]['height'],'width':article['multimedia'][0]['width'],'url':'https://www.nytimes.com/'+article['multimedia'][0]['url']} 
                }
        # md5.update(record['title'].encode(encoding='utf-8'))
        # id = md5.hexdigest()
        tmp.update({id:record})
        # id += 1
    records.update(tmp)
    print('更新后总新闻数：', len(records))
    json.dump(records, open('./nytimes_news/nytimes_news.json','w'))

if __name__ == '__main__':
    year = 2022
    for month in range(1,6):
        nytimes_news(year,month)