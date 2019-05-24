# coding=utf-8

import requests
from bs4 import BeautifulSoup

'''
网页爬虫

'''

target = "http://www.xbiquge.la/13/13959/5939026.html"
req = requests.get(url=target)
# 由于响应内容采用iso-8859-1编码，所以需要先解码，再用python默认的utf-8编码
print(req.encoding)

html = req.text.encode(req.encoding).decode('utf-8')
bf = BeautifulSoup(html, features="html.parser")
texts = bf.find_all(name='div', attrs={'id': 'content'})

if __name__ == '__main__':  # 判断执行脚本是否在当前文件，是才会执行后续输出
    # print(html)
    print(requests.sessions)
    print(texts[0].text)  # debug 发现print再控制台打印显示不完整

    # f = open('d:/' + str(time.time()) + '.txt', mode='w', encoding='utf-8')
    # print(texts[0].text, file=f)  # 输出的是想要的内容

    print('输出成功')
