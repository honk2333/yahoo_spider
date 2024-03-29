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
        try:
            record = {
                    # 'title':article['headline']['print_headline'], 
                    'title':article['headline']['print_headline'] if len(article['headline']['print_headline'])>len(article['headline']['main']) else article['headline']['main'], 
                    'summary': article['abstract'],
                    'url':article['web_url'], 
                    'category': article['section_name'], 
                    # 'image':{'heigh':article['multimedia'][0]['height'],'width':article['multimedia'][0]['width'],'url':'https://www.nytimes.com/'+article['multimedia'][0]['url']} 
                    'image':{'heigh':article['multimedia'][2]['height'],'width':article['multimedia'][2]['width'],'url':'https://www.nytimes.com/'+article['multimedia'][2]['url']} 
                    }
            # md5.update(record['title'].encode(encoding='utf-8'))
            # id = md5.hexdigest()
            tmp.update({id:record})
        except:
            continue
        # id += 1
    records.update(tmp)
    print('更新后总新闻数：', len(records))
    json.dump(records, open('./nytimes_news/nytimes_news.json','w'))


def nytimes_new_2():
    json_list = os.listdir('./nytimes_news')
    json_list = [ f for f in json_list if f[:2]=='20']
    print(len(json_list))
    records = {}
    for f in json_list:
        data = json.load(open(os.path.join('./nytimes_news', f),'r'))
        articles = data['response']['docs']
        print(len(articles))
        for article in articles:
            if article['type_of_material'] != 'News':
                continue
            if len(article['multimedia']) == 0 :
                continue
            id = article['_id']
            try:
                record = {
                        'title':article['headline']['print_headline'] if len(article['headline']['print_headline'])>len(article['headline']['main']) else article['headline']['main'], 
                        'summary': article['abstract'],
                        'url':article['web_url'], 
                        'category': article['section_name'], 
                        'image':{'heigh':article['multimedia'][2]['height'],'width':article['multimedia'][2]['width'],'url':'https://www.nytimes.com/'+article['multimedia'][2]['url']} 
                        }
                records.update({id:record})
            except:
                continue
    print(len(records))
    json.dump(records, open('./nytimes_news2.json','w'))


if __name__ == '__main__':
    year = 2015
    for month in range(1,13):
        nytimes_news(year,month)
    # nytimes_new_2()