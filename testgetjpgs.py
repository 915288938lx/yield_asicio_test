import requests
from lxml import etree
from collections import OrderedDict
import threading
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


def main_page(main_url,headers):
    response = requests.get(main_url,headers=headers)
    html_doc = response.content
    tree = etree.HTML(html_doc)

    li_titles = tree.xpath('//*[@id="main"]/div/div[1]/div/ul//li/a/text()') #[标题列表]
    li_hrefs = tree.xpath('//*[@id="main"]/div/div[1]/div/ul//li/a/@href') #[标题链接列表]
    title_href_dict = OrderedDict(zip(li_titles,li_hrefs))
    li_next_page = tree.xpath('//*[@id="pages"]/a[1]/@href')[0] # 下一页链接
    return title_href_dict, li_next_page

def parse_url(href,headers,img_name): # 解析某个链接的图片
    response = requests.get(href, headers=headers)
    html_doc = str(response.content,'utf-8')
    tree = etree.HTML(html_doc)
    img_urls = tree.xpath('//*[@id="main"]/div/div[1]/div//p/img/@src') # [图片链接的列表]
    n = 0
    for img_url in img_urls:
        n = n+1
        real_img_url = "http:"+img_url
        img_response = requests.get(real_img_url, stream=True, allow_redirects=True)
        img_stream = img_response.content
        # img_name = img_name+str(n)+".jpg"
        with open(img_name+str(n)+".jpg",'wb') as f:
            f.write(img_stream)
            print(1)



if __name__ == '__main__':
    main_url = 'http://6666av.vip/html/tupian/yazhou/index_51.html'
    page_head = 'http://6666av.vip'
    title_href_dict, li_next_page = main_page(main_url,headers=headers)
    n = 0
    for (title, href) in title_href_dict.items():
        real_href = page_head+href
        img_name = title
        threads = []
        for i in range(1,9):
            thread = threading.Thread(target=parse_url,args=(real_href,headers,img_name))
            threads.append(thread)
            thread.start()
        for x in threads:
            x.join()

        # parse_url(href=real_href,headers=headers,img_name=img_name)
