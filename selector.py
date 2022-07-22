import requests
from lxml import etree
import random
import time
import json
from selenium import webdriver
from tqdm import tqdm

def get_film_list():
    proxies = {
        'http':'114.212.85.117:808',
        'https':'114.212.85.117:808'
    }
    url = 'https://www.imdb.com/chart/top-english-movies?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=AS1AYHZTCWF506448ZG7&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_4'
    headers = {'content-language': 'en'}
    res = requests.get(url, proxies=proxies, headers=headers)
    res.encoding = res.apparent_encoding
    xpath = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]/a'

    tree = etree.HTML(res.text)
    films = tree.xpath(xpath)
    print(len(films))
    film_file = open('./selector/film_list', 'w')
    for film in films:
        name = film.text
        people = film.attrib.get('title')
        print(name, '\t', people)
        film_file.write(name + '\t' +  people + '\n')

class Crawler_google_images:
    # 初始化
    def __init__(self):
        self.url = url

    # 获得Chrome驱动，并访问url
    def init_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        # 访问url
        browser.get(self.url)
        # 最大化窗口，之后需要爬取窗口中所见的所有图片
        browser.maximize_window()
        return browser

    # 下载图片
    def download_images(self, browser, num=100):
        #存储路径
        picpath = './cat'
        # 路径不存在时创建一个
        if not os.path.exists(picpath): os.makedirs(picpath)

        count = 0  # 图片序号
        pos = 0
        # print(num)

        while (True):
            try:
                # 向下滑动
                js = 'var q=document.documentElement.scrollTop=' + str(pos)
                pos += 500
                browser.execute_script(js)
                time.sleep(1)
                # 找到图片
                # html = browser.page_source#也可以抓取当前页面的html文本，然后用beautifulsoup来抓取
                # 直接通过tag_name来抓取是最简单的，比较方便
                img_elements = browser.find_elements_by_xpath('//a[@class="wXeWr islib nfEiy mM5pbd"]')
                try:
                    for img_element in img_elements:
                        #点开大图页面
                        img_element.click()
                        time.sleep(0.5)
                        try:
                            # 这里balabala里面有好几个，所以要过滤一下
                            # 取名好烦哦···
                            balabalas = browser.find_elements_by_xpath('//img[@class="n3VNCb"]')

                            if (balabalas):
                                for balabala in balabalas:
                                    src = balabala.get_attribute('src')
                                    #过滤掉缩略图和无关干扰信息
                                    if src.startswith('http') and not src.startswith(
                                            'https://encrypted-tbn0.gstatic.com'):
                                        print('Found' + str(count) + 'st image url')
                                        # img_url_dic.append(src)
                                        self.save_img(count, src, picpath)
                                        count += 1
                                        #爬取到指定数量图片后退出
                                        if (count >= num):
                                            return "stop"
                        except:
                            print('获取图片失败')

                    #回退
                    browser.back()
                    time.sleep(0.3)
                except:
                    print('获取页面失败')
            except:
                print("划不动了")

    def save_img(self, count, img_src, picpath):
        filename = picpath + '/' + str(count) + '.jpg'
        r = requests.get(img_src)
        with open(filename, 'wb') as f:
            f.write(r.content)
        f.close()

    def run(self):
        self.__init__()
        browser = self.init_browser()
        self.download_images(browser, 100)  # 可以修改爬取的图片数
        browser.close()
        print("############爬取完成")


def get_actorimgs():
    with open('./selector/film_list','r') as f:
        contents = f.readlines()
    # print(len(contents), contents[0])
    user_agent_list = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    ]
    proxies = {
        'http':'114.212.85.117:808',
        'https':'114.212.85.117:808'
    }
    actorimgs = {}
    # actorimgs = json.load(open('./selector/actor_url.json','r'))
    for line in tqdm(contents):
        actors = line.split('\t')[1].split(',')[1:]
        actors = [actor.strip() for actor in actors]
        print(actors)
        for actor in actors:
            # if actor in actorimgs:
            #     continue

            # 修改keyword便可以修改搜索关键词 建议也修改存储目录
            keyword = actor + ' movie'
            url = 'https://www.google.com.hk/search?q=' + keyword + '&source=lnms&tbm=isch'
            actorimgs[actor] = []
            craw = Crawler_google_images(url)
            craw.run()       


            def requests_spider():
                params = {
                    'q': actor + ' movie',
                    'tbm': 'isch',
                    'ved': '2ahUKEwig_rSN8oz5AhXRitgFHdiECFYQ2-cCegQIABAA',
                    'oq': actor + ' movie',
                    'gs_lcp': 'CgNpbWcQAzIFCAAQgAQyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB5QAFiWAWDlA2gAcAB4AIABqwGIAcMCkgEDMC4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE',
                    'sclient': 'img',
                    'ei': '8czaYuDBE9GV4t4P2ImisAU',
                    'bih': '978',
                    'biw': '1920',
                }
                # '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
                headers = {
                    'content-language': 'en',
                    "User-Agent": random.choice(user_agent_list),
                }
                res = requests.get('https://www.google.com/search', params=params, headers=headers, proxies=proxies)
                res.encoding = res.apparent_encoding
                print(res)
                # with open('./test.html','w') as f: f.write(res.text)
                # //*[@id="islrg"]/div[1]/div[9]/a[1]
                xpath = '//*[@id="islrg"]/div[1]/div/a[1]'
                tree = etree.HTML(res.text)
                imgs = tree.xpath(xpath)
                print(len(imgs))
                for item in imgs[:15]:
                    h1 = item.attrib.get('href')
                    res2 = requests.get(url=h1, proxies=proxies)
                    tree2 = etree.HTML(res2.text)
                    imgurl = tree2.xpath('//*[@id="imi"]')[0].attrib.get('src')
                    actorimgs[actor].append(imgurl)
                    print(actor, imgurl)
                json.dump(actorimgs, open('./selector/actor_url.json','w'))
                time.sleep(2)
            

    
if __name__ == '__main__':
    # get_film_list()
    get_actorimgs()