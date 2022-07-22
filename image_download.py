import os
import wget
import json
from tqdm import tqdm
from math import sqrt
from joblib import Parallel, delayed
import multiprocessing

def down_url(param = ()):
    content, k = param
    url = content['image']['url']
    target_name = k.split('/')[-1]+'.jpg'
    path = os.path.join('/home/wanghk/Extractor/spider/google/images', target_name)
    if os.path.exists(path):
        return
    try:
        file_name = wget.download(url, out=path)
    except:
        return

if __name__ == '__main__':
    path = '/home/wanghk/Extractor/spider/google/google_sports.json'
    news = json.load(open(path,'r'))
    # print(len(news))
    # path = '/home/wanghk/Extractor/NER/output/allenelmo_out/nytimes_news_ner_elmo.json'
    # entity = json.load(open(path,'r'))
    # print(len(entity))
    params = { k:v for k,v in news.items()}
    # print(params)
    print(len(params))
    # Parallel(n_jobs=1)(delayed(down_url)(news, k, v) for k,v in tqdm(entity.items()) )
    thread_num = 4
    pool = multiprocessing.Pool(thread_num)
    multi_result = pool.map_async(down_url, [ (news[k],k) for k,v in params.items() ] )
    multi_results = multi_result.get()
    # _ = list(map(caption_dic.update, multi_results))
    # json.dump(caption_dic,open('./mega/googlesearch.json','w'))