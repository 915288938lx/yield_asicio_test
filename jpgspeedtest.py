import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from collections import OrderedDict
response = str(requests.get('https://www.vooc.net/2202.html').content,'utf-8')
tree = etree.HTML(response)
links = tree.xpath('/html/body/section/div/div/article/div[3]/p//img/@src')
name = tree.xpath('/html/body/section/div/div/article/div[3]/p//img/@title')
dic = OrderedDict(zip(links,name))
print(links)
for (link,name) in dic.items():
    with open(name+'.jpg','wb') as f:
        f.write(requests.get(link,stream=True).content)

