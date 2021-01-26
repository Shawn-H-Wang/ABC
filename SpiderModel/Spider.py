# -*- coding:utf-8 -*-
# @Author: wanghe
# @Time: 2021/1/22 16:20
# @Filename: Spider.py
# @Software: PyCharm

import random
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode
from urllib import error


class Spider(object):

    def __init__(self):
        self.user_agent = [
            "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; OMNIA7)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)",
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Referer": "http://www.baidu.com/"
        }

    def fetch_web_page(self, i: int, words):
        """
        Fetch the messege from baidu serch engine with keyword.
        The page is no.i

        :param i: Number of the current page
        :param words: The search keyword
        :param headers: Web request header
        :return: contents: The web's elements, which has the data
        """
        self.headers['User-Agent'] = self.user_agent[random.randint(0, len(self.user_agent) - 1)]
        url = 'http://www.baidu.com/s?' + urlencode({"wd": words}) + '&pn=' + str(i) + '0'
        try:
            req = requests.get(url=url, headers=self.headers)
            html = req.text
            soup = BeautifulSoup(html, 'lxml')
            if soup.body is None:
                return None
            else:
                all_elements = soup.select('.result')
                if len(all_elements) <= 0:
                    print("第{}页\t网络不给力".format(i + 1))
                    return None
                elements = []
                for i in range(len(all_elements)):
                    elements.append(all_elements[i])
        except error.URLError as e:
            if hasattr(e, 'code'):
                print("HTTP Error")
                print(e.code)
            elif hasattr(e, 'reason'):
                print("URL Error")
                print(e.reason)
            return None
        except:
            print("Network failed")
            return None
        return elements

    def select_data(self, elements):
        """
        Select the data from the HTML text

        :param elements:
        :return:
        """

        num = 1
        datas = []
        for element in elements:
            try:
                title = element.select('.t')[0]
                abstracts = element.select('.c-abstract')[0]
            except:
                continue
            t = title.text
            link = title.select('a')[0].attrs['href']
            abs = abstracts.text
            print("第", num, "条\t:", "title=[", t, "],url=[", link, "] ,快照内容为=[", abs + "]")
            data = "title=[{}],url=[{}],快照内容为=[{}]".format(t, link, abs)
            datas.append(data)
            num += 1
        return datas
