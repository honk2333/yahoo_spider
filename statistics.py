from importlib import import_module
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
from nltk import word_tokenize
from tqdm import tqdm

interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']   #定义符号列表
# 加载停用词
with open('/home/wanghk/stopwords/baidu_stopwords.txt') as f:
    stopwords = f.read().split('\n')
print(len(stopwords))
print(stopwords[:20])

news = json.load(open('./yahoo_sports.json','r'))

word_dict = {}
for id, new in tqdm(news.items()):
    title = new['title']
    words = word_tokenize(title)
    words = [word for word in words if word not in interpunctuations]   #去除标点符号
    # print(words)
    for word in words:
        if word in stopwords:
            continue
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

cloud = WordCloud(scale=4, max_words=100, max_font_size=60,random_state=20, background_color='white')
res = cloud.fit_words(word_dict)

plt.imshow(res)
plt.axis('off')
plt.savefig('./wordcloud.png', dpi=600)