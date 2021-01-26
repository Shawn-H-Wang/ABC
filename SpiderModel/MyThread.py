# -*- coding:utf-8 -*-
# @Author: wanghe
# @Time: 2021/1/25 17:11
# @Filename: MyThread.py
# @Software: PyCharm

import threading
import time, random
from Spider import Spider
from File import FileHelper

D = FileHelper('../Data/Diseases.txt')
V = FileHelper('../Data/Verbs.txt')
A = FileHelper('../Data/Attributes.txt')
E = FileHelper('../Data/Execute.txt')

diseases = D.read_file_to_diseases()
verbs = V.read_file_to_list()
attrs = A.read_file_to_list()
execute = int(E.read_file_to_list()[0])

class MyThread(threading.Thread):

    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name
        self.lock = threading.Lock()

    def run(self):
        global diseases, verbs, attrs
        global execute
        spider = Spider()
        spider.__init__()
        while True:
            self.lock.acquire()
            disease = diseases[execute]
            execute += 1
            E.write_exec_to_file(execute)
            self.lock.release()
            for verb in verbs:
                for attr in attrs:
                    word = disease.name + " " + verb + " " + attr
                    reload = 0
                    revisit = 0
                    for i in range(10):
                        print(self.name)
                        elements = spider.fetch_web_page(i, word)
                        if elements is None or elements.__len__() <= 0:
                            if reload > 4:
                                continue
                            i -= 1
                            reload += 1
                            time.sleep(random.randint(10, 20))
                            continue
                        print('第', i + 1, '页')
                        links = spider.select_data(elements)
                        if links.__len__() <= 0:
                            print("没有东西，再去试试......")
                            if revisit > 4:
                                continue
                            i -= 1
                            revisit += 1
                            time.sleep(random.randint(10, 20))
                            continue
                        E.write_links_to_file(disease.name, links, attr, "links.txt")
                        links.clear()
                        time.sleep(random.randint(60, 100))
                    time.sleep(random.randint(10, 20))
                time.sleep(random.randint(10, 20))
            print(disease.name + "结束，开始下一个...")
            time.sleep(random.randint(5, 10))
            if execute >= diseases.__len__():
                break
