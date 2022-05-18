import requests
import json
import time


# 从数据源读取文件
sources = json.load(open('./sources.json','r'))

params = sources['queries']
headers = sources['headers']
json_data = sources['data']
# print(json_data.values())
json_data = json.loads(list(json_data.keys())[0])
# print(list(json_data.keys())[0])
json_data['requests']['g0']['params']['batches']['size'] = 100
json_data['requests']['g0']['params']['batches']['total'] = 1200
# print(json_data['requests']['g0']['params']['batches'])



# 设置代理
proxies = {'http': '114.212.85.117:808', 'https': '114.212.85.117:808'}
iter = 1
for i in range(iter):
    records = json.load(open('./yahoo_sports.json','r'))
    records = [ for record in records]
    print('当前总新闻数',len(records))
    tmp = {}
    response = requests.post('https://sports.yahoo.com/site/api/resource',proxies=proxies, params=params,  headers=headers, json=json_data)
    # print(response.json())
    # exit(1)
    res = response.json()
    items = res['g0']['data']['stream_items']
    print('爬取：', len(items))
    for item in items:
        try:
            id = item['id']
            if item['categoryLabel'] != 'Sports':
                continue
            record = {'title':item['title'], 'summary':item['summary'], 'url':item['url'], 'category':item['categoryLabel'], 'image':item['images'][list(item['images'].keys())[-1]] }
            tmp.update({id:record})
        except:
            continue
    # time.sleep(10)
    print('过滤后得到的：', len(tmp.keys()))
    records.update(tmp)
    print('更新后总新闻数：', len(records))
    json.dump(records, open('./yahoo_sports.json','w'))
    print('-'*30)