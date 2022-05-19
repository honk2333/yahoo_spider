import requests
import json
import time
import fire
from bs4 import BeautifulSoup



def yahoo_sports():
    # 从数据源读取文件
    sources = json.load(open('./sources.json','r'))

    params = sources['queries']
    headers = sources['headers']
    json_data = sources['data']
    # print(json_data.values())
    json_data = json.loads(list(json_data.keys())[0]+list(json_data.values())[0])
    # print(list(json_data.keys())[0])
    json_data['requests']['g0']['params']['batches']['size'] = 100
    json_data['requests']['g0']['params']['batches']['total'] = 1200
    # print(json_data['requests']['g0']['params']['batches'])



    # 设置代理
    proxies = {'http': '114.212.85.117:808', 'https': '114.212.85.117:808'}
    iter = 1
    for i in range(iter):
        records = json.load(open('./yahoo_sports.json','r'))
        records= { k:v for k,v in records.items() if v['category'] == 'Sports' }
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


def ny_sports():
   
    headers = {
        'authority': 'samizdat-graphql.nytimes.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        # Already added when you pass json=
        'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        'cookie': 'nyt-a=u5r-9NTLSwOxez5k6KHfW9; nyt-gdpr=0; nyt-purr=cfhhcfhhhukf; nyt-b3-traceid=bc01504065384651aabf1cff5341aa88; nyt-m=5458FA868AF5EC0AF1B22C5BB5726A2E&igu=i.1&prt=i.0&iub=i.0&iru=i.1&v=i.0&pr=l.4.0.0.0.0&iue=i.0&igd=i.0&ira=i.0&s=s.core&e=i.1654070400&fv=i.0&imv=i.0&g=i.0&ier=i.0&ifv=i.0&igf=i.0&n=i.2&cav=i.0&iir=i.0&uuid=s.aabdbadd-7a6a-480e-bee9-b10196c53f38&vp=i.0&imu=i.1&er=i.1652957016&vr=l.4.0.0.0.0&rc=i.0&ft=i.0&ica=i.0&iga=i.0&ird=i.0&t=i.2; purr-cache=<K0<r<C_<G_<S0; b2b_cig_opt=%7B%22isCorpUser%22%3Afalse%7D; edu_cig_opt=%7B%22isEduUser%22%3Afalse%7D; nyt-jkidd=uid=0&lastRequest=1652957017545&activeDays=%5B0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1%5D&adv=1&a7dv=1&a14dv=1&a21dv=1&lastKnownType=anon; _gcl_au=1.1.557609778.1652957018; walley=GA1.2.852392110.1652957018; walley_gid=GA1.2.1082523256.1652957019; _ga=GA1.2.1106357322.1652957019; _gid=GA1.2.1583643512.1652957019; iter_id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhaWQiOiI2Mjg2MWY1ZDdjMTlmNTAwMDE3YjVhOTEiLCJjb21wYW55X2lkIjoiNWMwOThiM2QxNjU0YzEwMDAxMmM2OGY5IiwiaWF0IjoxNjUyOTU3MDIxfQ.X-QOZzCqF4dsZZCNkjqLwqtPerUoGBdXl2RsUpUoS-s; datadome=u3wqkadPFKkc1PUrMnzinOYmDNIM2L3WZQdhVWVhoAc8Gnk8EHah1V.TmF6DovuamXg4g0_DlZH2e_z~CazsN-hvKc2XzmTJ~~GhHwD~dBKC~tYW6i3xkqrfDmGAUEc',
        'nyt-app-type': 'project-vi',
        'nyt-app-version': '0.0.5',
        'nyt-token': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs+/oUCTBmD/cLdmcecrnBMHiU/pxQCn2DDyaPKUOXxi4p0uUSZQzsuq1pJ1m5z1i0YGPd1U1OeGHAChWtqoxC7bFMCXcwnE1oyui9G1uobgpm1GdhtwkR7ta7akVTcsF8zxiXx7DNXIPd2nIJFH83rmkZueKrC4JVaNzjvD+Z03piLn5bHWU6+w+rA+kyJtGgZNTXKyPh6EC6o5N+rknNMG5+CdTq35p8f99WjFawSvYgP9V64kgckbTbtdJ6YhVP58TnuYgr12urtwnIqWP9KSJ1e5vmgf3tunMqWNm6+AnsqNj8mCLdCuc5cEB74CwUeQcP2HQQmbCddBy2y0mEwIDAQAB',
        'origin': 'https://www.nytimes.com',
        'referer': 'https://www.nytimes.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'CollectionsQuery',
        'variables': {
            'id': '/section/sports',
            'first': 100,
            'streamQuery': {
                'sort': 'newest',
            },
            'exclusionMode': 'HIGHLIGHTS_AND_EMBEDDED',
            'isHighEnd': False,
            'highlightsListUri': 'nyt://per/personalized-list/__null__',
            'highlightsListFirst': 0,
            'hasHighlightsList': False,
            'cursor': 'YXJyYXljb25uZWN0aW9uOjk5',
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': 'e4aafca566109697de2df33ee87dbb1052e21c181688197bb7c0be8dac577fb9',
            },
        },
    }

    # 设置代理
    proxies = {'http': '114.212.85.117:808', 'https': '114.212.85.117:808'}

    # 从数据源读取文件
    # records = json.load(open('./yahoo_sports.json','r'))
    records = {}
    print('当前总新闻数',len(records))
    response = requests.post('https://samizdat-graphql.nytimes.com/graphql/v2',proxies=proxies, headers=headers, json=json_data)
    res =response.json()
    # json.dump(res, open('format.json','w'))
    items = res['data']['legacyCollection']['highlights']['edges']
    # print(res['data'].keys())
    # print(items.keys())
    tmp = {}
    print('爬取：', len(items))
    for item in items:
        item = item['node']
        
        id = item['id']
        # print(item['promotionalMedia']['crops'][2]['renditions'][2])
        image_info = item['promotionalMedia']['crops'][2]['renditions'][2]
        assert image_info['name'] == 'mediumThreeByTwo440'
        record = {'title':item['headline']['default'], 'summary':item['summary'], 'url':item['url'], 'category':'Sports', 'image':{'height':image_info['height'],'width':image_info['width'],'url':image_info['url']} }
        tmp.update({id:record})
      
    # time.sleep(10)
    print('过滤后得到的：', len(tmp.keys()))
    records.update(tmp)
    print('更新后总新闻数：', len(records))
    json.dump(records, open('./yahoo_sports.json','w'))
    print('-'*30)


if __name__ == '__main__':
    # fire.Fire()
    ny_sports()