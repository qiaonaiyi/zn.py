'''
#英雄榜头像图片
import requests
from bs4 import BeautifulSoup as bs
req = requests.get('http://mozhe.cn')
body = req.text
soup = bs(body, 'html.parser')
info = soup.select('div.rankList')[0]
imgs = info.select('img')
for img in imgs:
    print(img.attrs['src'])
'''
'''
import requests
r=requests.get('https://bj.lianjia.com/zufang')
r=requests.post('https://bj.lianjia.com/zufang',data={'key':'value'})
r=requests.put('https://bj.lianjia.com/zufang',data={'key':'value'})
r=requests.delete('https://bj.lianjia.com/zufang')
r=requests.head('https://bj.lianjia.com/zufang/')
r=requests.options('https://bj.lianjia.com/zufang')
#get传参
payload={'key1':'value1','key2':'value2'}
r=requests.get('https://bj.lianjia.com/zufang/',params=payload)
print(r.url)
'''
'''
import requests
r=requests.get('https://bj.lianjia.com/zufang')
print(r.text)
print(r.encoding)
r.encoding='ISO-8859-1'
print(r.encoding)

import requests
r=requests.get('https://api.github.com/events',stream=True)
r1=requests.get('https://bj.lianjia.com/zufang')
#print(r.json())
print(r1.raw)
print(r1.raw.read(10))
'''
'''
import requests
#url='https://api.github.com/some/endpoint'
#r=requests.get(url,headers=headers)
#print(r)
payload ={'1':'a','2':'b'}
r=requests.post('http://httpbin.org/post',data=payload)
#print(r.text)
payload=(('key1','value1'),('key1','value2'))
r=requests.post('http://httpbin.org/post',data=payload)
print(r.text)
'''
'''
import requests
import json
url='http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#id2'
payload={'some':'data'}
r=requests.post(url,json=payload)
print(r)
'''
'''
import time,csv
from random import uniform,choice
import requests
from bs4 import BeautifulSoup

cities = ['bj', 'sh', 'nj', 'wh', 'cd', 'xa','hf']
# 一个我们将要爬取城市的列表

def get_city():
    global cities
    try:
        city = choice(cities)
        cities.remove(city)
        # 随机选取一个城市进行爬取，然后再列表中删除这个城市
        print(cities)
    except IndexError:
        return None
    # 当没有城市了，就返回一个None
    return city
def get_url(index,city):
    if city == None:
        return
    # 城市值为None时，我们就跳出
    else:
        if index == 1:
            url = 'https://{city}.lianjia.com/zufang/'.format(city=city)
            return url
        # 这是首页链接
        else:
            url = 'https://{city}.lianjia.com/zufang/pg{index}'.format(index=index,city=city)
            return url

def get_ressponse(url,file,headers):
    html = requests.get(url=url,headers=headers,verify=False)
    Soup = BeautifulSoup(html.text,'lxml')
    house_list = Soup.find(attrs={'id':'house-lst'}).find_all('li')
    for li in house_list:
        detail_mes = li.a['href']
        img_house = li.img['src']
        title = li.h2.a.get_text(strip=True)
        region = li.find_next(attrs={'class':'where'}).a.get_text(strip=True)
        zone = li.find_next(attrs={'class':'zone'}).span.get_text(strip=True)
        meters = li.find_next(attrs={'class':'meters'}).get_text(strip=True)
        directory = li.find_next(attrs={'class':'meters'}).find_next_sibling('span').get_text()
        other = li.find_next(attrs={'class':'other'}).find('div').get_text(strip=True)
        chanquan = li.find_next(attrs={'class':'chanquan'}).get_text(strip=True)
        file.writerow([detail_mes,img_house,title,region,zone,meters,directory,other,chanquan])
        # 我们将传进一个csv的写的对象，对文件进行写操作

def main(city):
    for index in range(1, 101):
        try:
            if  index == 1 or index == 2:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Referer': 'https://{city}.lianjia.com/zufang/pg3'.format(city=city),
                    # 我们动态的调换跳转的页面，觉得更像人的点击行为
                    'Host': '{city}.lianjia.com'.format(city=city),
                    # 这里我们动态的调换要访问的主机
                }
            else:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Referer': 'https://{city}.lianjia.com/zufang/pg3'.format(city=city,index=index-1),
                    'Host': '{city}.lianjia.com'.format(city=city),
                }
                # 注意这里的请求头我们在不同的情况下值是不一样的
                # 当然请求头你不换也许并不会导致出错，但是这也是一种反爬虫的方法，学习一下？
            url = get_url(index,city)
            get_ressponse(url=url, file=writer,headers=headers)
            # 将请求头传入
            # 传进链接和写对象
            t = uniform(1, 3)
            time.sleep(t)
            # 强制要求请求休息一下，我们这里用1，3之间的随机数
        except AttributeError:
            print('我发现了一个错误')
        except UnicodeEncodeError:
            print('有一个编码错误')
        # 两个错误检查


if __name__ == '__main__':
    with open('D:/lianjia.csv','a',encoding='utf-8') as f:
        # 因为默认的读写操作是gbk，所以最好还是改成utf-8
        # 在这里打开文件而不是在循环中打开，我们就可以避免频繁的IO操作
        writer = csv.writer(f)
        # 创建一个写对象
        writer.writerow(['detail_mes','img_house','title','region','zone,meters','directory','other','chanquan'])
        # 写入表头
        for x in range(0,100):
            city = get_city()
            time.sleep(10)
            # 城市间的跳转等待时间稍微长一点，毕竟我们要更友好对不对！
            print('正在爬取的城市是：%s' % city)
            if city == None:
                break
                # 如果没有城市了，那就跳出循环停止了。
            main(city)
'''

html_doc =""" 
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)
'''
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p)
print(soup.a)
'''
print(soup.find_all('a'))
print(soup.find(id="link3"))

for link in soup.find_all('a'):
    print(link.get('href'))

