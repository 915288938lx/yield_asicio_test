import requests
from lxml import etree
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
tree = etree.HTML(html) # 树对象
tag_1 = tree.xpath('//*[@id="main"]/div/div[1]/div/ul/li[4]/a/@href')
tag_1_text_parent = tree.xpath('//*[@id="main"]/div/div[1]/div/ul//li/a/text()')
tag_1_href_parent = tree.xpath('//*[@id="main"]/div/div[1]/div/ul//li/a/@href')
tag_nextpage = tree.xpath('//*[@id="pages"]/a[1]/@href')
for tag in tag_1_text_parent:
    print(tag)
for href in tag_1_href_parent:
    print(href)
print(tag_nextpage[0])