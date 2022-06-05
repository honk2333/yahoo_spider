import os
import wget
import json
from tqdm import tqdm
from math import sqrt
from joblib import Parallel, delayed

def down_url(news, k,  v):
    if v['num'] == 1:
        content = news[k]
        url = content['image']['url']
        target_name = k.split('/')[-1]+'.jpg'
        path = os.path.join('/home/wanghk/spider/nytimes_news/images', target_name)
        if os.path.exists(path):
            return
        try:
            file_name = wget.download(url, out=path)
        except:
            return

if __name__ == '__main__':
    path = '/home/wanghk/spider/nytimes_news/nytimes_news.json'
    news = json.load(open(path,'r'))
    path = '/home/wanghk/Extractor/nytimes_news_ner_elmo.json'
    entity = json.load(open(path,'r'))
    print(len(entity))
    print(len([ v for k,v in entity.items() if v['num']==1 ]))
    Parallel(n_jobs=1)(delayed(down_url)(news, k, v) for k,v in tqdm(entity.items()) )
