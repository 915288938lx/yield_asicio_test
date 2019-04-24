import sys
import ssl
import urllib.request
import requests
from bs4 import BeautifulSoup as bs

def report(count, blockSize, totalSize):
    '''下载进度显示'''
    downloadedSize = count * blockSize
    percent = int(downloadedSize * 100 / totalSize)
    sys.stdout.write("\rDownloaded: {downloadedSize} bytes, Total: {totalSize} bytes, {percent} % complete")
    sys.stdout.flush()


headers= {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"__cfduid=debea90104586a125edc68032ecd037431532138348; Hm_lvt_4ab4576ab990d89616b2b6dc90c03dc1=1532138353,1532138658; Hm_lpvt_4ab4576ab990d89616b2b6dc90c03dc1=1532138658",
"Host":"6666av.vip",
"If-Modified-Since":"Fri, 13 Jul 2018 14:34:51 GMT",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
}

html =str(requests.get('http://6666av.vip/html/tupian/mingxing/index.html',headers=headers).content,'utf-8')
# print(html)
soup = bs(requests.get('http://6666av.vip/html/tupian/mingxing/index.html').content,'lxml')
# links = soup.find_all('li')
# main_tag = soup.find(id='main')
# art = main_tag.find('div',class_ = 'art')
# li = art.find_all('li')
li_ = soup.find(id='main').find('div',class_='art').find_all('li')
page_next = soup.find(id='pages').find(text='尾页').parent
print(page_next.get('href'))
# for li in li_:
#     print(li.text)
#     # print(li.a)
#     print('http://6666av.vip'+li.a.get('href'))

# print(li)
# print(main_tag)
# print(soup.title)
# print(soup.body.div.li)