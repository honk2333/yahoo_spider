from bs4 import BeautifulSoup
from urllib import request
import chardet

url = "https://www.huxiu.com"
response = request.urlopen(url)
html = response.read()
charset = chardet.detect(html)
html = html.decode(str(charset["encoding"]))  # 设置抓取到的html的编码方式

# 使用剖析器为html.parser
soup = BeautifulSoup(html, 'html.parser')
# 获取到每一个class=hot-article-img的a节点
allList = soup.select('.home-news-module__article-list__item')
print(len(allList))
#遍历列表，获取有效信息
for news in allList:
    aaa = news.select('a')
    divv = news.select('div')
    # print(aaa[0])
    # print(divv[0])
    # print(len(divv))
    # exit(1)
    # 只选择长度大于0的结果
    if len(aaa) > 0:
        # 文章链接
        try:#如果抛出异常就代表为空
            href = url + aaa[0]['href']
        except Exception:
            href=''
        # 文章图片url
        try:
            imgUrl = aaa[0].select('img')[0]['alt']
        except Exception:
            imgUrl=""
        # 新闻标题
        try:
            title = aaa[0]['title']
        except Exception:
            title = "标题为空"
        print("标题",title,"\nurl：",href,"\n图片地址：",imgUrl)
        print("==============================================================================================")