from bs4 import BeautifulSoup
from urllib import request
import chardet
from numpy import cfloat, short
import requests
import re


url = "https://sports.yahoo.com/news/"
response = request.urlopen(url)
html = response.read()
charset = chardet.detect(html)
html = html.decode(str(charset["encoding"]))  # 设置抓取到的html的编码方式


# 使用剖析器为html.parser
soup = BeautifulSoup(html, 'html.parser')
# 获取到每一个class=hot-article-img的a节点
finance = soup.select('.js-stream-content')
print(len(finance))


records = []
for info in finance:
    cf = info.select('.Cf')
    # print(cf)
    imgcf = cf[0].select(r'.H\(0\)')
    textcf = cf[0].select(r'.Ov\(h\)')
    imgurl = imgcf[0].select('img')[0]['src']
    # print(len(textcf[1].select('a')))
    title = textcf[1].select('a')[0].get_text()
    short = textcf[1].select('p')[0].get_text()
    print(imgurl)
    print(title)
    print(short)
    tag = 'sports'
    records.append({'title':title, 'intro':short, 'tag':tag, 'imgurl':imgurl })
    
print(len(records))