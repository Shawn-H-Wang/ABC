# -*- coding:utf-8 -*-
# @Author: wanghe
# @Time: 2021/1/22 16:19
# @Filename: __init__.py.py
# @Software: PyCharm

import time
import random

from File import FileHelper
from Spider import Spider
from MyThread import MyThread

if __name__ == '__main__':
    t1 = MyThread("thread1")
    t2 = MyThread("thread2")
    t3 = MyThread("thread3")
    t4 = MyThread("thread4")
    t5 = MyThread("thread5")
    t6 = MyThread("thread6")
    t7 = MyThread("thread7")
    t8 = MyThread("thread8")
    t9 = MyThread("thread9")
    t10 = MyThread("thread10")
    t11 = MyThread("thread11")
    t12 = MyThread("thread12")
    t13 = MyThread("thread13")
    t14 = MyThread("thread14")
    t15 = MyThread("thread15")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()

"""
word = "癫痫 发作 时间"
    spider = Spider()
    spider.__init__()
    for i in range(10):
        elements = spider.fetch_web_page(i, word)
        if elements is None or elements.__len__() <= 0:
            i -= 1
            continue
        print('第', i + 1, '页')
        links = spider.select_data(elements)
        E.write_links_to_file("癫痫", links, "连接列表", "links.txt")
        links.clear()
        time.sleep(random.randint(40, 60))
        
        
file = FileHelper("../Data/Diseases.txt")
diseses = file.read_file_to_diseases()
for disease in diseses:
    print(disease.name, "----->", disease.same_means)
print(len(diseses))
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 60; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}

words = '糖尿病 发作 时间'

for i in range(10):
    print('第', i + 1, '页')
    url = 'http://www.baidu.com/s?wd=' + words + '&pn=' + str(i) + '0'
    response = requests.get(url, headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    all_elements = soup.select('div#content_left')
    elements = all_elements[0]
    num = 1
    for element in elements.contents:
        if not isinstance(element, type(elements)):
            continue
        try:
            title = element.select('.t')[0]
            abstracts = element.select('.c-abstract')[0]
        except:
            continue
        t = title.text
        link = title.select('a')[0].attrs['href']
        abs = abstracts.text
        print("第", num, "条\t:", "title=[", t, "],url=[", link, ",快照内容为=[", abs + "]")
        num += 1
    time.sleep(random.randint(1, 30))

num = 1
for element in elements.contents:
    if not isinstance(element, type(elements)):
        continue
    try:
        title = element.select('.t')[0]
        abstracts = element.select('.c-abstract')[0]
    except:
        continue
    t = title.text
    link = title.select('a')[0].attrs['href']
    abs = abstracts.text
    print("第", num, "条\t:", "title=[", t, "],url=[", link, ",快照内容为=[", abs + "]")
    num += 1
"""
